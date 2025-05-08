from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

class BlockchainLogger:
    def __init__(self, abi_path, contract_address, ganache_url="http://127.0.0.1:7545"):
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        assert self.web3.is_connected(), "Web3 not connected to Ganache!"
        with open(abi_path) as f:
            abi = json.load(f)
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
        self.account = self.web3.eth.accounts[0]
        self.private_key = os.getenv("private_key")  # Replace with actual key

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

    def log_events_batch(self, events):
        tx = self.contract.functions.logEventsBatch(events).build_transaction({
            'from': self.account,
            'nonce': self.web3.eth.get_transaction_count(self.account),
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Batch of events stored in block:", receipt.blockNumber)
        return receipt
