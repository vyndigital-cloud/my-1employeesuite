# main.py
from order_processing import process_orders
from inventory import update_inventory
from reporting import generate_report

def run_suite():
    print("Starting 1 Employee Suite Automation ✅\n")

    print("Step 1: Processing Orders...")
    process_orders()  # no arguments

    print("\nStep 2: Updating Inventory...")
    update_inventory()

    print("\nStep 3: Generating Reports...")
    generate_report()

    print("\n1 Employee Suite run complete ✅")

if __name__ == "__main__":
    run_suite()


