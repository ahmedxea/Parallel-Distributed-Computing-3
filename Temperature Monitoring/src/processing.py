from queue import Queue

temperature_averages = {}  # Shared dictionary for average temperatures
data_queue = Queue()  # Thread-safe queue for sensor data

def process_temperatures(num_sensors, lock):
    """
    Continuously calculates the average temperature from queued sensor data.
    Updates the global `temperature_averages` dictionary.
    """
    sensor_readings = {i: [] for i in range(num_sensors)}  # Store past readings

    while True:
        sensor_id, temp = data_queue.get()  # Get new reading from queue
        with lock:
            sensor_readings[sensor_id].append(temp)
            if len(sensor_readings[sensor_id]) > 10:  # Keep last 10 readings
                sensor_readings[sensor_id].pop(0)
            temperature_averages[sensor_id] = sum(sensor_readings[sensor_id]) / len(sensor_readings[sensor_id])
