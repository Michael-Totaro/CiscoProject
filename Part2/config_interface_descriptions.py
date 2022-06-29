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

    import argparse
    parser = argparse.ArgumentParser(description='Deploying standard inteface descriptions to network.')

    parser.add_argument('--testbed', required=True, type=str, help='pyATS Testbed File')

    parser.add_argument('--sot', required=True, type=str, help='Interface Connection Source of Truth Spreadsheet')

    parser.add_argument('--apply', action='store_true', help='Should configurations be applied to network.' +
                        'If not set, config not applied.')

    args = parser.parse_args()

    print(f"Generating interface descriptions from file {args.sot} for testbed {args.testbed}.")

    if args.apply:
        print("Configurations will be applied to devices.")
    else:
        print("Configurations will NOT be applied to devices. They will be output to the screen only.")

    # Read data from CSV source of truth
    print("Opening and readying Source of Truth File.\n")

    with open(args.sot, "r") as sot_file:
        sot = csv.DictReader(sot_file)

        # Loop over each row in the Source of Truth
        for row in sot: 
            # For debugging, print out the raw data.
            print(row)
