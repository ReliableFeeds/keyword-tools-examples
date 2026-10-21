// Get Google search volume, CPC, difficulty and intent for a list of keywords.
//
// Usage:
//   npm install apify-client
//   export APIFY_TOKEN=your_token_here
//   node search_volume.mjs
//
// Price: $0.02 per run + $0.003 per keyword that returns data. Keywords with no data are free.
// Store page: https://apify.com/reliable-feeds/keyword-search-volume
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('reliable-feeds/keyword-search-volume').call({
    keywords: ['standing desk', 'standing desk converter', 'electric standing desk'],
    country: 'gb', // us, gb, ca, au, de, fr, es, it, nl, in, br ... (26 countries)
    findIdeas: false, // true = also add related Google autocomplete searches, all with metrics
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.table(items.map((r) => ({
    keyword: r.keyword,
    volume: r.searchVolume,
    cpc: r.cpc,
    difficulty: r.keywordDifficulty,
    intent: r.intent,
})));
