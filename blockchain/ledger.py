import hashlib
import time

class Transaction:
    def __init__(self, prev_hash, nonce, did, ts, signature, policy_hash):
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.did = did
        self.ts = ts
        self.signature = signature
        self.policy_hash = policy_hash

    def serialize(self):
        return f"{self.prev_hash}{self.nonce}{self.did}{self.ts}{self.signature}{self.policy_hash}".encode()

class Block:
    def __init__(self, prev_hash, tx_list):
        self.prev_hash = prev_hash
        self.tx_list = tx_list
        self.timestamp = int(time.time())
        self.merkle_root = self.compute_merkle_root()

    def compute_merkle_root(self):
        hashes = [hashlib.sha3_256(tx.serialize()).hexdigest() for tx in self.tx_list]
        while len(hashes) > 1:
            hashes = [hashlib.sha3_256((hashes[i] + hashes[i+1]).encode()).hexdigest()
                      for i in range(0, len(hashes), 2)]
        return hashes[0] if hashes else None

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def last_hash(self):
        return self.chain[-1].merkle_root if self.chain else "0"*64

    def add_transaction(self, tx):
        self.current_transactions.append(tx)

    def mine_block(self):
        block = Block(self.last_hash(), self.current_transactions)
        self.chain.append(block)
        self.current_transactions = []
