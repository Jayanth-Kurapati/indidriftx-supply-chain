def get_executive_summary(severity=40):
    severity_factor = severity / 40
    direct_loss = round(400 * (severity / 100), 1)
    total_loss = round(direct_loss * 3, 1)

    return {
        "title": "Executive Intelligence Brief",
        "subtitle": "Taiwan Semiconductor Supply Chain Disruption Scenario",
        "date": "June 2026",
        "classification": "BUSINESS SENSITIVE",

        "what_happened": {
            "heading": "What Happened",
            "content": f"A {severity}% disruption in Taiwan's semiconductor supply chain has been triggered, directly impacting TSMC — which controls 62-65% of the global foundry market (Gartner 2024) and 80-90% of advanced sub-7nm chip production globally. This is not a hypothetical risk — Deloitte's 2026 Global Semiconductor Outlook already identifies zero-sum competition for advanced wafer capacity as an active market condition. A {severity}% physical disruption would amplify this into a full scale supply crisis within weeks."
        },

        "who_is_affected": {
            "heading": "Who Is Affected",
            "sectors": [
                {
                    "name": "Consumer Electronics",
                    "impact": "Critical",
                    "detail": f"Apple purchases $67B in semiconductors annually from TSMC and is 100% dependent for A/M series chips. Qualcomm is 70-80% dependent overall and 100% for premium Snapdragon. Mid-range smartphone prices in India already hit all-time high ASP of $259 in 2024 (IDC) — a {severity}% disruption accelerates this sharply."
                },
                {
                    "name": "AI & Data Centers",
                    "impact": "Critical",
                    "detail": "NVIDIA H100/B200 GPUs are exclusively manufactured at TSMC. There is no alternative fab capable of producing these chips at any meaningful scale. Global AI infrastructure expansion pauses within 60 days of disruption."
                },
                {
                    "name": "Automotive & EV",
                    "impact": "High",
                    "detail": "EVs require 1,400-1,500 chips per vehicle vs 600-1,000 for combustion vehicles (McKinsey, Reuters). Tesla premium models use 2,500+ chips. Production halts begin within 90 days as existing inventory depletes."
                },
                {
                    "name": "Telecommunications",
                    "impact": "High",
                    "detail": "5G modem chips require advanced nodes exclusively produced at TSMC. With 79% of India smartphone shipments already 5G in 2024 (IDC), emerging markets face immediate network expansion delays."
                },
                {
                    "name": "Defense & Aerospace",
                    "impact": "High",
                    "detail": "Military modernization programs depend on advanced chips. Disruption immediately reframes semiconductor supply as national security emergency — CHIPS Act funding accelerates."
                }
            ]
        },

        "estimated_impact": {
            "heading": "Estimated Financial Impact",
            "global_gdp_impact_pct": round(-1.2 * severity_factor, 1),
            "total_industry_loss_bn": total_loss,
            "calculation_note": f"TSMC controls ~$400B of global chip supply. {severity}% disruption = ${direct_loss}B direct loss x McKinsey 3x GDP multiplier = ${total_loss}B downstream impact.",
            "consumer_extra_spend_bn": round(1200 * severity_factor),
            "inflation_contribution_pct": round(2.2 * severity_factor, 1),
            "market_correction_pct": round(-15 * severity_factor),
            "recovery_months": round(18 * severity_factor),
            "key_stat": f"Every 10% reduction in TSMC output = approximately ${round(400 * 0.10 * 3)}B in downstream industry losses globally (McKinsey multiplier applied to Gartner market share data)."
        },

        "recommendations": {
            "heading": "Strategic Recommendations",
            "for_businesses": [
                "Immediately audit semiconductor dependency across your entire product portfolio — identify which chips are TSMC-exclusive vs alternative-sourceable.",
                "Activate dual-sourcing agreements with Samsung Foundry and Intel Foundry Services for non-advanced node components where possible.",
                "Build 6-month chip inventory buffers for mission-critical components — 2021 chip crisis proved companies with buffers survived better.",
                "Accelerate R&D into chip-efficient product designs to reduce per-unit semiconductor dependency.",
                "Engage government relations teams for priority access under CHIPS Act provisions — defense and healthcare applications get priority."
            ],
            "for_investors": [
                "Rotate out of fabless chip companies (NVIDIA, AMD, Qualcomm) short term — their zero-fab model becomes their biggest vulnerability.",
                "Strong buy on US domestic chip makers: Intel Foundry, GlobalFoundries, Micron — Samsung only holds 15-17% of foundry market and is already at capacity.",
                "Strong buy on chip equipment makers: ASML, Applied Materials, Lam Research — every government will fund new fabs, all need equipment.",
                "Reduce Apple exposure — $67B annual TSMC spend with no alternative means hardware margins collapse in a sustained disruption.",
                "Monitor India consumer market — already showing price stress signals (IDC 2024 ASP data) that will amplify under disruption."
            ],
            "for_policymakers": [
                "Fast-track CHIPS Act funding disbursement — fab construction takes 3-5 years, every month of delay extends vulnerability.",
                "Establish national semiconductor strategic reserve similar to oil reserves — prioritize defense, healthcare, and critical infrastructure chips.",
                "Strengthen Taiwan relations and invest in supply chain diversification across South Korea, Japan, and EU.",
                "Mandate semiconductor supply chain transparency reporting for critical industries.",
                "Invest in workforce development — US needs 90,000 additional chip engineers by 2030 (SIA estimate)."
            ]
        },

        "bottom_line": f"A {severity}% Taiwan semiconductor disruption is not a technology problem — it is a national security and economic emergency. The $630B global semiconductor market (your research) with TSMC controlling 62-65% (Gartner) means there is no quick fix. Organizations that act within the first 30 days will minimize losses. Those that wait will face 18-24 months of constrained operations. The 2021 chip shortage cost the automotive industry alone $210B in lost revenue — and that was a minor disruption compared to this scenario."
    }