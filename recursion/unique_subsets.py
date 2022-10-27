def unique_subsets(l):
    mp = {} 
    ans = []
    for ch in l:
        if ch not in mp:
            ans.append(ch)
            mp[ch] = 1
    return ans

def subsets(ip,op,l):
    if len(ip) == 0:
        l.append(op)
        return l 
    op1 = op2 = op 
    op2 += ip[0]
    ip = ip[1:]
    subsets(ip,op1,l)
    subsets(ip,op2,l)
    return l

def main():
    ip = input()
    op = ""
    l = []
    all_subsets = subsets(ip,op,l)
    print(unique_subsets(all_subsets))

if __name__ == "__main__":
    main()

