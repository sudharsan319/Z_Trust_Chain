from identity.did import generate_did
from crypto.ecdsa import generate_keypair, sign_message, verify_signature
from crypto.shamir import generate_shares, reconstruct_secret
from blockchain.ledger import BlockchainLogger
from policy.access import compute_access_score, compute_risk_score
from policy.engine import enforce_policy
from session.manager import create_session, is_session_valid
from crypto.utils import contextual_nonce, sha3_256
import time
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Step 1: Identity and Key Generation
    did = generate_did()
    priv, pub = generate_keypair()
    print(f"Generated DID: {did}")

    # Step 2: Shamir Secret Sharing for session key
    secret = b'sessionraw123456'
    shares = generate_shares(secret, 3, 5)
    recovered = reconstruct_secret(shares[:3])
    assert recovered == secret

    # Step 3: Prepare message and sign
    nonce = contextual_nonce("tpmPCRvalue", "00:11:22:33:44:55", time.time())
    timestamp = int(time.time())
    policy_hash = "some_policy_hash"
    message = f"{did}{nonce}{timestamp}{policy_hash}".encode()
    signature = sign_message(priv, message)

    # Step 4: Verify signature before proceeding
    assert verify_signature(pub, message, signature), "Signature verification failed!"
    print("Signature verified successfully.")

    # Step 5: Log multiple events to blockchain and calculate TPS
    prev_hash = sha3_256(b'previous_block')  # For demo; replace with actual previous block hash
    abi_path = "build/AuthEvents_abi.json"
    contract_address = os.getenv("contract_address")
    logger = BlockchainLogger(abi_path, contract_address)

    total_transactions = 500  # Total number of transactions to log
    max_transactions_per_block = 200  # Max transactions per block
    start_time = time.time()

    for block_start in range(0, total_transactions, max_transactions_per_block):
        block_transactions = min(max_transactions_per_block, total_transactions - block_start)
        events_batch = []
        for i in range(block_transactions):
            event = {
                'prevHash': prev_hash,
                'nonce': nonce,
                'did': did,
                'timestamp': timestamp + block_start + i,
                'signature': signature.hex(),
                'policyHash': policy_hash
            }
            events_batch.append(event)
        logger.log_events_batch(events_batch)
        print(f"Block with {block_transactions} transactions logged.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    tps = total_transactions / elapsed_time

    print(f"Logged {total_transactions} transactions in {elapsed_time:.2f} seconds.")
    print(f"Transactions per second (TPS): {tps:.2f}")

if __name__ == "__main__":
    main()
