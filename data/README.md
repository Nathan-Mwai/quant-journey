# Data

## usd_kes_cbk_2026.csv
- **What:** Central Bank of Kenya (CBK) indicative exchange rate, Kenyan shillings (KES) per 1 US dollar (USD)
- **Downloaded:** 10 November 2026, through the Frankfurter API
- **Request:** https://api.frankfurter.dev/v2/rates.csv?base=usd&quotes=kes&providers=cbk&from=2026-01-01&to=2026-11-09
- **Original source:** https://www.centralbank.go.ke/forex/
- **Columns:** `date`, `base` (USD), `quote` (KES), `rate`

## Things to know about this file
- **The first row is 31 December 2025,** not 1 January 2026. The API included the last rate before the start date, probably because 1 January is a public holiday.
- **Only weekdays have rates.** There are no weekend rows. Missing dates aren't errors.
- **It's an indicative rate,** a reference rate from CBK, not the price a bank or bureau charges you.
- **Spot check:** the same API gives KES 157.9012 for 5 January 2024, which matches the figure on CBK's own forex page.
- Frankfurter says rates come with no warranty and "can be late, missing, or revised." Check CBK's own publication for anything important.
