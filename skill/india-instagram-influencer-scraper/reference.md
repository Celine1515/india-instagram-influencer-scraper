# Indra actor reference

## Identity

- Actor: `social_developer/india-instagram-influencer-scraper-modashs`
- ID: `s4XRSzZuVqawl63Ih`
- Publisher GitHub: `Celine1515`

## Input

| Field | Type | Notes |
|---|---|---|
| `category` | string | 120 Indian Instagram verticals |
| `followerBracket` | string | Nano / Micro / Mid-tier / Macro / Mega |
| `regionalFocus` | string | 650+ cities, e.g. Mumbai, Delhi |
| `avgViews` | string | `under_10k`, `10k_50k`, `50k_200k`, `200k_1m`, `1m_plus` (confirm against live schema) |
| `searchQuery` | string | Optional name or handle |
| `sortBy` | string | Default `sequential` |
| `resultsLimit` | integer | 1–10,000 |

Read the live Input tab before inventing enum values: https://console.apify.com/actors/s4XRSzZuVqawl63Ih

## Output row

`fullName`, `username`, `url`, `category`, `followersCount`, `followerBracket`, `regionalFocus`, `postsCount`, `engagementRate`, `avgLikes`, `avgComments`, `avgViews`, `verified`, `discoveryCategories`, `country`, `platform`

`engagementRate` is a ratio (`0.0618` = 6.18%).
