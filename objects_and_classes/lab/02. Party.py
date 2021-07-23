class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    cmd = input()
    if cmd == "End":
        print(f"Going: {', '.join(party.people)}\nTotal: {len(party.people)}")
        break
    party.people.append(cmd)
