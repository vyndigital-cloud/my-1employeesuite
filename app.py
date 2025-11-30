# app.py
from flask import Flask, jsonify
from order_processing import process_orders
from inventory import update_inventory
from reporting import generate_report
import logging

# Setup logging
logging.basicConfig(filename='suite.log', level=logging.INFO, format='%(asctime)s %(message)s')

app = Flask(__name__)

@app.route('/process_orders', methods=['GET'])
def process_orders_route():
    try:
        result = process_orders()
        logging.info("Orders processed ✅")
        return jsonify({"message": result if result else "Orders processed ✅"})
    except Exception as e:
        logging.error(f"Error processing orders: {e}")
        return jsonify({"message": f"Error processing orders: {e}"}), 500

@app.route('/update_inventory', methods=['GET'])
def update_inventory_route():
    try:
        result = update_inventory()
        logging.info("Inventory updated ✅")
        return jsonify({"message": result if result else "Inventory updated ✅"})
    except Exception as e:
        logging.error(f"Error updating inventory: {e}")
        return jsonify({"message": f"Error updating inventory: {e}"}), 500

@app.route('/generate_report', methods=['GET'])
def generate_report_route():
    try:
        result = generate_report()
        logging.info("Report generated ✅")
        return jsonify({"message": result if result else "Report generated ✅"})
    except Exception as e:
        logging.error(f"Error generating report: {e}")
        return jsonify({"message": f"Error generating report: {e}"}), 500

if __name__ == "__main__":
    # Run app on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)

