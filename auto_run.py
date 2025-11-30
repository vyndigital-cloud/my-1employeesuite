# auto_run.py
from order_processing import process_orders
from inventory import update_inventory
from reporting import generate_report

def run_suite():
    print("Starting 1 Employee Suite Automation ✅\n")

    print("Step 1: Processing Orders...")
    result_orders = process_orders()
    print(result_orders)

    print("\nStep 2: Updating Inventory...")
    result_inventory = update_inventory()
    print(result_inventory)

    print("\nStep 3: Generating Reports...")
    result_report = generate_report()
    print(result_report)

    print("\n1 Employee Suite run complete ✅")

if __name__ == "__main__":
    run_suite()

