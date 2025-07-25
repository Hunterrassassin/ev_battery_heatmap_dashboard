import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from parser import load_log_data
from thresholds import get_safe_limit

def plot_temp_heatmap():
    df = load_log_data()
    if df is None:
        return


    # Check for overheating and print alerts
    overheating_rows = df[df.apply(lambda row: row['temp_c'] > get_safe_limit(row['rpm']), axis=1)]

    if not overheating_rows.empty:
        print("\n⚠️ Smart ALERT: RPM-based Overheating detected!\n")
        for _, row in overheating_rows.iterrows():
            print(f"🚨 Temp = {row['temp_c']}°C at {row['timestamp']}s | RPM = {row['rpm']} (limit: {get_safe_limit(row['rpm'])}°C)")
    else:
        print("\n✅ All temperatures are within safe range.\n")




    # Round timestamps to nearest 0.1s for grouping
    df['timestamp'] = df['timestamp'].round(1)

    # Pivot for heatmap: rows = RPM, columns = Time, values = Temp
    heatmap_data = df.pivot(index='rpm', columns='timestamp', values='temp_c')

    # Plotting
    plt.figure(figsize=(14, 6))
    sns.heatmap(heatmap_data, cmap='hot', annot=False, fmt=".1f",cbar_kws={'label': 'Temperature (°C)'})
    plt.gca().invert_yaxis()
    plt.title("EV Battery Temperature Heatmap (RPM vs Time)")
    plt.xlabel("Time (s)")
    plt.ylabel("Motor RPM")
    plt.tight_layout()
    os.makedirs('static', exist_ok=True)
    plt.savefig("static/heatmaps/temp3.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_temp_heatmap()
