let map;
let markers = [];
let industryChart = null;

const slider = document.getElementById("severitySlider");
const severityValue = document.getElementById("severityValue");
const reportButton =
    document.getElementById("downloadReportBtn");

slider.addEventListener("input", () => {
    const val = slider.value;
    const min = slider.min || 10;
    const max = slider.max || 80;
    const pct = ((val - min) / (max - min)) * 100;
    slider.style.background = `linear-gradient(to right, #3b82f6 ${pct}%, #2a2a4a ${pct}%)`;
    severityValue.textContent = val + "%";
    loadShockData(val);
});

function initializeMap() {

    map = L.map("map", {
        scrollWheelZoom: false,
        minZoom: 2,
        maxZoom: 6,
        maxBounds: [[-85, -180], [85, 180]],
        maxBoundsViscosity: 1.0
    }).setView([20, 0], 2);

L.tileLayer(
        "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        {
            attribution: "&copy; OpenStreetMap"
        }
    ).addTo(map);

    const legend = L.control({ position: "bottomright" });

    legend.onAdd = function () {
        const div = L.DomUtil.create("div", "map-legend");
        div.innerHTML = `
            <strong>Risk Level</strong><br>
            <span style="color:#ef4444;">● Critical (80-100)</span><br>
            <span style="color:#f97316;">● High (60-79)</span><br>
            <span style="color:#eab308;">● Medium (40-59)</span><br>
            <span style="color:#22c55e;">● Low (0-39)</span>
        `;
        return div;
    };

    legend.addTo(map);
}

function getCountryCoordinates(country) {

    const locations = {
        "Taiwan": [23.7, 121.0],
        "South Korea": [36.5, 127.8],
        "USA": [37.0, -95.0],
        "China": [35.0, 104.0],
        "Japan": [36.0, 138.0],
        "Germany": [51.0, 10.0],
        "India": [21.0, 78.0],
        "Vietnam": [16.0, 108.0],
        "Netherlands": [52.1, 5.3],
        "Malaysia": [4.2, 102.0]
    };

    return locations[country];
}

function updateMap(countries) {

    markers.forEach(marker => {
        map.removeLayer(marker);
    });

    markers = [];

    countries.forEach(country => {

        const coords = getCountryCoordinates(country.country);

        if (!coords) return;

        let color = "#22c55e";
        if (country.risk >= 80) color = "#ef4444";
        else if (country.risk >= 60) color = "#f97316";
        else if (country.risk >= 40) color = "#eab308";

        const circle = L.circleMarker(coords, {
            radius: 8 + (country.risk / 10),
            fillColor: color,
            color: color,
            weight: 2,
            opacity: 0.9,
            fillOpacity: 0.5
        }).addTo(map);

        circle.bindPopup(`
            <div style="font-family: sans-serif; min-width: 160px;">
                <strong style="font-size: 1rem;">${country.country}</strong><br>
                <span style="color: #666;">${country.role}</span><br><br>
                <span style="
                    background: ${color};
                    color: white;
                    padding: 2px 8px;
                    border-radius: 4px;
                    font-weight: bold;
                ">Risk Score: ${country.risk}</span>
            </div>
        `);

        markers.push(circle);
    });
}

function renderRippleEffects() {
    const rippleContainer = document.getElementById("rippleContainer");

    const chains = [
        {
            title: "AI & Data Centers Chain",
            color: "#3b82f6",
            nodes: [
                { label: "Taiwan Disruption", impact: 100, icon: "⚡" },
                { label: "TSMC Output Reduced", impact: 95, icon: "🏭" },
                { label: "NVIDIA / AMD Supply Falls", impact: 88, icon: "💻" },
                { label: "Cloud Infrastructure Costs Rise", impact: 74, icon: "☁️" },
                { label: "AI Services Expensive", impact: 60, icon: "🤖" }
            ]
        },
        {
            title: "Consumer Electronics Chain",
            color: "#ef4444",
            nodes: [
                { label: "Taiwan Disruption", impact: 100, icon: "⚡" },
                { label: "TSMC Chip Supply Falls", impact: 95, icon: "🏭" },
                { label: "Apple / Samsung Production Cuts", impact: 85, icon: "📱" },
                { label: "Retail Inventory Depletes", impact: 70, icon: "🏬" },
                { label: "Phone Prices Rise 35%", impact: 58, icon: "💸" }
            ]
        },
        {
            title: "Automotive & EV Chain",
            color: "#f97316",
            nodes: [
                { label: "Taiwan Disruption", impact: 100, icon: "⚡" },
                { label: "Automotive Chip Shortage", impact: 87, icon: "🏭" },
                { label: "EV Production Delayed", impact: 76, icon: "🚗" },
                { label: "Delivery Waitlists Grow", impact: 62, icon: "📋" },
                { label: "EV Prices Rise 18%", impact: 50, icon: "💸" }
            ]
        },
        {
            title: "Telecom & 5G Chain",
            color: "#8b5cf6",
            nodes: [
                { label: "Taiwan Disruption", impact: 100, icon: "⚡" },
                { label: "Qualcomm Supply Constrained", impact: 82, icon: "🏭" },
                { label: "5G Equipment Shortage", impact: 70, icon: "📡" },
                { label: "Network Rollout Delayed", impact: 58, icon: "🗼" },
                { label: "5G Delayed 12-18 Months", impact: 45, icon: "⏳" }
            ]
        }
    ];

    rippleContainer.innerHTML = chains.map(chain => `
        <div class="ripple-chain">
            <div class="chain-title" style="border-left: 4px solid ${chain.color}">
                ${chain.title}
            </div>
            <div class="chain-flow">
                ${chain.nodes.map((node, index) => `
                    <div class="chain-node-wrapper">
                        <div class="chain-node" style="border-color: ${chain.color}">
                            <div class="chain-icon">${node.icon}</div>
                            <div class="chain-label">${node.label}</div>
                            <div class="chain-impact" style="color: ${chain.color}">
                                Impact: ${node.impact}
                            </div>
                        </div>
                        ${index < chain.nodes.length - 1 ? `
                            <div class="chain-arrow" style="color: ${chain.color}">→</div>
                        ` : ''}
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

async function loadConsumerData(severity = 40) {

    const response = await fetch(
        `http://127.0.0.1:5000/api/consumer?severity=${severity}`
    );

    const data = await response.json();

    const consumerContainer =
        document.getElementById("consumerContainer");

    consumerContainer.innerHTML = "";

    data.products.forEach(product => {

        consumerContainer.innerHTML += `
            <div class="consumer-card">

                <h3>${product.product}</h3>

                <div class="price-increase">
                    +${product.price_increase_pct}%
                </div>

                <p class="new-price">
                    New Price: $${product.new_avg_price_usd}
                </p>

                <p>
                    Timeline:
                    ${product.timeline_months} months
                </p>

                <p class="consumer-risk">
                    Risk: ${product.shortage_risk}
                </p>

            </div>
        `;
    });
}

async function loadExecutiveSummary(severity = 40) {

    const response = await fetch(
        `http://127.0.0.1:5000/api/summary?severity=${severity}`
    );

    const data = await response.json();

    const container =
        document.getElementById("executiveSummary");

    if (!container) return;

    container.innerHTML = `

        <div class="summary-title">
            ${data.title}
        </div>

        <div class="summary-subtitle">
            ${data.subtitle}
        </div>

        <div class="severity-badge">
            Severity Level: ${severity}%
        </div>

        <div class="summary-grid">

            <div class="summary-metric">
                <h4>Industry Loss</h4>
                <p>$${data.estimated_impact.total_industry_loss_bn}B</p>
            </div>

            <div class="summary-metric">
                <h4>Consumer Impact</h4>
                <p>$${data.estimated_impact.consumer_extra_spend_bn}</p>
            </div>

            <div class="summary-metric">
                <h4>Inflation Impact</h4>
                <p>${data.estimated_impact.inflation_contribution_pct}%</p>
            </div>

            <div class="summary-metric">
                <h4>Recovery</h4>
                <p>${data.estimated_impact.recovery_months} Mo</p>
            </div>

        </div>

        <div class="executive-highlight-grid">

            <div class="executive-highlight">
                <h4>Top Risk Sector</h4>
                <p>AI & Data Centers</p>
            </div>

            <div class="executive-highlight">
                <h4>Top Investment Opportunity</h4>
                <p>US Domestic Chip Makers</p>
            </div>

        </div>

        <div class="executive-narrative">
            <h4>Situation Overview</h4>
            <p>
                ${data.what_happened.content}
            </p>
        </div>

        <div class="summary-bottom">
            <strong>Executive Bottom Line</strong>
            <br><br>
            ${data.bottom_line}
        </div>
    `;
}

async function loadInvestmentData(severity = 40) {

    const response = await fetch(
        `http://127.0.0.1:5000/api/investment?severity=${severity}`
    );

    const data = await response.json();

    const investmentContainer =
        document.getElementById("investmentContainer");

    investmentContainer.innerHTML = "";

    data.sectors.forEach(sector => {

        let signalClass = "signal-hold";

        if (sector.signal.includes("BUY")) {
            signalClass = "signal-buy";
        }

        if (sector.signal.includes("RISK")) {
            signalClass = "signal-risk";
        }

        investmentContainer.innerHTML += `
            <div class="investment-card">

                <h3>${sector.sector}</h3>

                <div class="investment-signal ${signalClass}">
                    ${sector.signal}
                </div>

                <div class="score-row">
                    <span>Risk Score</span>
                    <strong>${sector.risk_score}</strong>
                </div>

                <div class="score-row">
                    <span>Opportunity Score</span>
                    <strong>${sector.opportunity_score}</strong>
                </div>

                <div class="expected-move">

    <div class="expected-move-value ${
        sector.expected_change_pct >= 0
            ? "move-positive"
            : "move-negative"
    }">

        ${sector.expected_change_pct}%

    </div>

    <div class="expected-move-label">
        Expected Move
    </div>

</div>

                <p>
                    ${sector.reasoning}
                </p>

                <div class="stock-list">
                    ${sector.key_stocks.join(" • ")}
                </div>

                <div class="action-text">
                    ${sector.action}
                </div>

            </div>
        `;
    });
}

async function loadShockData(severity = 40) {

    const response = await fetch(
        `http://127.0.0.1:5000/api/shock?severity=${severity}`
    );

    const data = await response.json();

    document.getElementById("totalLoss").textContent =
        "$" + data.total_estimated_loss_bn + " Billion";

    document.getElementById("scenario").textContent =
        data.scenario;

    document.getElementById("timeline").textContent =
        data.timeline;

    const tbody =
        document.querySelector("#industryTable tbody");

    tbody.innerHTML = "";

    data.industries.forEach(industry => {

        const row = `
            <tr>
                <td>${industry.name}</td>
                <td>${industry.dependency}</td>
                <td class="${industry.impact_level.toLowerCase()}">
                    ${industry.impact_level}
                </td>
                <td>${industry.revenue_loss_bn}</td>
            </tr>
        `;

        tbody.innerHTML += row;
    });

    const labels =
    data.industries.map(i => i.name);

const losses =
    data.industries.map(i => i.revenue_loss_bn);

if (industryChart) {
    industryChart.destroy();
}

const ctx2 = document.getElementById("industryChart");

industryChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: labels,
        datasets: [{
            label: "Revenue Loss ($B)",
            data: losses,
            backgroundColor: [
                "rgba(239, 68, 68, 0.8)",
                "rgba(249, 115, 22, 0.8)",
                "rgba(59, 130, 246, 0.8)",
                "rgba(234, 179, 8, 0.8)",
                "rgba(139, 92, 246, 0.8)",
                "rgba(34, 197, 94, 0.8)"
            ],
            borderColor: [
                "#ef4444",
                "#f97316",
                "#3b82f6",
                "#eab308",
                "#8b5cf6",
                "#22c55e"
            ],
            borderWidth: 2,
            borderRadius: 6,
            borderSkipped: false
        }]
    },
    options: {
        responsive: true,
        animation: {
            duration: 600,
            easing: "easeInOutQuart"
        },
        plugins: {
            legend: { display: false },
            tooltip: {
                backgroundColor: "#1a1a2e",
                titleColor: "#ffffff",
                bodyColor: "#aaaacc",
                borderColor: "#3b82f6",
                borderWidth: 1,
                padding: 12,
                callbacks: {
                    label: function(context) {
                        return ` $${context.parsed.y}B estimated loss`;
                    }
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: "#aaaacc",
                    font: { size: 11 },
                    maxRotation: 25
                },
                grid: { color: "rgba(255,255,255,0.05)" }
            },
            y: {
                ticks: {
                    color: "#aaaacc",
                    font: { size: 11 },
                    callback: function(value) {
                        return "$" + value + "B";
                    }
                },
                grid: { color: "rgba(255,255,255,0.05)" }
            }
        }
    }
});

const ctx =
    document.getElementById("industryChart");

industryChart = new Chart(ctx2, {
    type: "bar",

    data: {
        labels: labels,

        datasets: [{
            label: "Revenue Loss ($B)",
            data: losses,
            backgroundColor: [
                "#ef4444",
                "#f97316",
                "#3b82f6",
                "#eab308",
                "#8b5cf6",
                "#22c55e"
            ]
        }]
    },

    options: {
        responsive: true,

        plugins: {
            legend: {
                labels: {
                    color: "#ffffff"
                }
            }
        },

        scales: {
            x: {
                ticks: {
                    color: "#ffffff"
                }
            },

            y: {
                ticks: {
                    color: "#ffffff"
                }
            }
        }
    }
});

    const riskContainer =
        document.getElementById("countryRiskContainer");

    riskContainer.innerHTML = "";

    data.affected_countries.forEach(country => {

        let riskClass = "risk-low";

        if (country.risk >= 80) {
            riskClass = "risk-high";
        } else if (country.risk >= 60) {
            riskClass = "risk-medium";
        }

        riskContainer.innerHTML += `
            <div class="risk-card">
                <h3>${country.country}</h3>
                <p>${country.role}</p>
                <p class="risk-score ${riskClass}">
                    ${country.risk}
                </p>
            </div>
        `;
    });

    updateMap(data.affected_countries);

    await loadConsumerData(severity);
    await loadExecutiveSummary(severity);
    await loadInvestmentData(severity);
}

window.addEventListener("DOMContentLoaded", () => {

    initializeMap();

    renderRippleEffects();

    const initialVal = slider.value;
    const initialMin = slider.min || 10;
    const initialMax = slider.max || 80;
    const initialPct = ((initialVal - initialMin) / (initialMax - initialMin)) * 100;
    slider.style.background = `linear-gradient(to right, #3b82f6 ${initialPct}%, #2a2a4a ${initialPct}%)`;

    loadShockData();

    reportButton.addEventListener("click", () => {

        const severity = slider.value;

        window.open(
            `http://127.0.0.1:5000/api/report?severity=${severity}`,
            "_blank"
        );
    });

});

