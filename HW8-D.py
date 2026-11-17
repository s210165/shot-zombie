n = int(input())
inventory = {}
for _ in range(n):
    item, stock = input().split()
    inventory[item] = int(stock)

q = int(input())
sold_total = 0
rejected_count = 0

for _ in range(q):
    action, item, qty_str = input().split()
    qty = int(qty_str)
    if action == "ADD":
        inventory[item] = inventory.get(item, 0) + qty
    elif action == "BUY":
        if item in inventory and inventory[item] >= qty:
            inventory[item] -= qty
            sold_total += qty
        else:
            rejected_count += 1

print(f"{sold_total} {rejected_count}")
for item in sorted(inventory.keys()):
    print(f"{item} {inventory[item]}")