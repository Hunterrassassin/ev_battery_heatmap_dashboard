import os
from flask import Flask, render_template
from analysis.parser import load_log_data
from analysis.thresholds import get_safe_limit

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Load battery data
    data = load_log_data()
    alerts = []

    if data is not None:
        for _, row in data.iterrows():
            safe_limit = get_safe_limit(row['rpm'])
            if row['temp_c'] > safe_limit:
                alerts.append(
                    f"⚠️ Temp = {row['temp_c']}°C at {row['timestamp']}s | RPM = {row['rpm']} (limit: {safe_limit}°C)"
                )

    # Load heatmaps from static/heatmaps/
    image_folder = os.path.join('static', 'heatmaps')
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    image_files = [
        f"heatmaps/{f}"
        for f in os.listdir(image_folder)
        if f.lower().endswith('.png')
    ]
    print("[DEBUG] Image files found:", image_files)
    return render_template("dashboard.html", alerts=alerts, images=image_files)

if __name__ == "__main__":
    app.run(debug=True)
