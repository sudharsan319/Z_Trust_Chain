from crypto.utils import sha3_256

def create_session(did, nonce, ts_start):
    data = f"{did}{nonce}{ts_start}".encode()
    return sha3_256(data)

def is_session_valid(start_time, t_valid, last_activity, ip_change):
    # For demo, just check time and IP change
    now = last_activity
    if now - start_time > t_valid:
        return False
    if ip_change:
        return False
    return True
