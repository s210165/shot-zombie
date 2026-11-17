n = int(input())
unique_stamps = set()

for _ in range(n):
    student, booth = input().split()
    unique_stamps.add((student, booth))

counts = {}
for student, booth in unique_stamps:
    counts[student] = counts.get(student, 0) + 1

# 排序規則：章數由大到小 (-x[1]) -> 姓名字典序由小到大 (x[0])
ranking = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

print(len(unique_stamps))
for student, total in ranking:
    print(f"{student} {total}")