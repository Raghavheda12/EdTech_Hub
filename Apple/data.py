from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Employee data for Apple
employee_data = {
    "2020": {"count": 147000, "change": 11000, "percentage": 8.07},
    "2021": {"count": 154000, "change": 7000, "percentage": 4.76},
    "2022": {"count": 160000, "change": 6000, "percentage": 3.90},
    "2023": {"count": 165000, "change": 5000, "percentage": 3.13},
    "2024": {"count": 170000, "change": 5000, "percentage": 3.03}
}

@app.route("/")
def home():
    return render_template("apple.html")  # Ensure this file exists

@app.route("/employee-data")
def employee_data_endpoint():
    return jsonify(employee_data)

@app.route("/employee-chart")
def employee_chart():
    # Generate a static image link or return a pre-generated chart image
    # Assuming you have a pre-generated employee growth chart saved as 'employee_growth_chart_apple.png'
    return send_file('employee_growth_chart_apple.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
