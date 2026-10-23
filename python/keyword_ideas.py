"""Seed keywords -> autocomplete ideas from Google and YouTube -> CSV.

Usage:
    pip install apify-client
    export APIFY_TOKEN=your_token_here
    python keyword_ideas.py "standing desk"

Price: $0.005 per run + $0.0005 per lookup (one lookup returns up to 10-25 ideas).
Store page: https://apify.com/reliable-feeds/autocomplete-keyword-ideas
"""
import csv
import os
import sys

from apify_client import ApifyClient

seeds = sys.argv[1:] or ["standing desk"]
client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("reliable-feeds/autocomplete-keyword-ideas").call(
    run_input={
        "keywords": seeds,
        "sources": ["google", "youtube"],          # also: "bing", "amazon"
        "expansions": ["alphabet", "questions"],    # also: "prepositions", "numbers"
        "country": "us",
        "language": "en",
        "maxResults": 2000,
    }
)

rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())
fields = ["keyword", "suggestion", "source", "isQuestion", "position", "wordCount", "query"]
out = "keyword_ideas.csv"
with open(out, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

questions = [r for r in rows if r["isQuestion"]]
print(f"{len(rows)} unique ideas ({len(questions)} questions) saved to {out}")
for r in questions[:10]:
    print(f"  [{r['source']}] {r['suggestion']}")
