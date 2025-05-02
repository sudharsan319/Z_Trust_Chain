import hashlib

def sha3_256(data):
    return hashlib.sha3_256(data).hexdigest()

def merkle_root(leaves):
    hashes = [sha3_256(leaf.encode()) for leaf in leaves]
    while len(hashes) > 1:
        hashes = [sha3_256((hashes[i] + hashes[i+1]).encode())
                  for i in range(0, len(hashes), 2)]
    return hashes[0] if hashes else None
