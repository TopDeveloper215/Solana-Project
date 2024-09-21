import os
import time

for i in range(10):
    print(f"Running iteration {i + 1} of 10...")
    os.system('python ./create_token.py')
    time.sleep(10)  # This adds a 2-second delay between each iteration
    os.system('python ./airdrop.py')
    
    # Optional: Add a delay between iterations, if needed
    time.sleep(30)  # This adds a 2-second delay between each iteration
