import threading
import time
from src.sensor import simulate_sensor, latest_temperatures
from src.processing import process_temperatures, data_queue, temperature_averages
from src.display import initialize_display, update_display
from src.synchronization import lock

NUM_SENSORS = 3  # Define number of sensors

# Initialize console display
initialize_display(NUM_SENSORS)

# ✅ Start Sensor Threads
sensor_threads = []
for i in range(NUM_SENSORS):
    thread = threading.Thread(target=simulate_sensor, args=(i, lock, data_queue), daemon=True)
    sensor_threads.append(thread)
    thread.start()

# ✅ Start Data Processing Thread
processing_thread = threading.Thread(target=process_temperatures, args=(NUM_SENSORS, lock), daemon=True)
processing_thread.start()

# ✅ Start Display Update Thread
def display_update_loop():
    while True:
        update_display(NUM_SENSORS, latest_temperatures, temperature_averages)
        time.sleep(5)  # Update every 5 seconds

display_thread = threading.Thread(target=display_update_loop, daemon=True)
display_thread.start()

# ✅ Keep main thread running
while True:
    time.sleep(1)
