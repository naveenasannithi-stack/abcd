import pandas as pd

# Load CSV file
data = pd.read_csv("internet_log.csv")

# Total records
total_records = len(data)

# Count Up and Down
up_count = len(data[data["Status"] == "Up"])
down_count = len(data[data["Status"] == "Down"])

# Calculate uptime percentage
uptime_percentage = (up_count / total_records) * 100

# Display results
print("\n----- Internet Reliability Report -----\n")

print(f"Total Records : {total_records}")
print(f"Up Count      : {up_count}")
print(f"Down Count    : {down_count}")
print(f"Uptime %      : {uptime_percentage:.2f}%")