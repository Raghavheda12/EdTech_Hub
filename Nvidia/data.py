from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Employee data for NVIDIA
employee_data = {
    "2020": {"count": 13000, "change": 1000, "percentage": 8.33},
    "2021": {"count": 14500, "change": 1500, "percentage": 11.54},
    "2022": {"count": 16000, "change": 1500, "percentage": 10.34},
    "2023": {"count": 17500, "change": 1500, "percentage": 9.38},
    "2024": {"count": 19000, "change": 1500, "percentage": 8.57}
}

@app.route("/")
def home():
    return render_template("nvidia.html")  # Ensure this file exists and reflects NVIDIA

@app.route("/employee-data")
def employee_data_endpoint():
    return jsonify(employee_data)

@app.route("/employee-chart")
def employee_chart():
    # Generate a static image link or return a pre-generated chart image
    # Assuming you have a pre-generated employee growth chart saved as 'employee_growth_chart_nvidia.png'
    return send_file('employee_growth_chart_nvidia.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
