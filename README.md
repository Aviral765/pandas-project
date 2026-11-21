# Titanic Data Cleaning with Pandas

A beginner data analysis project that cleans the Titanic passenger dataset using Python and pandas.

## Dataset

`Titanic-Dataset.csv` has 891 passengers and 12 columns, including `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `Fare`, `Cabin` and `Embarked`.

Missing values in the raw data:

| Column   | Missing values |
|----------|----------------|
| Age      | 177            |
| Cabin    | 687            |
| Embarked | 2              |

## What the script does

1. Loads the raw CSV file
2. Drops duplicate rows and any extra index column
3. Removes extra spaces from column names and text columns
4. Fills missing values instead of deleting rows:
   - `Age` is filled with the median
   - `Embarked` is filled with the most common value (mode)
   - `Cabin` is filled with `"Unknown"`
5. Keeps only valid rows (Age > 0, Fare >= 0, Survived is 0 or 1, Pclass is 1, 2 or 3)
6. Saves the result as `cleaned_titanic.csv`

Result: 891 rows and 12 columns, with 0 missing values.

## Files

- `pandascodefile.py` - the cleaning script
- `Titanic-Dataset.csv` - raw data
- `cleaned_titanic.csv` - cleaned data (output)

## How to run

```bash
pip install pandas
python pandascodefile.py
```

## Tools used

Python, pandas

## Author

Aviral Shukla
