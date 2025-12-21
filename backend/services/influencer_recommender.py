# very simple heuristic-based recommender
# map keywords to influencer categories

CATEGORY_MAP = {
    "beauty": ["beauty", "skincare", "makeup"],
    "fitness": ["fitness", "gym", "workout"],
    "tech": ["saas", "software", "tech"],
    "food": ["food", "restaurant", "cafe", "bakery"]
}

SAMPLE_INFLUENCERS = {
    "beauty": [
        {"handle":"@microbeauty_01","followers":12000},
        {"handle":"@skincare_tips","followers":53000}
    ],
    "fitness": [
        {"handle":"@fit_coach_1","followers":45000},
    ],
    "tech": [
        {"handle":"@tech_explain","followers":67000},
    ],
    "food": [
        {"handle":"@cityfoodlover","followers":21000},
    ]
}

def recommend_influencers(description: str, top_n:int=3):
    desc = (description or "").lower()
    best = "general"
    for cat, keywords in CATEGORY_MAP.items():
        for k in keywords:
            if k in desc:
                best = cat
                break
    return SAMPLE_INFLUENCERS.get(best, [])[:top_n]
