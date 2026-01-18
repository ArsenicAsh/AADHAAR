def classify_stress(error_rate):
    if error_rate >= 8:
        return "High"
    elif error_rate >= 4:
        return "Medium"
    return "Low"
