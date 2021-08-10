f = open("C:/Users/Hoseon1/gmProject/output.txt",'r')
f_ = open("C:/Users/Hoseon1/gmProject/output_no_dup.txt",'w')

gameid = []
output = ""
cnt = 0

for line in f.readlines():
	linedata = line.strip().split(',')
	print("iter :",cnt)
	if len(linedata) != 11:
		print("???",linedata)
	if linedata[0] not in gameid:
		gameid.append(linedata[0])
		output = output + linedata[1]
		for i in range(4):
			output = output + "," + linedata[i+2]
		output = output + "/" + linedata[1]
		for i in range(4):
			output = output + "," + linedata[i+7]
		output = output + "\n"
	cnt = cnt + 1

f_.write(output[:-1])

f.close()
f_.close()