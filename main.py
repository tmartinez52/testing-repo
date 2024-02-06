import os
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="A script that uses either environment variables or command-line arguments.")
parser.add_argument('--source-url', type=str, help='source url')
parser.add_argument('--source-token', type=str, help='source token')
parser.add_argument('--destination-url', type=str, help='dest url')
parser.add_argument('--destination-token', type=str, help='dest token')

# Parse the command-line arguments
args = parser.parse_args()

# Determine the values to use, preferring CLI arguments over environment variables
source_url = args.source_url if args.source_url is not None else os.environ.get('SOURCE_URL')
source_token = args.source_token if args.source_token is not None else os.environ.get('SOURCE_TOKEN')
destination_url = args.destination_url if args.destination_url is not None else os.environ.get('DESTINATION_URL')
destination_token = args.destination_token if args.destination_token is not None else os.environ.get('DESTINATION_TOKEN')

# Use the determined values in your code
print(f"Using source One: {source_url}")
print(f"Using source Two: {source_token}")
print(f"Using dest One: {destination_url}")
print(f"Using dest Two: {destination_token}")

# Example usage with the determined values
