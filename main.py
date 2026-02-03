# AIM: Calculating Simple Interest
# Coder: Adi Baluch
# Class = F.E.Computers 1
# UIN/Roll no = 251P012 / 11
# Date: 16-01-2026

PA = input('Enter Principle Amount: ')
rate = input('Enter Rate of Interest: ')
TP = input('Enter Time Period in Years: ')
SI = (float(PA) * float(rate) * float(TP)) / 100
f"SI = {SI:.2f}"
print('\nSimple Interest:',float(SI))
