import os

def generate_did():
    rand = os.urandom(4).hex()
    return f"did:ztrust:{rand}:publicKey=ecdsa-p256-k1"
