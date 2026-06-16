def get_investment_data(severity=40):
    severity_factor = severity / 40

    # Verified sources:
    # - Gartner 2024: TSMC 62-65% foundry market share
    # - McKinsey 2024: Semiconductor GDP multiplier 3x
    # - Deloitte 2026: Zero-sum competition for advanced wafer capacity
    # - Counterpoint Research: Samsung Foundry 15-17% market share

    sectors = [
        {
            "sector": "AI & Data Centers",
            "signal": "HIGH RISK",
            "risk_score": min(100, round(92 * severity_factor)),
            "opportunity_score": min(100, max(10, round(35 / severity_factor))),
            "reasoning": f"NVIDIA and AMD are fully fabless — 100% dependent on TSMC for H100/B200 GPUs. A {severity}% disruption halts AI infrastructure expansion globally within 60 days. Deloitte 2026 confirms zero-sum wafer competition already underway.",
            "key_stocks": ["NVDA", "AMD", "SMCI"],
            "action": "SELL / SHORT TERM AVOID",
            "expected_change_pct": round(-45 * severity_factor),
            "color": "red",
            "human_insight": "Every major AI data center project globally depends on TSMC-made chips. There is no alternative fab capable of producing H100-class GPUs at any scale."
        },
        {
            "sector": "Consumer Electronics",
            "signal": "HIGH RISK",
            "risk_score": min(100, round(88 * severity_factor)),
            "opportunity_score": min(100, max(10, round(30 / severity_factor))),
            "reasoning": f"Apple purchases $67B in semiconductors annually from TSMC. A {severity}% disruption cuts iPhone production within 90 days. Mid-range Android brands already passing costs to consumers — trend accelerates sharply.",
            "key_stocks": ["AAPL", "SSNLF", "SONY"],
            "action": "SELL / REDUCE EXPOSURE",
            "expected_change_pct": round(-38 * severity_factor),
            "color": "red",
            "human_insight": "Apple survived 2022 chip crunch by using services revenue buffer. A 40%+ disruption eliminates that buffer entirely — hardware margins collapse."
        },
        {
            "sector": "Automotive (EV)",
            "signal": "HIGH RISK",
            "risk_score": min(100, round(82 * severity_factor)),
            "opportunity_score": min(100, max(10, round(40 / severity_factor))),
            "reasoning": f"EVs use 1,400-1,500 chips vs 600-1,000 in combustion vehicles (McKinsey, Reuters). Tesla uses 2,500+ chips per vehicle. A {severity}% disruption causes immediate production halts across all EV manufacturers.",
            "key_stocks": ["TSLA", "RIVN", "GM"],
            "action": "REDUCE EXPOSURE",
            "expected_change_pct": round(-28 * severity_factor),
            "color": "red",
            "human_insight": "Unlike 2021 chip shortage where automakers used older chips, modern EVs require cutting-edge nodes only TSMC can produce. No workaround exists."
        },
        {
            "sector": "US Domestic Chip Makers",
            "signal": "BUY OPPORTUNITY",
            "risk_score": max(10, round(25 / severity_factor)),
            "opportunity_score": min(100, round(90 * severity_factor)),
            "reasoning": f"Intel Foundry, GlobalFoundries, and Micron directly benefit as governments accelerate CHIPS Act funding. Every 10% TSMC capacity loss drives $15-20B in redirected orders to US fabs.",
            "key_stocks": ["INTC", "GFS", "MU"],
            "action": "STRONG BUY",
            "expected_change_pct": round(42 * severity_factor),
            "color": "green",
            "human_insight": "Samsung Foundry holds only 15-17% of global market and is already at capacity (Counterpoint Research). US domestic fabs are the only credible alternative — governments will fund them aggressively."
        },
        {
            "sector": "Defense & Aerospace",
            "signal": "BUY OPPORTUNITY",
            "risk_score": max(10, round(30 / severity_factor)),
            "opportunity_score": min(100, round(82 * severity_factor)),
            "reasoning": f"Governments accelerate defense spending and domestic chip security programs under national security framing. CHIPS Act provisions prioritize defense applications.",
            "key_stocks": ["LMT", "RTX", "NOC"],
            "action": "BUY",
            "expected_change_pct": round(28 * severity_factor),
            "color": "green",
            "human_insight": "Taiwan disruption immediately reframes semiconductor supply as a national security issue — defense budgets expand rapidly in response."
        },
        {
            "sector": "Chip Equipment Makers",
            "signal": "BUY OPPORTUNITY",
            "risk_score": max(10, round(28 / severity_factor)),
            "opportunity_score": min(100, round(88 * severity_factor)),
            "reasoning": f"ASML, Applied Materials, Lam Research see order surge as every government rushes to build domestic fabs. ASML is sole manufacturer of EUV machines — irreplaceable in this scenario.",
            "key_stocks": ["ASML", "AMAT", "LRCX"],
            "action": "STRONG BUY",
            "expected_change_pct": round(38 * severity_factor),
            "color": "green",
            "human_insight": "ASML EUV machines take 12-18 months to manufacture and cost $150M+ each. Demand will far exceed supply — pricing power is enormous."
        },
        {
            "sector": "Logistics & Shipping",
            "signal": "HOLD",
            "risk_score": min(100, round(55 * severity_factor)),
            "opportunity_score": min(100, round(55 * severity_factor)),
            "reasoning": "Air freight demand spikes for chip components and alternative sourcing. Overall electronics volume drops. Mixed signals create volatile but not catastrophic outlook.",
            "key_stocks": ["FDX", "UPS", "MAERSK"],
            "action": "HOLD",
            "expected_change_pct": round(5 * severity_factor),
            "color": "yellow",
            "human_insight": "Logistics benefits from rerouting supply chains but loses volume from reduced electronics manufacturing. Net effect is roughly neutral."
        },
        {
            "sector": "Banking & Finance",
            "signal": "HOLD",
            "risk_score": min(100, round(52 * severity_factor)),
            "opportunity_score": min(100, max(10, round(50 / severity_factor))),
            "reasoning": "Credit risk rises for electronics manufacturers. Trade finance disrupted. Inflation pressure increases interest rate uncertainty.",
            "key_stocks": ["JPM", "GS", "BAC"],
            "action": "HOLD — MONITOR",
            "expected_change_pct": round(-5 * severity_factor),
            "color": "yellow",
            "human_insight": "Banks with heavy exposure to consumer electronics manufacturers face rising credit default risk as revenue shortfalls emerge."
        },
        {
            "sector": "FMCG & Retail",
            "signal": "HOLD",
            "risk_score": min(100, round(45 * severity_factor)),
            "opportunity_score": min(100, max(10, round(52 / severity_factor))),
            "reasoning": "Indirect impact through inflation and reduced consumer discretionary spending. Electronics price hikes redirect wallet share away from FMCG.",
            "key_stocks": ["PG", "WMT", "COST"],
            "action": "HOLD",
            "expected_change_pct": round(-8 * severity_factor),
            "color": "yellow",
            "human_insight": "Indian middle class consumers already stretched by smartphone price hikes will reduce discretionary FMCG spending further."
        },
        {
            "sector": "Energy",
            "signal": "HOLD",
            "risk_score": min(100, round(40 * severity_factor)),
            "opportunity_score": min(100, round(55 * severity_factor)),
            "reasoning": "Reduced industrial activity lowers energy demand slightly. Solar and wind energy projects unaffected but smart grid chip dependent projects delayed.",
            "key_stocks": ["XOM", "NEE", "CVX"],
            "action": "HOLD",
            "expected_change_pct": round(-3 * severity_factor),
            "color": "yellow",
            "human_insight": "Energy transition projects requiring smart grid chips face delays — but traditional energy demand remains stable."
        }
    ]

    portfolio_summary = {
        "strong_buy": [s["sector"] for s in sectors if s["action"] == "STRONG BUY"],
        "buy": [s["sector"] for s in sectors if s["action"] == "BUY"],
        "hold": [s["sector"] for s in sectors if s["signal"] == "HOLD"],
        "avoid": [s["sector"] for s in sectors if s["risk_score"] > 75],
        "overall_market_impact": f"Negative — estimated {round(12 * severity_factor)}-{round(18 * severity_factor)}% broad market correction in first 90 days",
        "recovery_timeline": "18-24 months for full market stabilization",
        "key_opportunity": "US domestic chip makers and equipment suppliers are the primary beneficiaries — governments will fund them aggressively under national security framing"
    }

    return {
        "sectors": sectors,
        "portfolio_summary": portfolio_summary,
        "total_sectors_analyzed": len(sectors),
        "data_sources": [
            "Gartner 2024 - Foundry Market Share",
            "McKinsey Semiconductors 2024 - GDP Multiplier",
            "Deloitte 2026 - Global Semiconductor Outlook",
            "Counterpoint Research - Samsung Foundry Share",
            "Reuters - EV Semiconductor Count",
            "IDC India 2024 - Consumer Market Impact"
        ]
    }