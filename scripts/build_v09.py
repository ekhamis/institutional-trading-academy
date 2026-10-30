"""Reproduce the English Level 4 completion increment."""
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parents[1]
def load(p): return json.loads((R/p).read_text(encoding='utf-8'))
def save(p, value): (R/p).write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')

# Numeric cases are synthetic exercises, not historical trades or signals.
cases = [
('Absorption Hypotheses','700 ask-classified contracts trade while the high advances only one tick; 100 contracts traded in the comparison window.', ['Aggressive volume with limited price progress is consistent with absorption, but does not establish a hidden seller or reversal.', 'Compare equal-duration windows, volatility, trade classification and price location. Resting size alone cannot establish absorption.'], 'Wait for a defined structural response; invalidate the reversal hypothesis on accepted continuation above the test.', ['Classified contracts', 'Price progress (ticks)'], [700,1], ['SIERRA_NUMBERS_BARS','CME_MBO']),
('Exhaustion Hypotheses','A push trades 300 contracts across six ticks; the next equal-duration push trades 80 across one tick.', ['Declining participation and progress can support an exhaustion hypothesis. A quiet period or incomplete feed can produce similar observations.', 'Absorption emphasizes opposing liquidity against aggressive trades; exhaustion emphasizes declining aggressive activity. They can coexist.'], 'Reject the hypothesis if participation and directional progress return; avoid inferring direction from low volume alone.', ['Earlier volume','Later volume'], [300,80], ['SIERRA_NUMBERS_BARS']),
('Stacked Imbalances','Three consecutive diagonal ask/bid comparisons are 120/30, 150/40 and 90/20. The test ratio is 3 and minimum numerator is 80.', ['The ratios are 4, 3.75 and 4.5, so all three satisfy this explicitly defined synthetic rule.', 'Platform diagonal conventions, zero handling, tick grouping and minimum-volume filters change results. A stack describes a calculation, not a profitable entry.'], 'Require contextual acceptance; cancel if price returns through the tested area or the settings cannot be reproduced.', ['Ratio x100: A','Ratio x100: B','Ratio x100: C'], [400,375,450], ['SIERRA_NUMBERS_BARS']),
('Price and Delta Divergence','Price highs move from 5000 to 5002 while comparable-window delta falls from +600 to +200.', ['Price and delta are not obliged to move together. Passive liquidity and different volume distributions can explain divergence.', 'Use the same contract, venue, session boundaries and classification method. Do not compare estimated spot/CFD delta with exchange futures delta as identical evidence.'], 'Accepted higher prices can invalidate a bearish interpretation despite divergence.', ['First delta','Second delta'], [600,200], ['SIERRA_CVD','SIERRA_NUMBERS_BARS']),
('Book Resiliency','Displayed depth falls from 400 to 100 after a trade burst, then recovers to 300 after 500 milliseconds.', ['The observed recovery is 200 contracts in 500 milliseconds; it does not show that the same participant replenished.', 'Separate cancellations, additions and executions. Timestamp resolution and feed gaps can invalidate a recovery-time estimate.'], 'Avoid execution when spread and depth fail to recover within the predefined observation window.', ['Before depth','After burst','Recovered depth'], [400,100,300], ['CME_MBO']),
('Order Flow Confluence','Footprint ask-minus-bid equals +250, candle delta is +250 and CVD increases by +250.', ['These can be three representations of the same executions, rather than three independent confirmations.', 'List each observation and its underlying input. Structure and execution cost answer different questions from signed traded volume.'], 'A repeated metric cannot compensate for an invalid structural plan or excessive spread.', ['Footprint delta','Candle delta','CVD change'], [250,250,250], ['SIERRA_NUMBERS_BARS','SIERRA_CVD']),
('Replay Without Lookahead','Pause at 09:35, record a plan, then reveal the 09:36 bar. The later high is unavailable at decision time.', ['Save the decision timestamp, visible data window, settings and written conditional plan before revealing the outcome.', 'A chart screenshot taken afterward can contain hindsight labels. Mark which evidence was genuinely available at the pause.'], 'Discard a trial if future bars or outcomes were seen before recording the decision.', ['Plan timestamp','Reveal timestamp'], [935,936], ['SIERRA_REPLAY']),
('Replay Measurement and Costs','A synthetic trade earns 10 gross ticks; fees equal 2 ticks and modeled slippage is 3 ticks.', ['Net result is 5 ticks. Cost assumptions must match size, instrument and execution conditions; a replay fill is not proof of a live fill.', 'Select sessions before viewing outcomes, retain losses and no-trades, separate development from held-out evaluation, and report sample size and uncertainty.'], 'Stop evaluation if fills are modeled from unavailable depth or if the test set influenced parameter selection.', ['Gross ticks','Fees ticks','Slippage ticks','Net ticks'], [10,2,3,5], ['SIERRA_REPLAY','CME_RISK']),
('Advanced No-Trade Conditions','A depth feed is 2 seconds stale during a burst while the price feed updates every 100 milliseconds.', ['A stale depth snapshot and current price are not a synchronized order-flow view. Restore and verify timestamps before interpreting.', 'No trade is justified for missing history, inconsistent sessions, unsuitable venue comparisons, late confirmation or unbounded execution cost.'], 'Resume observation only after the original data and risk conditions can be verified again.', ['Depth age (ms)','Price age (ms)'], [2000,100], ['CME_MBO','CME_RISK']),
('Level 4 Completion Assessment','Case A has synchronized futures data; case B combines delayed depth with estimated CFD delta. Both appear bullish.', ['Submit provenance, settings, observations, competing hypotheses, conditional confirmation, invalidation, costs and a trade/no-trade conclusion for both cases.', 'Score provenance 25, interpretation 25, replay integrity 20 and risk 30. Require 80/100 and no critical failure: lookahead, unbounded loss or false data equivalence.'], 'Case B should be declined until comparability is established. Case A still needs a defensible risk plan; bullish evidence alone is insufficient.', ['Provenance','Interpretation','Replay integrity','Risk'], [25,25,20,30], ['CME_MBO','SIERRA_NUMBERS_BARS','SIERRA_REPLAY','CME_RISK'])
]

def main():
    sources=load('data/sources.json')
    sources['SIERRA_REPLAY']={'title':'Replay Chart - Sierra Chart','url':'https://www.sierrachart.com/index.php?page=doc/ReplayChart.html','kind':'official','checked':'2026-10-30'}
    save('data/sources.json',sources)
    missions=load('data/missions_en-US_01_70.json'); new=[]
    fontpath='C:/Windows/Fonts/arial.ttf'
    for i,(title,scenario,core,rule,labels,values,refs) in enumerate(cases,11):
        mid=f'L04-M{i:02d}'; visual=f'{56+i:02d}_level4_{i:02d}.png'
        m=dict(id=mid,title=title,time='35 minutes' if i<20 else '75 minutes',visual=visual,competencies=['order_flow','data_literacy','risk_management'],prerequisites=[f'L04-M{i-1:02d}'],objective=f'Evaluate {title.lower()} using reproducible observations and a conditional risk decision.',why='Separating observation from interpretation makes the decision auditable and exposes alternatives before risk is taken.',core=core+[rule,'All numeric examples are synthetic and must not be interpreted as historical performance.'],scenario=scenario,exercise='Recalculate the worked case, state one alternative explanation, and submit a decision-time record with data settings, confirmation, invalidation, costs and a justified no-trade condition.',quiz=[['What does the worked case establish?',core[0]],['What cancels or limits the interpretation?',rule],['Does this example establish a profitable strategy?','No. It is a synthetic reasoning exercise; an edge requires separate cost-aware evaluation.']],mistake='Inferring participant identity or a trade signal from a descriptive metric without validating data and risk.',evidence='Platform documentation plus explicitly labelled practitioner hypotheses and synthetic exercises',sources=refs)
        new.append(m)
        directory=R/'content/en-US/liquidity-order-flow'; directory.mkdir(exist_ok=True)
        text=f"# {mid} - {title}\n\n## Objective\n{m['objective']}\n\n## Worked synthetic example\n{scenario}\n\n## Interpretation and alternatives\n"+'\n'.join('- '+x for x in m['core'])+f"\n\n## Practice\n{m['exercise']}\n\n## Answer rationale\n"+'\n'.join(f'- {q} {a}' for q,a in m['quiz'])+'\n\n## Sources\n'+'\n'.join(f"- [{sources[s]['title']}]({sources[s]['url']})" for s in refs)+'\n'
        (directory/f'{mid}_{title.replace(" ","_")}.md').write_text(text,encoding='utf-8')
        image=Image.new('RGB',(1600,900),'#111827'); d=ImageDraw.Draw(image)
        d.text((60,40),f'{mid} | {title}',font=ImageFont.truetype(fontpath,38),fill='white')
        d.text((60,110),'SYNTHETIC EXERCISE | Values use the units in each label',font=ImageFont.truetype(fontpath,24),fill='#a7f3d0')
        for j,(label,value) in enumerate(zip(labels,values)):
            y=210+j*115; width=int(value/max(values)*850)
            d.text((60,y),label,font=ImageFont.truetype(fontpath,26),fill='white')
            d.rectangle((450,y,450+width,y+45),fill=['#38bdf8','#34d399','#fbbf24','#f472b6'][j%4]);d.text((1320,y),str(value),font=ImageFont.truetype(fontpath,26),fill='white')
        d.text((60,790),'Observation -> alternative explanation -> conditional decision',font=ImageFont.truetype(fontpath,28),fill='white')
        image.save(R/'assets/illustrations'/visual)
    missions+=new;save('data/missions_en-US_01_80.json',missions);save('data/level4_completion_missions_en-US.json',new)
    c=load('data/curriculum.json');c.update(version='0.9.0',authored_missions=80);c['content_status']['en-US']='missions_01_80_authored';save('data/curriculum.json',c)
    t=load('data/translation_status.json');t['project_version']='0.9.0';t['english_master']['authored_missions']=80;t['missions'] += [{'id':m['id'],'en-US':'draft_complete','ar':'deferred'} for m in new];save('data/translation_status.json',t)
    (R/'VERSION').write_text('0.9.0\n')
    for p in ['README.md','docs/04_KNOWLEDGE_GRAPH.md','docs/10_ROADMAP.md']:
        s=(R/p).read_text(encoding='utf-8').replace('0.8.0','0.9.0').replace('**70**','**80**').replace('70 canonical English missions','80 canonical English missions').replace('01-70','01-80')
        if p=='README.md':s=s.replace('merged and validated on `main` (release-ready but unpublished; latest published release remains v0.6.0)','candidate on build/v0.9.0; publication follows validation')
        (R/p).write_text(s,encoding='utf-8')
    (R/'docs/28_BUILD_STATUS_v0.9.md').write_text('# Build status v0.9.0\n\n80 canonical English missions. Ten Level 4 completion lessons, synthetic numeric exercises, distinct charts and assessment rubric authored. English remains in review; Arabic deferred. Publication requires passing local validation and CI.\n',encoding='utf-8')
    (R/'scripts/push_v0.9_candidate.ps1').write_text('git push origin build/v0.9.0\nif ($LASTEXITCODE -ne 0) { throw "Push failed" }\n')
    subprocess.run(['python','scripts/build_handbook.py'],cwd=R,check=True)
    folder=R/'release/v0.9.0';folder.mkdir(parents=True,exist_ok=True)
    tracked=subprocess.check_output(['git','diff','--name-only'],cwd=R,text=True).splitlines()
    untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=R,text=True).splitlines()
    paths=sorted(set(tracked+untracked+['release/v0.9.0/update_manifest.txt']))
    (folder/'update_manifest.txt').write_text('\n'.join(paths)+'\n')

if __name__=='__main__': main()
