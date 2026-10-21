"""Get Google search volume, CPC, difficulty and intent for a list of keywords.

Usage:
    pip install apify-client
    export APIFY_TOKEN=your_token_here
    python search_volume.py

Price: $0.02 per run + $0.003 per keyword that returns data. Keywords with no data are free.
Store page: https://apify.com/reliable-feeds/keyword-search-volume
"""
import csv
import os

from apify_client import ApifyClient

KEYWORDS = [
    "standing desk",
    "standing desk converter",
    "electric standing desk",
    "how tall should a standing desk be",
]

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("reliable-feeds/keyword-search-volume").call(
    run_input={
        "keywords": KEYWORDS,
        "country": "us",          # us, gb, ca, au, de, fr, es, it, nl, in, br ... (26 countries)
        "minSearchVolume": 0,     # e.g. 100 to leave out tiny keywords (they are not charged)
        "includeNoData": True,    # list keywords with no data too (free)
    }
)

rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())
fields = ["keyword", "searchVolume", "cpc", "competitionLevel", "keywordDifficulty", "intent", "trend12mPct", "hasData"]

with open("search_volume.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

for r in rows:
    print(f"{r['keyword']:<40} {r['searchVolume'] or '-':>8}  CPC {r['cpc'] or '-':>6}  KD {r['keywordDifficulty'] or '-':>3}  {r['intent'] or ''}")
print(f"\nSaved {len(rows)} rows to search_volume.csv")
