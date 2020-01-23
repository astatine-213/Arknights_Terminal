with open("terminal.py",encoding="utf-8") as f:
	tmp=f.read();f.close()
tmp=tmp.replace("","")
tmp=tmp.replace("","")
tmp=tmp.replace("","")
tmp=tmp.replace("","")
tmp=tmp.replace("","")
tmp=tmp.replace("","")
tmp=tmp.replace("","")
for x in out:
	msg+=x+"\n"
with open("terminal.py","w",encoding="utf-8") as f:
	tmp=f.write(msg);f.close()
