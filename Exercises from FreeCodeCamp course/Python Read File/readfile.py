
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

#try:
fh = open(fname,'r')
#except:
#    print("Error. The file can not be read.")
#    quit()

counter = 0
averge = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    numberLine = line.find("0.")
    number = float(line[numberLine:])
    counter += 1
    averge = averge + number

averge = averge / counter
print("Average spam confidence:", averge)
