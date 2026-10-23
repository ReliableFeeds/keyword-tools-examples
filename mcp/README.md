# Use from AI agents (MCP)

The tool works through the [Apify MCP server](https://docs.apify.com/platform/integrations/mcp), so Claude, Cursor, VS Code and other MCP-capable agents can call it directly.

## Hosted server (recommended)

Add this server URL to your MCP client. On first connection you sign in to Apify in the browser (OAuth):

```
https://mcp.apify.com?tools=reliable-feeds/autocomplete-keyword-ideas
```

Or authenticate with a token instead of signing in:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com?tools=reliable-feeds/autocomplete-keyword-ideas",
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
      "args": ["-y", "@apify/actors-mcp-server", "--tools", "reliable-feeds/autocomplete-keyword-ideas"],
      "env": { "APIFY_TOKEN": "<APIFY_TOKEN>" }
    }
  }
}
```

## Things to ask your agent

- "Find the questions people search about standing desks on Google and YouTube."
- "What do shoppers type into Amazon UK about electric bikes?"
- "Give me 200 long-tail blog topic ideas around home espresso machines, grouped by question type."

Billing is per lookup through your Apify account ($0.0005 per lookup, up to 10–25 ideas each). Set a maximum cost per run in Apify Console for a hard cap.
