tariff_category = input("Enter the tariff category (D, E1, E2, or E3): ")

if tariff_category == "D":
    usage_kwh = float(input("Enter the monthly electricity usage in kWh: "))
    if usage_kwh <= 200:
        bill = max(7.20, usage_kwh * 0.38)
    else:
        bill = 7.20 + ((usage_kwh - 200) * 0.441)

elif tariff_category == "E1":
    usage_kwh = float(input("Enter the monthly electricity usage in kWh: "))
    demand_kw = float(input("Enter the maximum demand in kW: "))
    bill = max(600.00, (demand_kw * 29.60) + (usage_kwh * 0.337))

elif tariff_category == "E2":
    peak_demand_kw = float(input("Enter the maximum demand in kW during peak period: "))
    peak_usage_kwh = float(input("Enter the electricity usage in kWh during peak period: "))
    off_peak_usage_kwh = float(input("Enter the electricity usage in kWh during off-peak period: "))
    bill = max(600.00, (peak_demand_kw * 37.00) + (peak_usage_kwh * 0.355) + (off_peak_usage_kwh * 0.219))

elif tariff_category == "E3":
    peak_demand_kw = float(input("Enter the maximum demand in kW during peak period: "))
    peak_usage_kwh = float(input("Enter the electricity usage in kWh during peak period: "))
    off_peak_usage_kwh = float(input("Enter the electricity usage in kWh during off-peak period: "))
    bill = max(600.00, (peak_demand_kw * 35.50) + (peak_usage_kwh * 0.337) + (off_peak_usage_kwh * 0.202))

else:
    print("Invalid tariff category")

print(f"The estimated bill for tariff category {tariff_category} is RM {bill:.2f}")
