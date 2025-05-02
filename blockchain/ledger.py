from web3 import Web3
import json

class BlockchainLogger:
    def __init__(self, abi_path, contract_address, ganache_url="http://127.0.0.1:7545"):
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        assert self.web3.is_connected(), "Web3 not connected to Ganache!"
        with open(abi_path) as f:
            abi = json.load(f)
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
        self.account = self.web3.eth.accounts[0]
        # For demo only; use secure key management in production
        self.private_key = "0xd4edac3929bd2377508e3d4f1ff47ef5f54ea896392a1afb9039c1afcecb8057"  # Replace with actual key

    def log_event(self, prev_hash, nonce, did, timestamp, signature, policy_hash):
        tx = self.contract.functions.logEvent(
            prev_hash, nonce, did, timestamp, signature, policy_hash
        ).build_transaction({
            'from': self.account,
            'nonce': self.web3.eth.get_transaction_count(self.account),
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Event stored in block:", receipt.blockNumber)
        return receipt
