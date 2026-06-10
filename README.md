# Global Supply Chain Shock Intelligence Platform

A web-based intelligence platform that simulates and analyzes the impact of global supply chain disruptions on industries, consumers, and investors.

## Scenario
**Scenario C — Taiwan Semiconductor Supply Chain 40% Disruption**

TSMC produces 92% of the world's most advanced chips. A 40% disruption cascades across every technology-dependent industry globally within months.

## Features
- **Shock Severity Simulator** — Adjust disruption level from 10% to 80% and see all metrics update dynamically
- **Industry Impact Analysis** — Revenue loss and dependency scores across 6 critical industries
- **Global Risk Map** — Color-coded country risk intensity with Leaflet.js
- **Supply Chain Ripple Effect** — Visual chain analysis across 4 industries (AI, Electronics, Automotive, Telecom)
- **Consumer Impact Analyzer** — Price increases and shortage timelines for 8 product categories
- **Investment Intelligence Dashboard** — Buy/Hold/Risk signals across 10 sectors
- **Executive Summary + PDF Export** — One-page CEO brief with downloadable report

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Leaflet.js, Chart.js
- **Backend:** Python, Flask, Flask-CORS
- **Data:** FRED API, World Bank, TSMC Public Filings, UN Comtrade

## Running Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend
Open `frontend/index.html` with Live Server in VS Code.

## Data Sources
- FRED (Federal Reserve Economic Data)
- World Bank Open Data
- TSMC Annual Reports 2024
- UN Comtrade Semiconductor Trade Data