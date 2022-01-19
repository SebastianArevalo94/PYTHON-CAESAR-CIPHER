import random
import io

def cesarC(txt, randomListNum):
	abc0="abcdefghijklmnopqrstuvwxyz"
	abc1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newText=""
	newTextVariable=""
	#lista=generateList(txt)
	lista=randomListNum
	counter=0
	for i in txt:
		if i in abc0:
			ck=abc0.find(i)
			ck+=lista[counter]
			counter=counter+1
			if ck >= len(abc0):
				ck-= len(abc0)
			elif ck < 0:
				ck+= len(abc0)
			newText+=abc0[ck]
		elif i in abc1:
			ck=abc1.find(i)
			ck+=lista[counter]
			counter=counter+1
			if ck >= len(abc1):
				ck-= len(abc1)
			elif ck < 0:
				ck+= len(abc1)
			newText+=abc1[ck]
		else:
			newText+=i
	
	return newText		

def cesarD(txt, keyList):
	userKeyList=keyList.rsplit(", ")
	numberList=list(map(int, userKeyList))
	abc0="abcdefghijklmnopqrstuvwxyz"
	abc1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	counter=0
	newText=""

	for i in txt:
		if i in abc0:
			ck=abc0.find(i)
			ck-=numberList[counter]
			counter=counter+1
			if ck>=len(abc0):
				ck-=len(abc0)
			elif ck<0:
				ck+=len(abc0)
			newText+=abc0[ck]
		elif i in abc1:
			ck=abc1.find(i)
			ck-=numberList[counter]
			counter=counter+1
			if ck>=len(abc1):
				ck-=len(abc1)
			elif ck<0:
				ck+=len(abc1)
			newText+=abc1[ck]
		else:
			newText+=i

	return newText
