import multiprocessing
import time

class ConnectionPool:
    """
    Simulates a pool of database connections using a semaphore to control access.
    """
    def __init__(self, max_connections):
        """
        Initializes the pool with a limited number of connections.
         
        Parameters:
        - max_connections (int): The number of available connections.
        """
        self.semaphore = multiprocessing.Semaphore(max_connections)  # Limits access
        self.connections = [f"Connection-{i}" for i in range(max_connections)]  # Pool
        self.lock = multiprocessing.Lock()  # Ensures thread-safe access

    def get_connection(self):
        """
        Acquires a connection from the pool.
        
        Returns:
        - str: Connection ID
        """
        self.semaphore.acquire()  # Block if no connections available
        with self.lock:
            if self.connections:
                return self.connections.pop(0)  # Get an available connection

    def release_connection(self, connection):
        """
        Releases a connection back to the pool.
        
        Parameters:
        - connection (str): Connection ID to be released
        """
        with self.lock:
            self.connections.append(connection)  # Return connection to the pool
        self.semaphore.release()  # Allow another process to acquire a connection
