
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# Sample in-memory data
sensor_data = {
    "occupancy_status": "Occupied",
    "bad_smell_level": 65,
    "water_leakage": "No Leakage",
    "handwash_level": "Low: 10%",
    "theft_detected": "No Theft",
    "tissue_shortage": "Critical: 5%"
}

@app.route('/update', methods=['POST'])
def update_data():
    global sensor_data
    sensor_data = request.json
    return jsonify({"status": "received"})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sensor_data)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/washroom/<washroom_id>')
def washroom(washroom_id):
    return render_template('washroom.html', washroom_id=washroom_id)

@app.route('/tissue')
def tissue():
    return render_template('tissue.html')

@app.route('/handwash')
def handwash():
    return render_template('handwash.html')

if __name__ == "__main__":
    app.run(debug=True)
