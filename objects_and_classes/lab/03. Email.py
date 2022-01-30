class Email:
    def __init__(self, sdr, rvr, cnt, snt=False):
        self.sdr, self.rvr, self.cnt, self.snt = sdr, rvr, cnt, snt

    def send(self):
        self.snt = True

    def get_info(self):
        print(f"{self.sdr} says to {self.rvr}: {self.cnt}. Sent: {self.snt}")


mails = []
while True:
    cmd = input()
    if cmd == "Stop":
        break
    sender, receiver, content = cmd.split()
    email = Email(sender, receiver, content)
    mails.append(email)
idx = list(map(int, input().split(", ")))
[mails[i].send() for i in idx], [i.get_info() for i in mails]
