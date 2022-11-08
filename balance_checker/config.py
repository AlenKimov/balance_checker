from os import makedirs

from definitions import SETTINGS_DIR,PUBLIC_KEYS_TXT, PRIVATE_KEYS_TXT, MNEMONICS_TXT


makedirs(SETTINGS_DIR, exist_ok=True)


with open(PUBLIC_KEYS_TXT, 'a'): pass
with open(PUBLIC_KEYS_TXT) as file:
    addresses = [address.strip() for address in file]

with open(PRIVATE_KEYS_TXT, 'a'): pass
with open(PRIVATE_KEYS_TXT) as file:
    private_keys = [private_key.strip() for private_key in file]

with open(MNEMONICS_TXT, 'a'): pass
with open(MNEMONICS_TXT) as file:
    mnemonics = [mnemonic.strip() for mnemonic in file]
