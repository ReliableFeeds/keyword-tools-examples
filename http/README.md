# Plain HTTP (curl)

One call runs the tool, waits for it to finish and returns the results as JSON. Works from any language, Zapier/Make webhooks, Google Apps Script, and so on.

## Search volume, CPC, difficulty, intent

```bash
curl -X POST \
  "https://api.apify.com/v2/acts/reliable-feeds~keyword-search-volume/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["standing desk", "standing desk converter"], "country": "us"}'
```

## Autocomplete keyword suggestions

```bash
curl -X POST \
  "https://api.apify.com/v2/acts/reliable-feeds~autocomplete-keyword-ideas/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["standing desk"], "sources": ["google", "youtube"], "expansions": ["questions"], "country": "us", "language": "en"}'
```

## Notes

- Get your token in Apify Console → Settings → API & Integrations. Keep it secret.
- Note the `~` between the username and the tool name in the URL.
- Synchronous calls wait up to about 5 minutes. For very large runs (thousands of keywords with ideas switched on), start the run with `/runs` and fetch the dataset when it finishes. See [Apify API docs](https://docs.apify.com/api/v2).
- Optional cost cap: add `?maxTotalChargeUsd=1` to the URL to cap a run at $1.
