users = {}
out = {}
while True:
    data = input()
    if data == "Lumpawaroo":
        break
    if " | " in data:
        side, user = data.split(" | ")
        if user not in users:
            users[user] = side
    if " -> " in data:
        user, side = data.split(" -> ")
        users[user] = side
        print(f"{user} joins the {side} side!")
for user, side in users.items():
    if side not in out:
        out[side] = []
        out[side].append(user)
    else:
        out[side].append(user)
out = dict(sorted(out.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in out.items():
    print(f"Side: {k}, Members: {len(v)}")
    [print(f"! {name}") for name in sorted(v)]
