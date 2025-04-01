from mpi4py import MPI
import numpy as np
import time
import socket

def compute_squares(start, end):
    return [i ** 2 for i in range(start, end)]

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hostname = socket.gethostname()

# Set range
n = int(1e8)  # You can modify this for experimentation
chunk_size = n // size
start_index = rank * chunk_size + 1
end_index = n + 1 if rank == size - 1 else start_index + chunk_size

# Timing
start_time = MPI.Wtime()

# Compute local squares
local_squares = compute_squares(start_index, end_index)

# Gather all results at root
all_squares = comm.gather(local_squares, root=0)

end_time = MPI.Wtime()

# Root process prints results
if rank == 0:
    flat = [item for sublist in all_squares for item in sublist]
    print(f"Process {rank} on {hostname}:")
    print(f"Total squares computed: {len(flat)}")
    print(f"Last square is: {flat[-1]}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
