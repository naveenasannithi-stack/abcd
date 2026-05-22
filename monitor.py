import time
import csv
import platform
from datetime import datetime
import subprocess
import os
import re

# Function to check internet and latency
def check_internet():
    host = "8.8.8.8"

    param = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", param, "1", host]

    result = subprocess.run(command, capture_output=True, text=True)

    output = result.stdout

    if result.returncode == 0:

        # Extract latency
        latency_match = re.search(r"time[=<]\s*(\d+)", output)

        if latency_match:
            latency = latency_match.group(1) + " ms"
        else:
            latency = "N/A"

        return "Up", latency

    else:
        return "Down", "N/A"

# CSV file
file_name = "internet_log.csv"

file_exists = os.path.isfile(file_name)

with open(file_name, mode="a", newline="") as file:

    writer = csv.writer(file)

    # Write headings once
    if not file_exists:
        writer.writerow(["Timestamp", "Status", "Latency"])

    while True:

        status, latency = check_internet()

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        writer.writerow([current_time, status, latency])

        print(f"{current_time} --> {status} --> {latency}")

        file.flush()

        time.sleep(5)