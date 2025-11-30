# reporting.py
import pandas as pd

def generate_report():
    try:
        # Example static report — replace with real logic later
        data = {
            "product": ["Widget A", "Widget B"],
            "price": [50, 75],
            "quantity": [2, 1],
            "cost": [30, 45],
            "profit": [20, 30]
        }
        df = pd.DataFrame(data)
        print("Report generated ✅")
        return "Report generated ✅"
    except Exception as e:
        return f"Error generating report: {e}"

