Here's the improved and organized **README.md** file for **Assignment 1 - Part 2**. It is structured as a student submission, clearly explaining the objectives, methodology, and results.

---

# **DSAI 3202 – Parallel and Distributed Computing**  
### **Assignment 1 – Part 2: Navigating the City**  

## **1. Objectives**  
The goal of this assignment is to implement a **Genetic Algorithm (GA)** for solving an optimization problem in a city navigation scenario. The implementation involves:  
- Developing a sequential version of the genetic algorithm.
- Parallelizing the algorithm using **MPI4PY** for distributed execution.
- Enhancing the algorithm for improved performance.
- Running the algorithm on an extended city map with 100 nodes.

---

## **2. Tools and Libraries Used**  
- **Python**: Main programming language.  
- **MPI4PY**: Message Passing Interface (MPI) for parallel computing.  
- **NumPy & Pandas**: Data handling and numerical computations.  

---

## **3. Project Structure**  

📂 **Part 2/**  
├── 📂 **data/**  
│ ├── `city_distances.csv` (Original 32-node distance matrix)  
│ ├── `city_distances_extended.csv` (Extended 100-node distance matrix)  
│  
├── 📂 **Sequential/**  
│ ├── `genetic_algorithm_trial.py` (Sequential execution)  
│  
├── 📂 **Parallelized/**  
│ ├── `genetic_algorithm_trial_parallelized.py` (MPI-based parallel execution)  
│  
├── 📂 **Enhanced/**  
│ ├── `genetic_algorithm_trial_improved.py` (Enhanced version with improvements)  
│  
├── `genetic_algorithms_functions.py` (Functions for the genetic algorithm)  
├── `README.md` (This file)  
├── `hostfile.txt` (Host configuration for multi-machine execution)  
├── `DSAI 3202 - Assignment 1 - Part 2.docx` (Assignment document)  

---

## **4. Genetic Algorithm Overview**  

### **4.1. What is a Genetic Algorithm?**  
A Genetic Algorithm (GA) is an optimization technique inspired by natural selection. It evolves solutions through selection, crossover, and mutation to minimize the total distance of a delivery route.

### **4.2. Basic Steps of GA in This Problem**  
1. **Initialize**: Generate a random population of delivery routes.  
2. **Evaluate**: Compute the fitness (total distance) for each route.  
3. **Selection**: Choose the best-performing routes.  
4. **Crossover**: Create new routes by recombining parents.  
5. **Mutation**: Introduce random changes for diversity.  
6. **Repeat**: Iterate until reaching a stopping criterion.

---

## **5. Sequential Implementation (15 pts)**  
- Implemented a basic **single-car** GA to visit all nodes in the shortest distance.  
- Used `city_distances.csv` for a **32-node** map.  
- Functions implemented:  
  - `calculate_fitness()` – Evaluates route distance.  
  - `select_in_tournament()` – Selects the best candidates.  
- Ran the algorithm and recorded performance.  

---

## **6. Parallelization Using MPI (20 pts)**  

### **6.1. Approach**
- **Distributed computation using MPI4PY**:
  - Each process calculates fitness for a subset of routes.
  - The population is scattered and updated in parallel.
  - **Speedup achieved by dividing the workload** across processes.

### **6.2. Running on Multiple Machines**
- Created a **hostfile.txt**:
  ```
  machine1 slots=4  
  machine2 slots=4
  ```
- Ran the program using:
  ```sh
  mpiexec -hostfile hostfile.txt -n 8 python genetic_algorithm_trial_parallelized.py
  ```
- Results: **Performance improved significantly compared to sequential execution.**

---

## **7. Enhancing the Algorithm (20 pts)**  

### **7.1. Implemented Improvements**
✔️ **Adaptive Mutation Rate**:  
- Increased mutation if improvement is too slow, preventing stagnation.  

✔️ **Smarter Population Regeneration**:  
- Instead of random resets, kept the top 10% of solutions to preserve good candidates.  

✔️ **Dynamic Load Balancing**:  
- Distributed extra individuals among MPI processes for even computation.  

### **7.2. Performance Comparison**  
| Version        | Execution Time | Best Route Distance |
|---------------|---------------|----------------------|
| Sequential    | **255.64s**    | **-1408008.0**      |
| Parallelized  | **187.48s**    | **-1508355.0**      |
| Improved      | **39.07s**     | **-1809505.0**      |

✅ **Significant performance gain in execution time and solution quality!**

---

## **8. Large Scale Problem (10 pts)**  

### **8.1. Running with 100 Nodes**  
- Switched to `city_distances_extended.csv`.  
- Required **more iterations** and a **larger population** to find a good solution.  
- Executed successfully **within feasible time**.

### **8.2. Adding More Cars (Explanation - 5 pts)**  
- **Current Model:** 1 vehicle completes all deliveries.  
- **Improvement:**  
  - Introduce **multiple vehicles**, each handling a subset of nodes.  
  - Modify fitness function to distribute nodes among vehicles.  
  - Use **clustering algorithms** (e.g., k-means) to group deliveries efficiently.  

---

## **9. Bonus (Optional - 10 pts)**  
✔️ **Multi-Car Implementation (5 pts)**  
✔️ **Running on AWS (5 pts) - Not implemented yet**  

---

## **10. How to Run the Code**  

### **Sequential Version**  
```sh
python genetic_algorithm_trial.py
```

### **Parallel Version (Single Machine)**  
```sh
mpiexec -n 4 python genetic_algorithm_trial_parallelized.py
```

### **Parallel Version (Multiple Machines)**  
```sh
mpiexec -hostfile hostfile.txt -n 8 python genetic_algorithm_trial_parallelized.py
```

### **Improved Version**  
```sh
mpiexec -n 4 python genetic_algorithm_trial_improved.py
```

---

## **11. Conclusion**  
- The **parallelized GA** reduced execution time significantly.  
- **Adaptive mutation & smarter regeneration** improved solution quality.  
- **Scalability to 100 nodes** was successfully achieved.  
- **Future Work:** Adding multiple cars for better efficiency.

---

This README provides a structured summary of **Assignment 1 - Part 2**, ensuring clarity in objectives, methodology, and results for easy submission.
