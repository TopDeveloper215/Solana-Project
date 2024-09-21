import subprocess
import json
import os

# Helper function to run CLI commands
def run_cli_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None

def load_wallet(json_file):
    try:
        with open(json_file) as f:
            wallet = json.load(f)
        return wallet
    except Exception as e:
        print(f"Error loading wallet from JSON: {e}")
        return None

def main():
    # Load wallet configuration
    wallet_file = 'token1.json'
    wallet = load_wallet(wallet_file)
    if not wallet:
        print("Failed to load wallet configuration.")
        return

    # Ensure that Solana CLI is installed and accessible
    if not run_cli_command("solana --version"):
        print("Solana CLI not found. Please install it and ensure it's in your PATH.")
        return

    token_addresses = []

    # Loop to create 100 different tokens
    for i in range(560):
        print(f"Creating token {i+1}...")
        
        # Create a new token
        token_create_output = run_cli_command("spl-token create-token")
        if token_create_output:
            token_mint_address = token_create_output.split()[2]
            token_addresses.append(token_mint_address)
            print(f"Token {i+1} Created: {token_mint_address}")

            # Create a token account for the new token
            account_create_output = run_cli_command(f"spl-token create-account {token_mint_address}")
            if account_create_output:
                print(f"Token Account for Token {i+1} Created: {account_create_output}")

                # Mint some tokens (you can choose how many) to the created account
                mint_output = run_cli_command(f"spl-token mint {token_mint_address} 1000")
                
            else:
                print(f"Failed to create token account for Token {i+1}.")
        else:
            print(f"Failed to create Token {i+1}.")

    # Save the generated token addresses to a file for future reference

if __name__ == "__main__":
    main()
