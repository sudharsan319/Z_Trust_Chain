def enforce_policy(access_score, risk_score):
    if access_score >= 0.85 and risk_score <= 0.4:
        return "Access Granted"
    elif risk_score > 0.7:
        return "Step-up Authentication Required"
    else:
        return "Access Denied"
