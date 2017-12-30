#!/usr/bin/env python3

# A simple OFFLINE wallet generator / recovery tool using BIP39 mnemonic wordlists

# Instructions:
#  Current Pypi module 'stellar-base' appears to be abandoned.  You'll need to use
#  a local PIP installation for now.  This should be 'StellarCN/py-stellar-base', but
#  until https://github.com/StellarCN/py-stellar-base/pull/62 is merged, use 'overcat/py-stellar-base':
#
#
#    python3 -m venv stellar_dw
#    cd stellar_dw
#    . bin/activate
#    git clone https://github.com/overcat/py-stellar-base.git
#    pip3 install ./py-stellar-base
#    now run this script, eg: python3 ./stellar_dw.py


from stellar_base.utils import StellarMnemonic
from stellar_base.keypair import Keypair


recovery = input("recovering a seed from a wordlist? (y/n)")

if recovery[0].lower() == "y":
  wordlist = input("OK, paste your complete wordlist here, no special formatting or quotes" '\n')
  print('\n' "Recovering your keypair from wordlist")
  kp = Keypair.deterministic(wordlist)
  publickey = kp.address().decode()
  seed = kp.seed().decode()
  print('\n' "Public key / funds address:")
  print("   " + publickey)
  print('\n' "Secret seed:")
  print("   " + seed)

else:
  print('\n' "OK, let's generate a wordlist then")
  sm = StellarMnemonic()
  m = sm.generate()
  print('\n' "Secret word list for deterministic seed:")
  print("   " + m)
  kp = Keypair.deterministic(m, lang='english')
  publickey = kp.address().decode()
  seed = kp.seed().decode()
  print('\n' "Public key / funds address:")
  print("   " + publickey)
  print('\n' "Secret seed:")
  print("   " + seed)
