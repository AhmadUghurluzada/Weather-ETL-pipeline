from extract import extract_data
from transform import transform_data
from load import load_data
import json

# Extract
raw_data = extract_data()

# Transform
df = transform_data(raw_data)

# Load
load_data(df)
