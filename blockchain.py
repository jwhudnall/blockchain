# Credit: https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531 

import hashlib # encryption
import json # format blocks
from time import time # block timestamp


class Blockchain(object):
    def __init__(self):
        self.chain = [] # block-chain
        self.pending_transactions = [] # Transactions populate this list until approved/added to new block

        self.new_block(previous_hash='Something original', proof=100)



    def new_block(self, proof, previous_hash=None):
        '''Creates new blocks.
        
        Args:
            proof: 
            previous_hash:
            
        Returns:
            block
        '''
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @ property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True) # unpacks block
        block_string = string_object.encode() # Convert to bytes

        raw_hash = hashlib.sha256(block_string) # Convert to sha256 hash object
        hex_hash = raw_hash.hexdigest() # Convert hash to hex

        return hex_hash

