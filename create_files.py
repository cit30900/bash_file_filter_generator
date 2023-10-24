import os
import random
from datetime import datetime, timedelta

# Directory to create the files
directory = "log_files"

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Function to generate a random creation date
def random_date():
    # Define the date range: 22 months ago and 2 months from now
    end_date = datetime.now() + timedelta(days=60)  # 2 months from now
    start_date = end_date - timedelta(days=660)     # 22 months ago

    # Generate a random number of seconds within the date range
    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))

    # Create a random datetime object within the specified range
    random_datetime = start_date + timedelta(seconds=random_seconds)
    return random_datetime

# Loop to create 10000 empty files with random filenames and creation dates
for i in range(10000):
    # Generate a random filename
    random_filename = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(16))
    random_filename = random_filename + ".log"
    file_path = os.path.join(directory, random_filename)

    # Generate a random creation date
    random_creation_date = random_date()

    # Create an empty file with the generated filename
    open(file_path, 'w').close()

    # Set the creation date
    os.utime(file_path, (random_creation_date.timestamp(), random_creation_date.timestamp()))
