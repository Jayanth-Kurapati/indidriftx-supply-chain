def get_consumer_impact(severity=40):

    severity_factor = severity / 40

    products = [
        {
            "product": "Smartphones (Premium)",
            "current_avg_price_usd": 999,
            "price_increase_pct": round(35 * severity_factor),
            "new_avg_price_usd": round(
                999 * (
                    1 + (round(35 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "Critical",
            "timeline_months": 3,
            "reason": "A-series, Snapdragon chips 100% TSMC dependent",
            "affected_brands": ["Apple", "Samsung", "Google"]
        },
        {
            "product": "Laptops & PCs",
            "current_avg_price_usd": 1100,
            "price_increase_pct": round(28 * severity_factor),
            "new_avg_price_usd": round(
                1100 * (
                    1 + (round(28 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "High",
            "timeline_months": 4,
            "reason": "Intel, AMD processors rely on TSMC advanced nodes",
            "affected_brands": ["Apple", "Dell", "HP", "Lenovo"]
        },
        {
            "product": "Electric Vehicles",
            "current_avg_price_usd": 45000,
            "price_increase_pct": round(18 * severity_factor),
            "new_avg_price_usd": round(
                45000 * (
                    1 + (round(18 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "High",
            "timeline_months": 5,
            "reason": "EVs use 3x more semiconductors than combustion vehicles",
            "affected_brands": ["Tesla", "BYD", "Rivian", "GM"]
        },
        {
            "product": "AI Servers & Cloud Services",
            "current_avg_price_usd": 30000,
            "price_increase_pct": round(65 * severity_factor),
            "new_avg_price_usd": round(
                30000 * (
                    1 + (round(65 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "Critical",
            "timeline_months": 2,
            "reason": "NVIDIA H100/B200 GPUs exclusively fabbed at TSMC",
            "affected_brands": ["AWS", "Google Cloud", "Microsoft Azure"]
        },
        {
            "product": "Smart TVs",
            "current_avg_price_usd": 600,
            "price_increase_pct": round(22 * severity_factor),
            "new_avg_price_usd": round(
                600 * (
                    1 + (round(22 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "Medium",
            "timeline_months": 6,
            "reason": "Display driver ICs and SoCs sourced from TSMC",
            "affected_brands": ["Samsung", "LG", "Sony"]
        },
        {
            "product": "Home Appliances (Smart)",
            "current_avg_price_usd": 800,
            "price_increase_pct": round(15 * severity_factor),
            "new_avg_price_usd": round(
                800 * (
                    1 + (round(15 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "Medium",
            "timeline_months": 7,
            "reason": "IoT chips and microcontrollers sourced from Taiwan",
            "affected_brands": ["LG", "Whirlpool", "Bosch"]
        },
        {
            "product": "Gaming Consoles",
            "current_avg_price_usd": 500,
            "price_increase_pct": round(30 * severity_factor),
            "new_avg_price_usd": round(
                500 * (
                    1 + (round(30 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "High",
            "timeline_months": 4,
            "reason": "Custom AMD chips for PS5 and Xbox fabbed at TSMC",
            "affected_brands": ["Sony PlayStation", "Microsoft Xbox"]
        },
        {
            "product": "Medical Devices",
            "current_avg_price_usd": 5000,
            "price_increase_pct": round(20 * severity_factor),
            "new_avg_price_usd": round(
                5000 * (
                    1 + (round(20 * severity_factor) / 100)
                )
            ),
            "shortage_risk": "High",
            "timeline_months": 6,
            "reason": "Critical diagnostic equipment relies on advanced chips",
            "affected_brands": ["Medtronic", "GE Healthcare", "Philips"]
        }
    ]

    spending_impact = {
        "average_household_extra_annual_spend_usd": round(
            1850 * severity_factor
        ),
        "most_impacted_income_group": "Middle class (largest electronics consumers)",
        "inflation_contribution_pct": round(
            2.8 * severity_factor,
            1
        ),
        "consumer_confidence_drop_pct": round(
            18 * severity_factor
        ),
        "description": f"""
        A {severity}% Taiwan semiconductor disruption
        increases consumer spending globally due to
        higher electronics, transport and cloud service costs.
        """
    }

    shortage_timeline = [
        {
            "month": "Month 1-2",
            "event": "Chip inventory buffers begin depleting. Spot prices surge."
        },
        {
            "month": "Month 3-4",
            "event": "Smartphone and laptop production cuts announced."
        },
        {
            "month": "Month 5-6",
            "event": "EV deliveries delayed. AI cloud pricing increases."
        },
        {
            "month": "Month 7-9",
            "event": "Full price impact visible across electronics categories."
        },
        {
            "month": "Month 10-12",
            "event": "Alternative suppliers partially absorb demand."
        },
        {
            "month": "Month 13-18",
            "event": "Recovery begins as new capacity comes online."
        }
    ]

    return {
        "severity": severity,
        "products": products,
        "spending_impact": spending_impact,
        "shortage_timeline": shortage_timeline,
        "total_products_affected": len(products)
    }