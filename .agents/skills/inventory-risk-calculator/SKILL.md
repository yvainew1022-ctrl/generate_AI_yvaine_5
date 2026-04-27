---
name: inventory-risk-calculator
description: Calculates inventory aging and waste risk for perishable flower inventory based on intake date, shelf life, stock quantity, and recent demand. Use when evaluating whether existing inventory may expire before being sold.
---

# When to use
Use this skill when the user wants to evaluate inventory risk for perishable goods such as flowers, especially when considering waste due to short shelf life.

# When not to use
Do not use this skill to make final purchase decisions.
Do not use this skill for financial forecasting or supplier evaluation.

# Inputs
- flower variety
- inventory quantity
- intake date (YYYY-MM-DD)
- current date (YYYY-MM-DD)
- shelf life (in days)
- average daily demand

# Steps
1. Calculate how many days the inventory has been in storage.
2. Calculate remaining shelf life.
3. Estimate how many units can be sold before expiration.
4. Estimate how many units will expire.
5. Assign a risk level based on waste proportion.

# Output format
- Flower variety
- Days in storage
- Days remaining
- Estimated sellable quantity
- Estimated waste quantity
- Risk level (Low / Medium / High)
- Short recommendation

# Limitations
This skill provides decision support only. It does not replace human judgment or make final procurement decisions.