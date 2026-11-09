import csv

def percent_change(old, new):
    return ((new - old) / old) * 100

def load_rates(path):
    dates = []
    rates = []

    with open(path, encoding="utf-8") as file:
        for row in csv.DictReader(file):
            dates.append(row["date"])
            rates.append(float(row["rate"]))
    return dates, rates

dates, rates = load_rates("data/usd_kes_cbk_2026.csv")


weakening_days = 0
flattening_days = 0
strengthening_days = 0

def daily_changes(rates):
    changes = []
    for i in range(1, len(rates)):
        today = rates[i]
        yesterday = rates[i - 1]
        change = percent_change(yesterday, today)

        changes.append(change)
    return changes

changes = daily_changes(rates)

for change in changes:
    if change < 0:
        strengthening_days += 1
    elif change == 0:
        flattening_days += 1
    else:
        weakening_days += 1

position = changes.index(max(changes))
print("Weakening days:", weakening_days)
print("Flattening days:", flattening_days)
print("Strengthening days:", strengthening_days)
print("Max daily change:", round(max(changes), 3))
print("Min daily change:", round(min(changes), 3))
print("Date of max daily change:", dates[position + 1])

# Answers
# Weakening days: 92
# Flattening days: 46
# Strengthening days: 77
# Max daily change: 0.217
# Min daily change: -0.408
# Date of max daily change: 2026-04-14