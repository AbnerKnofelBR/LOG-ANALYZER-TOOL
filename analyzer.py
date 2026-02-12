def analyze_log(file_path):
    error_500 = 0
    timeout = 0
    db_error = 0

    with open(file_path, "r") as file:
        for line in file:
            if "500" in line:
                error_500 += 1
            if "Timeout" in line:
                timeout += 1
            if "Database connection failed" in line:
                db_error += 1

    print("=== INCIDENT REPORT ===")
    print(f"500 Errors: {error_500}")
    print(f"Timeouts: {timeout}")
    print(f"Database Errors: {db_error}")


if __name__ == "__main__":
    analyze_log("log-analyzer/sample.log")
