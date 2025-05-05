import serial
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------- CONFIG ------------
PORT = 'COM5'           # Change this to your actual port (e.g., '/dev/ttyUSB0')
BAUDRATE = 115200
CSV_FILE = 'weights.csv'
# -------------------------------

# Initialize serial connection
ser = serial.Serial(PORT, BAUDRATE, timeout=1)
time.sleep(2)  # wait for connection to establish

# Prepare CSV logging
csv_file = open(CSV_FILE, mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Timestamp", "Weight"])

# Store weight values for plotting
weights = []
timestamps = []

# Setup matplotlib plot
plt.style.use('ggplot')
fig, ax = plt.subplots()
line, = ax.plot([], [], label='Weight (g)')
ax.set_title('Real-Time Weight Signal')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Weight (g)')
ax.legend()

start_time = time.time()

def update(frame):
    global weights, timestamps
    try:
        line_raw = ser.readline().decode().strip()
        if line_raw.startswith("Weight:"):
            weight_str = line_raw.replace("Weight:", "").strip()
            weight = float(weight_str)

            now = time.time() - start_time
            timestamps.append(now)
            weights.append(weight)
            csv_writer.writerow([now, weight])

            # Limit data to last 100 points
            timestamps = timestamps[-100:]
            weights = weights[-100:]

            line.set_data(timestamps, weights)
            ax.relim()
            ax.autoscale_view()
    except Exception as e:
        print(f"Error: {e}")

    return line,

ani = FuncAnimation(fig, update, interval=100)

try:
    plt.show()
except KeyboardInterrupt:
    pass
finally:
    print("Closing...")
    ser.close()
    csv_file.close()
