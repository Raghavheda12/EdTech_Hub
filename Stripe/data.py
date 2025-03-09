from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Employee data for Google
employee_data = {
    "2020": {"count": 156500, "change": 15000, "percentage": 10.58},
    "2021": {"count": 168000, "change": 11500, "percentage": 7.27},
    "2022": {"count": 174000, "change": 6000, "percentage": 3.57},
    "2023": {"count": 180000, "change": 6000, "percentage": 3.45},
    "2024": {"count": 185000, "change": 5000, "percentage": 2.78}
}

@app.route("/")
def home():
    return render_template("google.html")  # Ensure this file exists

@app.route("/employee-data")
def employee_data_endpoint():
    return jsonify(employee_data)

@app.route("/employee-chart")
def employee_chart():
    # Generate a static image link or return a pre-generated chart image
    # Assuming you have a pre-generated employee growth chart saved as 'employee_growth_chart_google.png'
    return send_file('employee_growth_chart_google.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
