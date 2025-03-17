# **Parallel and Distributed Computing - Assignment 1**

## **Part 1 - Answers**

- In the square program, different multiprocessing approaches were tested to optimize execution time. The sequential method was the slowest since it processed numbers one by one. Using individual processes for each number was inefficient due to the high overhead of process creation. The multiprocessing pool with map() provided a significant speedup by efficiently distributing tasks, while apply() was slower since it handled one element at a time. The ProcessPoolExecutor performed similarly to Pool.map() and was easier to use. When testing with a larger dataset (10^7 numbers), parallel processing methods showed a clear advantage, with Pool.map() and ProcessPoolExecutor being the most efficient choices.

- For the semaphore synchronization task, semaphores were used to manage limited resources in a connection pool. When more processes tried to access the pool than available connections, they had to wait until a connection was released. This ensured controlled execution and prevented overuse of resources. Semaphores effectively prevented race conditions by limiting concurrent access and maintaining order. The experiment showed how semaphores help synchronize shared resources efficiently while ensuring that processes do not conflict or overload the system.
  
