def calculate_impact_level(dependency, disruption_pct):
    impact_score = dependency * disruption_pct

    if impact_score >= 35:
        return "Critical"
    elif impact_score >= 25:
        return "High"
    elif impact_score >= 15:
        return "Medium"
    else:
        return "Low"


def calculate_revenue_loss(trade_value, dependency, disruption_pct):
    return round(
        trade_value * (dependency / 100) * disruption_pct * 0.25,
        1
    )

def calculate_country_risk(base_risk, disruption_pct):
    risk = base_risk * (0.5 + disruption_pct)
    return min(round(risk), 100)