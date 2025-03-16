import random
import csv

# 20 random org names
organization_names = [
    "FutureTech Innovations",
    "Green Earth Initiative",
    "Health for All",
    "AI for Good",
    "Clean Water Project",
    "Sustainable Farming Solutions",
    "Space Exploration Trust",
    "EdTech Revolution",
    "Disaster Relief Network",
    "Ocean Cleanup Mission",
    "Zero Hunger Foundation",
    "Renewable Energy Research",
    "Wildlife Conservation Fund",
    "Global Literacy Project",
    "Medical Breakthroughs Inc.",
    "Autonomous Vehicles Research",
    "Neural Interfaces Lab",
    "Cybersecurity Initiative",
    "Mental Health Awareness",
    "Quantum Computing Society"
]

# org ID to name mappings
organizations = {f"org_{i+1}": name for i, name in enumerate(organization_names)}

# 30 evaluator IDs
evaluators = [f"evaluator_{i+1}" for i in range(30)]

data = []

# Evaluation scores for each category are between 1 and 10
min_score = 1
max_score = 10

def clamp(val):
    return max(min(val, max_score), min_score)

for evaluator in evaluators:
    for org_id, org_name in organizations.items():
        evaluator_confidence = random.randint(min_score, max_score)
        # to make scores seem somewhat realistic, the rest of the metrics are evaluator_confidence +/- 4
        impact = clamp(evaluator_confidence + random.randint(-4, 4))
        feasibility = clamp(evaluator_confidence + random.randint(-4, 4))
        cost_effectiveness = clamp(evaluator_confidence + random.randint(-4, 4))

        data.append([evaluator, org_id, org_name, impact, feasibility, cost_effectiveness, evaluator_confidence])

# Write data to CSV file
filename = "evaluations.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["evaluator_id", "organization_id", "organization_name", "impact", "feasibility", "cost_effectiveness", "evaluator_confidence"])
    writer.writerows(data)

print("CSV file generated successfully!")
