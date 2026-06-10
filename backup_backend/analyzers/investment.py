def get_investment_data():
    sectors = [
        {
            "sector": "AI & Data Centers",
            "signal": "HIGH RISK",
            "risk_score": 92,
            "opportunity_score": 35,
            "reasoning": "NVIDIA, AMD fully dependent on TSMC. GPU supply halts within 60 days. Short-term severe loss expected.",
            "key_stocks": ["NVDA", "AMD", "SMCI"],
            "action": "SELL / SHORT TERM AVOID",
            "expected_change_pct": -45,
            "color": "red"
        },
        {
            "sector": "Consumer Electronics",
            "signal": "HIGH RISK",
            "risk_score": 88,
            "opportunity_score": 30,
            "reasoning": "Apple, Samsung face immediate production halts. Revenue loss of $67B expected in Q1 post-shock.",
            "key_stocks": ["AAPL", "SSNLF", "SONY"],
            "action": "SELL / REDUCE EXPOSURE",
            "expected_change_pct": -38,
            "color": "red"
        },
        {
            "sector": "Automotive (EV)",
            "signal": "HIGH RISK",
            "risk_score": 82,
            "opportunity_score": 40,
            "reasoning": "EVs use 3x more chips than combustion vehicles. Tesla, BYD face delivery delays and margin compression.",
            "key_stocks": ["TSLA", "RIVN", "GM"],
            "action": "REDUCE EXPOSURE",
            "expected_change_pct": -28,
            "color": "red"
        },
        {
            "sector": "US Domestic Chip Makers",
            "signal": "BUY OPPORTUNITY",
            "risk_score": 25,
            "opportunity_score": 90,
            "reasoning": "Intel, GlobalFoundries, Micron benefit directly. US CHIPS Act funding accelerates. Demand for domestic production surges.",
            "key_stocks": ["INTC", "GFS", "MU"],
            "action": "STRONG BUY",
            "expected_change_pct": 42,
            "color": "green"
        },
        {
            "sector": "Defense & Aerospace",
            "signal": "BUY OPPORTUNITY",
            "risk_score": 30,
            "opportunity_score": 82,
            "reasoning": "Governments accelerate defense spending and domestic chip security programs. Lockheed, Raytheon benefit.",
            "key_stocks": ["LMT", "RTX", "NOC"],
            "action": "BUY",
            "expected_change_pct": 28,
            "color": "green"
        },
        {
            "sector": "Chip Equipment Makers",
            "signal": "BUY OPPORTUNITY",
            "risk_score": 28,
            "opportunity_score": 88,
            "reasoning": "ASML, Applied Materials, Lam Research see surge in orders as countries rush to build domestic fabs.",
            "key_stocks": ["ASML", "AMAT", "LRCX"],
            "action": "STRONG BUY",
            "expected_change_pct": 38,
            "color": "green"
        },
        {
            "sector": "Logistics & Shipping",
            "signal": "HOLD",
            "risk_score": 55,
            "opportunity_score": 58,
            "reasoning": "Mixed signals. Air freight demand spikes for chip components but overall electronics volume drops.",
            "key_stocks": ["FDX", "UPS", "MAERSK"],
            "action": "HOLD",
            "expected_change_pct": 8,
            "color": "yellow"
        },
        {
            "sector": "Banking & Finance",
            "signal": "HOLD",
            "risk_score": 52,
            "opportunity_score": 50,
            "reasoning": "Credit risk rises for electronics manufacturers. Trade finance disrupted. Inflation pressure on interest rates.",
            "key_stocks": ["JPM", "GS", "BAC"],
            "action": "HOLD — MONITOR",
            "expected_change_pct": -5,
            "color": "yellow"
        },
        {
            "sector": "FMCG & Retail",
            "signal": "HOLD",
            "risk_score": 45,
            "opportunity_score": 52,
            "reasoning": "Indirect impact through inflation and reduced consumer spending on discretionary goods.",
            "key_stocks": ["PG", "WMT", "COST"],
            "action": "HOLD",
            "expected_change_pct": -8,
            "color": "yellow"
        },
        {
            "sector": "Energy",
            "signal": "HOLD",
            "risk_score": 40,
            "opportunity_score": 55,
            "reasoning": "Reduced industrial activity lowers energy demand slightly. Solar/wind unaffected but smart grid projects delayed.",
            "key_stocks": ["XOM", "NEE", "CVX"],
            "action": "HOLD",
            "expected_change_pct": -3,
            "color": "yellow"
        }
    ]

    portfolio_summary = {
        "strong_buy": [s["sector"] for s in sectors if s["action"] == "STRONG BUY"],
        "buy": [s["sector"] for s in sectors if s["action"] == "BUY"],
        "hold": [s["sector"] for s in sectors if s["signal"] == "HOLD"],
        "avoid": [s["sector"] for s in sectors if s["risk_score"] > 75],
        "overall_market_impact": "Negative — estimated 12-18% broad market correction in first 90 days",
        "recovery_timeline": "18-24 months for full market stabilization"
    }

    return {
        "sectors": sectors,
        "portfolio_summary": portfolio_summary,
        "total_sectors_analyzed": len(sectors)
    }