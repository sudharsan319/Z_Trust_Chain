import os

def generate_did():
    # Simulate a unique DID (for demo)
    rand = os.urandom(4).hex()
    return f"did:ztrust:{rand}:publicKey=ecdsa-p256-k1"
