from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Employee data for Stripe
employee_data = {
    "2020": {"count": 4000, "change": 800, "percentage": 25.0},
    "2021": {"count": 6000, "change": 2000, "percentage": 50.0},
    "2022": {"count": 7000, "change": 1000, "percentage": 16.67},
    "2023": {"count": 7500, "change": 500, "percentage": 7.14},
    "2024": {"count": 8000, "change": 500, "percentage": 6.67}
}

@app.route("/")
def home():
    return render_template("stripe.html")  # Ensure this file exists

@app.route("/employee-data")
def employee_data_endpoint():
    return jsonify(employee_data)

@app.route("/employee-chart")
def employee_chart():
    # Generate a static image link or return a pre-generated chart image
    # Assuming you have a pre-generated employee growth chart saved as 'employee_growth_chart_stripe.png'
    return send_file('employee_growth_chart_stripe.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
