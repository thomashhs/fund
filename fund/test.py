fund_ids=[]
with open(r'C:\Users\34587\fund\jysld_fund_id.txt') as f:
    for line in f.readlines():
        fund_ids.append(line.strip())

print(len(fund_ids))