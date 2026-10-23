# n8n

Use the built-in **HTTP Request** node. No community nodes needed.

1. Add an **HTTP Request** node.
2. **Method:** `POST`
3. **URL:** `https://api.apify.com/v2/acts/reliable-feeds~autocomplete-keyword-ideas/run-sync-get-dataset-items`
4. **Authentication:** Generic credential type → **Header Auth**.
   - Name: `Authorization`
   - Value: `Bearer YOUR_APIFY_TOKEN`
5. **Send Body:** on. **Body Content Type:** JSON. **Specify Body:** Using JSON:

   ```json
   {
     "keywords": ["standing desk"],
     "sources": ["google", "youtube"],
     "expansions": ["alphabet", "questions"],
     "country": "us",
     "language": "en"
   }
   ```

   To feed seeds from an earlier node, use an expression, e.g. `{{ JSON.stringify({ keywords: $json.keywords, sources: ["google"] }) }}`.
6. Run the node. Each suggestion comes back as one item (`suggestion`, `source`, `isQuestion`, `position`, and so on). Send them to Google Sheets, Airtable, Notion or Slack from there.

**Idea:** schedule it weekly for your core topics and post the new questions to a Slack channel as content ideas.
