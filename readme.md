# Grant Allocation System

This project simulates the process of evaluating organizations for grant funding and fairly distributes funds based on their expected utility scores. It consists of two main scripts:

1. **`generate_csv.py`** - Generates randomized grant requests, evaluator budgets, and evaluation data.
2. **`allocate_grants.py`** - Allocates funds to organizations based on their computed utility scores.

## How It Works

### 1. Generate Data

Run this command to generate sample data:

```sh
python generate_csv.py
```

This creates three CSV files:

- `evaluations.csv`: Scores given to organizations by evaluators.
- `organizations.csv`: Organizations and the amount of funding they request.
- `evaluators.csv`: Evaluators and their available budget.

### 2. Allocate Grants

Once the data is generated, run:

```sh
python allocate_grants.py
```

This script:

- Computes an **Expected Utility (EU) score** for each organization based on evaluator ratings.
- Distributes total available funds proportionally based on EU scores.
- Caps grants at the requested amount to prevent overfunding.

The final grant allocations are saved in `grant_allocation.csv`.

## Theory Behind the Allocation

Grants are allocated using a weighted evaluation system, where:

- Evaluators rate organizations on **impact**, **feasibility**, and **cost-effectiveness**.
- Evaluators also rate their **confidence** in these scores.
- A **weighted sum** is calculated, with weights:
  - Impact: 40%
  - Feasibility: 30%
  - Cost-effectiveness: 30%
- Scores are **adjusted for evaluator confidence**, so confident evaluators have more influence on EU scores.
- The total available funds are **distributed proportionally** based on the **EU scores**.
- A **cap is applied** to ensure no organization receives more than it requested.

This method ensures that organizations with the highest evaluated utility receive funding while preventing excessive allocation.
