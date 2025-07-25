import matplotlib.pyplot as plt
from parser import load_log_data

def plot_battery_metrics():
    df = load_log_data()
    if df is None:
        return

    # Plot
    plt.figure(figsize=(12, 6))

    plt.plot(df['timestamp'], df['temp_c'], label='Temperature (°C)', color='red', linewidth=2)
    plt.plot(df['timestamp'], df['voltage_v'], label='Voltage (V)', color='blue', linewidth=2)
    plt.plot(df['timestamp'], df['current_a'], label='Current (A)', color='green', linewidth=2)

    plt.title('EV Battery Metrics Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_battery_metrics()
