n = int(input())
records = []
for _ in range(n):
    u, item = input().split()
    records.append((u, item))

target, k_str = input().split()
k = int(k_str)

# 1. 建立 user -> 購買商品 set 的字典
user_items = {}
for u, item in records:
    if u not in user_items:
        user_items[u] = set()
    user_items[u].add(item)

target_items = user_items[target]

# 2. 找出相似使用者並累計候選商品分數
scores = {}
for u, items in user_items.items():
    if u == target:
        continue
    # 交集非空代表至少買過一件相同商品
    if target_items & items:
        # 差集找出目標使用者尚未買過的商品
        candidates = items - target_items
        for cand in candidates:
            scores[cand] = scores.get(cand, 0) + 1

# 3. 依分數由大到小、商品名稱字典序由小到大排序
ranked_items = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

if not ranked_items:
    print(0)
else:
    r = min(k, len(ranked_items))
    print(r)
    for item, score in ranked_items[:r]:
        print(f"{item} {score}")