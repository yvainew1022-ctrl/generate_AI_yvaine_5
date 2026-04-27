from datetime import datetime
import csv

def calculate_risk(row):
    variety = row["flower_variety"]
    qty = int(row["inventory_quantity"])
    intake_date = datetime.strptime(row["intake_date"], "%Y-%m-%d")
    current_date = datetime.strptime(row["current_date"], "%Y-%m-%d")
    shelf_life = int(row["shelf_life_days"])
    demand = float(row["avg_daily_demand"])

    days_in_storage = (current_date - intake_date).days
    days_remaining = max(0, shelf_life - days_in_storage)

    sellable = min(qty, demand * days_remaining)
    waste = max(0, qty - sellable)

    waste_ratio = waste / qty if qty > 0 else 0

    if waste_ratio < 0.2:
        risk = "Low"
    elif waste_ratio < 0.5:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "variety": variety,
        "days_in_storage": days_in_storage,
        "days_remaining": days_remaining,
        "sellable": int(sellable),
        "waste": int(waste),
        "risk": risk
    }


def process_csv(file_path):
    results = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(calculate_risk(row))
    return results


if __name__ == "__main__":
    file_path = "sample_data/inventory_examples.csv"
    results = process_csv(file_path)

    for r in results:
        print(f"\n=== {r['variety']} ===")
        print(f"Inventory age: {r['days_in_storage']} days")
        print(f"Remaining shelf life: {r['days_remaining']} days")
        print(f"Estimated sellable units: {r['sellable']}")
        print(f"Estimated waste: {r['waste']}")
        print(f"Risk level: {r['risk']}")

        if r['risk'] == "High":
            print("⚠️ High risk of waste. Avoid additional purchasing.")
        elif r['risk'] == "Medium":
            print("⚠️ Moderate risk. Monitor demand closely.")
        else:
            print("✅ Low risk. Inventory level is healthy.")