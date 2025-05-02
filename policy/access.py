def compute_access_score(device_health, network_trust, geo_loc, time_ctx):
    return 0.4 * device_health + 0.3 * network_trust + 0.2 * geo_loc + 0.1 * time_ctx

def compute_risk_score(rh, rc, rr):
    import math
    return 0.5 * rh + 0.3 * (1 - math.exp(-2 * rc)) + 0.2 * rr
