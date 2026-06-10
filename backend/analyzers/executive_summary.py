def get_executive_summary(severity=40):

    severity_factor = severity / 40

    total_loss = round(240 * severity_factor)
    consumer_spend = round(1850 * severity_factor)
    inflation = round(2.8 * severity_factor, 1)
    market_correction = round(15 * severity_factor)
    recovery = round(18 * severity_factor)

    return {
        "title": "Executive Intelligence Brief",

        "subtitle": f"Taiwan Semiconductor Supply Chain — {severity}% Disruption Scenario",

        "date": "June 2026",

        "classification": "BUSINESS SENSITIVE",

        "what_happened": {
            "heading": "What Happened",
            "content": f"""
A {severity}% disruption in Taiwan's semiconductor supply chain has been triggered,
directly impacting TSMC and advanced chip production globally.
This disruption affects consumer electronics, AI infrastructure,
automotive manufacturing and telecommunications within weeks.
            """
        },

        "who_is_affected": {
            "heading": "Who Is Affected",
            "sectors": [
                {
                    "name": "Consumer Electronics",
                    "impact": "Critical",
                    "detail": "Apple, Samsung and Google face production constraints."
                },
                {
                    "name": "AI & Data Centers",
                    "impact": "Critical",
                    "detail": "GPU shortages increase cloud and AI infrastructure costs."
                },
                {
                    "name": "Automotive & EV",
                    "impact": "High",
                    "detail": "Vehicle production delays and semiconductor shortages."
                },
                {
                    "name": "Telecommunications",
                    "impact": "High",
                    "detail": "5G and networking equipment deployment slows."
                },
                {
                    "name": "Defense & Aerospace",
                    "impact": "High",
                    "detail": "Strategic procurement programs face delays."
                }
            ]
        },

        "estimated_impact": {
            "heading": "Estimated Financial Impact",
            "global_gdp_impact_pct": round(-1.2 * severity_factor, 1),
            "total_industry_loss_bn": total_loss,
            "consumer_extra_spend_bn": consumer_spend,
            "inflation_contribution_pct": inflation,
            "market_correction_pct": -market_correction,
            "recovery_months": recovery,
            "key_stat": f"""
Estimated global industry losses exceed
${total_loss} billion under the current scenario.
            """
        },

        "recommendations": {
            "heading": "Strategic Recommendations",

            "for_businesses": [
                "Audit semiconductor dependency across critical products.",
                "Activate secondary sourcing agreements.",
                "Increase inventory buffers for critical chips.",
                "Accelerate supply chain diversification.",
                "Review contingency procurement plans."
            ],

            "for_investors": [
                "Increase exposure to alternative foundries.",
                "Monitor semiconductor equipment makers.",
                "Reduce concentration risk in fabless chip companies.",
                "Track government semiconductor incentives.",
                "Focus on resilient infrastructure sectors."
            ],

            "for_policymakers": [
                "Accelerate domestic semiconductor initiatives.",
                "Diversify strategic supply chains.",
                "Increase transparency requirements.",
                "Strengthen international partnerships.",
                "Expand semiconductor workforce development."
            ]
        },

        "bottom_line": f"""
A {severity}% Taiwan semiconductor disruption represents a major
economic and strategic risk. Organizations that diversify supply
chains early will significantly reduce operational and financial impact.
        """
    }