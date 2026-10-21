# n8n

Use the built-in **HTTP Request** node. No community nodes needed.

1. Add an **HTTP Request** node.
2. **Method:** `POST`
3. **URL:** `https://api.apify.com/v2/acts/reliable-feeds~keyword-search-volume/run-sync-get-dataset-items`
4. **Authentication:** Generic credential type → **Header Auth**.
   - Name: `Authorization`
   - Value: `Bearer YOUR_APIFY_TOKEN`
5. **Send Body:** on. **Body Content Type:** JSON. **Specify Body:** Using JSON:

   ```json
   {
     "keywords": ["standing desk", "standing desk converter"],
     "country": "us",
     "minSearchVolume": 50
   }
   ```

   To feed keywords from an earlier node, use an expression, e.g. `{{ JSON.stringify({ keywords: $json.keywords, country: "us" }) }}`.
6. Run the node. Each keyword comes back as one item: `keyword`, `searchVolume`, `cpc`, `keywordDifficulty`, `intent`, and so on. Send them to Google Sheets, Airtable or Slack from there.

For autocomplete ideas, use the same setup with this URL:

`https://api.apify.com/v2/acts/reliable-feeds~autocomplete-keyword-ideas/run-sync-get-dataset-items`

and a body like `{"keywords": ["standing desk"], "sources": ["google"], "expansions": ["alphabet", "questions"]}`.

**Idea:** schedule the workflow monthly to track search volume for your core keywords over time, using the `trend3mPct` and `trend12mPct` fields.
