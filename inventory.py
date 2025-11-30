import requests
import time

def update_inventory():
    for attempt in range(3):
        try:
            response = requests.get("https://httpbin.org/status/200")  # replace with real endpoint
            if response.status_code == 200:
                print("Inventory updated successfully ✅")
                return "Inventory updated ✅"
            else:
                print(f"Attempt {attempt+1}: Error updating inventory: {response.status_code}")
                time.sleep(2)
        except Exception as e:
            print(f"Attempt {attempt+1}: Exception: {e}")
            time.sleep(2)
    return "Failed to update inventory after 3 attempts ❌"

