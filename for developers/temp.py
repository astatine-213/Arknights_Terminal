import os
def readxp1file(filename):
	with open(os.getcwd()+os.sep+"datas"+os.sep+filename+".xp1",encoding="utf-8") as f:
		tmp=f.read();f.close()
	return tmp
def writexp1file(filename,data):
	with open(os.getcwd()+os.sep+"datas"+os.sep+filename+".xp1","w",encoding="utf-8") as f:
		f.write(data);f.close()
tmp=readxp1file("data")
tmp=tmp.replace(",[],[],",",{},[],")
# ~ tmp=tmp.split("\n")
# ~ out=[]
# ~ for x in tmp:
	# ~ out.append(x[:-2]+"]],\n")
# ~ tmp=tmp.replace("optionlist[4]","optionlist[3]")
# ~ tmp=tmp.replace("optionlist[1000]","optionlist[4]")
# ~ tmp=tmp.replace("optionlist[1]","optionlist[1000]")
# ~ tmp=tmp.replace("optionlist[2]","optionlist[1]")
# ~ tmp=tmp.replace("optionlist[1000]","optionlist[2]")
# ~ tmp=""
# ~ for x in out:
	# ~ tmp+=x
writexp1file("data",tmp)


