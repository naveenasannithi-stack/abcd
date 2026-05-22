import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("internet_log.csv")

# Convert Status to numbers
# Up = 1, Down = 0
data["Value"] = data["Status"].map({
    "Up": 1,
    "Down": 0
})

# Create graph
plt.figure(figsize=(10,5))

plt.plot(data["Value"], marker='o')

# Labels
plt.title("Internet Connection Health")
plt.xlabel("Checks")
plt.ylabel("Status")

# Y-axis labels
plt.yticks([0,1], ["Down","Up"])

# Grid
plt.grid(True)

# Show graph
plt.show()