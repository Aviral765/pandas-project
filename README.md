# Titanic Data Cleaning and Analysis

A small pandas project that cleans the Titanic passenger dataset and summarizes survival patterns with charts.

## Dataset

`Titanic-Dataset.csv` contains 891 passengers and 12 columns. The raw dataset has 177 missing `Age` values, 687 missing `Cabin` values, and 2 missing `Embarked` values.

## What it does

`pandascodefile.py` cleans the raw data by removing duplicate rows and any extra index column, trimming whitespace, filling missing values (`Age` with the median, `Embarked` with the mode, and `Cabin` with `Unknown`), and filtering invalid values. It writes `cleaned_titanic.csv` with 891 rows, 12 columns, and no missing values.

`analysis.py` reads the cleaned file and prints survival rates and averages. It also creates three charts: survival by gender, survival by passenger class, and age distribution by survival.

Both scripts read and write files beside themselves, so they also work when launched from another directory.

## Setup

Use Python 3.9 or newer and install the dependencies:

```bash
python -m venv .venv
```

Activate the environment, then run:

```bash
python -m pip install -r requirements.txt
```

On macOS/Linux, activate with `source .venv/bin/activate`. On Windows PowerShell, use `.venv/Scripts/Activate.ps1`.

## Run

Run these commands from the project directory:

```bash
python pandascodefile.py
python analysis.py
```

The analysis step requires `cleaned_titanic.csv`, so run the cleaning step first. The scripts write the cleaned CSV and chart images into the project directory.

## Tests

Run the script-location regression tests with:

```bash
python -m unittest discover -s tests -v
```

## Project files

- `Titanic-Dataset.csv` — source dataset
- `pandascodefile.py` — data-cleaning script
- `cleaned_titanic.csv` — cleaned output
- `analysis.py` — summary statistics and charts
- `requirements.txt` — Python dependencies
- `tests/` — automated regression tests

## Author

Aviral Shukla
