#!/usr/bin/env python3
"""
A basic network inventory generation script.

Goal:
- Create a csv inventory file device name, software version, uptime,
  serial number.
"""

from pyats.topology.loader import load

# Script entry point
if __name__ == "__main__":
    import argparse

    print("Creating a network inventory script.")

    # Load pyATS testbed into script
    parser = argparse.ArgumentParser(description = 'Generate network inventory report')
    parser.add_argument('testbed', type=str, help='pyATS Testbed File' )

    args = parser.parse_args()

    # Create pyATS testbed object
    testbed = load(args.testbed)

    # Connect to network devices.
    testbed.connect()

    # Run commands to gather output from devices

    # Build inventory report data structure

    # Generate CSV file of data
