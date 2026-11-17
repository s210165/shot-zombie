n = int(input())
runners = []
for _ in range(n):
    name, time_str, penalty_str = input().split()
    runners.append((name, int(time_str), int(penalty_str)))

# 排序規則：總秒數小到大 -> 原始完賽秒數小到大 -> 姓名字典序小到大
runners.sort(key=lambda r: (r[1] + r[2], r[1], r[0]))

for name, time_val, penalty_val in runners:
    print(f"{name} {time_val + penalty_val}")