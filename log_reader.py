from utils.Messenger import Message

logfile = 'logs.txt'
with open(logfile, 'r') as file:
    lines = file.readlines()

print(lines[-10:])
message = ""
for line in lines[-20:]:
    message = message + line

Message.send_message([message])


