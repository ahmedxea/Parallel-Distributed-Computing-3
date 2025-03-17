# **Parallel and Distributed Computing - Assignment 1**

## **Part 2: Navigating the City** 

### **5. Sequential Implementation (15 pts)**  
- Implemented a basic **single-car** GA to visit all nodes in the shortest distance.  
- Used `city_distances.csv` for a **32-node** map.  
- Functions implemented:  
  - `calculate_fitness()` – Evaluates route distance.  
  - `select_in_tournament()` – Selects the best candidates.  
- Ran the algorithm and recorded performance.  

### **6. Parallelization Using MPI (20 pts)**  

#### **6.1. Approach**
- **Distributed computation using MPI4PY**:
  - Each process calculates fitness for a subset of routes.
  - The population is scattered and updated in parallel.
  - **Speedup achieved by dividing the workload** across processes.

#### **6.2. Running on Multiple Machines**
- Created a **hostfile.txt**:
- Ran the program using:
  ```sh
  mpiexec -hostfile hostfile.txt -n 8 python genetic_algorithm_trial_parallelized.py
  ```
- Results: **Performance improved significantly compared to sequential execution.**


### **7. Enhancing the Algorithm (20 pts)**  

#### **7.1. Implemented Improvements**
 **Adaptive Mutation Rate**:  
- Increased mutation if improvement is too slow, preventing stagnation.  

 **Smarter Population Regeneration**:  
- Instead of random resets, kept the top 10% of solutions to preserve good candidates.  

 **Dynamic Load Balancing**:  
- Distributed extra individuals among MPI processes for even computation.  

#### **7.2. Performance Comparison**  
| Version        | Execution Time | Best Route Distance |
|---------------|---------------|----------------------|
| Sequential    | **255.64s**    | **-1408008.0**      |
| Parallelized  | **187.48s**    | **-1508355.0**      |
| Improved      | **39.07s**     | **-1809505.0**      |

**Significant performance gain in execution time and solution quality!**

### **8. Large Scale Problem (10 pts)**  

#### **8.1. Running with 100 Nodes**  
- Switched to `city_distances_extended.csv`.  
- Required **more iterations** and a **larger population** to find a good solution.  
- Executed successfully **within feasible time**.

#### **8.2. Adding More Cars (Explanation - 5 pts)**  
- **Current Model:** 1 vehicle completes all deliveries.  
To extend the current **single-vehicle** model to multiple cars, the following modifications are needed:  

1. **Route Representation** – Each chromosome should encode multiple routes, one per car, ensuring all nodes are visited without duplication.  
2. **Fitness Function** – Evaluate total distance across all cars while penalizing missed or repeated nodes.  
3. **Population Generation** – Distribute nodes among cars using clustering (e.g., K-Means) or heuristics.  
4. **Crossover & Mutation** – Swap entire routes between cars and allow node reassignment between vehicles.  
5. **Parallelization** – Assign each MPI process a subset of cars for independent route optimization.  

This transforms the problem into a **Vehicle Routing Problem (VRP)**, optimizing delivery efficiency with multiple cars.
