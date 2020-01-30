# coding:utf-8
# Author:Astatine-213
# Sorry about that only Windows platform is supported
# data structure:
# [["name",height,[birthmonth,birthday],"foreign name",type,gender,star,organization,drawer,{infrapls:[infraspecial]},[tags],race]]
# description structure:
# {"name":"description"}
# optionlist:
# ["file name",]
# typetuple=("近卫","术师","医疗","特种","狙击","先锋","辅助","重装")
# organizationtuple=("罗德岛","喀兰贸易","龙门","莱茵生命","格拉斯哥帮","使徒","汐斯塔","深海猎人","SWEEP","乌萨斯学生自治团","王者之杖","企鹅物流","黑钢国际","维多利亚","卡西米尔无胄盟","莱塔尼亚")
# drawertuple=("Liduke","竜崎いち","虎三","Infukun","海猫络合物","Skade","NoriZC","m9nokuro","一立里子","谜肘","TOKI","neco","阿鬼","唯@W","alchemaniac","YUJI","HUG","戏言咸咸","下野宏铭","LLC","REALMBW","我妻洛酱","幻象黑兔","LM7","渣念","鸭","RAN","Lanzi","aZLing4","deel","时辰","Lpip","Iritoa","KENTllaall","Anmi","将","咩煲","藻","STAR影法师","KuroBlood","toast","")
# infrapls=("无","控制中枢","制造站","贸易站","发电站","宿舍","会客室","办公室","训练室","加工站")
# infraspecial=("无","效率（副产品百分比）加","效率（副产品百分比）减","扩容/增量","减容量","心情消耗减少（恢复加快）","心情消耗增加（恢复减慢）","针对特殊干员生效","仅对自身有效","仅对同设施其他干员有效","针对特殊物品加成","加成会随时间变化","加成恒定","加强效果","减弱效果")
# tagtuple=("不可公招","近卫干员","术士干员","医疗干员","特种干员","狙击干员","先锋干员","辅助干员","重装干员","新手","资深干员","高级资深干员","远程位","近战位","治疗","支援","输出","群攻","减速","生存","防护","削弱","位移","控场","爆发","召唤","快速复活","费用恢复","支援机械")
# racetuple=("菲林（猫科）","鬼","埃拉菲亚（梅花鹿）","丰蹄（）","萨弗拉（）","","","","","","","","","未公开")
# xp1file content:["",,[,],"",,,,,,[],[],[]],
# 公招tag:
# https://aktoolscn.graueneko.xyz/hr
#
#
#description部分感谢以下人士（网址已附上，顺便还有原帖链接）
#主要作者：
#印奇斯廷：https://www.bigfun.cn/user/211981/theme
#提供帮助和建议者：（排名不分先后）
#无lee旋转：https://www.bigfun.cn/user/822563/theme
#AshuraSJ：https://www.bigfun.cn/user/100332/theme
#iMaax：https://www.bigfun.cn/user/452139/theme
#
#原帖链接：
#https://www.bigfun.cn/post/65502
#
global searchdict,optionlist,dat,descriptiondict,vartuple,orgnizationtuple,typetuple,drawertuple
global infrapls,infraspecial,racetuple,tagtuple,tokendict
import os,time,xlsxwriter
typetuple=("近卫","术师","医疗","特种","狙击","先锋","辅助","重装")
organizationtuple=("罗德岛","喀兰贸易","龙门","莱茵生命","格拉斯哥帮","使徒","汐斯塔","深海猎人","SWEEP","乌萨斯学生自治团","王者之杖","企鹅物流","黑钢国际","维多利亚","卡西米尔无胄盟","莱塔尼亚")
drawertuple=("Liduke","竜崎いち","虎三","Infukun","海猫络合物","Skade","NoriZC","m9nokuro","一立里子","谜肘","TOKI","neco","阿鬼","唯@W","alchemaniac","YUJI","HUG","戏言咸咸","下野宏铭","LLC","REALMBW","我妻洛酱","幻象黑兔","LM7","渣念","鸭","RAN","Lanzi","aZLing4","deel","时辰","Lpip","Iritoa","KENTllaall","Anmi","将","咩煲","藻","STAR影法师","KuroBlood","toast","")
vartuple=("姓名","身高","生日","外文名","职业","性别","星级","所属组织","画师","基建位置","基建加成","公招tag","种族")
infrapls=("无","控制中枢","制造站","贸易站","发电站","宿舍","会客室","办公室","训练室","加工站")
tagtuple=("不可公招","近卫干员","术士干员","医疗干员","特种干员","狙击干员","先锋干员","辅助干员","重装干员","新手","资深干员","高级资深干员","远程位","近战位","治疗","支援","输出","群攻","减速","生存","防护","削弱","位移","控场","爆发","召唤","快速复活","费用恢复","支援机械")
infraspecial=("无","效率（副产品百分比）加","效率（副产品百分比）减","扩容/增量","减容量","心情消耗减少（恢复加快）","心情消耗增加（恢复减慢）","针对特殊干员生效","仅对自身有效","仅对同设施其他干员有效","针对特殊物品加成","加成会随时间变化","加成恒定","加强效果","减弱效果")

def allin(A, B): #仅可用于数字列表！！！
	A.sort()
	B.sort()
    if len(A) > len(B):
		allin(B,A)
    k = 0
    for i in range(0,len(A)):
        for j in range(k,len(B)):
            if A[i] == B[j]:
                if i == len(A)-1:
                    return True
                else:
                    break
        if j < len(B)-1:
            k = j+1
        else:
            break
    return False
def getday(datelist):
	months=[31,28,31,30,31,30,31,31,30,31,30,31];tmp=0;c=0
	while c<datelist[0]-1:
		tmp+=months[c];c+=1
	tmp+=datelist[1]
	return tmp
def sort_max(inlist):
	out=[]
	while inlist:
		maxi=0;maxindex=0
		for x in inlist:
			if x[1]>maxi:
				maxi=x[1]
				maxindex=inlist.index(x)
		out.append(inlist.pop(maxindex))
	return out
def sort_min(inlist):
	out=[]
	while inlist:
		mini=999;minindex=0
		for x in inlist:
			if x[1]<mini:
				mini=x[1]
				minindex=inlist.index(x)
		out.append(inlist.pop(minindex))
	return out
def clear():
		os.system("cls")
def confirm(inline):
	while True:
		tmp=input(inline+"(Y/N):").upper().strip()
		if tmp=="Y":
			return True
		elif tmp=="N":
			return False
		else:
			print("没有这个选项。")
def exitafter(seconds):
	c=1
	while c<=seconds:
		print("感谢您的使用，%d秒后程序自动关闭。"%(seconds-c),end="\r");time.sleep(1);c+=1
	exit()
def getchoice(inlist,instring,more=False):
	msg=instring+"\n";c=1
	for x in inlist:
		msg+="%d)%s\n"%(c,x);c+=1
	msg+="\n99)退出该程序\n"
	print(msg)
	if more:
		print("本选择支持多选，请使用空格分隔各个选项。")
		while True:
			tmp=input(">>>").strip().split(" ");out=[]
			try:
				for x in tmp:
					out.append(int(x))
			except Exception:
				print("检测到非数字字符，请重新输入。");continue
			else:
				c=0
				for x in out:
					if 0<x<=len(inlist):
						c+=1
					elif x==99:
						exitafter(3)
					else:
						print("输入的选项包含超出范围的内容，请重新输入。");break
				if c!=len(out):
					continue
				else:
					return out
	else:
		while True:
			tmp=input(">>>").strip()
			try:
				tmp=int(tmp)
			except Exception:
				print("检测到非数字字符，请重新输入。");continue
			else:
				if x==99:
					exitafter(3)
				elif tmp<1 or tmp>len(inlist):
					print("不存在这样的一个选项。");continue
				else:
					return tmp
def datelist_to_str(inlist):
	if inlist[0]==0 and inlist[1]==0:
		return "null"
	return "%d/%d"%(inlist[0],inlist[1])
def datestr_available(instr):
	instr=instr.split("/")
	if len(instr)!=2:
		return False
	tmp=[]
	try:
		tmp.append(int(instr[0]))
		tmp.append(int(instr[1]))
	except Exception:
		return False
	else:
		if 1<=tmp[0]<=12:
			if tmp[0] in [1,3,5,7,8,10,12]:
				if 1<=tmp[1]<=31:
					return True
			elif tmp[0]==2:
				if 1<=tmp[1]<=28:
					return True
			else:
				if 1<=tmp[1]<=30:
					return True
		return False
def datestr_to_list(instr):
	instr=instr.split("/")
	tmp=[]
	tmp.append(int(instr[0]))
	tmp.append(int(instr[1]))
	return tmp
def getformattedtime():
	return time.strftime("%F_%H%M%S")
def genderstr(innum):
	if innum==0:
		return "女"
	else:
		return "男"
def detailstring(inlist):
	msg=""
	for x in inlist:
		msg+="干员%s，身高%dcm，生日%s，外文名%s，职业%s，性别%s，星级%d，属于组织%s，是画师%s的作品。\n"%(x[0],x[1],datelist_to_str(x[2]),x[3],typetuple[x[4]],genderstr(x[5]),x[6],organizationtuple[x[7]],drawertuple[x[8]])
		if optionlist[4]:
			msg+="%s\n"%descriptiondict[x[0]]
		if optionlist[5]:
			msg+="%s\n"%tokendict[x[0]]
		msg+="\n"
	msg+="\n\n\n作者：Astatine-213\n"
	if optionlist[4]:
		desecriptionthankstr="干员姓名解析部分感谢以下人士（网址已附上，顺便还有原帖链接）\
		\n主要作者：\
		\n印奇斯廷：https://www.bigfun.cn/user/211981/theme\
		\n提供帮助和建议者：（排名不分先后）\
		\n无lee旋转：https://www.bigfun.cn/user/822563/theme\
		\nAshuraSJ：https://www.bigfun.cn/user/100332/theme\
		\niMaax：https://www.bigfun.cn/user/452139/theme\
		\n原帖链接：\nhttps://www.bigfun.cn/post/65502\
		\n链接2：https://www.bigfun.cn/post/113609"
		msg+=desecriptionthankstr
	return msg
def totxtfile(inlist):
	global optionlist
	with open(optionlist[0]+".txt","w",encoding="utf-8") as f:
		f.write(detailstring(inlist));f.close()
def toxlsxfile(inlist):
	workbook = xlsxwriter.Workbook(optionlist[0]+'.xlsx')
	worksheet = workbook.add_worksheet()
	cell_format = workbook.add_format()
	cell_format.set_align('center')
	cell_format.set_align('vcenter')
	cell_format.set_align('justify')
	worksheet.write(0,1,"姓名",cell_format)
	worksheet.write(0,2,"身高",cell_format)
	worksheet.write(0,3,"生日",cell_format)
	worksheet.write(0,4,"外文名",cell_format)
	worksheet.write(0,5,"职业",cell_format)
	worksheet.write(0,6,"性别",cell_format)
	worksheet.write(0,7,"星级",cell_format)
	worksheet.write(0,8,"组织",cell_format)
	worksheet.write(0,9,"画师",cell_format)
	if optionlist[4]:
		worksheet.write(0,10,"姓名解析")
	if optionlist[5]:
		worksheet.write(0,11,"干员信物")
	c=1
	for x in inlist:
		worksheet.write(c,1,x[0],cell_format)
		worksheet.write(c,2,x[1],cell_format)
		worksheet.write(c,3,datelist_to_str(x[2]),cell_format)
		worksheet.write(c,4,x[3],cell_format)
		worksheet.write(c,5,typetuple[x[4]],cell_format)
		worksheet.write(c,6,genderstr(x[5]),cell_format)
		worksheet.write(c,7,x[6],cell_format)
		worksheet.write(c,8,organizationtuple[x[7]],cell_format)
		worksheet.write(c,0,c,cell_format)
		worksheet.write(c,9,drawertuple[x[8]],cell_format)
		if optionlist[4]:
			worksheet.write(c,10,descriptiondict[x[0]])
		if optionlist[5]:
			worksheet.write(c,11,tokendict[x[0]])
		c+=1
	cf = workbook.add_format()
	cf.set_align('center')
	cf.set_align('vcenter')
	cf.set_center_across()
	worksheet.write(c,0,"制作者：Astatine-213",cf)
	top=9
	if optionlist[4]:
		top+=1
	if optionlist[5]:
		top+=1
	i=1
	while i<=top:
		worksheet.write(c,i,"",cf);i+=1
	if optionlist[4]:
		cf.set_text_wrap()
		desecriptionthankstr="干员姓名解析部分感谢以下人士（网址已附上，顺便还有原帖链接）\
		\n主要作者：\
		\n印奇斯廷：https://www.bigfun.cn/user/211981/theme\
		\n提供帮助和建议者：（排名不分先后）\
		\n无lee旋转：https://www.bigfun.cn/user/822563/theme\
		\nAshuraSJ：https://www.bigfun.cn/user/100332/theme\
		\niMaax：https://www.bigfun.cn/user/452139/theme\
		\n原帖链接：\nhttps://www.bigfun.cn/post/65502\
		\n链接2：https://www.bigfun.cn/post/113609"
		worksheet.write(c+1,0,desecriptionthankstr,cf)
		i=1
		while i<=top:
			worksheet.write(c+1,i,"",cf);i+=1
	if optionlist[5]:
		tokenthankstr="干员信物部分感谢bigfun用户印奇斯廷整理。"
		worksheet.write(c+2,0,tokenthankstr,cf)
		i=1
		while i<=top:
			worksheet.write(c+2,i,"",cf);i+=1
	workbook.close()
def getoption():
	global optionlist
	optionlist=[]
	if "search.config" in os.listdir():
		if confirm("找到已保存的配置文件，是否需要导入？"):
			with open("search.config",encoding="utf-8") as f:
				optionlist=f.read();f.close()
				optionlist=eval(optionlist);return
		else:
			if confirm("是否需要删除上一次保存的配置文件？"):
				os.remove(os.getcwd()+os.sep+"search.config")
	if confirm("是否需要修改默认文件名？"):
		optionlist.append(input("新文件名（不需要后缀）："))
	else:
		optionlist.append(getformattedtime())
	optionlist.append(confirm("输出为txt文件（Y）还是输出为xlsx文件（N）?"))
	optionlist.append(confirm("是否需要进行时间统计？"))
	optionlist.append(confirm("按照身高降序（Y）或者升序（N）输出？"))
	optionlist.append(confirm("是否需要干员姓名解析？"))
	optionlist.append(confirm("是否需要干员信物文档？"))
	if confirm("是否需要保存配置？"):
		with open("search.config","w",encoding="utf-8") as f:
			f.write(str(optionlist));f.close()
def readxp1file(filename):
	with open(os.getcwd()+os.sep+"datas"+os.sep+filename+".xp1",encoding="utf-8") as f:
		tmp=f.read();f.close()
	tmp=eval(tmp)
	return tmp
def startsearch():
	global dat,searchdict,optionlist
	tmp=dat;out=[]
	if "name" in searchdict:
		tmp1=searchdict["name"]
			if x[3] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "type" in searchdict:
		tmp1=searchdict["type"]
		for x in tmp:
			if x[4] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "gender" in searchdict:
		if "*" in tmp1:
			if optionlist[4]:
				tmp=sort_max(tmp)
			else:
				tmp=sort_min(tmp)
			return tmp
		for x in tmp:
			if x[0] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "height" in searchdict:
		tmp1=searchdict["height"]
		if len(tmp1)==1:    #仅范围值
			for x in tmp:
				if tmp1[0][0]<=x[1]<=tmp1[0][1]:
					out.append(x)
			tmp=out[:];out=[]
		elif len(tmp1[0])==0:    #仅值
			for x in tmp:
				if x[1] in tmp1:
					out.append(x)
			tmp=out[:];out=[]
		else:    #两个都有
			for x in tmp:
				if tmp1[0][0]<=x[1]<=tmp1[0][1] or x[1] in tmp:
					out.append(x)
			tmp=out[:];out=[]
	if "birthdate" in searchdict:
		tmp1=searchdict["birthdate"]
		if len(tmp1)==1:    #仅范围值
			for x in tmp:
				if tmp1[0][0]<=getday(x[2])<=tmp1[0][1]:
					out.append(x)
			tmp=out[:];out=[]
		elif len(tmp1[0])==0:    #仅值
			for x in tmp:
				if getday(x[2]) in tmp1:
					out.append(x)
			tmp=out[:];out=[]
		else:    #两个都有
			for x in tmp:
				if tmp1[0][0]<=getday(x[2])<=tmp1[0][1] or getday(x[2]) in tmp:
					out.append(x)
			tmp=out[:];out=[]
	if "foreignname" in searchdict:
		tmp1=searchdict["foreignname"]
		for x in tmp:
			if x[3] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "type" in searchdict:
		tmp1=searchdict["type"]
		for x in tmp:
			if x[4] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "gender" in searchdict:
		tmp1=searchdict["gender"]
		for x in tmp:
			if x[5] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "star" in searchdict:
		tmp1=searchdict["star"]
		for x in tmp:
			if x[6] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "organization" in searchdict:
		tmp1=searchdict["organization"]
		for x in tmp:
			if x[7] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "drawer" in searchdict:
		tmp1=searchdict["drawer"]
		for x in tmp:
			if x[8] in tmp1:
				out.append(x)
		tmp=out[:];out=[]
	if "infrapls" in searchdict:
		tmp1=searchdict["infrapls"]
		if len(tmp1)==1:    #只有一个值，视为模糊查询
			for x in tmp:
				infra=x[9]    #读取基建字典
				tmp_infrapls=[]
				for k,v in infra.items():
					tmp_infrapls.append(k)    #获取该干员所有基建位置
				if allin(tmp_infrapls,tmp1):    #当且仅当所有基建位置都一样的时候才能这么干
					out.append(x)
		else:    #视为精确查询
			for x in tmp:
				infra=x[9]    #读取基建字典
				tmp_infrapls=[]
				for k,v in infra.items():
					tmp_infrapls.append(k)    #获取该干员所有基建位置
				if tmp_infrapls==tmp1:    #当且仅当所有基建位置都一样的时候才返回范围值
					out.append(x)
		tmp=out[:];out=[]
	if "infraspecial" in searchdict:
		tmp1=searchdict["infraspecial"]
		for x in tmp:
			infra=x[9]    #读取基建字典
			for k,v in infra.items():
				if v==tmp1:
					out.append(x)
		tmp=out[:];out=[]
	if "tag" in searchdict:
		tmp1=searchdict["tag"]
		for x in tmp:
			c=0
			for y in tmp1:
				if y in x[11]:
					c+=1
			if c=len(tmp1):
				out.append(x)
		tmp=out[:];out=[]
	if "race" in searchdict:
		tmp1=searchdict["race"]
		for x in tmp:
			if allin(x[12],tmp1):
				out.append(x)
		tmp=out[:];out=[]
	if optionlist[4]:
		tmp=sort_max(tmp)
	else:
		tmp=sort_min(tmp)
	return tmp
descriptiondict=readxp1file("description")
dat=readxp1file("data")
tokendict=readxp1file("token")
searchdict={}
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
print("明日方舟干员数据快查器v0.0.1")
print("感谢 http://kokodayo.fun/ 提供相应数据。")
print("感谢 bigfun用户印奇斯廷提供大部分的帮助。")
print("获取设置……")
getoption()

while True:
	l1=getchoice(vartuple,"选择需要搜索的方向：",True)
	if 1 in l1 and len(l1)>1:
		print("警告：干员姓名这一方向是精准搜索，不会与其他搜索相配合。")
		if confirm("是否需要重新选择？"):
			continue
		l1=[1];break
	elif 4 in l1 and len(l1)>1 and 1 not in l1:
		print("警告：干员外文名这一方向是精准搜索，不会与其他搜索相配合。")
		if confirm("是否需要重新选择？"):
			continue
		l1=[4];break
	else:
		l1.sort();break


if 1 in l1:    #姓名
	os.system("cls")
	print("小提示：可以输入通配符“*”(shift+8)来输出整个数据库。")
	l2=getchoice(["单个","多个"],"搜索个数：")
	if l2==1:
		searchdict["name"]=[input("干员姓名：")]
	else:
		tmp=[]
		while True:
			tmp1=input("干员姓名（“^]”以结束输入）：")
			if tmp1=="^]" and len(tmp)!=0:
				break
			elif tmp1=="^]" and len(tmp)==0:
				print("警告：你还没有输入任何姓名。")
				if confirm("你确定要退出吗？"):
					break
				continue
			else:
				tmp.append(tmp1)
		searchdict["name"]=tmp


if 2 in l1:    #身高
	os.system("cls")
	tmp=[]
	l2=getchoice(["单值式","范围式","均有"],"选择身高查询方式")
	if l2==1:
		tmp=[[]]
		if confirm("是否需要输入多个值？"):
			while True:
				tmp1=input("干员身高（输入“^]”以结束）：")
				if tmp1=="^]" and len(tmp)<=1:
					print("警告：你还没有输入任何身高数据。")
					if confirm("你确定要退出吗？"):
						break
					continue
				elif tmp1=="^]" and len(tmp)>1:
					break
				else:
					try:
						tmp1=int(tmp1)
					except Exception:
						print("包含非数字字符，请重新输入。");continue
					else:
						tmp.append(tmp1)
		else:
			while True:
				try:
					tmp1=int(input("干员身高："))
				except Exception:
					print("包含非数字字符，请重新输入。");continue
				else:
					tmp.append(tmp1);break
	elif l2==2:
		tmp1=[];tmp=[]
		while True:
			try:
				tmp2=int(input("干员身高下限："))
				tmp3=int(input("干员身高上限："))
			except Exception:
				print("包含非数字字符，请重新输入。");continue
			else:
				if tmp2>tmp3:
					print("下限值低于上限值，请重新输入");continue
				else:
					tmp1.append(tmp2);tmp1.append(tmp3);tmp.append(tmp1);break
	else:
		tmp=[]
		print("范围式数据采集：")
		tmp1=[]
		while True:
			try:
				tmp2=int(input("干员身高下限："))
				tmp3=int(input("干员身高上限："))
			except Exception:
				print("包含非数字字符，请重新输入。");continue
			else:
				if tmp2>tmp3:
					print("下限值低于上限值，请重新输入");continue
				else:
					tmp1.append(tmp2);tmp1.append(tmp3);tmp.append(tmp1);break
		print("单值式数据采集：")
		if confirm("是否需要输入多个值？"):
			while True:
				tmp1=input("干员身高（输入“^]”以结束）：")
				if tmp1=="^]" and len(tmp)<=1:
					print("警告：你还没有输入任何身高数据。")
					if confirm("你确定要退出吗？"):
						break
					continue
				elif tmp1=="^]" and len(tmp)>1:
					break
				else:
					try:
						tmp1=int(tmp1)
					except Exception:
						print("包含非数字字符，请重新输入。");continue
					else:
						tmp.append(tmp1)
		else:
			while True:
				try:
					tmp1=int(input("干员身高："))
				except Exception:
					print("包含非数字字符，请重新输入。");continue
				else:
					tmp.append(tmp1);break
	searchdict["height"]=tmp


if 3 in l1:    #生日
	os.system("cls")
	l2=getchoice(["单值式","范围式","均有"],"选择生日查询方式：")
	print("\n请以“月份/日期”形式输入生日数据。\n")
	if l2==1:
		tmp=[[]]
		if confirm("是否需要输入多个值？"):
			while True:
				tmp1=input("干员生日（输入“^]”以结束）：")
				if tmp1=="^]" and len(tmp)<=1:
					print("警告：你还没有输入任何生日数据。")
					if confirm("你确定要退出吗？"):
						break
					continue
				elif tmp1=="^]" and len(tmp)>1:
					break
				else:
					if datestr_available(tmp1):
						tmp.append(getday(datestr_to_list(tmp1)))
					else:
						print("生日数据不合法，请重新输入");continue
		else:
			while True:
				tmp1=int(input("干员生日："))
				if datestr_available(tmp1):
					tmp.append(getday(datestr_to_list(tmp1)));break
				else:
					print("生日数据不合法，请重新输入");continue
	elif l2==2:
		tmp1=[];tmp=[]
		while True:
			tmp2=input("干员生日下限：")
			tmp3=input("干员生日上限：")
			if datestr_available(tmp2) and datestr_available(tmp3):
				if getday(datestr_to_list(tmp2))<getday(datestr_to_list(tmp3)):
					tmp1.append(getday(datestr_to_list(tmp2)));tmp1.append(getday(datestr_to_list(tmp3)));tmp.append(tmp1);break
				else:
					print("下限值低于上限值，请重新输入")
			else:
				print("生日数据不合法，请重新输入。");continue
	else:
		tmp=[]
		print("范围式数据采集：")
		tmp1=[]
		while True:
			tmp2=input("干员生日下限：")
			tmp3=input("干员生日上限：")
			if datestr_available(tmp2) and datestr_available(tmp3):
				if getday(datestr_to_list(tmp2))<getday(datestr_to_list(tmp3)):
					tmp1.append(getday(datestr_to_list(tmp2)));tmp1.append(getday(datestr_to_list(tmp3)));tmp.append(tmp1);break
				else:
					print("下限值低于上限值，请重新输入")
			else:
				print("生日数据不合法，请重新输入。");continue
		print("单值式数据采集：")
		if confirm("是否需要输入多个值？"):
			while True:
				tmp1=input("干员生日（输入“^]”以结束）：")
				if tmp1=="^]" and len(tmp)<=1:
					print("警告：你还没有输入任何生日数据。")
					if confirm("你确定要退出吗？"):
						break
					continue
				elif tmp1=="^]" and len(tmp)>1:
					break
				else:
					if datestr_available(tmp1):
						tmp.append(getday(datestr_to_list(tmp1)))
					else:
						print("生日数据不合法，请重新输入");continue
		else:
			while True:
				tmp1=int(input("干员生日："))
				if datestr_available(tmp1):
					tmp.append(getday(datestr_to_list(tmp1)));break
				else:
					print("生日数据不合法，请重新输入");continue
	searchdict["birthdate"]=tmp


if 4 in l1:    #外文名
	os.system("cls")
	l2=getchoice(["单个","多个"],"搜索个数：")
	if l2==1:
		searchdict["foreignname"]=[input("干员姓名：").encode('utf-8').decode('utf-8')]
	else:
		tmp=[]
		while True:
			tmp1=input("干员外文名（“^]”以结束输入）：").encode('utf-8').decode('utf-8')
			if tmp1=="^]" and len(tmp)!=0:
				break
			elif tmp1=="^]" and len(tmp)==0:
				print("警告：你还没有输入任何外文名。")
				if confirm("你确定要退出吗？"):
					break
				continue
			else:
				tmp.append(tmp1)
		searchdict["foreignname"]=tmp


if 5 in l1:    #职业
	os.system("cls")
	tmp=getchoice(typetuple,"选择干员职业：",True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["type"]=tmp


if 6 in l1:    #性别
	os.system("cls")
	tmp=getchoice(["女","男"],"选择干员性别：")
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["gender"]=tmp


if 7 in l1:    #星级
	os.system("cls")
	searchdict["type"]=getchoice(["1星","2星","3星","4星","5星","6星"],"选择干员星级：",True)


if 8 in l1:    #所属组织
	os.system("cls")
	tmp=getchoice(organizationtuple,"选择干员组织：",True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["organization"]=tmp


if 9 in l1:    #画师
	os.system("cls")
	tmp=getchoice(drawertuple,"选择画师：",True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["drawer"]=tmp

if 10 in l1:   #基建位置
	os.system("cls")
	print("注意：如果在这里单选将查询所有包含这些基建位置的干员（数学上的“属于”关系）")
	print("如果在这里多选将会以“当且仅当干员拥有输入基建位置”查询（数学上的“等于”关系）")
	tmp=getchoice(infrapls,True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["infrapls"]=tmp

if 11 in l1:   #基建加成
	os.system("cls")
	print("注意：这里的多选是在一个基建位置中的所有加成。")
	tmp=getchoice(infraspecial,True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["infraspecial"]=tmp

if 12 in l1:   #公招tag
	os.system("cls")
	print("注意：这里可以看做一个模拟的公招，但是不会划掉你的tag。")
	tmp=getchoice(tagtuple,True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["tag"]=tmp

if 13 in l1:   #种族
	os.system("cls")
	tmp=getchoice(racetuple,True)
	for x in tmp:
		tmp[tmp.index(x)]=x-1
	searchdict["race"]=tmp

os.system("cls")
if optionlist[2]:
	time1=time.time()
result=startsearch()
if optionlist[2]:
	time2=time.time()
	deltatime=int((time2-time1)*1000)/1000
	print("本次搜索耗时%f秒."%deltatime)
print(detailstring(result))
if optionlist[1]:
	totxtfile(result)
else:
	toxlsxfile(result)
