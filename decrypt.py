def decCount(S: str) -> str:
    return ''.join(f"{S[i]}{int(S[i+1], 16)}" for i in range(0, len(S), 2))

def addChar(S: str) -> str:
    i = 0
    outS = []
    while i < len(S):
        ch = S[i]
        count = int(S[i+1])
        if i+2 < len(S) and S[i+2].isdigit():
            count = count * 10 + int(S[i+2])
            i += 3
        else:
            i += 2
        outS.append(ch * count)
    return ''.join(outS)

