import random
import time
import threading

latest_temperatures = {}  # Shared dictionary for latest sensor readings

def simulate_sensor(sensor_id, lock, data_queue):
    """
    Simulates temperature readings from a sensor every second.
    Updates shared dictionary and sends data to the processing queue.
    """
    while True:
        temp = random.randint(15, 40)  # Generate random temperature
        with lock:  # Ensure safe access to shared data
            latest_temperatures[sensor_id] = temp
        data_queue.put((sensor_id, temp))  # Send reading to processing queue
        time.sleep(1)  # Wait for 1 second