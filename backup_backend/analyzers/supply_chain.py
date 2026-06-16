def get_supply_chain_data():
    nodes = [
        {
            "id": "TSMC",
            "type": "supplier",
            "country": "Taiwan",
            "description": "World's largest semiconductor foundry. Produces 92% of world's most advanced chips (sub-7nm).",
            "disruption_impact": "Critical — no immediate alternative exists",
            "lat": 24.1477,
            "lng": 120.6736
        },
        {
            "id": "ASML",
            "type": "equipment",
            "country": "Netherlands",
            "description": "Sole manufacturer of EUV lithography machines required for advanced chip production.",
            "disruption_impact": "High — machines take 12-18 months to manufacture",
            "lat": 51.4416,
            "lng": 5.4697
        },
        {
            "id": "Samsung Foundry",
            "type": "supplier",
            "country": "South Korea",
            "description": "Second largest foundry. Can absorb ~15% of TSMC capacity at most.",
            "disruption_impact": "High — partial alternative but capacity constrained",
            "lat": 37.5665,
            "lng": 126.9780
        },
        {
            "id": "Apple",
            "type": "consumer",
            "country": "USA",
            "description": "100% dependent on TSMC for A-series and M-series chips.",
            "disruption_impact": "Critical — iPhone and Mac production halts within 60 days",
            "lat": 37.3349,
            "lng": -122.0090
        },
        {
            "id": "NVIDIA",
            "type": "consumer",
            "country": "USA",
            "description": "All AI GPUs (H100, B200) manufactured exclusively by TSMC.",
            "disruption_impact": "Critical — AI infrastructure expansion halts globally",
            "lat": 37.3688,
            "lng": -122.0363
        },
        {
            "id": "Intel",
            "type": "mixed",
            "country": "USA",
            "description": "Has own fabs but outsources advanced nodes to TSMC.",
            "disruption_impact": "Medium — can partially self-supply but loses competitive edge",
            "lat": 45.3311,
            "lng": -122.9937
        },
        {
            "id": "Toyota",
            "type": "consumer",
            "country": "Japan",
            "description": "Heavily dependent on automotive chips for smart vehicles and EVs.",
            "disruption_impact": "High — production slowdown within 90 days",
            "lat": 35.0844,
            "lng": 137.1522
        },
        {
            "id": "Foxconn",
            "type": "assembly",
            "country": "Taiwan",
            "description": "Primary assembler for Apple and other electronics brands.",
            "disruption_impact": "Critical — assembly halts if chip supply stops",
            "lat": 22.6273,
            "lng": 120.3014
        },
        {
            "id": "Qualcomm",
            "type": "consumer",
            "country": "USA",
            "description": "Snapdragon chips for Android smartphones — all fabbed at TSMC.",
            "disruption_impact": "Critical — Android ecosystem severely impacted",
            "lat": 32.8963,
            "lng": -117.2013
        },
        {
            "id": "MediaTek",
            "type": "consumer",
            "country": "Taiwan",
            "description": "Largest chip designer for mid-range smartphones globally.",
            "disruption_impact": "Critical — directly co-located with disruption source",
            "lat": 24.7881,
            "lng": 120.9969
        }
    ]

    dependency_chains = [
        {
            "chain": "TSMC → Apple → iPhone Production → Consumer Electronics Prices",
            "impact": "iPhone prices increase 25-40% within 6 months"
        },
        {
            "chain": "TSMC → NVIDIA → AI GPU Supply → Global AI Infrastructure",
            "impact": "AI server costs increase 60-80%, cloud pricing rises"
        },
        {
            "chain": "TSMC → Qualcomm → Android Phones → Telecom Industry",
            "impact": "Android mid-range phones face 3-6 month supply gap"
        },
        {
            "chain": "TSMC → Automotive Chips → Toyota/GM/Tesla → EV Production",
            "impact": "EV deliveries delayed 4-8 months, prices rise 15-20%"
        },
        {
            "chain": "ASML → TSMC Equipment → Samsung → Secondary Supply",
            "impact": "No new fab capacity possible for 18-24 months"
        }
    ]

    risk_by_country = [
        {"country": "Taiwan", "lat": 24.1477, "lng": 120.6736, "risk_score": 100, "reason": "Epicenter of disruption"},
        {"country": "USA", "lat": 37.0902, "lng": -95.7129, "risk_score": 88, "reason": "Largest consumer of advanced chips"},
        {"country": "China", "lat": 35.8617, "lng": 104.1954, "risk_score": 85, "reason": "Restricted access + high dependency"},
        {"country": "South Korea", "lat": 35.9078, "lng": 127.7669, "risk_score": 75, "reason": "Samsung under pressure to absorb demand"},
        {"country": "Japan", "lat": 36.2048, "lng": 138.2529, "risk_score": 70, "reason": "Automotive and electronics exposure"},
        {"country": "Germany", "lat": 51.1657, "lng": 10.4515, "risk_score": 68, "reason": "Automotive sector chip dependency"},
        {"country": "Netherlands", "lat": 52.1326, "lng": 5.2913, "risk_score": 62, "reason": "ASML equipment demand surge"},
        {"country": "Vietnam", "lat": 14.0583, "lng": 108.2772, "risk_score": 58, "reason": "Assembly hub disruption"},
        {"country": "Malaysia", "lat": 4.2105, "lng": 101.9758, "risk_score": 55, "reason": "Packaging and testing slowdown"},
        {"country": "India", "lat": 20.5937, "lng": 78.9629, "risk_score": 48, "reason": "Growing electronics import dependency"}
    ]

    return {
        "nodes": nodes,
        "dependency_chains": dependency_chains,
        "risk_by_country": risk_by_country,
        "total_nodes": len(nodes)
    }