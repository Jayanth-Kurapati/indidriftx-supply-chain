def get_investment_data(severity=40):

    severity_factor = severity / 40

    sectors = [
        {
            "sector": "AI & Data Centers",
            "signal": "HIGH RISK",
            "risk_score": min(100, round(92 * severity_factor)),
            "opportunity_score": max(5, round(35 / severity_factor)),
            "reasoning": "NVIDIA, AMD fully dependent on TSMC. GPU supply halts within 60 days. Short-term severe loss expected.",
            "key_stocks": ["NVDA", "AMD", "SMCI"],
            "action": "SELL / SHORT TERM AVOID",
            "expected_change_pct": round(-45 * severity_factor),
            "color": "red"
        },
        {
            "sector": "Consumer Electronics",
            "signal": "HIGH RISK",
            "risk_score": min(100, round(88 * severity_factor)),
            "opportunity_score": max(5, round(30 / severity_factor)),
            "reasoning": "Apple, Samsung face immediate production halts. Revenue loss expected post-shock.",
            "key_stocks": ["AAPL", "SSNLF", "SONY"],
            "action": "SELL / REDUCE EXPOSURE",
            "expected_change_pct": round(-38 * severity_factor),
            "color": "red"
        },
        {
            "sector": "Automotive (EV)",
            "signal": "HIGH RISK",
            "risk_score": min(100, round(82 * severity_factor)),
            "opportunity_score": max(5, round(40 / severity_factor)),
            "reasoning": "EVs use 3x more chips than combustion vehicles. Production delays increase with severity.",
            "key_stocks": ["TSLA", "RIVN", "GM"],
            "action": "REDUCE EXPOSURE",
            "expected_change_pct": round(-28 * severity_factor),
            "color": "red"
        },
        {
            "sector": "US Domestic Chip Makers",
            "signal": "BUY OPPORTUNITY",
            "risk_score": max(5, round(25 / severity_factor)),
            "opportunity_score": min(100, round(90 * severity_factor)),
            "reasoning": "Intel, GlobalFoundries, Micron benefit directly as demand shifts away from Taiwan.",
            "key_stocks": ["INTC", "GFS", "MU"],
            "action": "STRONG BUY",
            "expected_change_pct": round(42 * severity_factor),
            "color": "green"
        },
        {
            "sector": "Defense & Aerospace",
            "signal": "BUY OPPORTUNITY",
            "risk_score": max(5, round(30 / severity_factor)),
            "opportunity_score": min(100, round(82 * severity_factor)),
            "reasoning": "Governments accelerate domestic semiconductor security programs.",
            "key_stocks": ["LMT", "RTX", "NOC"],
            "action": "BUY",
            "expected_change_pct": round(28 * severity_factor),
            "color": "green"
        },
        {
            "sector": "Chip Equipment Makers",
            "signal": "BUY OPPORTUNITY",
            "risk_score": max(5, round(28 / severity_factor)),
            "opportunity_score": min(100, round(88 * severity_factor)),
            "reasoning": "ASML and equipment providers benefit as countries build alternative fabs.",
            "key_stocks": ["ASML", "AMAT", "LRCX"],
            "action": "STRONG BUY",
            "expected_change_pct": round(38 * severity_factor),
            "color": "green"
        },
        {
            "sector": "Logistics & Shipping",
            "signal": "HOLD",
            "risk_score": min(100, round(55 * severity_factor)),
            "opportunity_score": min(100, round(58 * severity_factor)),
            "reasoning": "Air freight demand rises while electronics volume declines.",
            "key_stocks": ["FDX", "UPS", "MAERSK"],
            "action": "HOLD",
            "expected_change_pct": round(8 * severity_factor),
            "color": "yellow"
        },
        {
            "sector": "Banking & Finance",
            "signal": "HOLD",
            "risk_score": min(100, round(52 * severity_factor)),
            "opportunity_score": min(100, round(50 * severity_factor)),
            "reasoning": "Credit and trade finance risks increase as supply chains weaken.",
            "key_stocks": ["JPM", "GS", "BAC"],
            "action": "HOLD — MONITOR",
            "expected_change_pct": round(-5 * severity_factor),
            "color": "yellow"
        },
        {
            "sector": "FMCG & Retail",
            "signal": "HOLD",
            "risk_score": min(100, round(45 * severity_factor)),
            "opportunity_score": min(100, round(52 * severity_factor)),
            "reasoning": "Indirect impact from inflation and reduced discretionary spending.",
            "key_stocks": ["PG", "WMT", "COST"],
            "action": "HOLD",
            "expected_change_pct": round(-8 * severity_factor),
            "color": "yellow"
        },
        {
            "sector": "Energy",
            "signal": "HOLD",
            "risk_score": min(100, round(40 * severity_factor)),
            "opportunity_score": min(100, round(55 * severity_factor)),
            "reasoning": "Industrial demand slows, but energy infrastructure remains resilient.",
            "key_stocks": ["XOM", "NEE", "CVX"],
            "action": "HOLD",
            "expected_change_pct": round(-3 * severity_factor),
            "color": "yellow"
        }
    ]

    portfolio_summary = {
        "strong_buy": [s["sector"] for s in sectors if s["action"] == "STRONG BUY"],
        "buy": [s["sector"] for s in sectors if s["action"] == "BUY"],
        "hold": [s["sector"] for s in sectors if s["signal"] == "HOLD"],
        "avoid": [s["sector"] for s in sectors if s["risk_score"] > 75],
        "overall_market_impact": f"Severity {severity}% shock expected to create elevated market volatility and semiconductor shortages.",
        "recovery_timeline": "18-24 months for full market stabilization"
    }

    return {
        "severity": severity,
        "sectors": sectors,
        "portfolio_summary": portfolio_summary,
        "total_sectors_analyzed": len(sectors)
    }