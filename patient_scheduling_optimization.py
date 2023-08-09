import numpy as np
import pandas as pd
import random as rd

patients = ["P1", "P2", "P3", "P4", "P5"]
doctors = ["D1", "D2", "D3"]
time_slots = ["Slot1", "Slot2", "Slot3"]

patient_preferences = {p: rd.sample(time_slots, len(time_slots)) for p in patients}
doctor_availability = {d: rd.sample(time_slots, len(time_slots)) for d in doctors}
resource_constraints = {"Resource1": rd.sample(time_slots, len(time_slots))}

def fitness_function(schedule):
    total_waiting_time = 0
    for patient, assigned_slot in schedule.items():
        patient_waiting_time = abs(time_slots.index(assigned_slot) - time_slots.index(patient_preferences[patient][0]))
        total_waiting_time += patient_waiting_time
    return -total_waiting_time

def initialize_population(pop_size):
    population = []
    for _ in range(pop_size):
        schedule = {p: rd.choice(time_slots) for p in patients}
        population.append(schedule)
    return population

def tournament_selection(population, tournament_size):
    tournament = rd.sample(population, tournament_size)
    tournament.sort(key=lambda x: fitness_function(x), reverse=True)
    return tournament[0]

def single_point_crossover(parent1, parent2):
    crossover_point = rd.randint(1, len(patients) - 1)
    child1 = {p: parent1[p] if i < crossover_point else parent2[p] for i, p in enumerate(patients)}
    child2 = {p: parent2[p] if i < crossover_point else parent1[p] for i, p in enumerate(patients)}
    return child1, child2

def mutation(schedule, mutation_prob):
    mutated_schedule = schedule.copy()
    for patient in patients:
        if rd.random() < mutation_prob:
            mutated_schedule[patient] = rd.choice(time_slots)
    return mutated_schedule

p_c = 0.8
p_m = 0.1
tournament_size = 3
pop_size = 100
gen = 30

population = initialize_population(pop_size)
best_solution = max(population, key=lambda x: fitness_function(x))
best_fitness = fitness_function(best_solution)

for generation in range(gen):
    new_population = []
    
    for _ in range(pop_size // 2):
        parent1 = tournament_selection(population, tournament_size)
        parent2 = tournament_selection(population, tournament_size)
        
        if rd.random() < p_c:
            child1, child2 = single_point_crossover(parent1, parent2)
        else:
            child1, child2 = parent1.copy(), parent2.copy()
        
        child1 = mutation(child1, p_m)
        child2 = mutation(child2, p_m)
        
        new_population.extend([child1, child2])
    
    population = new_population
    
    current_best = max(population, key=lambda x: fitness_function(x))
    current_best_fitness = fitness_function(current_best)
    if current_best_fitness > best_fitness:
        best_solution = current_best
        best_fitness = current_best_fitness

print("Best Scheduling Solution:")
for patient, time_slot in best_solution.items():
    print(f"Patient: {patient}, Assigned Slot: {time_slot}")

print("Best Fitness Score:", best_fitness)
print("### METHODS ###")
print("# Selection Method = Tournament Selection")
print("# Crossover = Single-point Crossover")
print("# Mutation = Random Mutation")
print("### METHODS ###")
