import hashlib as hasher
import datetime as dt

KelleyChain = []

class KelleyCoin:
	# init for creating a KelleyCoin object
	def __init__(self, index, ts, value, prev_hash):
		self.index = index
		self.ts = ts
		self.value = value
		self.prev_hash = prev_hash
		self.hash = self.hasher()

	# method to return hash of value passed
	def hasher(self):
		sha = hasher.sha256()
		value = str(self.index) + str(self.ts) + str(self.value) + str(self.prev_hash)
		sha.update(value)
		return sha.hexdigest()

# creating the genesis block
def genesis():
	return KelleyCoin(0,dt.datetime.now(), 1, '0')

# creating a new block
def gen_new_block(prev_block):
	new_index = prev_block.index + 1
	new_ts = dt.datetime.now()
	new_value = prev_block.value * 2
	# the hash value here is the hash of previous block, to identify which block is where in the chain. 
	new_hash = prev_block.hash
	return KelleyCoin(new_index, new_ts, new_value, new_hash)

# Initiating the blockchain with genesis block
KelleyChain.append(genesis())
previous_block = KelleyChain[0]

# number of blocks(coins) to be added after genesis
no_coins = input('How many coins would you like? ')

# add the coins in the chain
for i in range(0, no_coins):
	new_coin = gen_new_block(previous_block)
	KelleyChain.append(new_coin)
	previous_block = new_coin
	print "Added coin number", new_coin.index, "with value = $",new_coin.value
	print "Hash value = ",new_coin.hash

