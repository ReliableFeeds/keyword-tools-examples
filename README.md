# Keyword ideas API examples (Apify)

Copy-paste examples for [**Keyword Suggestions: Google, YouTube, Bing, Amazon Autocomplete**](https://apify.com/reliable-feeds/autocomplete-keyword-ideas), a pay-per-use tool on the Apify Store.

It turns seed keywords into hundreds of real search phrases from the autocomplete boxes of Google, YouTube, Bing and Amazon, including the "how / what / why…" questions people ask, in any country and language.

**Price:** $0.005 per run + $0.0005 per lookup. One lookup (one typed query) returns up to 10–25 suggestions, so you pay per lookup, not per suggestion. In a test on 17 Oct 2026, one seed keyword with alphabet + questions expansion made 40 lookups and returned 527 unique ideas for $0.025.

You need a free [Apify account](https://apify.com) and its API token (Console → Settings → API & Integrations).

## Examples

| Folder | What's in it |
|---|---|
| [`python/`](python) | Seed keywords → ideas from Google + YouTube → CSV |
| [`javascript/`](javascript) | The same in Node.js |
| [`http/`](http) | One `curl` call that runs the tool and returns results directly |
| [`mcp/`](mcp) | Use it from Claude, Cursor, VS Code or any MCP-capable AI agent |
| [`n8n/`](n8n) | Call it from an n8n workflow with the HTTP Request node |

## Quick start (Python)

```bash
pip install apify-client
export APIFY_TOKEN=your_token_here
python python/keyword_ideas.py "standing desk"
```

## Output fields

`keyword` (your seed), `suggestion`, `source` (google, youtube, bing, amazon), `query` (the exact text typed), `modifierType`, `modifier`, `position` (rank in the autocomplete list), `depth`, `country`, `language`, `wordCount`, `isQuestion`.

## Feedback

Found a bug or want another source? Open an issue on the tool's **Issues** tab on Apify, or here.

MIT licence. Examples only; the tool itself runs on Apify.
