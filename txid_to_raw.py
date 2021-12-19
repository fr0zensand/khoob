def txid_to_rawhex(txid):
    import os ; import subprocess
    os.system('electrum daemon -d')
    raw = subprocess.check_output('electrum gettransaction '+txid, shell=True)
    raw = str(raw.decode("utf-8")).replace('\n','')
    return raw
with open('txhashes','r') as infile:
    txhashes = infile.read().split('\n')
for txid in txhashes:
    raw = txid_to_rawhex(txid)
    print(raw,file=open('rawtx','a'))
