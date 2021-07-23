class Email:
    def __init__(self, sdr, rvr, cnt, is_sent=False):
        self.sdr, self.rvr, self.cnt, self.is_sent = sdr, rvr, cnt, is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sdr} says to {self.rvr}: {self.cnt}. Sent: {self.is_sent}"


mails = []
while True:
    cmd = input()
    if cmd == "Stop":
        break
    sender, receiver, content = cmd.split()
    email = Email(sender, receiver, content)
    mails.append(email)
idx = list(map(int, input().split(", ")))
[mails[i].send() for i in idx]
[print(i.get_info()) for i in mails]
