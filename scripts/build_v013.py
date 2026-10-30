import json, sys, subprocess
from pathlib import Path

R = Path(r"C:\Users\ekham\Documents\Codex\2026-07-13\referenced-chatgpt-conversation-this-is-untrusted\work\ita-current")

CASES = [
('Index Opening Context', 'ES opens above the prior synthetic value area after an overnight rise.', 'Separate the overnight auction, cash open, and prior-session references. An opening location is context, not a direction forecast.', 'Write bullish, bearish, and no-trade hypotheses with observable invalidation.', 'A valid plan states what would disconfirm each path and avoids treating the opening location as a signal.'),
('Trend-Day Hypothesis', 'Synthetic NQ holds above an opening range while pullbacks become shallower.', 'A trend-day label is a revisable hypothesis based on acceptance, range expansion, and failed counter-auctions.', 'Define two confirmation observations and two invalidation observations.', 'The playbook remains conditional; a strong early move alone does not prove a trend day.'),
('Failed Breakout Decision Tree', 'ES trades above a prior synthetic high, then returns inside the range.', 'A breakout and a failed breakout require acceptance tests, time windows, and explicit risk limits rather than narrative hindsight.', 'Build continue, fail, and stand-aside branches without choosing one in advance.', 'Branching rules protect against converting one rejected price into a guaranteed reversal call.'),
('Rotation and Mean-Reversion Limits', 'Synthetic ES rotates repeatedly through a reference price in a balanced session.', 'Mean reversion is a regime-dependent hypothesis. Expansion, event risk, thin liquidity, or changing value can invalidate it.', 'Specify eligibility, entry evidence, target logic, and hard invalidation.', 'A rotation playbook is valid only while balance evidence persists; it is not a promise that extremes will hold.'),
('Index Event-Risk Protocol', 'A position idea overlaps a scheduled FOMC announcement and employment release.', 'Scheduled events can change liquidity, volatility, spreads, and correlation. The safe default is to reduce assumptions and predefine exposure.', 'Create before, during, and after-event gates including a no-trade option.', 'The protocol manages uncertainty; it does not predict the announcement or market response.'),
('Gold Catalyst Map', 'GC moves sharply while the dollar and yields also change in a synthetic scenario.', 'Gold can respond to rates, currencies, inflation expectations, risk sentiment, and positioning, but relationships vary through time.', 'List competing explanations and the evidence needed to distinguish them.', 'Cross-market moves are context, not causal proof or automatic confirmation.'),
('Gold Session and Liquidity Plan', 'A GC setup appears during a thin synthetic interval before a major release.', 'Session participation and order-book conditions affect slippage and stop behavior. A chart pattern cannot substitute for liquidity checks.', 'Define minimum liquidity evidence, maximum execution uncertainty, and cancellation rules.', 'The plan stands aside when execution conditions cannot be bounded.'),
('Gold Curve and Basis Context', 'Near and deferred synthetic gold contracts show different prices.', 'Futures curves reflect financing, storage, convenience, expectations, and contract mechanics. A spread is not a simple spot-direction signal.', 'Compare like-for-like contracts and record expiry, units, timestamp, and source.', 'A defensible comparison normalizes contract identity and avoids inferring direction from curve shape alone.'),
('Cross-Market Confirmation Limits', 'ES, NQ, GC, yields, and a currency index move together for fifteen minutes.', 'Confirmation is sensitive to window, lag, common catalysts, and data quality. Correlation can change or be coincidental.', 'Create a confirmation score that includes disagreement and missing-data penalties.', 'Divergence and missing evidence reduce confidence; they are not permission to invent a story.'),
('Specialist Playbook Assessment', 'An unseen case combines an index open, a scheduled event, GC curve data, and conflicting cross-market evidence.', 'A specialist playbook is a precommitted decision process with eligibility, evidence, invalidation, sizing, execution, and review.', 'Submit an index or gold playbook plus a source-stamped decision log.', 'Pass only when the learner can choose no trade, identify invalidation, and separate evidence from inference.')]

SOURCES = {
'CME_ES':('E-mini S&P 500 Futures Contract Specs - CME Group','https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html'),
'CME_NQ':('E-mini Nasdaq-100 Futures Contract Specs - CME Group','https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html'),
'CME_GOLD':('Gold Futures - CME Group','https://www.cmegroup.com/markets/metals/precious/gold.html'),
'CME_HOURS':('CME Group Holiday and Trading Hours','https://www.cmegroup.com/trading-hours.html'),
'CFTC_BASICS':('Basics of Futures Trading - CFTC','https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/FuturesMarketBasics/index.htm'),
'FED_CAL':('FOMC Calendars - Federal Reserve','https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'),
'BLS_CAL':('BLS Release Calendar - U.S. Bureau of Labor Statistics','https://www.bls.gov/schedule/'),
}

def load(p): return json.loads((R/p).read_text(encoding='utf-8'))
def save(p,v): (R/p).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')

def main():
    sources=load('data/sources.json'); sources.update({k:{'title':t,'url':u,'kind':'official'} for k,(t,u) in SOURCES.items()}); save('data/sources.json',sources)
    new=[]; folder=R/'content/en-US/specialist-index-gold-playbooks'; folder.mkdir(parents=True,exist_ok=True)
    for i,(title,scenario,concept,exercise,answer) in enumerate(CASES,11):
        mid=f'L06-M{i:02d}'; visual=f'{100+i:03d}_playbook_{i:02d}.png'; refs=list(SOURCES)
        m={'id':mid,'title':title,'time':'45 minutes' if i<20 else '90 minutes','visual':visual,'competencies':['playbook_design','risk_management','evidence_reasoning'],'prerequisites':[f'L06-M{i-1:02d}'],'objective':f'Build and test a conditional {title.lower()} playbook.','why':'Specialist practice requires explicit evidence, invalidation, risk and stand-aside rules.','core':[concept,'Every example is original and synthetic. No pattern is presented as a signal or proven edge.','Verify live specifications, schedules, data entitlements and broker rules before any real decision.'],'scenario':scenario,'exercise':exercise,'quiz':[['What makes the playbook falsifiable?',answer],['What remains uncertain?','Outcome, liquidity, slippage, correlations, event response and whether the observed regime persists.']],'mistake':'Treating contextual agreement as proof of direction or edge.','evidence':'Official exchange, regulator and economic-calendar sources checked 2026-10-30; original synthetic cases.','sources':refs}
        new.append(m)
        body=f'# {mid} - {title}\n\n## Objective\n{m["objective"]}\n\n## Synthetic case\n{scenario}\n\n## Concept\n{concept}\n\n![{title}](../../../assets/illustrations/{visual})\n\n## Practice\n{exercise}\n\n## Answer rationale\n{answer}\n\n## References\n'+ '\n'.join(f'- [{SOURCES[k][0]}]({SOURCES[k][1]})' for k in refs)+'\n'
        (folder/f'{mid}.md').write_text(body,encoding='utf-8')
    save('data/missions_en-US_01_120.json',load('data/missions_en-US_01_110.json')+new); save('data/level6_specialist_playbooks_en-US.json',new)
    c=load('data/curriculum.json'); c.update(version='0.13.0',authored_missions=120); c['content_status']['en-US']='missions_01_120_authored'; save('data/curriculum.json',c)
    t=load('data/translation_status.json'); t['project_version']='0.13.0'; t['english_master']['authored_missions']=120; ids={m['id'] for m in new}; t['missions']=[m for m in t['missions'] if m['id'] not in ids]+[{'id':m['id'],'en-US':'draft_complete','ar':'deferred'} for m in new]; save('data/translation_status.json',t)
    readme=(R/'README.md').read_text(encoding='utf-8').replace('Version: **0.12.0** local candidate; publication follows validation and review','Version: **0.13.0** local candidate; publication follows validation and review').replace('Authored missions: **110**','Authored missions: **120**').replace('Missions 01-110','Missions 01-120')
    (R/'README.md').write_text(readme,encoding='utf-8')
    roadmap=(R/'docs/10_ROADMAP.md').read_text(encoding='utf-8')
    roadmap=roadmap.replace('## Current build increment\n','## Current build increment\n\nv0.13.0 adds ten specialist index and gold playbook missions, bringing the English master to 120 missions. Every playbook is conditional, falsifiable and includes a no-trade branch; no pattern is presented as a signal or proven edge. Official exchange, regulator and economic-calendar sources support the original synthetic cases.\n')
    roadmap=roadmap.replace('The next increment should use the verified specification foundation to introduce specialist index and gold playbooks without presenting patterns as signals or proven edge. Private source images remain outside all public deliverables.','After English review of the 120-mission master, define the v1.0.0 English lock and review gates before Arabic authoring. Private source images remain outside all public deliverables.')
    (R/'docs/10_ROADMAP.md').write_text(roadmap,encoding='utf-8')
    graph=(R/'docs/04_KNOWLEDGE_GRAPH.md').read_text(encoding='utf-8')
    graph=graph.replace('## Authored mission chain - v0.12.0','## Authored mission chain - v0.13.0').replace('110 canonical English missions through L06-M10','120 canonical English missions through L06-M20')
    if 'L06-M11 through L06-M20 add conditional specialist index and gold playbooks' not in graph:
        graph += '\nL06-M11 through L06-M20 add conditional specialist index and gold playbooks with explicit eligibility, evidence, invalidation, risk, execution and no-trade gates.\n'
    (R/'docs/04_KNOWLEDGE_GRAPH.md').write_text(graph,encoding='utf-8')
    (R/'docs/34_BUILD_PLAN_v0.13.md').write_text('# v0.13.0 Build Plan\n\n## Scope\nTen original English missions, L06-M11 through L06-M20, covering conditional index and gold playbooks.\n\n## Guardrails\n- No pattern is a signal or claim of edge.\n- Every playbook includes eligibility, evidence, invalidation, risk and no-trade rules.\n- Examples are synthetic; sources are official and source originals remain private.\n- Arabic remains deferred until the English master is reviewed and locked.\n\n## Acceptance\n120 canonical English missions; project validation clean; arithmetic and privacy regressions pass; package contains no private-source or identifying metadata.\n',encoding='utf-8')
    (R/'docs/35_BUILD_STATUS_v0.13.md').write_text('# v0.13.0 Build Status\n\n- English missions L06-M11 through L06-M20: authored\n- Canonical English master: 120 canonical English missions\n- Original diagrams 111-120: generated\n- Arabic: deferred\n- Publication: pending validation, review, merge, tag and release\n',encoding='utf-8')
    test='''import json\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nmissions = json.loads((ROOT / "data/level6_specialist_playbooks_en-US.json").read_text(encoding="utf-8"))\nassert len(missions) == 10\nassert [m["id"] for m in missions] == [f"L06-M{i:02d}" for i in range(11, 21)]\nfor mission in missions:\n    joined = " ".join(mission["core"]).lower()\n    assert "no pattern is presented as a signal or proven edge" in joined\n    assert any("uncertain" in (question + " " + answer).lower() for question, answer in mission["quiz"])\n    assert "synthetic" in (mission["scenario"] + " " + joined).lower()\nprint("specialist playbook guardrails: 10 missions OK")\n'''
    (R/'scripts/test_playbook_guardrails.py').write_text(test,encoding='utf-8')
    push='''git push -u origin build/v0.13.0\nif ($LASTEXITCODE -ne 0) { throw "Push failed" }\n'''
    (R/'scripts/push_v0.13_candidate.ps1').write_text(push,encoding='utf-8')
    (R/'scripts/build_v013.py').write_text(Path(__file__).read_text(encoding='utf-8'),encoding='utf-8')
    manifest=['README.md','VERSION']
    manifest += [f'assets/illustrations/{100+i:03d}_playbook_{i:02d}.png' for i in range(11,21)]
    manifest += [f'content/en-US/specialist-index-gold-playbooks/L06-M{i:02d}.md' for i in range(11,21)]
    manifest += ['data/curriculum.json','data/level6_specialist_playbooks_en-US.json','data/missions_en-US_01_120.json','data/sources.json','data/translation_status.json','docs/04_KNOWLEDGE_GRAPH.md','docs/10_ROADMAP.md','docs/33_DECISION_QUALITY_PRACTICE.md','docs/34_BUILD_PLAN_v0.13.md','docs/35_BUILD_STATUS_v0.13.md','handbooks/ITA_English_Handbook_Missions_01_120_v0.13.md','release/v0.13.0/update_manifest.txt','scripts/build_v013.py','scripts/push_v0.13_candidate.ps1','scripts/test_playbook_guardrails.py']
    release=R/'release/v0.13.0'; release.mkdir(parents=True,exist_ok=True)
    (release/'update_manifest.txt').write_text('\n'.join(manifest)+'\n',encoding='utf-8')
    (R/'VERSION').write_text('0.13.0\n',encoding='utf-8'); subprocess.run([sys.executable,'scripts/build_handbook.py'],cwd=R,check=True)

if __name__=='__main__': main()
