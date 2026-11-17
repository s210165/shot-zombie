n, m = map(int, input().split())
line_a = input().split()
line_b = input().split()

set_a = set(line_a)
set_b = set(line_b)

results = [
    sorted(set_a & set_b),  # 交集
    sorted(set_a | set_b),  # 聯集
    sorted(set_a - set_b),  # A 減 B
    sorted(set_b - set_a)   # B 減 A
]

for res in results:
    if res:
        print(" ".join(res))
    else:
        print("NONE")