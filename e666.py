# ==========================================
# 1. 建立通用 Token 生成器
# @ 避免測資跨行導致 input() 讀取錯位
# @ 不使用 import，純靠 yield 逐一產出被空格或換行隔開的資料單元
# @ 自動捕捉 EOFError，在多筆測資輸入結束時直接退出
def get_tokens():
    while True:
        try:
            line = input().strip()
            if not line:     # 過濾純空行，防止 split() 產出空串列或誤判。
                continue
            for token in line.split():
                yield token
        except EOFError:
            break


# 實例化生成器
tokens = get_tokens()

# ==========================================
# 2. 定義核心查詢邏輯：區間扣除法 
# @ 查詢第 t 個字母時，不需要耗費大量記憶體與時間拼出超長字串
# @ 依序遍歷「(字母, 出現次數)」，若 t 小於等於當前字母數量，代表落在此字母區間內；
#   否則扣除該次數繼續往後找
def ans(t, sd):
    for k, v in sd:
        if t <= v:
            return k
        t -= v  # 扣除前一個字母佔用的長度，平移相對索引
    return ""
# ( 也可以用前綴和 )

# ==========================================
# 3. 主迴圈：處理每一筆測資
# @ 外層使用 for t in tokens 能自動處理多筆測資，直到生成器耗盡
for t in tokens:
    a = int(t)                      # 字串長度
    b = int(next(tokens))           # 查詢的數量
    words = next(tokens)            # 目標字串

    # ------------------------------------------
    # 統計字母頻率 : 
    # 使用字典計數，能以 O(N) 的線性時間精準統計各字母出現次數
    sd = {}
    for i in words:
        sd[i] = sd.get(i, 0) + 1

    # ------------------------------------------
    # 依字母 ASCII 碼排序
    # @ 題目要求依照字典順序排列字元。
    # @ sd.items() 產出 (key, value) 為 turple ，sorted 會預設根據 key（字母）進行升序排序
    sorted_sd = sorted(sd.items())

    # ------------------------------------------
    # 讀取 b 個查詢數字並印出結果
    # @ 利用 next(tokens) 精準抓取 b 個數字，即使數字分散在不同行也能正確對齊
    # @ 輸出使用 end="" 讓該筆測資的結果連續顯示在同一行
    for _ in range(b):
        n = int(next(tokens))
        print(ans(n, sorted_sd), end="")

    # ------------------------------------------
    # 行尾換行
    # - 每筆測資結束必須輸出換行符號，避免答案連在一起導致判題系統回傳格式錯誤 (PE/WA)
    print()


# e666.108 p4. 排序問題
# https://zerojudge.tw/ShowProblem?problemid=e666