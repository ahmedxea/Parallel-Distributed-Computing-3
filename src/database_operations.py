import time
import random

def access_database(pool, process_id):
    """
    Simulates a process performing a database operation.
    
    Parameters:
    - pool (ConnectionPool): The shared connection pool.
    - process_id (int): The ID of the process.
    """
    print(f"Process-{process_id} is waiting for a connection...")

    connection = pool.get_connection()  # Acquire connection
    print(f"Process-{process_id} acquired {connection}")

    time.sleep(random.uniform(1, 3))  # Simulate work

    print(f"Process-{process_id} releasing {connection}")
    pool.release_connection(connection)  # Release connection
