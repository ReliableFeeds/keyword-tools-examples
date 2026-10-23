// Seed keywords -> autocomplete ideas from Google, YouTube, Bing and Amazon.
//
// Usage:
//   npm install apify-client
//   export APIFY_TOKEN=your_token_here
//   node keyword_ideas.mjs
//
// Price: $0.005 per run + $0.0005 per lookup (one lookup returns up to 10-25 ideas).
// Store page: https://apify.com/reliable-feeds/autocomplete-keyword-ideas
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('reliable-feeds/autocomplete-keyword-ideas').call({
    keywords: ['standing desk'],
    sources: ['google', 'youtube', 'bing', 'amazon'], // Amazon: US, CA, MX, GB, DE, FR, IT, ES
    expansions: ['questions'],
    country: 'gb',
    language: 'en',
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.table(items.slice(0, 25).map((r) => ({ source: r.source, suggestion: r.suggestion, question: r.isQuestion })));
console.log(`${items.length} unique ideas`);
