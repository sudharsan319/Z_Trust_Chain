# Z-TrustChain Prototype

## How to Run

1. Deploy the AuthEvent.sol contract to Ganache and save the ABI and address.
2. Install dependencies:
   pip install -r requirements.txt
3. Update contract address and private key in blockchain/ledger.py and main.py.
4. Run the main script:
   python main.py

## What Happens

- Generates DID and keypair
- Demonstrates Shamir secret sharing
- Signs and verifies an authentication event
- Logs the event to the blockchain (Ganache)
- Computes access/risk scores and enforces policy
- Manages session and prints results
