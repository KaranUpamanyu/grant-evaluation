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

# Evaluation scores for each category are between 1 and 10
min_score = 1
max_score = 10

def clamp(val):
    return max(min(val, max_score), min_score)

# generate evaluation data
evaluation_data = []
for evaluator in evaluators:
    for org_id, org_name in organizations.items():
        evaluator_confidence = random.randint(min_score, max_score)
        # to make scores seem somewhat realistic, the rest of the metrics are evaluator_confidence +/- 4
        impact = clamp(evaluator_confidence + random.randint(-4, 4))
        feasibility = clamp(evaluator_confidence + random.randint(-4, 4))
        cost_effectiveness = clamp(evaluator_confidence + random.randint(-4, 4))

        evaluation_data.append([evaluator, org_id, impact, feasibility, cost_effectiveness, evaluator_confidence])

# grant amount requested by organizations
grant_requested_by_orgs = []
for org_id, org_name in organizations.items():
    grant_requested = random.randint(50000, 200000)  # Orgs request between 50K and 200K
    grant_requested_by_orgs.append([org_id, org_name, grant_requested])

# assign random budgets to evaluators
evaluator_budgets = []
for evaluator in evaluators:
    budget = random.randint(50000, 150000)  # Evaluators have between 50K and 150K
    evaluator_budgets.append([evaluator, budget])

# Write evaluation data to CSV file
filename = "evaluations.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["evaluator_id", "organization_id", "impact", "feasibility", "cost_effectiveness", "evaluator_confidence",])
    writer.writerows(evaluation_data)

# Write organization requests to CSV file
with open("organizations.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["organization_id", "organization_name", "grant_requested"])
    writer.writerows(grant_requested_by_orgs)

# Write evaluator budgets to CSV file
with open("evaluators.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["evaluator_id", "budget"])
    writer.writerows(evaluator_budgets)

print("CSV files generated successfully!")
