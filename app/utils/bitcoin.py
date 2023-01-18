from bitcoinlib.keys import HDKey
from bitcoinlib.mnemonic import Mnemonic


def generate_mnemonic():
    words = Mnemonic().generate(strength=256)
    return words


def get_master_privatekey(mnemonic):
    seed = Mnemonic().to_seed(mnemonic).hex()
    private_key = HDKey().from_seed(seed)
    return private_key.hex()


def get_xpub_from_private_key(pk):
    k = HDKey(pk)
    pm = k.public_master()
    return pm.hex()
