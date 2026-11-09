# Lesson 3: Functions and reading real data
#
# The data is REAL: Central Bank of Kenya (CBK) indicative exchange rates,
# downloaded through the free Frankfurter API on 10 November 2026.
# Source: https://api.frankfurter.dev/v2/rates.csv?base=usd&quotes=kes&providers=cbk&from=2026-01-01&to=2026-11-09
# Each "rate" is how many Kenyan shillings (KES) one US dollar (USD) costs.

# IMPORT brings in code that someone else wrote.
# csv is part of Python's standard library, which ships with Python itself,
# so nothing needs to be installed.
import csv


# A FUNCTION is a named, reusable piece of code.
#   def           starts the definition
#   old, new      are PARAMETERS: the inputs the function needs
#   return        hands the answer back to whoever called the function
def percent_change(old, new):
    return (new - old) / old * 100


# This function reads the CSV file and returns two lists: dates and rates.
def load_rates(path):
    dates = []
    rates = []
    # "with open(...)" opens the file and closes it again automatically.
    with open(path, encoding="utf-8") as file:
        # DictReader uses the header row (date,base,quote,rate) as names,
        # so each row works like row["date"] and row["rate"].
        for row in csv.DictReader(file):
            dates.append(row["date"])
            # Everything read from a file is TEXT. "129.71" is not a number
            # until float() converts it.
            rates.append(float(row["rate"]))
    return dates, rates


# Below here, we USE the functions. Nothing above runs until it's called.
dates, rates = load_rates("data/usd_kes_cbk_2026.csv")

print("Rows read:", len(rates))
print("First:", dates[0], "KES", rates[0], "per USD")
print("Last: ", dates[-1], "KES", rates[-1], "per USD")

# The same function works for any two numbers. That's why we wrote it.
change = percent_change(rates[0], rates[-1])
print("Change over the period:", round(change, 2), "%")

# A rising KES-per-USD rate means a dollar costs MORE shillings,
# so the shilling has become WEAKER. This is called depreciation.
if change > 0:
    print("The shilling weakened against the dollar.")
elif change < 0:
    print("The shilling strengthened against the dollar.")
else:
    print("No change.")
