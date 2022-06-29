#!/usr/bin/env python3

"""
A script to create and apply interface descriptions from CSV
file based source of truth.

Goal:
  - Create interface description config from CSV file
  - Apply configurations to devices with confirmation
  - Record initial/old interface description back to CSV
  - Verify if interfaces are connected as documented in CSV
"""

# Script entry point
if __name__ == "__main__":
    print("Deploying standard inteface interface descriptions to network.")

    # Read data from CSV source of truth
    # Generate desired interface description configurations
    # Load pyATS testbed and connect to devices
    # Lookup current inteface descriptions
    # Apply new interface description configuration (with confirmation)
    # Gather CDP/LLDP neighbor details from devices
    # Check if neightbor details match source of truth
    # Disconnect from devices
    # Update Source of Truth with results 
