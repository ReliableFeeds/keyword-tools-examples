"""Seed keyword -> autocomplete ideas (Google + YouTube) -> search volume for every idea -> CSV.

Usage:
    pip install apify-client
    export APIFY_TOKEN=your_token_here
    python ideas_to_volume.py "standing desk"

Step 1: Keyword Suggestions ($0.005 per run + $0.0005 per lookup; one lookup returns up to 10-25 ideas)
        https://apify.com/reliable-feeds/autocomplete-keyword-ideas
Step 2: Bulk Keyword Search Volume ($0.02 per run + $0.003 per keyword with data)
        https://apify.com/reliable-feeds/keyword-search-volume

Tip: the search volume tool also has a built-in "findIdeas" option (Google ideas only),
so for Google-only research you can skip step 1 and just set "findIdeas": True.
"""
import csv
import os
import sys

from apify_client import ApifyClient

seed = sys.argv[1] if len(sys.argv) > 1 else "standing desk"
client = ApifyClient(os.environ["APIFY_TOKEN"])

# 1) Ideas from Google and YouTube autocomplete
ideas_run = client.actor("reliable-feeds/autocomplete-keyword-ideas").call(
    run_input={
        "keywords": [seed],
        "sources": ["google", "youtube"],
        "expansions": ["alphabet", "questions"],
        "country": "us",
        "language": "en",
        "maxResults": 1000,
    }
)
ideas = sorted({row["suggestion"] for row in client.dataset(ideas_run["defaultDatasetId"]).iterate_items()})
print(f"Found {len(ideas)} unique ideas for '{seed}'")

# 2) Search volume, CPC, difficulty and intent for every idea
volume_run = client.actor("reliable-feeds/keyword-search-volume").call(
    run_input={"keywords": [seed] + ideas, "country": "us", "minSearchVolume": 10, "includeNoData": False}
)
rows = list(client.dataset(volume_run["defaultDatasetId"]).iterate_items())

fields = ["keyword", "searchVolume", "cpc", "keywordDifficulty", "intent", "isQuestion", "trend12mPct"]
out = f"{seed.replace(' ', '_')}_keywords.csv"
with open(out, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

print(f"{len(rows)} keywords with at least 10 searches a month saved to {out}")
for r in rows[:10]:
    print(f"  {r['keyword']:<45} {r['searchVolume']:>7}  KD {r['keywordDifficulty'] if r['keywordDifficulty'] is not None else '-':>3}  {r['intent'] or ''}")
