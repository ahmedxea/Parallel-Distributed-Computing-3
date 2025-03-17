import multiprocessing
from connection_pool import ConnectionPool
from database_operations import access_database

def main():
    max_connections = 3  # Limit database connections
    pool = ConnectionPool(max_connections)  # Initialize connection pool

    num_processes = 8  # More processes than available connections
    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(target=access_database, args=(pool, i))
        processes.append(p)
        p.start()  # Start process

    for p in processes:
        p.join()  # Wait for all processes to complete

if __name__ == "__main__":
    main()
