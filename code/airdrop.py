import subprocess

def run_cli_command(command, shell_type='powershell'):
    try:
        if shell_type == 'powershell':
            command = f'powershell -Command {command}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None

def airdrop_sol():
    print("Requesting airdrop of 2 SOL...")
    airdrop_output = run_cli_command("solana airdrop 2", shell_type='powershell')
    if airdrop_output:
        print(f"Airdrop Result: {airdrop_output}")
    else:
        print("Airdrop failed. Try again later.")

def main():
    # Ensure that Solana CLI is installed and accessible
    if not run_cli_command("solana --version"):
        print("Solana CLI not found. Please install it and ensure it's in your PATH.")
        return
    
    airdrop_sol()

if __name__ == "__main__":
    main()
