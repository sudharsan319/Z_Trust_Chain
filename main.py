from identity.did import generate_did
from crypto.ecdsa import generate_keypair, sign_message, verify_signature
from crypto.shamir import generate_shares, reconstruct_secret
from blockchain.ledger import BlockchainLogger
from policy.access import compute_access_score, compute_risk_score
from policy.engine import enforce_policy
from session.manager import create_session, is_session_valid
from crypto.utils import contextual_nonce, sha3_256
import time

def main():
    # Step 1: Identity and Key Generation
    did = generate_did()
    priv, pub = generate_keypair()
    print(f"Generated DID: {did}")

    # Step 2: Shamir Secret Sharing for session key
    secret = b'sessionkey123456'
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

    # Step 5: Log event to blockchain (Ganache)
    prev_hash = sha3_256(b'previous_block')  # For demo; replace with actual previous block hash
    abi_path = "build/AuthEvents_abi.json"
    contract_address = "0x4f3D04bEfD49CC50fd60c452A0685D2a284CD5cE"  # Replace with your deployed contract address
    logger = BlockchainLogger(abi_path, contract_address)
    logger.log_event(
        prev_hash=prev_hash,
        nonce=nonce,
        did=did,
        timestamp=timestamp,
        signature=signature.hex(),
        policy_hash=policy_hash
    )

    # Step 6: Compute access and risk score
    access_score = compute_access_score(0.95, 0.9, 0.8, 0.7)
    risk_score = compute_risk_score(0.1, 0.2, 0.05)
    print(f"Access Score: {access_score}, Risk Score: {risk_score}")

    # Step 7: Enforce policy
    access = enforce_policy(access_score, risk_score)
    print(f"Policy Decision: {access}")

    # Step 8: Session management
    session_id = create_session(did, nonce, timestamp)
    valid = is_session_valid(timestamp, 300, timestamp+100, False)
    print(f"Session ID: {session_id}, Valid: {valid}")

if __name__ == "__main__":
    main()
