from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from flask import send_file
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

FRED_API_KEY = os.getenv("FRED_API_KEY")

from analyzers.shock_simulator import get_shock_analysis
from analyzers.supply_chain import get_supply_chain_data
from analyzers.consumer_impact import get_consumer_impact
from analyzers.investment import get_investment_data
from analyzers.executive_summary import get_executive_summary
from analyzers.report_generator import generate_report


@app.route("/api/shock", methods=["GET"])
def shock():
    severity = float(request.args.get("severity", 40))
    return jsonify(get_shock_analysis(severity))


@app.route("/api/supplychain", methods=["GET"])
def supplychain():
    return jsonify(get_supply_chain_data())


@app.route("/api/consumer", methods=["GET"])
def consumer():
    severity = int(request.args.get("severity", 40))
    return jsonify(get_consumer_impact(severity))


@app.route("/api/investment", methods=["GET"])
def investment():
    severity = int(request.args.get("severity", 40))
    return jsonify(get_investment_data(severity))


@app.route("/api/summary", methods=["GET"])
def summary():
    severity = int(request.args.get("severity", 40))
    return jsonify(get_executive_summary(severity))


@app.route("/api/report", methods=["GET"])
def report():

    severity = int(request.args.get("severity", 40))

    shock_data = get_shock_analysis(severity)

    consumer_data = get_consumer_impact(severity)

    investment_data = get_investment_data(severity)

    summary_data = get_executive_summary(severity)

    pdf_buffer = generate_report(
        severity,
        shock_data,
        consumer_data,
        investment_data,
        summary_data
    )

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f"IndiDriftX_Report_{severity}.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)