import os

def generate_ephemeral_key():
    return os.urandom(32)  # 256-bit key

def rotate_key():
    return generate_ephemeral_key()
