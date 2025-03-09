from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Employee data
employee_data = {
    "2020": {"count": 163000, "change": 19000, "percentage": 13.19},
    "2021": {"count": 181000, "change": 18000, "percentage": 11.04},
    "2022": {"count": 221000, "change": 40000, "percentage": 22.10},
    "2023": {"count": 221000, "change": 0, "percentage": 0.00},
    "2024": {"count": 228000, "change": 7000, "percentage": 3.17}
}

@app.route("/")
def home():
    return render_template("microsoft.html")  # Ensure this file exists

@app.route("/employee-data")
def employee_data_endpoint():
    return jsonify(employee_data)

@app.route("/employee-chart")
def employee_chart():
    # Generate a static image link or return a pre-generated chart image
    # Assuming you have a pre-generated employee growth chart saved as 'employee_growth_chart.png'
    return send_file('employee_growth_chart.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)

