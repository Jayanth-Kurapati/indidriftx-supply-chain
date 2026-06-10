from analyzers.impact_engine import (
    calculate_impact_level,
    calculate_revenue_loss,
    calculate_country_risk
)

import requests
import os

FRED_API_KEY = os.getenv("FRED_API_KEY")


def fetch_fred(series_id):
    url = "https://api.stlouisfed.org/fred/series/observations"

    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        return float(data["observations"][0]["value"])
    except:
        return None


def get_shock_analysis(severity=40):
    semiconductor_trade_value = 600
    disruption_pct = severity / 100

    industries = [
        {
            "name": "Consumer Electronics",
            "dependency": 92,
            "revenue_loss_bn": calculate_revenue_loss(
                semiconductor_trade_value,
                92,
                disruption_pct
            ),
            "key_companies": ["Apple", "Samsung", "Sony"],
            "impact_level": calculate_impact_level(
                92,
                disruption_pct
            )
        },
        {
            "name": "Automotive (EV & Smart Vehicles)",
            "dependency": 87,
            "revenue_loss_bn": calculate_revenue_loss(
                semiconductor_trade_value,
                87,
                disruption_pct
            ),
            "key_companies": ["Tesla", "Toyota", "GM"],
            "impact_level": calculate_impact_level(
                87,
                disruption_pct
            )
        },
        {
            "name": "AI & Data Centers",
            "dependency": 95,
            "revenue_loss_bn": calculate_revenue_loss(
                semiconductor_trade_value,
                95,
                disruption_pct
            ),
            "key_companies": ["NVIDIA", "AMD", "Intel"],
            "impact_level": calculate_impact_level(
                95,
                disruption_pct
            )
        },
        {
            "name": "Telecommunications",
            "dependency": 78,
            "revenue_loss_bn": calculate_revenue_loss(
                semiconductor_trade_value,
                78,
                disruption_pct
            ),
            "key_companies": ["Qualcomm", "Ericsson", "Nokia"],
            "impact_level": calculate_impact_level(
                78,
                disruption_pct
            )
        },
        {
            "name": "Defense & Aerospace",
            "dependency": 72,
            "revenue_loss_bn": calculate_revenue_loss(
                semiconductor_trade_value,
                72,
                disruption_pct
            ),
            "key_companies": ["Lockheed Martin", "Raytheon", "BAE Systems"],
            "impact_level": calculate_impact_level(
                72,
                disruption_pct
            )
        },
        {
            "name": "Medical Devices",
            "dependency": 65,
            "revenue_loss_bn": calculate_revenue_loss(
                semiconductor_trade_value,
                65,
                disruption_pct
            ),
            "key_companies": ["Medtronic", "Philips", "GE Healthcare"],
            "impact_level": calculate_impact_level(
                65,
                disruption_pct
            )
        }
    ]

    affected_countries = [
        {
            "country": "Taiwan",
            "role": "Primary Supplier",
            "risk": calculate_country_risk(100, disruption_pct)
        },
        {
            "country": "South Korea",
            "role": "Secondary Supplier",
            "risk": calculate_country_risk(78, disruption_pct)
        },
        {
            "country": "USA",
            "role": "Major Consumer",
            "risk": calculate_country_risk(85, disruption_pct)
        },
        {
            "country": "China",
            "role": "Consumer & Restricted",
            "risk": calculate_country_risk(90, disruption_pct)
        },
        {
            "country": "Japan",
            "role": "Equipment Supplier",
            "risk": calculate_country_risk(70, disruption_pct)
        },
        {
            "country": "Germany",
            "role": "Automotive Consumer",
            "risk": calculate_country_risk(72, disruption_pct)
        },
        {
            "country": "India",
            "role": "Emerging Consumer",
            "risk": calculate_country_risk(55, disruption_pct)
        },
        {
            "country": "Vietnam",
            "role": "Assembly Hub",
            "risk": calculate_country_risk(60, disruption_pct)
        },
        {
            "country": "Netherlands",
            "role": "ASML Equipment",
            "risk": calculate_country_risk(65, disruption_pct)
        },
        {
            "country": "Malaysia",
            "role": "Packaging & Testing",
            "risk": calculate_country_risk(68, disruption_pct)
        }
    ]

    total_loss = sum(
        industry["revenue_loss_bn"]
        for industry in industries
    )

    return {
        "scenario": f"Taiwan Semiconductor Supply Chain — {severity}% Disruption",
        "disruption_percentage": severity,
        "total_estimated_loss_bn": round(total_loss, 1),
        "industries": industries,
        "affected_countries": affected_countries,
        "shock_type": "Semiconductor",
        "timeline": (
    "Impact felt within 1–2 months globally" if severity >= 60
    else "Impact felt within 3–6 months globally" if severity >= 30
    else "Impact felt within 6–12 months globally"
),
    }