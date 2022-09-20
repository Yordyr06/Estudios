my_list = [7, 9, 10, 57, 5]
n = "init"

for x in my_list:
    if n == "init":
        n = x
    else:
        n = x if x  < n else n
print(n)