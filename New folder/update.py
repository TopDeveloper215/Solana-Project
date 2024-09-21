import subprocess

# Helper function to run CLI commands
def run_cli_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None

def load_tokens_from_file(file_path):
    tokens_to_update = []
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

            # Start reading after the header line (skip the first 2 lines)
            for line in lines[2:]:
                parts = line.split()
                if len(parts) == 2:
                    token_address = parts[0]
                    balance = int(parts[1])
                    
                    if balance < 1000:
                        tokens_to_update.append((token_address, balance))
                        
        return tokens_to_update
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def mint_tokens_if_needed(token_address, current_balance, required_balance=1000):
    if current_balance < required_balance:
        amount_to_mint = required_balance - current_balance
        print(f"Minting {amount_to_mint} tokens to {token_address}.")
        mint_command = f"spl-token mint {token_address} {amount_to_mint}"
        run_cli_command(mint_command)
    else:
        print(f"Token {token_address} already has sufficient balance: {current_balance}.")

def main():
    # File containing the token balances
    token_file = 'tokens.txt'

    # Load tokens from the file where balance < 1000
    tokens_to_update = load_tokens_from_file(token_file)

    if not tokens_to_update:
        print("No tokens found with balance less than 1000 or error reading file.")
        return

    # Mint tokens for each account where balance is less than 1000
    for token_address, balance in tokens_to_update:
        mint_tokens_if_needed(token_address, balance)

if __name__ == "__main__":
    main()
