def engagement_rate(likes: int, followers: int) -> float:
    try:
        if followers <= 0:
            return 0.0
        return round((likes / followers) * 100, 2)
    except:
        return 0.0

def safe_int(v):
    try:
        return int(v)
    except:
        return 0
