# analysis/thresholds.py

rpm_temp_limits = {
    1200: 45,
    1800: 47,
    2400: 48.5,
    3000: 49.5
}

def get_safe_limit(rpm):
    # Default to highest threshold if unknown RPM
    return rpm_temp_limits.get(rpm, 80)

