a=[]
with open(r'C:\Users\34587\fund\fund_id.txt') as f:
    for line in f.readlines():
        a.append(line.strip())

print(a)