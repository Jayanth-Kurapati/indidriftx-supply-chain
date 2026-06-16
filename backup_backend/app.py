from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
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


@app.route("/api/shock", methods=["GET"])
def shock():
    severity = int(request.args.get("severity", 40))
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
    return jsonify(get_investment_data())


@app.route("/api/summary", methods=["GET"])
def summary():
    return jsonify(get_executive_summary())


if __name__ == "__main__":
    app.run(debug=True, port=5000)