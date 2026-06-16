def get_consumer_impact(severity=40):
    severity_factor = severity / 40

    # Verified sources:
    # - Deloitte 2026: 50% memory price spikes projected
    # - IDC India 2024: Smartphone ASP hit $259 all time high
    # - Counterpoint Research 2024: Mid range segment grew 35.3% YoY
    # - McKinsey/Reuters: EV chip count 1400-1500 vs 600-1000 ICE

    products = [
        {
            "product": "Smartphones (Premium)",
            "current_avg_price_usd": 999,
            "price_increase_pct": round(30 * severity_factor),
            "new_avg_price_usd": round(999 * (1 + 0.30 * severity_factor)),
            "shortage_risk": "Critical" if severity >= 40 else "High",
            "timeline_months": max(1, round(3 / severity_factor)),
            "reason": "Apple 100% TSMC dependent for A/M series. Qualcomm 100% TSMC dependent for premium Snapdragon chips.",
            "real_world_evidence": "Apple maintained prices but expanded margins to 46.2% in 2024 by shifting costs to services. A disruption removes this buffer entirely.",
            "affected_brands": ["Apple", "Samsung", "Google"]
        },
        {
            "product": "Smartphones (Mid-Range)",
            "current_avg_price_usd": 259,
            "price_increase_pct": round(25 * severity_factor),
            "new_avg_price_usd": round(259 * (1 + 0.25 * severity_factor)),
            "shortage_risk": "Critical" if severity >= 40 else "High",
            "timeline_months": max(1, round(2 / severity_factor)),
            "reason": "Mid-range brands already quietly raised prices 1000-3000 INR in India in 2024 due to memory chip costs (IDC, Counterpoint Research).",
            "real_world_evidence": "India smartphone ASP hit all time high of $259 in 2024. Mid range segment grew 35.3% YoY as consumers moved up tiers due to price pressure.",
            "affected_brands": ["Samsung", "Xiaomi", "Vivo", "Oppo"]
        },
        {
            "product": "Laptops & PCs",
            "current_avg_price_usd": 1100,
            "price_increase_pct": round(25 * severity_factor),
            "new_avg_price_usd": round(1100 * (1 + 0.25 * severity_factor)),
            "shortage_risk": "High",
            "timeline_months": max(1, round(4 / severity_factor)),
            "reason": "Intel and AMD processors rely on TSMC advanced nodes. Apple M-series 100% TSMC dependent.",
            "real_world_evidence": "Deloitte 2026 projects 50% memory price spikes creating severe supply constraints for standard electronics.",
            "affected_brands": ["Apple", "Dell", "HP", "Lenovo"]
        },
        {
            "product": "Electric Vehicles",
            "current_avg_price_usd": 45000,
            "price_increase_pct": round(15 * severity_factor),
            "new_avg_price_usd": round(45000 * (1 + 0.15 * severity_factor)),
            "shortage_risk": "High",
            "timeline_months": max(1, round(5 / severity_factor)),
            "reason": "EVs use 1,400-1,500 chips vs 600-1,000 in combustion vehicles (McKinsey, Reuters). Premium EVs like Tesla use 2,500+ chips.",
            "real_world_evidence": "2021 chip shortage caused automotive industry to lose $210B in revenue demonstrating direct semiconductor dependency.",
            "affected_brands": ["Tesla", "BYD", "Rivian", "GM"]
        },
        {
            "product": "AI Servers & Cloud Services",
            "current_avg_price_usd": 30000,
            "price_increase_pct": round(50 * severity_factor),
            "new_avg_price_usd": round(30000 * (1 + 0.50 * severity_factor)),
            "shortage_risk": "Critical",
            "timeline_months": max(1, round(2 / severity_factor)),
            "reason": "NVIDIA H100/B200 GPUs exclusively fabbed at TSMC. Deloitte confirms zero-sum competition for advanced wafer capacity.",
            "real_world_evidence": "Deloitte 2026 Global Semiconductor Outlook projects 50% price spikes in advanced components already underway.",
            "affected_brands": ["AWS", "Google Cloud", "Microsoft Azure"]
        },
        {
            "product": "Smart TVs",
            "current_avg_price_usd": 600,
            "price_increase_pct": round(20 * severity_factor),
            "new_avg_price_usd": round(600 * (1 + 0.20 * severity_factor)),
            "shortage_risk": "Medium",
            "timeline_months": max(1, round(6 / severity_factor)),
            "reason": "Display driver ICs and SoCs sourced from TSMC advanced nodes.",
            "real_world_evidence": "Consumer electronics BOM highly vulnerable to semiconductor cost increases per McKinsey analysis.",
            "affected_brands": ["Samsung", "LG", "Sony"]
        },
        {
            "product": "Gaming Consoles",
            "current_avg_price_usd": 500,
            "price_increase_pct": round(28 * severity_factor),
            "new_avg_price_usd": round(500 * (1 + 0.28 * severity_factor)),
            "shortage_risk": "High",
            "timeline_months": max(1, round(4 / severity_factor)),
            "reason": "Custom AMD chips for PS5 and Xbox Series X exclusively fabbed at TSMC on advanced nodes.",
            "real_world_evidence": "PS5 shortages during 2021-2022 chip crisis demonstrated how quickly gaming supply collapses under semiconductor stress.",
            "affected_brands": ["Sony PlayStation", "Microsoft Xbox"]
        },
        {
            "product": "Medical Devices",
            "current_avg_price_usd": 5000,
            "price_increase_pct": round(18 * severity_factor),
            "new_avg_price_usd": round(5000 * (1 + 0.18 * severity_factor)),
            "shortage_risk": "High" if severity >= 50 else "Medium",
            "timeline_months": max(1, round(6 / severity_factor)),
            "reason": "Critical diagnostic and monitoring equipment relies on advanced processors.",
            "real_world_evidence": "Healthcare sector faced severe device shortages during 2021 chip crisis highlighting critical infrastructure vulnerability.",
            "affected_brands": ["Medtronic", "GE Healthcare", "Philips"]
        }
    ]

    spending_impact = {
        "average_household_extra_annual_spend_usd": round(1200 * severity_factor),
        "most_impacted_segment": "Mid-range consumers — largest electronics buyers globally",
        "india_specific_impact": "India smartphone ASP already at all-time high $259 (IDC 2024). Mid-range price hikes of 1000-3000 INR already visible in market.",
        "inflation_contribution_pct": round(2.2 * severity_factor, 1),
        "description": f"A {severity}% Taiwan semiconductor disruption will add approximately ${round(1200 * severity_factor)} in extra annual spending per household globally, with mid-range consumers in emerging markets like India feeling the impact first and most severely."
    }

    shortage_timeline = [
        {
            "month": "Month 1-2",
            "event": "Chip inventory buffers begin depleting. Spot prices surge 40-50%. Premium smartphone and AI server allocations prioritized."
        },
        {
            "month": "Month 3-4",
            "event": "Mid-range smartphone and laptop production cuts announced. Brands quietly raise prices 15-25%. India market ASP rises further."
        },
        {
            "month": "Month 5-6",
            "event": "EV deliveries delayed globally. Cloud service pricing increases 30-50%. Consumer panic buying begins in electronics."
        },
        {
            "month": "Month 7-9",
            "event": "Full price impact visible across all categories. Medical device shortages emerge. Government intervention begins."
        },
        {
            "month": "Month 10-12",
            "event": "Samsung Foundry absorbs partial demand but cannot fill gap. CHIPS Act funding accelerated. Prices stabilize but remain elevated."
        },
        {
            "month": "Month 13-18",
            "event": "New fab investments announced. Slow recovery begins. Prices remain 15-20% above pre-shock levels for advanced products."
        }
    ]

    return {
        "products": products,
        "spending_impact": spending_impact,
        "shortage_timeline": shortage_timeline,
        "total_products_affected": len(products),
        "data_sources": [
            "IDC India 2024 - Smartphone Market Report",
            "Counterpoint Research 2024 - India Smartphone Share",
            "Deloitte 2026 Global Semiconductor Outlook",
            "McKinsey Semiconductors 2024",
            "Reuters - EV Semiconductor Count",
            "Morningstar - Apple Profit Margin Analysis"
        ]
    }