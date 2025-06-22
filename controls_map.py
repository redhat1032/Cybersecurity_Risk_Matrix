import json

# Load control data
with open("sample_controls.json", "r") as file:
    controls = json.load(file)

# Group by risk level
risk_matrix = {"High": [], "Medium": [], "Low": []}

for control in controls:
    risk_level = control.get("risk_level", "Unknown")
    risk_matrix.setdefault(risk_level, []).append(control)

# Print summary
for level, items in risk_matrix.items():
    print(f"\n{level} Risk Controls:")
    for item in items:
        print(f" - {item['id']}: {item['name']}")