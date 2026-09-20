"""Thin client for Indra — India Instagram influencer scraper."""

from __future__ import annotations

import os
from typing import Any, Iterable

ACTOR_ID = "s4XRSzZuVqawl63Ih"
ACTOR = "social_developer/india-instagram-influencer-scraper-modashs"
STORE = f"https://apify.com/{ACTOR}"


def search_influencers(
    *,
    category: str = "",
    follower_bracket: str = "",
    regional_focus: str = "",
    avg_views: str = "",
    search_query: str = "",
    sort_by: str = "sequential",
    results_limit: int = 100,
    token: str | None = None,
) -> list[dict[str, Any]]:
    """Fetch India Instagram influencer rows from the Indra graph."""
    from apify_client import ApifyClient

    client = ApifyClient(token or os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR_ID).call(
        run_input={
            "category": category,
            "followerBracket": follower_bracket,
            "regionalFocus": regional_focus,
            "avgViews": avg_views,
            "searchQuery": search_query,
            "sortBy": sort_by,
            "resultsLimit": results_limit,
        }
    )
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


def iterate_influencers(**kwargs: Any) -> Iterable[dict[str, Any]]:
    yield from search_influencers(**kwargs)


if __name__ == "__main__":
    rows = search_influencers(regional_focus="Mumbai", results_limit=5)
    for row in rows:
        print(row.get("username"), row.get("followersCount"))
