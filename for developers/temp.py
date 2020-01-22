with open("data.xp1",encoding="utf-8") as f:
	tmp=f.read();f.close()
tmp1=tmp.split("\n")[:-1];out=[]
for x in tmp1:
	x+=",,,,,"
	out.append(x.replace("],,,,,,",",[],[],,],"))
print(out)
msg=""
for x in out:
	msg+=x+"\n"
with open("data.xp1","w",encoding="utf-8") as f:
	tmp=f.write(msg);f.close()
