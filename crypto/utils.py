import hashlib

def sha3_256(data):
    return hashlib.sha3_256(data).hexdigest()

def contextual_nonce(tpm_pcr, mac_addr, ts):
    data = f"{tpm_pcr}{mac_addr}{int(ts)//300}".encode()
    return sha3_256(data)
