# simple Faucet Vault for Python2
# By Conor Howland (Snaddyvitch-Dispenser.github.io)

def simpleFaucetVault(has, inVault, max_amt, cost, per, rounding = 2):
    """Has: Amount Player Has. Max_Amt: Maximum before vaulting. Cost: Cost Per Turn for each PER amount"""
    if (has<max_amt):
        has = has + inVault
        inVault = 0

    if (has>max_amt):
        inVault += has - max_amt
        has = max_amt
    
    if (inVault >  0):
        inVaultB = inVault
        inVault -= round(((float(inVault)*float(float(cost)/float(per)))),rounding)
        inVault = round(inVault, rounding)
        if (round(inVaultB, rounding) == inVault):
            inVault -= 0.01
            inVault = round(inVault, rounding)
        
    return [has, inVault]

#bal = 7000

#while bal > 5000:
#    tmp = simpleFaucetVault(bal,0, 5000, 1, 100, 2)

#    print tmp
    
#    bal = tmp[0] + tmp[1]
