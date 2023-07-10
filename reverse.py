

def reverseStr(str):
    bag = ""
    for el in str:
        bag = el+bag
    return bag



ans = reverseStr("nuf si nohtyP")
print(ans)