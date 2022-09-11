
'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = "mbox-short.txt"
handle = open(name)

mails = []
counts = {}

for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    mails.append(words[1])
for mail in mails:
    counts[mail] = counts.get(mail,0) + 1
    
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)