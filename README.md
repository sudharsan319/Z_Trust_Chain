# Z-TrustChain Prototype

## How to Run

1. Install dependencies:
   `pip install -r requirements.txt`

2. Download and set up Ganache:
   - Download Ganache from [https://trufflesuite.com/ganache/](https://trufflesuite.com/ganache/).
   - Start Ganache and create a new workspace or use the default one.
   - Copy the contract address and private key from the Ganache interface and paste them in the .env file.

3. Run the main script:
   `python main.py`

## What to Expect

- Generates a DID and keypair
- Demonstrates Shamir secret sharing
- Adds a transaction to a blockchain and mines a block
- Computes access and risk scores
- Enforces a sample policy and prints the result
- Creates and validates a session

