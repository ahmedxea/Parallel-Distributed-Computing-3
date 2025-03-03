# Parallel-Distributed-Computing-3 - Lab 4 Part 1: Temperature Monitoring System 🌡️

## Objectives
- Simulate temperature sensors generating real-time readings.
- Process temperature data and compute averages.
- Display updated data on the console with proper synchronization.

## Synchronization Mechanisms Used:
1. **Locks (`RLock`)**: Ensures only one thread modifies `latest_temperatures` at a time.
2. **Queue (`Queue`)**: Thread-safe communication for sensor readings.
3. **Condition (`Condition`)**: Synchronizes access to display updates.

## Why No Performance Metrics?
The professor didn't ask for metrics because this lab focuses on **synchronization, concurrency, and real-time display handling**, rather than performance analysis.
