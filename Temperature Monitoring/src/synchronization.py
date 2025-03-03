from threading import RLock, Condition

lock = RLock()  # Reentrant lock for thread safety
condition = Condition(lock)  # Synchronization control
