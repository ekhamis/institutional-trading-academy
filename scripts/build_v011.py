"""Build original performance-review exercises without private source ingestion."""
import json
import subprocess
import sys
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parents[1]
CASES = [
    ('Partial Exits and Weighted R', 'A simulated position starts with $100 planned risk. Half exits at +1R and half at +3R. Total costs are $12.', 'Weight every exit by its fraction of the original quantity. Keep the original risk denominator.', 'Compute gross and net R; compare with exiting all at +3R without assuming that target always fills.', '0.5 x 1 + 0.5 x 3 = 2 gross R; ($200 - $12) / $100 = 1.88 net R.', 'Half at +1R | Half at +3R | Costs 0.12R | Net +1.88R'),
    ('Precommitted Time Stops', 'A synthetic plan requires a review after six completed five-minute bars. Price has not reached its trigger at that time.', 'Distinguish an entry expiry from a time-based exit of an existing position. Define the clock, timezone and exact rule before replay.', 'Write separate expiry and filled-position exit rules. Mark which applies to this unfilled case.', 'The entry plan expires after 30 minutes under this exercise rule. There is no filled position to exit.', 'Start clock | Six closed bars | No trigger | Cancel entry'),
    ('Breakeven Is Not Risk-Free', 'A simulated long fills at 100 and its stop moves to 100. The exit fills at 99.8; quantity is 50 and total costs are $5.', 'A stop trigger at entry does not guarantee a flat net result. Trailing rules change the payoff distribution and require testing.', 'Calculate net P/L and explain why moving a stop cannot be called removing all risk.', '(99.8 - 100) x 50 - 5 = -$15. Gaps, slippage and costs remain.', 'Entry 100 | Stop trigger 100 | Fill 99.8 | Net loss $15'),
    ('Correlated Portfolio Scenarios', 'Two index-related simulated positions each have $100 planned risk. A common shock causes losses of $140 and $160.', 'More tickers do not establish independent exposures. Evaluate common drivers and stressed combined loss; correlations are not fixed.', 'Compare the sum of planned stop risks with the stated common-shock result. Do not infer a covariance matrix from this example.', '$200 planned risk versus $300 scenario loss. The shock exceeds the planned sum by 50%.', 'Position A -140 | Position B -160 | Shared shock | Total -300'),
    ('Journal Evidence and Missing Fills', 'A chart box shows a target reached. The journal has no order confirmation, quantity or exit fill.', 'Separate plan, submitted order, confirmed execution and claimed result. Preserve unknowns; do not turn annotations into audited performance.', 'Create a record with timestamp, instrument/feed, plan version, order IDs, fill quantities/prices and costs. Leave unsupported fields unknown.', 'This is an unverified outcome, not a realized winner. Missing evidence is a review task, not permission to invent fills.', 'Plan | Order | Confirmed fills | Reconciled journal'),
    ('Expectancy and Sample Uncertainty', 'Ten synthetic outcomes contain four +2R wins and six -1R losses before costs. Modeled costs total 1R.', 'Sample mean is an estimate, not proof of future edge. Dependence, changing conditions and selective reporting can invalidate simple confidence arguments.', 'Compute gross and net mean R. List missing evidence before accepting the strategy.', '(4 x 2 - 6) / 10 = +0.2R gross per trade; (2 - 1) / 10 = +0.1R net. Ten outcomes do not establish a stable edge.', '4 wins +8R | 6 losses -6R | Costs -1R | Mean +0.1R'),
    ('Drawdown and Recovery', 'A synthetic equity series starts at 10000, peaks at 12000 and falls to 9000.', 'Measure drawdown from a prior peak, not the starting deposit. Recovery uses the smaller current balance as denominator.', 'Calculate peak-to-trough drawdown and the percentage gain needed to regain the peak. Ignore deposits and withdrawals in this example.', '(12000 - 9000) / 12000 = 25% drawdown. 3000 / 9000 = 33.33% recovery gain.', 'Peak 12000 | Trough 9000 | Drawdown 25% | Recovery 33.33%'),
    ('Losing Streaks and Risk Controls', 'Five simulated losses each remove 1% of then-current equity from an initial 10000, ignoring costs.', 'Compounding changes risk dollars. Streak probabilities require assumptions; a small backtest cannot guarantee a maximum future losing streak.', 'Compute remaining equity. Write a precommitted pause/review rule without increasing size to recover losses.', '10000 x 0.99^5 = 9509.90, approximately 4.90% drawdown. The next trade is not owed a win.', '10000 | Five 1% losses | 9509.90 | Pause and review'),
    ('Held-Out Testing Without Leakage', 'A researcher tunes rules on January-June, evaluates July-August, then repeatedly changes rules after viewing September-October test results.', 'A test set used for tuning is no longer untouched. Split chronologically, preserve configurations and account for overlapping labels or forward-looking features.', 'Design training, validation and final held-out periods. Explain how contaminated results must be labeled.', 'September-October became development data. Freeze a new specification and evaluate on new untouched data; do not relabel the old test as independent evidence.', 'Train | Validate | Freeze rules | Untouched test'),
    ('Performance Review Assessment', 'Review an unseen synthetic journal containing partial exits, costs, a missing fill, correlated positions and an overstated result.', 'Score arithmetic, evidence integrity, risk aggregation, uncertainty, test separation and remediation from 0 to 2. Require 10/12 and no critical failure.', 'Submit calculations, corrected unknowns, a stress scenario and a reproducible evaluation plan. A fabricated fill, hidden cost or leaked test is a critical failure.', 'Advance only after the rubric passes and all critical failures are repaired on a new case. This is an internal educational assessment, not accreditation.', 'Evidence | Arithmetic | Risk and uncertainty | Remediation')
]

def load(name):
    return json.loads((R / name).read_text(encoding='utf-8'))

def save(name, value):
    (R / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def main():
    refs = ['CME_RISK', 'SEC_DIVERSIFICATION', 'CFTC_HYPOTHETICAL']
    sources = load('data/sources.json')
    sources.update({
        'SEC_DIVERSIFICATION': dict(title='Asset Allocation and Diversification - Investor.gov', url='https://www.investor.gov/introduction-investing/getting-started/asset-allocation', kind='official'),
        'CFTC_HYPOTHETICAL': dict(title='Commodity Trading Systems Sold on the Internet - CFTC', url='https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_tradingsystem.html', kind='official')
    })
    save('data/sources.json', sources)
    new = []
    folder = R / 'content/en-US/performance-review'
    folder.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 32)
    small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 26)
    for number, (title, case, concept, exercise, answer, flow) in enumerate(CASES, 11):
        mid = f'L05-M{number:02d}'
        visual = f'{80+number:03d}_review_{number:02d}.png'
        mission = dict(id=mid, title=title, time='45 minutes' if number < 20 else '90 minutes', visual=visual,
            competencies=['risk_management', 'trade_planning', 'data_literacy'], prerequisites=[f'L05-M{number-1:02d}'],
            objective=f'Apply {title.lower()} to a reproducible decision record.', why='Honest measurement prevents outcome bias and unsupported claims.',
            core=[concept, 'Every example here is original and synthetic. It is not verified historical performance or a trading recommendation.', 'Arithmetic is illustrative; rules and assessment thresholds are curriculum policy, not evidence of profitable edge.'],
            scenario=case, exercise=exercise, quiz=[['Explain the result and its limitations.', answer], ['What evidence must remain unknown?', 'Any execution, cost or timing field not established by the supplied record.']],
            mistake='Treating an attractive chart or small sample as proof of net realized performance.',
            evidence='Official general risk guidance plus original educational arithmetic and research-design practice; not a validated strategy.', sources=refs)
        new.append(mission)
        body = f'# {mid} - {title}\n\n## Objective\n{mission["objective"]}\n\n## Synthetic case\n{case}\n\n## Concept\n{concept}\n\n![{title}](../../../assets/illustrations/{visual})\n\n## Practice\n{exercise}\n\n## Answer rationale\n{answer}\n\n## References\n'
        body += '\n'.join(f'- [{sources[k]["title"]}]({sources[k]["url"]})' for k in refs)
        (folder / f'{mid}.md').write_text(body+'\n', encoding='utf-8')
        im = Image.new('RGB', (1600, 900), '#fafafa'); d = ImageDraw.Draw(im)
        d.text((60, 45), f'{mid} | {title}', font=font, fill='#171717')
        d.text((60, 110), 'ORIGINAL SYNTHETIC EXERCISE | Not historical performance', font=small, fill='#166534')
        for index, stage in enumerate(flow.split(' | ')):
            y = 200 + index * 125
            d.rectangle((60,y,1540,y+95), outline='#737373', width=2)
            d.text((90,y+28), f'{index+1}. {stage}', font=font, fill=['#166534','#1d4ed8','#9f1239','#171717'][index])
        d.text((60, 755), '\n'.join(textwrap.wrap(answer, 105)), font=small, fill='#171717')
        im.save(R / 'assets/illustrations' / visual)
    save('data/missions_en-US_01_100.json', load('data/missions_en-US_01_90.json') + new)
    save('data/level5_review_missions_en-US.json', new)
    c=load('data/curriculum.json'); c.update(version='0.11.0', authored_missions=100)
    c['content_status']['en-US']='missions_01_100_authored'; save('data/curriculum.json',c)
    t=load('data/translation_status.json'); t['project_version']='0.11.0'; t['english_master']['authored_missions']=100
    t['missions']=[m for m in t['missions'] if m['id'] not in {x['id'] for x in new}]+[{'id':m['id'],'en-US':'draft_complete','ar':'deferred'} for m in new]
    save('data/translation_status.json',t)
    (R/'VERSION').write_text('0.11.0\n')
    subprocess.run([sys.executable, 'scripts/build_handbook.py'],cwd=R,check=True)

if __name__ == '__main__':
    main()
