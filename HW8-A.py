n = int(input())
playlist = input().split() if n > 0 else []
if n == 0:
    input()  # 讀取 N=0 時的空白行

q = int(input())
for _ in range(q):
    cmd = input().split()
    if cmd[0] == "ADD":
        playlist.append(cmd[1])
    elif cmd[0] == "REMOVE":
        if cmd[1] in playlist:
            playlist.remove(cmd[1])
    elif cmd[0] == "REVERSE":
        playlist.reverse()

print(len(playlist))
if playlist:
    print(" ".join(playlist))
else:
    print("EMPTY")