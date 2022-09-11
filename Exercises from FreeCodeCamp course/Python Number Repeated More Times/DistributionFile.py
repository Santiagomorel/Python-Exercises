


name = 'mbox-short.txt'
handle = open(name)
hours = list()
list = list()
count = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    timelist = time.split(':')
    hours.append(timelist[0])
for hour in hours:
    count[hour] = count.get(hour,0) + 1

for k,v in count.items():
    newtup = (k,v)
    list.append(newtup)

list = sorted(list)

for k,v in list:
    print(k,v)



