#!/bin/bash

# Path to your Python virtual environment (optional, if you use one)
# source ~/Documents/1EmployeeSuite/venv/bin/activate

# Base URL for local Flask server
BASE_URL="http://127.0.0.1:5000"

# Log file location
LOG_FILE="$HOME/Documents/1EmployeeSuite/suite.log"

# Timestamp
echo "==== Run started: $(date) ====" >> $LOG_FILE

# Process Orders
ORDERS=$(curl -s $BASE_URL/process_orders)
echo "Process Orders Response: $ORDERS" >> $LOG_FILE

# Update Inventory
INVENTORY=$(curl -s $BASE_URL/update_inventory)
echo "Update Inventory Response: $INVENTORY" >> $LOG_FILE

# Generate Report
REPORT=$(curl -s $BASE_URL/generate_report)
echo "Generate Report Response: $REPORT" >> $LOG_FILE

echo "==== Run finished: $(date) ====" >> $LOG_FILE
echo "" >> $LOG_FILE

