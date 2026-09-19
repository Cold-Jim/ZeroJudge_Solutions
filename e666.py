def get_tokens():
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            for token in line.split():
                yield token
        except EOFError:
            break
        
tokens = get_tokens()

for t in tokens:
    a = int(t)
    b = int(next(tokens))
    words = next(tokens)

    sd = {}
    for i in words:
        sd[i] = sd.get(i , 0) + 1
    sorted_sd = sorted(sd.items())

    def ans(t , sd):
        for k , v in sd:
            if t <= v:
                return k
            t -= v
        return ""

    for _ in range(b):
        n = int(next(tokens))
        print(ans(n , sorted_sd) , end = "")
    print()



# e666.108 p4. 排序問題
# https://zerojudge.tw/ShowProblem?problemid=e666