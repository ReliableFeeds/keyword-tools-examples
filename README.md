# Keyword research API examples (Apify)

Copy-paste examples for two pay-per-use keyword tools on the Apify Store:

| Tool | What it returns | Price |
|---|---|---|
| [**Bulk Keyword Search Volume, CPC, Difficulty & Intent**](https://apify.com/reliable-feeds/keyword-search-volume) | Monthly Google search volume, CPC, competition, keyword difficulty, search intent, 3- and 12-month trends, 12 months of history. Up to 10,000 keywords per run, 26 countries. | $0.02 per run + $0.003 per keyword **with** data. Keywords with no data are free. |
| [**Keyword Suggestions: Google, YouTube, Bing, Amazon Autocomplete**](https://apify.com/reliable-feeds/autocomplete-keyword-ideas) | Real autocomplete suggestions and questions from Google, YouTube, Bing and Amazon, in any country and language. | $0.005 per run + $0.0005 per lookup (one lookup returns up to 10–25 suggestions). |

No Google Ads account, no SEO subscription. You need a free [Apify account](https://apify.com) and its API token (Console → Settings → API & Integrations).

## Examples

| Folder | What's in it |
|---|---|
| [`python/`](python) | Search volume for a keyword list; seed keyword → ideas → volumes, saved to CSV |
| [`javascript/`](javascript) | The same in Node.js |
| [`http/`](http) | One `curl` call that runs a tool and returns the results directly |
| [`mcp/`](mcp) | Use both tools from Claude, Cursor, VS Code or any MCP-capable AI agent |
| [`n8n/`](n8n) | Call the tools from an n8n workflow with the HTTP Request node |

## Quick start (Python)

```bash
pip install apify-client
export APIFY_TOKEN=your_token_here
python python/search_volume.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("reliable-feeds/keyword-search-volume").call(
    run_input={"keywords": ["standing desk", "standing desk converter"], "country": "gb"}
)
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row["keyword"], row["searchVolume"], row["cpc"], row["keywordDifficulty"], row["intent"])
```

Example output from a real UK run (17 Oct 2026):

| Keyword | Monthly searches | CPC (USD) | Difficulty | Intent |
|---|---|---|---|---|
| standing desk | 33,100 | 3.40 | 19 | transactional |
| standing desk converter | 3,600 | 1.17 | 0 | transactional |
| standing desk uk | 1,900 | 5.08 | 32 | navigational |
| standing desk benefits | 1,000 | 2.02 | 26 | commercial |

## Output fields (search volume tool)

`keyword`, `hasData`, `searchVolume`, `cpc`, `competition`, `competitionLevel`, `keywordDifficulty`, `intent`, `secondaryIntents`, `trend3mPct`, `trend12mPct`, `lowTopOfPageBid`, `highTopOfPageBid`, `monthlySearches`, `isQuestion`, `wordCount`, `origin`, `seedKeyword`, `country`, `language`, `dataUpdatedAt`.

Full input options are in the **Input** tab of each Store page.

## Keeping costs predictable

- Both tools are pay per event: you only pay for what a run returns.
- Set a **maximum cost per run** in Apify Console, or pass `maxTotalChargeUsd` on API runs. The search volume tool then only looks up as many keywords as that budget covers.
- Data source for search volume: [DataForSEO](https://dataforseo.com), based on Google Ads Keyword Planner data, updated monthly.

## Feedback

Found a bug or want a country or field added? Open an issue on the tool's **Issues** tab on Apify, or here.

MIT licence. Examples only; the tools themselves run on Apify.
