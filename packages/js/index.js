import { ApifyClient } from "apify-client";

export const ACTOR = "social_developer/india-instagram-influencer-scraper-modashs";
export const ACTOR_ID = "s4XRSzZuVqawl63Ih";
export const STORE = `https://apify.com/${ACTOR}`;

export async function searchInfluencers({
  category = "",
  followerBracket = "",
  regionalFocus = "",
  avgViews = "",
  searchQuery = "",
  sortBy = "sequential",
  resultsLimit = 100,
  token = process.env.APIFY_TOKEN,
} = {}) {
  const client = new ApifyClient({ token });
  const run = await client.actor(ACTOR_ID).call({
    category,
    followerBracket,
    regionalFocus,
    avgViews,
    searchQuery,
    sortBy,
    resultsLimit,
  });
  const { items } = await client.dataset(run.defaultDatasetId).listItems();
  return items;
}
