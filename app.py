from flask import Flask, render_template
import pandas as pd
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():

    # Read CSV file
    data = pd.read_csv("internet_log.csv")

    # Metrics
    total_records = len(data)

    up_count = len(data[data["Status"] == "Up"])

    down_count = len(data[data["Status"] == "Down"])

    uptime_percentage = (up_count / total_records) * 100

    return render_template(
        "index.html",
        total_records=total_records,
        up_count=up_count,
        down_count=down_count,
        uptime_percentage=round(uptime_percentage, 2),
        logs=data.tail(10).values.tolist()
    )

if __name__ == "__main__":

    # Automatically open browser
    webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)