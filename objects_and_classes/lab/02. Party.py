class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    cmd = input()
    if cmd == "End":
        break
    party.people.append(cmd)
print(f"Going: {', '.join(party.people)}\nTotal: {len(party.people)}")
