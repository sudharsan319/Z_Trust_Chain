from ecdsa import SigningKey, NIST256p

def generate_keypair():
    priv = SigningKey.generate(curve=NIST256p)
    pub = priv.get_verifying_key()
    return priv, pub

#priv - ECSDA private key
#pub - ECSDA public key
#ECSDA - Elliptic Curve Digital Signature Algorithm

def sign_message(priv, message):
    return priv.sign(message)

def verify_signature(pub, message, signature):
    return pub.verify(signature, message)
