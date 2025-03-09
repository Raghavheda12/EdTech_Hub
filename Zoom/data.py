from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Employee data for GitHub
employee_data = {
    "2020": {"count": 2000, "change": 300, "percentage": 17.65},
    "2021": {"count": 2500, "change": 500, "percentage": 25.00},
    "2022": {"count": 3000, "change": 500, "percentage": 20.00},
    "2023": {"count": 3500, "change": 500, "percentage": 16.67},
    "2024": {"count": 4000, "change": 500, "percentage": 14.29}
}

@app.route("/")
def home():
    return render_template("github.html")  # Ensure this file exists

@app.route("/employee-data")
def employee_data_endpoint():
    return jsonify(employee_data)

@app.route("/employee-chart")
def employee_chart():
    # Generate a static image link or return a pre-generated chart image
    # Assuming you have a pre-generated employee growth chart saved as 'employee_growth_chart_github.png'
    return send_file('employee_growth_chart_github.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
