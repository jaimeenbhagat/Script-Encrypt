def countChar(S: str) -> str:
    from itertools import groupby
    
    return ''.join(f"{char}{len(list(group))}" for char, group in groupby(S))

def hexCount(S: str) -> str:
    i = 0
    outS = []
    while i < len(S):
        ch = S[i]
        count = int(S[i+1])
        if i + 2 < len(S) and S[i+2].isdigit():
            count = count * 10 + int(S[i+2])
            i += 3
        else:
            i += 2
        outS.append(f"{ch}{hex(count)[2:]}")
    return ''.join(outS)
