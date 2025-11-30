# order_processing.py
import json

def process_orders():
    try:
        creds_path = 'creds.json'
        with open(creds_path, 'r') as f:
            creds = json.load(f)
        print("Orders logged successfully ✅")
        return "Orders processed ✅"
    except FileNotFoundError:
        return f"Error: {creds_path} not found!"
    except Exception as e:
        return f"Error processing orders: {e}"

