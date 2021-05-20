accounts = [[1, 4, 3], [4, 2, 1]]

m = sum(accounts[0])


for idx, account in enumerate(accounts):
    n = sum(account)
    if m < n:
        m = n
print(m)
