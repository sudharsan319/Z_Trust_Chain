from identity.did import generate_did
from crypto.ecdsa import generate_keypair, sign_message, verify_signature
from crypto.shamir import generate_shares, reconstruct_secret
from blockchain.ledger import Blockchain, Transaction
from policy.access import compute_access_score, compute_risk_score
from policy.engine import enforce_policy
from session.manager import create_session, is_session_valid

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

    # Step 3: Create a blockchain and add a transaction
    chain = Blockchain()
    tx = Transaction(prev_hash=chain.last_hash(), nonce="nonce", did=did, ts=1234567890, signature=b'sig', policy_hash="hash")
    chain.add_transaction(tx)
    chain.mine_block()

    # Step 4: Compute access and risk score
    access_score = compute_access_score(0.95, 0.9, 0.8, 0.7)
    risk_score = compute_risk_score(0.1, 0.2, 0.05)
    print(f"Access Score: {access_score}, Risk Score: {risk_score}")

    # Step 5: Enforce policy
    access = enforce_policy(access_score, risk_score)
    print(f"Policy Decision: {access}")

    # Step 6: Session management
    session_id = create_session(did, "nonce", 1234567890)
    valid = is_session_valid(1234567890, 300, 1234567900, False)
    print(f"Session ID: {session_id}, Valid: {valid}")

if __name__ == "__main__":
    main()
