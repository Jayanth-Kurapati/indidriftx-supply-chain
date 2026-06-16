import requests
import os

FRED_API_KEY = os.getenv("FRED_API_KEY")

def get_shock_analysis(severity=40):
    severity_factor = severity / 40
    disruption_pct = severity / 100

    # Verified: Global semiconductor market $630.5B (SIA / WSTS 2024 Factbook)
    # Verified: TSMC holds 62-65% of foundry market (Gartner 2024)
    # TSMC holds 80-90% of advanced chip market (sub-7nm) - cited as industry context, not yet pinned to one named report
    # Verified: McKinsey 3x GDP multiplier for semiconductor impact
    tsmc_revenue = 90  # USD Billion - TSMC Annual Revenue 2024
    tsmc_market_share = 0.63  # Gartner 2024
    global_semi_market = 630  # USD Billion - SIA/WSTS 2024 (rounded from $630.5B)
    tsmc_controlled = global_semi_market * tsmc_market_share  # ~$397B
    direct_loss = tsmc_controlled * disruption_pct
    multiplier = 3  # McKinsey GDP multiplier
    total_loss = direct_loss * multiplier

    industries = [
        {
            "name": "Consumer Electronics",
            "dependency": 90,
            "revenue_loss_bn": round(total_loss * 0.28, 1),
            "key_companies": ["Apple", "Samsung", "Qualcomm"],
            "impact_level": "Critical" if severity >= 40 else "High",
            "verified_insight": "Apple 100% TSMC dependent for A/M series chips. Qualcomm 70-80% dependent, 100% for premium Snapdragon. Mid-range phone prices in India already rose 25% YoY (IDC, Counterpoint Research 2024)."
        },
        {
            "name": "Automotive (EV & Smart Vehicles)",
            "dependency": 85,
            "revenue_loss_bn": round(total_loss * 0.22, 1),
            "key_companies": ["Tesla", "Toyota", "GM"],
            "impact_level": "Critical" if severity >= 60 else "High",
            "verified_insight": "EVs use 1,400-1,500 chips vs 600-1,000 in combustion vehicles (McKinsey, Reuters). Premium EVs like Tesla use up to 2,500+ chips. Supply disruption directly halts EV production lines."
        },
        {
            "name": "AI & Data Centers",
            "dependency": 95,
            "revenue_loss_bn": round(total_loss * 0.25, 1),
            "key_companies": ["NVIDIA", "AMD", "Intel"],
            "impact_level": "Critical",
            "verified_insight": "NVIDIA H100/B200 GPUs exclusively manufactured at TSMC. Deloitte 2026 outlook confirms zero-sum competition for advanced wafer capacity already causing 50% memory price spikes."
        },
        {
            "name": "Telecommunications",
            "dependency": 75,
            "revenue_loss_bn": round(total_loss * 0.12, 1),
            "key_companies": ["Qualcomm", "Ericsson", "Nokia"],
            "impact_level": "High",
            "verified_insight": "5G modem chips are exclusively advanced node products. 79% of India smartphone shipments in 2024 were 5G — directly exposed to TSMC disruption (IDC India 2024)."
        },
        {
            "name": "Defense & Aerospace",
            "dependency": 70,
            "revenue_loss_bn": round(total_loss * 0.08, 1),
            "key_companies": ["Lockheed Martin", "Raytheon", "BAE Systems"],
            "impact_level": "High",
            "verified_insight": "Military modernization programs depend on advanced chips. Governments will fast track domestic chip programs under CHIPS Act."
        },
        {
            "name": "Medical Devices",
            "dependency": 60,
            "revenue_loss_bn": round(total_loss * 0.05, 1),
            "key_companies": ["Medtronic", "Philips", "GE Healthcare"],
            "impact_level": "Medium" if severity < 60 else "High",
            "verified_insight": "Diagnostic and monitoring equipment rely on advanced processors. Supply disruption creates critical healthcare infrastructure risk."
        }
    ]

    affected_countries = [
        {
            "country": "Taiwan",
            "role": "Primary Supplier",
            "risk": min(100, round(100 * severity_factor)),
            "insight": "Epicenter. TSMC alone accounts for 62-65% of global foundry market (Gartner 2024)."
        },
        {
            "country": "USA",
            "role": "Major Consumer",
            "risk": min(100, round(88 * severity_factor)),
            "insight": "Apple purchases $67B in semiconductors annually from TSMC. NVIDIA, Qualcomm, AMD all fabless and TSMC dependent."
        },
        {
            "country": "China",
            "role": "Consumer & Restricted",
            "risk": min(100, round(85 * severity_factor)),
            "insight": "Already restricted from advanced TSMC nodes. Disruption accelerates domestic chip push but short term impact severe."
        },
        {
            "country": "South Korea",
            "role": "Secondary Supplier",
            "risk": min(100, round(75 * severity_factor)),
            "insight": "Samsung Foundry holds ~15-17% of global foundry market. Cannot absorb TSMC demand — already at capacity for AI chips."
        },
        {
            "country": "Japan",
            "role": "Equipment Supplier",
            "risk": min(100, round(70 * severity_factor)),
            "insight": "Toyota and automotive sector exposed. Japan also supplies critical chip manufacturing chemicals and equipment."
        },
        {
            "country": "India",
            "role": "Emerging Consumer",
            "risk": min(100, round(58 * severity_factor)),
            "insight": "India smartphone ASP hit all-time high of $259 in 2024 (IDC). Mid-range brands quietly raised prices 1000-3000 INR. 79% of shipments are 5G — highly chip dependent."
        },
        {
            "country": "Germany",
            "role": "Automotive Consumer",
            "risk": min(100, round(72 * severity_factor)),
            "insight": "BMW, Volkswagen, Mercedes heavily exposed. European EV transition makes automotive chip dependency critical."
        },
        {
            "country": "Netherlands",
            "role": "ASML Equipment",
            "risk": min(100, round(62 * severity_factor)),
            "insight": "ASML is sole manufacturer of EUV lithography machines. Paradoxically benefits from disruption as new fab orders surge."
        },
        {
            "country": "Vietnam",
            "role": "Assembly Hub",
            "risk": min(100, round(58 * severity_factor)),
            "insight": "Major electronics assembly hub for Samsung and Intel. Chip shortage halts assembly lines directly."
        },
        {
            "country": "Malaysia",
            "role": "Packaging & Testing",
            "risk": min(100, round(55 * severity_factor)),
            "insight": "Critical semiconductor packaging and testing hub. Disruption cascades into final chip delivery timelines."
        }
    ]

    total_loss_rounded = round(total_loss, 1)

    timeline = (
        "Impact felt within 1-2 months globally" if severity >= 60
        else "Impact felt within 3-6 months globally" if severity >= 30
        else "Impact felt within 6-12 months globally"
    )

    return {
        "scenario": "Taiwan Semiconductor Supply Chain Disruption",
        "disruption_percentage": severity,
        "total_estimated_loss_bn": total_loss_rounded,
        "tsmc_controlled_bn": round(tsmc_controlled, 1),
        "calculation_basis": f"TSMC controls ${round(tsmc_controlled)}B of global chip supply. {severity}% disruption = ${round(direct_loss)}B direct loss x McKinsey 3x multiplier ~= ${total_loss_rounded}B downstream impact.",
        "calculation_inputs": {
            "global_semiconductor_market_bn": global_semi_market,
            "tsmc_foundry_share_pct": round(tsmc_market_share * 100, 1),
            "mckinsey_gdp_multiplier": multiplier
        },
        "industries": industries,
        "affected_countries": affected_countries,
        "shock_type": "Semiconductor",
        "timeline": timeline,
        "data_sources": [
            "SIA / WSTS 2024 Factbook - Global Semiconductor Market Size",
            "Gartner 2024 - TSMC Foundry Market Share",
            "McKinsey Semiconductors 2024 - GDP Multiplier",
            "Deloitte 2026 Global Semiconductor Outlook",
            "IDC India 2024 - Smartphone Market",
            "Counterpoint Research 2024 - India Smartphone",
            "Reuters - EV Semiconductor Count",
            "TSMC Annual Report 2024"
        ]
    }