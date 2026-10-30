"""Build original instrument-specification exercises from official public sources."""
import json
import subprocess
import sys
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parents[1]
CASES = [
    ('Verify the Tradable Contract', 'A note says only "S&P at 6200" with no venue, symbol, expiry or feed.', 'An index value, ETF, CFD and futures contract are different instruments. Record venue, product, contract month, currency and data source before calculating risk.', 'Rewrite the note as a verification checklist and leave every unsupported field unknown.', 'The note is not execution-ready. A complete identity might name CME ES plus a specific month, but the case supplies no basis to invent one.', 'Label | Venue | Contract month | Feed'),
    ('Index Futures Multipliers', 'A synthetic ES move is 8.00 index points and a synthetic NQ move is 25.00 points, one contract each.', 'Contract value changes by price move times the exchange multiplier. Current specifications must be checked at the exchange rather than copied from memory.', 'Using the cited specifications, compute gross changes before fees and explain why equal point moves are not equal risk.', 'ES uses $50 per index point, so 8 points is $400. NQ uses $20 per index point, so 25 points is $500.', 'Points | Multiplier | Contracts | Gross change'),
    ('Minimum Tick and Order Validity', 'A learner proposes an ES limit at 6200.10 and a GC limit at 2750.05.', 'A price must conform to the contract minimum fluctuation. Display precision is not permission to submit every decimal value.', 'Check both prices against the cited minimum ticks and provide the nearest valid prices on either side.', 'ES trades in 0.25-point increments, so 6200.10 is invalid; adjacent ticks are 6200.00 and 6200.25. GC trades in $0.10 increments, so 2750.05 is invalid; adjacent ticks are 2750.00 and 2750.10.', 'Proposed price | Tick grid | Reject | Correct'),
    ('E-mini, Micro and Gold Sizing', 'A plan compares one ES, one MES, one GC and one MGC without recording multipliers.', 'Similar product names can hide tenfold size differences. Verify the exact product and calculate dollar risk from stop distance before choosing quantity.', 'Create a four-row specification card with multiplier, tick and a clearly labeled hypothetical stop distance.', 'The exercise must show that product selection changes exposure. Margin is not the maximum possible loss and must not replace stop-risk arithmetic.', 'Product | Multiplier | Stop distance | Dollar risk'),
    ('Trading Hours and Trade Date', 'A platform chart labels a Sunday-evening fill as Monday while a local export shows Sunday.', 'Globex sessions can cross midnight and use exchange trade dates. Timezone, daylight-saving rule, session template and holiday schedule must accompany timestamps.', 'Normalize the record to UTC and exchange time, then state which label remains platform-defined.', 'Both timestamps may describe the same event. Preserve the original timezone and trade-date fields; do not infer an error from the calendar label alone.', 'Raw timestamp | Timezone | UTC | Trade date'),
    ('Cash Index, Futures and ETF', 'A screenshot overlays an S&P 500 cash index, ES futures and an ETF, then claims every price difference is bad data.', 'Cash indices, futures and ETFs have different construction, trading hours and carrying relationships. Alignment requires instrument identity and synchronized timestamps.', 'List the evidence required before comparing the three series. Do not force them onto one price scale.', 'Record symbol, venue, currency, adjustment method, timestamp, session and whether the value is indicative, executable or calculated.', 'Cash calculation | Futures market | ETF market | Align evidence'),
    ('Expiry and Roll Verification', 'A continuous futures chart jumps when its provider changes the lead contract.', 'Futures expire. Continuous-series providers can roll on different dates and can back-adjust prices, changing historical levels without changing individual contracts.', 'Separate the raw contract series from the continuous series and document the provider roll rule.', 'A roll gap is not automatically a market gap. Reproduce analysis on named contracts and preserve the continuous-series transformation.', 'Named contracts | Roll rule | Adjustment | Reproduce'),
    ('Gold Settlement and Delivery Risk', 'A learner holds a GC contract toward expiry believing every futures position is always cash settled.', 'GC is a physically delivered COMEX contract. Delivery procedures and broker liquidation rules require current verification; education must not imply that a stop guarantees exit before delivery obligations.', 'Build a pre-expiry checklist using the contract page and broker-specific unknowns.', 'Confirm contract month, last trading day, delivery mechanism, account eligibility and broker cutoffs. If any operational fact is unknown, escalate before trading.', 'Expiry | Delivery | Broker cutoff | Escalate'),
    ('Feed Delay and Data Provenance', 'A public CME quote, broker chart and paid API show different last prices at the same wall-clock moment.', 'Public CME quotes are delayed by at least ten minutes, while licensed products can provide real-time, delayed or end-of-day data. Vendors may also use different aggregation and session settings.', 'Create a provenance record that can explain the difference without choosing a winner by appearance.', 'Record source, entitlement, delay, timestamp semantics, trade or quote field, aggregation, session and corrections. Compare like with like.', 'Entitlement | Delay | Field | Aggregation'),
    ('Instrument Verification Assessment', 'An unseen case mixes ES, NQ and GC records with invalid ticks, missing expiries, ambiguous timestamps and a delayed feed.', 'Score identity, specification arithmetic, session normalization, expiry handling, delivery awareness and provenance from 0 to 2. Require 10/12 and no critical failure.', 'Submit corrected specification cards, calculations and a source-stamped decision log. Trading an unidentified contract or inventing a missing field is a critical failure.', 'Advance only after a fresh case passes. Specifications and schedules can change, so every card needs an as-of date and official source.', 'Identity | Arithmetic | Sessions and expiry | Provenance')
]

SOURCES = {
    'CME_ES_SPEC': ('E-mini S&P 500 Futures Contract Specs - CME Group', 'https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html'),
    'CME_NQ_SPEC': ('E-mini Nasdaq-100 Futures Contract Specs - CME Group', 'https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html'),
    'CME_GC_SPEC': ('Gold Futures Contract Specs - CME Group', 'https://www.cmegroup.com/markets/metals/precious/gold.contractSpecs.html'),
    'CME_MICRO_EQUITY': ('Micro E-mini Equity Index Futures - CME Group', 'https://www.cmegroup.com/markets/equities/micro-e-mini-futures.html'),
    'CME_MGC_SPEC': ('Micro Gold Futures Contract Specs - CME Group', 'https://www.cmegroup.com/markets/metals/precious/e-micro-gold.contractSpecs.html'),
    'CME_HOURS': ('CME Group Holiday and Trading Hours', 'https://www.cmegroup.com/trading-hours.html'),
    'CME_DELAYED': ('Delayed Quotes - CME Group', 'https://www.cmegroup.com/market-data/browse-data/delayed-quotes.html'),
    'CME_DATA': ('Real-Time and Historical Data - CME Group', 'https://www.cmegroup.com/market-data/real-time-and-historical-data.html'),
}

def load(name): return json.loads((R / name).read_text(encoding='utf-8'))
def save(name, value): (R / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def main():
    sources = load('data/sources.json')
    sources.update({k: {'title': v[0], 'url': v[1], 'kind': 'official'} for k, v in SOURCES.items()})
    save('data/sources.json', sources)
    refs = list(SOURCES)
    new = []
    folder = R / 'content/en-US/instrument-specifications'; folder.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 32); small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 25)
    for number, (title, case, concept, exercise, answer, flow) in enumerate(CASES, 1):
        mid = f'L06-M{number:02d}'; visual = f'{100+number:03d}_instrument_{number:02d}.png'
        prereq = ['L05-M20'] if number == 1 else [f'L06-M{number-1:02d}']
        mission = dict(id=mid, title=title, time='45 minutes' if number < 10 else '90 minutes', visual=visual,
            competencies=['instrument_literacy', 'risk_management', 'data_literacy'], prerequisites=prereq,
            objective=f'Apply {title.lower()} with a source-stamped specification record.', why='Instrument identity and current specifications are prerequisites for valid risk and execution decisions.',
            core=[concept, 'Every example is original and synthetic. Verify live specifications, schedules and broker rules before any real decision.', 'This curriculum is educational and does not recommend a product, provider or trade.'], scenario=case, exercise=exercise,
            quiz=[['Explain the result and its limitations.', answer], ['What must be rechecked before use?', 'The current exchange specification, schedule, data entitlement and any broker-specific operational rule.']],
            mistake='Using a familiar ticker or chart label as proof of contract identity and current specifications.', evidence='Official CME product, schedule and market-data pages, checked 2026-10-30; original educational scenarios.', sources=refs)
        new.append(mission)
        body = f'# {mid} - {title}\n\n## Objective\n{mission["objective"]}\n\n## Synthetic case\n{case}\n\n## Concept\n{concept}\n\n![{title}](../../../assets/illustrations/{visual})\n\n## Practice\n{exercise}\n\n## Answer rationale\n{answer}\n\n## References\n'
        body += '\n'.join(f'- [{SOURCES[k][0]}]({SOURCES[k][1]})' for k in refs) + '\n'
        (folder / f'{mid}.md').write_text(body, encoding='utf-8')
        im = Image.new('RGB', (1600, 900), '#f7fafc'); d = ImageDraw.Draw(im)
        d.text((60, 45), f'{mid} | {title}', font=font, fill='#172554')
        d.text((60, 110), 'ORIGINAL SYNTHETIC EXERCISE | Verify current official specifications', font=small, fill='#166534')
        for index, stage in enumerate(flow.split(' | ')):
            y = 200 + index * 125; d.rounded_rectangle((60,y,1540,y+95), radius=12, outline='#64748b', width=3)
            d.text((90,y+28), f'{index+1}. {stage}', font=font, fill=['#1d4ed8','#166534','#9f1239','#172554'][index])
        d.text((60, 755), '\n'.join(textwrap.wrap(answer, 108)), font=small, fill='#171717')
        im.save(R / 'assets/illustrations' / visual)
    save('data/missions_en-US_01_110.json', load('data/missions_en-US_01_100.json') + new)
    save('data/level6_instrument_missions_en-US.json', new)
    c=load('data/curriculum.json'); c.update(version='0.12.0', authored_missions=110); c['content_status']['en-US']='missions_01_110_authored'; save('data/curriculum.json',c)
    t=load('data/translation_status.json'); t['project_version']='0.12.0'; t['english_master']['authored_missions']=110
    t['missions']=[m for m in t['missions'] if m['id'] not in {x['id'] for x in new}]+[{'id':m['id'],'en-US':'draft_complete','ar':'deferred'} for m in new]; save('data/translation_status.json',t)
    (R/'VERSION').write_text('0.12.0\n', encoding='utf-8')
    subprocess.run([sys.executable, 'scripts/build_handbook.py'], cwd=R, check=True)

if __name__ == '__main__': main()
