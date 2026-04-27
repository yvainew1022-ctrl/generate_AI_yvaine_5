# Inventory Risk Calculator Skill

## What it does
This skill evaluates inventory aging and estimates waste risk for perishable flower stock, helping users make data-driven procurement and inventory decisions.

## Why I chose it
Fresh flowers have an extremely short shelf life (typically 2–3 days), and any unsold stock translates directly into financial loss. This skill provides a consistent, structured way to quantify that risk before it becomes a sunk cost.

## When to use
Use this skill whenever you need to assess whether current inventory is likely to expire before it can be sold. It is especially useful for daily procurement planning and ongoing inventory management of perishable goods.

## How to use
Provide a CSV file containing the following inventory data:

Inventory quantity
Intake date
Current date
Shelf life (in days)
Average daily demand

## Why a script is required
The Python script handles deterministic calculations that a language model alone cannot perform reliably, including:

Computing precise date differences (inventory age)
Calculating remaining shelf life
Estimating sellable versus waste quantities
Assigning a consistent, rule-based risk level

Using code ensures accuracy and reproducibility, which is critical for time-sensitive, quantity-driven decisions.

## Output
The skill returns:

Inventory age
Remaining shelf life
Estimated sellable quantity
Estimated waste quantity
Risk level (Low / Medium / High)
A brief, actionable recommendation

## Limitations
This skill is intended for decision support only. It does not issue final Buy / Do Not Buy decisions and should always be used in combination with human judgment and business context.

## Video link
(Add your video link here)