# Weather ETL Pipeline

## Project Overview
This project is an ETL (Extract, Transform, Load) pipeline that fetches daily weather data from the Open-Meteo API, cleans and transforms it, and saves it as a CSV for further analysis. It demonstrates a modular Python ETL workflow using `requests` and `pandas`.

---
## Features
- Extracts daily weather data (temperature, precipitation, sunrise, weather code) for Baku, Azerbaijan.
- Converts raw JSON data into a clean Pandas DataFrame.
- Performs basic data validation:
  - Checks for missing values
  - Removes duplicate dates
  - Ensures valid temperature ranges and non-negative precipitation
- Saves transformed data as CSV in `data/processed/`.
- Modular design for easy expansion or replacement of data sources.

---

## Getting Started
### Installation
1. Clone the repository:

```bash
git clone <https://github.com/AhmadUghurluzada/Weather-ETL-pipeline.git>
cd <Weather-ETL-pipeline>
```

---

## Data Source
- **API:** Open-Meteo  
- **Location:** Baku, Azerbaijan  
- **Frequency:** Daily  
- **Metrics:**
  - Maximum temperature (°C)
  - Minimum temperature (°C)
  - Precipitation (mm)
  - Sunrise time
  - Weather code

---

## ETL Process

### 1. Extract
- Sends a GET request to the Open-Meteo API
- Saves raw JSON data to:

### 2. Transform
- Converts raw JSON into a Pandas DataFrame
- Sets date as a `DatetimeIndex`
- Renames columns to consistent, readable names
- Performs data quality checks:
- Detects missing values
- Removes duplicate dates
- Ensures:
  - `temp_max_c >= temp_min_c`
  - `precipitation_mm >= 0`

### 3. Load
- Writes cleaned data to: `data/processed/`.


---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Run the full pipeline
```bash
python src/pipeline.py
```