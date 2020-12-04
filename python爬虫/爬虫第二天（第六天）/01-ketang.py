def treetop(n, p):
    for i in range(n):
        print("" * (n - i - 1) + p * (2 * i + 1))

def treeroot(m):
    for i in range(m):
        print("   #")

treetop(6, "k")
treeroot(3)