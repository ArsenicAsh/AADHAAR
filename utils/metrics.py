def compute_summary_metrics(df):
    total_enrollments = df["enrollments"].sum()
    total_updates = df["updates"].sum()

    success_rate = (
        df["success_count"].sum() / df["updates"].sum()
    ) * 100

    error_rate = (
        df["error_count"].sum() / df["updates"].sum()
    ) * 100

    return {
        "total_enrollments": int(total_enrollments),
        "daily_updates": int(total_updates),
        "success_rate": round(success_rate, 2),
        "error_rate": round(error_rate, 2),
    }
