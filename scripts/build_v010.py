"""Author the synthetic Level 5 planning batch; no private source ingestion."""
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parents[1]

CASES = [
('A Conditional Trading Plan', 'A synthetic index trades at 5000 below resistance at 5004. Plan a short only after a test above 5004 and a close back below 5003. The trigger never occurs.', ['Context is not an entry. Separate the observation, testable hypothesis, trigger, invalidation and execution instruction.', 'Write the plan before revealing later bars. The correct outcome here is no trade, not a retrospective entry.'], 'Do not trade without the stated trigger; cancel after the observation window expires.', 'No trade. Record an untriggered plan rather than inventing a fill.'),
('Invalidation and Protective Stops', 'A hypothetical long entry is 100, structural invalidation is below 98, planned stop is 97.8 and the nearest target is 103.', ['The planned price risk is 2.2 per unit; the gross reward is 3, or approximately 1.36R.', 'Place a stop for a stated invalidation, then size to the budget. Do not tighten it merely to manufacture a preferred reward/risk ratio. Stops may fill worse than their trigger.'], 'Skip if the minimum tradable size exceeds the budget or the expected fill cannot be bounded sufficiently.', '3 / 2.2 = 1.36 gross R, before fees and slippage; this is not a guarantee.'),
('Sizing From a Loss Budget', 'An educational simulation has a $100 risk budget, a 12-point stop, $2 per point per contract and $6 modeled round-trip cost per contract.', ['Modeled risk is 12 x 2 + 6 = $30 per contract. Floor(100 / 30) gives 3 contracts and $90 modeled loss.', 'Check currency, multiplier, tick size, minimum quantity and cost units. Margin is not the loss budget. A gap can exceed this model.'], 'Reject the order if contract specifications are unknown or even one unit exceeds the budget.', 'Three contracts; four would model $120 and breach the budget.'),
('Order Choice and Fill Uncertainty', 'A buy limit at 100 is touched but no execution confirmation appears. The next bar rises to 102.', ['A touched price does not prove that a queued limit order filled. Record no confirmed fill until execution evidence exists.', 'A market order prioritizes execution over price; a limit controls the worst acceptable price but may not fill. Stop-limit orders can remain unfilled.'], 'Do not turn an unfilled limit into a market chase without a new documented plan.', 'Unconfirmed, not a winning trade. Price movement alone cannot establish queue priority.'),
('Costs Change the Decision', 'A modeled setup risks 10 ticks and targets 20. Round-trip fees equal 2 ticks and adverse slippage is modeled at 1 tick on either outcome.', ['Net target is 17 ticks and modeled loss is 13 ticks, giving 17 / 13 = 1.31 reward/risk.', 'At those fixed outcomes the break-even win fraction is 13 / 30 = 43.33%, ignoring other costs. The original gross 2R label overstates this modeled payoff.'], 'Skip if costs consume the planned advantage; actual distributions and gap risk require separate testing.', '1.31 modeled net reward/risk; break-even 43.33% under the stated assumptions only.'),
('Daily Loss and Correlated Exposure', 'A simulated session loss ceiling is $200. Two completed trades lost $70 and $80. A new plan risks $60; another Nasdaq-related position is already open.', ['Only $50 remains under the session ceiling before existing open risk. The new $60 plan does not fit.', 'Aggregate open risk and related exposures rather than counting each chart as independent. A daily limit is an operational control, not a guaranteed cap during gaps.'], 'Stop opening risk when the remaining budget is insufficient; do not increase the ceiling to recover losses.', 'Decline the new plan; include open exposure before calculating any remaining capacity.'),
('Managing a Losing Trade', 'A synthetic long is filled at 100 with a protective stop at 98 and a target at 104. Price trades down and the exit fills at 97.8.', ['Planned 1R is 2 price units. Gross realized result is -2.2 / 2 = -1.1R before costs.', 'Keep the original denominator for review. Do not widen the stop, add to a loser or redefine R afterward to hide the loss.'], 'Follow the planned exit and record slippage; investigate whether execution conditions exceeded assumptions.', '-1.1 gross R, with a worse net result after costs. A planned stop did not guarantee -1R.'),
('A Disciplined Skipped Trade', 'A valid-looking gold pattern appears immediately before a scheduled announcement. The written simulator rule excludes new positions within five minutes of that event.', ['The appropriate action is to skip under this plan even if later price reaches the target.', 'Grade compliance using evidence available at decision time. A profitable counterfactual does not make breaking a risk rule correct.'], 'Resume only when the written event window and post-event spread conditions are satisfied.', 'A compliant no-trade. The five-minute window is an exercise assumption, not a universal safety rule.'),
('Ambiguous Evidence and Review', 'A chart contains a risk/reward box and a claimed 6R result, but no timestamped plan, quantity, fills, stop history or costs.', ['A chart annotation and reported outcome are not verified execution. Preserve an explicit unknown status.', 'Request the missing evidence before calculating realized R. Review the reasoning independently of whether the reported result is positive.'], 'Do not use an unverifiable claim as proof of edge, certification or a real trade record.', 'Insufficient evidence. Do not invent entry, stop, quantity, fill sequence or net performance.'),
('Level 5 Planning Assessment', 'Submit four synthetic cases: one triggered loss, one untriggered plan, one announcement skip and one ambiguous reported result.', ['Score six dimensions from 0 to 2: context, trigger, invalidation, sizing and costs, contradictory evidence, and review integrity.', 'Require at least 10/12 plus no critical safety failure. Missing loss budget, lookahead, fabricated fills or publishing private source material is a critical failure regardless of score.'], 'Remediate failed dimensions with a new unseen case before advancing; this internal assessment is not professional accreditation.', 'Include a decision-time record and outcome evidence for each case. Correctly declining a case can earn full credit.')
]

def load(path):
    return json.loads((R / path).read_text(encoding='utf-8'))

def save(path, value):
    (R / path).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def main():
    old = load('data/missions_en-US_01_80.json')
    new = []
    sources = load('data/sources.json')
    refs = ['CME_RISK']
    assert all(key in sources for key in refs)
    folder = R / 'content/en-US/planning-execution'
    folder.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 30)
    small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 24)
    for i, (title, scenario, core, cancel, answer) in enumerate(CASES, 1):
        mid = f'L05-M{i:02d}'
        visual = f'{80+i:02d}_planning_{i:02d}.png'
        mission = dict(id=mid, title=title, time='40 minutes' if i < 10 else '90 minutes',
            visual=visual, competencies=['risk_management','trade_planning','data_literacy'],
            prerequisites=['L04-M20'] if i == 1 else [f'L05-M{i-1:02d}'],
            objective=f'Demonstrate {title.lower()} with a timestamped, cost-aware decision.',
            why='Assess decisions before outcomes and preserve unknowns rather than reward hindsight.',
            core=core + [cancel, 'All cases are original synthetic exercises, not live recommendations or historical performance.'],
            scenario=scenario,
            exercise='Record the visible evidence, alternative explanation, exact trigger, cancellation, entry/stop/target, size and modeled costs before revealing the result. State unknown fields explicitly. Then grade the decision, not the profit.',
            quiz=[['What is the correct interpretation of this case?', answer], ['What prevents or cancels the trade?', cancel], ['Does a good process guarantee profit?', 'No. Losses and execution uncertainty remain; separate strategy testing is required.']],
            mistake='Using a favorable outcome to excuse missing risk controls or fabricated execution evidence.',
            evidence='Official risk principles plus original synthetic practice rules; thresholds are curriculum policy, not proven trading edges.', sources=refs)
        new.append(mission)
        body = f'# {mid} - {title}\n\n## Objective\n{mission["objective"]}\n\n## Synthetic case\n{scenario}\n\n## Reasoning\n' + '\n'.join('- '+x for x in mission['core'])
        body += f'\n\n## Practice\n{mission["exercise"]}\n\n## Answer rationale\n{answer}\n\n## Source\n[{sources[refs[0]]["title"]}]({sources[refs[0]]["url"]})\n'
        (folder / f'{mid}.md').write_text(body, encoding='utf-8')
        im = Image.new('RGB',(1600,900),'#fafafa'); d = ImageDraw.Draw(im)
        d.text((60,45),f'{mid} | {title}',font=font,fill='#181818')
        d.text((60,105),'ORIGINAL SYNTHETIC CASE | Decide before revealing the outcome',font=small,fill='#166534')
        stages = [('OBSERVE','Context + evidence'),('PLAN','Trigger + invalidation'),('CHECK','Size + costs + limits'),('REVIEW','Fills + unknowns')]
        for j,(label,detail) in enumerate(stages):
            y=200+j*135
            d.rectangle((60,y,1540,y+105),outline='#777777',width=2)
            d.text((90,y+16),label,font=font,fill=['#166534','#1d4ed8','#9f1239','#262626'][j])
            d.text((500,y+22),detail,font=font,fill='#181818')
        d.text((60,790),'Safety failure overrides the score. No fill evidence means no verified fill.',font=small,fill='#9f1239')
        im.save(R/'assets/illustrations'/visual)
    save('data/missions_en-US_01_90.json',old+new)
    save('data/level5_planning_missions_en-US.json',new)
    c=load('data/curriculum.json'); c.update(version='0.10.0',authored_missions=90)
    c['content_status']['en-US']='missions_01_90_authored'; save('data/curriculum.json',c)
    t=load('data/translation_status.json'); t['project_version']='0.10.0'; t['english_master']['authored_missions']=90
    t['missions']=[m for m in t['missions'] if not m['id'].startswith('L05-')]+[{'id':m['id'],'en-US':'draft_complete','ar':'deferred'} for m in new]
    save('data/translation_status.json',t)
    (R/'VERSION').write_text('0.10.0\n')
    subprocess.run([sys.executable,'scripts/build_handbook.py'],cwd=R,check=True)
    release = R / 'release/v0.10.0'
    release.mkdir(parents=True, exist_ok=True)
    changed = subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).splitlines()
    added = subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=R,text=True).splitlines()
    paths = sorted(set(changed + added + ['release/v0.10.0/update_manifest.txt', 'scripts/push_v0.10_candidate.ps1']))
    (release/'update_manifest.txt').write_text('\n'.join(paths)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
