# Use from AI agents (MCP)

Both tools work through the [Apify MCP server](https://docs.apify.com/platform/integrations/mcp), so Claude, Cursor, VS Code and other MCP-capable agents can call them directly.

## Hosted server (recommended)

Add this server URL to your MCP client. On first connection you sign in to Apify in the browser (OAuth):

```
https://mcp.apify.com?tools=reliable-feeds/keyword-search-volume,reliable-feeds/autocomplete-keyword-ideas
```

Or authenticate with a token instead of signing in:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com?tools=reliable-feeds/keyword-search-volume,reliable-feeds/autocomplete-keyword-ideas",
      "headers": {
        "Authorization": "Bearer <APIFY_TOKEN>"
      }
    }
  }
}
```

## Local server (if your client doesn't support remote servers)

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server", "--tools", "reliable-feeds/keyword-search-volume,reliable-feeds/autocomplete-keyword-ideas"],
      "env": { "APIFY_TOKEN": "<APIFY_TOKEN>" }
    }
  }
}
```

## Things to ask your agent

- "Get UK search volume, CPC and difficulty for these 50 keywords and sort by volume."
- "Find question keywords about electric bikes with at least 100 searches a month in the US."
- "Find UK keywords about standing desks with over 500 searches a month and difficulty under 30."
- "What do people type into YouTube about home espresso machines? Then get Google search volume for the top 30."

The agent pays per event through your Apify account: $0.003 per keyword with data for search volume, and $0.0005 per lookup for autocomplete. Set a maximum cost per run in Apify Console if you want a hard cap.
