import requests
import os

FRED_API_KEY = os.getenv("FRED_API_KEY")

def fetch_fred(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations"
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

def get_shock_analysis():
    semiconductor_trade_value = 600  # USD Billion - TSMC + Taiwan exports real 2024 value
    disruption_pct = 0.40

    industries = [
        {
            "name": "Consumer Electronics",
            "dependency": 92,
            "revenue_loss_bn": round(semiconductor_trade_value * disruption_pct * 0.28, 1),
            "key_companies": ["Apple", "Samsung", "Sony"],
            "impact_level": "Critical"
        },
        {
            "name": "Automotive (EV & Smart Vehicles)",
            "dependency": 87,
            "revenue_loss_bn": round(semiconductor_trade_value * disruption_pct * 0.22, 1),
            "key_companies": ["Tesla", "Toyota", "GM"],
            "impact_level": "Critical"
        },
        {
            "name": "AI & Data Centers",
            "dependency": 95,
            "revenue_loss_bn": round(semiconductor_trade_value * disruption_pct * 0.25, 1),
            "key_companies": ["NVIDIA", "AMD", "Intel"],
            "impact_level": "Critical"
        },
        {
            "name": "Telecommunications",
            "dependency": 78,
            "revenue_loss_bn": round(semiconductor_trade_value * disruption_pct * 0.12, 1),
            "key_companies": ["Qualcomm", "Ericsson", "Nokia"],
            "impact_level": "High"
        },
        {
            "name": "Defense & Aerospace",
            "dependency": 72,
            "revenue_loss_bn": round(semiconductor_trade_value * disruption_pct * 0.08, 1),
            "key_companies": ["Lockheed Martin", "Raytheon", "BAE Systems"],
            "impact_level": "High"
        },
        {
            "name": "Medical Devices",
            "dependency": 65,
            "revenue_loss_bn": round(semiconductor_trade_value * disruption_pct * 0.05, 1),
            "key_companies": ["Medtronic", "Philips", "GE Healthcare"],
            "impact_level": "Medium"
        }
    ]

    affected_countries = [
        {"country": "Taiwan", "role": "Primary Supplier", "risk": 100},
        {"country": "South Korea", "role": "Secondary Supplier", "risk": 78},
        {"country": "USA", "role": "Major Consumer", "risk": 85},
        {"country": "China", "role": "Consumer & Restricted", "risk": 90},
        {"country": "Japan", "role": "Equipment Supplier", "risk": 70},
        {"country": "Germany", "role": "Automotive Consumer", "risk": 72},
        {"country": "India", "role": "Emerging Consumer", "risk": 55},
        {"country": "Vietnam", "role": "Assembly Hub", "risk": 60},
        {"country": "Netherlands", "role": "ASML Equipment", "risk": 65},
        {"country": "Malaysia", "role": "Packaging & Testing", "risk": 68}
    ]

    total_loss = sum(i["revenue_loss_bn"] for i in industries)

    return {
        "scenario": "Taiwan Semiconductor Supply Chain — 40% Disruption",
        "disruption_percentage": 40,
        "total_estimated_loss_bn": round(total_loss, 1),
        "industries": industries,
        "affected_countries": affected_countries,
        "shock_type": "Semiconductor",
        "timeline": "Impact felt within 3–6 months globally"
    }