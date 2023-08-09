### Description:
In the healthcare analytics domain, effective patient scheduling plays a crucial role in providing quality medical care while optimizing resource usage. This project leverages Genetic Algorithms to address the complexities of patient scheduling, taking into account various factors such as patient preferences, doctor availability, and resource constraints.

The code comprises the following key components:

**1. Data Initialization:** Simulated data is used to represent patients, doctors, time slots, patient preferences, doctor availability, and resource constraints.

**2. Fitness Function:** A fitness function evaluates the quality of a scheduling solution based on patient waiting times. The goal is to minimize the total waiting time for patients.

**3. Population Initialization:** The initial population of schedules is generated randomly.

**4. Selection:** Tournament selection is used to choose parents for crossover.

**5. Crossover:** Single-point crossover is applied to create new schedules from selected parents.

**6. Mutation:** Random mutation introduces diversity into the population by making small random changes to schedules.

**7. Genetic Algorithm Loop:** The genetic algorithm iterates through generations, applying selection, crossover, and mutation to improve the quality of schedules.

**8. Results and Visualization:** The project outputs the best scheduling solution, showing the assigned time slots for each patient. Additionally, it displays the best fitness score achieved during optimization.

### Methods Used:
**1. Selection Method:** Tournament Selection
   
**2. Crossover:** Single-point Crossover

**3. Mutation:** Random Mutation
