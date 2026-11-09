# Exercise 3: The shilling in 2026

## Before you code: predict
Look at a few rows of `data/usd_kes_cbk_2026.csv` in VS Code, then write down your guesses:
1. Out of 215 trading days, on roughly how many did the shilling weaken?
2. Was the biggest one-day move a weakening or a strengthening?

## Tasks
1. **Load the data.** Copy `percent_change` and `load_rates` into your file.
2. **Write a function `daily_changes(rates)`** that returns a **list** of daily percent changes.
   Inside it, use `percent_change`. Don't repeat the formula.
3. **Count the days.** Print how many days the shilling weakened (change above 0), strengthened (below 0), and stayed flat (exactly 0).
   Check: your three counts must add up to 215.
4. **Biggest moves.** Print the largest daily change and the smallest, as percentages rounded to 3 decimal places.
   You can now use Python's built-in `max()` and `min()` on your list.
5. **Which day?** Print the **date** of the largest change.
   Hint: `my_list.index(value)` tells you where a value sits in a list. Think carefully about how your changes line up with `dates`, because there's one fewer change than there are dates.

## Economics questions (answer in a comment at the bottom of your file)
1. The rate went from about 129.01 to 129.96 this year. Who in Kenya is hurt when the shilling weakens, and who benefits? Give one example of each.
2. If a dollar costs 0.74% more shillings, has the shilling lost exactly 0.74% of its value in dollars? Work it out using 1 / rate.
3. In January 2024 the rate was about 157.90. Compared with now, is the shilling stronger or weaker than it was then?

## When you're done
Run it, compare with your predictions, then commit:
```
git add exercise_03.py
git commit -m "Add Exercise 3: shilling daily moves"
git push
```
Remember to add a row for each new file to your README.
