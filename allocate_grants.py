import pandas as pd
import numpy as np

impact_weight = 0.4
feasibility_weight = 0.3
cost_effectiveness_weight = 0.3

# columns: evaluator_id, budget
evaluators_df = pd.read_csv("evaluators.csv")
# columns: organization_id, organization_name, requested_grant
organizations_df = pd.read_csv("organizations.csv")
# columns: evaluator_id, organization_id, impact, feasibility, cost_effectiveness, evaluator_confidence
evaluations_df = pd.read_csv("evaluations.csv")


# compute expected utility score for each organization
def compute_eu(group):
    # confident evaluators have more influence on the weighted scores 
    weighted_scores = (impact_weight * group["impact"] + feasibility_weight * group["feasibility"] + cost_effectiveness_weight * group["cost_effectiveness"]) * group["evaluator_confidence"]
    total_confidence = group["evaluator_confidence"].sum()
    return weighted_scores.sum() / total_confidence

# group evaluations by org id and compute EU score for each one
eu_scores = evaluations_df.groupby("organization_id").apply(compute_eu, include_groups=False).reset_index(name="EU_score")

# merge EU scores with organization data
organizations_df = organizations_df.merge(eu_scores, on="organization_id", how="left")


# Calculate total available funds
total_funds = evaluators_df["budget"].sum()
print(f"Total funds available: {total_funds}")


# Allocate grants to organizations in proportion to their EU scores, compared to the sum of all EU scores
# The grant amount is capped at the requested amount
organizations_df["grant_awarded"] = np.minimum(np.floor(organizations_df["EU_score"] / organizations_df["EU_score"].sum() * total_funds).astype(int), organizations_df["grant_requested"])
# Optionally, we can remove the cap on the grant amount at the requested amount.
# But as a result, some orgs may receive significantly more than they requested, which may seem unfair.
# organizations_df["grant_awarded"] = np.floor(organizations_df["EU_score"] / organizations_df["EU_score"].sum() * total_funds).astype(int)

# Write the results to a CSV file
organizations_df.to_csv("grant_allocation.csv", columns=["organization_id", "organization_name", "grant_requested", "grant_awarded"], index=False)


# funds may remain if we cap the grant amount at the requested amount
# remaining_funds = total_funds - organizations_df["grant_awarded"].sum()
# print(f"Remaining funds: {remaining_funds}")
