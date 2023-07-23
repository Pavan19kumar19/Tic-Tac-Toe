import random
#Creating a Board
size = 3
temp =[]
dic =[]
print("""
	Welcome!!
		Hello Friends Let's Play game
		------------Tic-Tac-Toe----------

""")
def createBoard():
	board =[]
	values = 1
	for i in range(size):
		row =[]
		for j in range(size):
			row.append(values)
			values +=1
		board.append(row)
	boardG(board)
	return board
def boardG(dic):
	print("\t+-----------+")
	print("\t|---|---|---|")
	for i in dic:
		print("\t| {} | {} | {} |".format(i[0],i[1],i[2]))
		print("\t|---|---|---|")
	print("\t+-----------+")
def userDetails(n):	
	while True:
		p1 = input("\tEnter Player{} name:".format(n))
		p1C = input("\tChoose X or O :")
		p1C = p1C.upper()
		while True:
			if p1C == 'X' or p1C == 'O':
				p1C = p1C
				break
			else:
				print("\tChoose Valid Option")
				p1C = input("\tChoose X or O :")
				p1C = p1C.upper()
		return p1,p1C
def userTurn(sy_U,player):
		print("\t {}'s Turn :".format(player))
		va = int(input("\tEnter B/W [1-9]:"))
		if va not in temp:
			for i in dic:
				for j in range(len(i)):
						if va == i[j]:
							i[j] = sy_U
							ind = dic.index(i)
							dic[ind] = i
							temp.append(va)
							break
			boardG(dic)
			print("\t",temp)

			if check(player):
				return True
			else:
				return False
			
			# print(temp)
			
		else:
			print("\tIt is not range[1-9] or It is already filled")
			userTurn(sy_U,player)
		# print("\tNext Computer's turn")

def compterTurn(sy_C):
	print("\tComputer's Turn")
	while True:
		va  = random.randint(1,9)
		va = int(va)
		if va not in temp:
			for i in dic:
				for j in range(len(i)):
					if va == i[j]:
						i[j] = sy_C
						ind = dic.index(i)
						dic[ind] = i
						temp.append(va)
						break
			boardG(dic)
			print("\tComputer Picked ",temp[-1])
			print("\t",temp)
			if check():
				return True
			else:
				# print("\tPlayer A turn")
				return False			
		# else:
		# 	print("It is not Valid Range or It is already filled")
		# 	print("Again choosen")
def check(name ="Computer"):
	if dic[0][0]==dic[0][1]==dic[0][2]:
		if dic[0][0] == "X" and sy_U == "X":
			print("\t MAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True
	elif dic[1][0]==dic[1][1]==dic[1][2]:
		if dic[1][0] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True
	elif dic[2][0]==dic[2][1]==dic[2][2]:
		if dic[2][0] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True	
	elif dic[0][0]==dic[1][1]==dic[2][2]:
		if dic[0][0] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True	
	elif dic[0][2]==dic[1][1]==dic[2][0]:
		if dic[0][2] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True	
	elif dic[0][0]==dic[1][0]==dic[2][0] :
		if dic[0][0] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True	
	elif dic[0][1]==dic[1][1]==dic[2][1] :
		if dic[0][1] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True	
	elif dic[0][2]==dic[1][2]==dic[2][2] :
		if dic[0][2] == "X" and sy_U == "X":
			print("\tMAtch Won by ",p1.upper(),"............")
		else:
			print("\tMAtch Won by ",name,"............")
		return True	
team = input("\t Play with Friend(f) or Computer(c)")
if team.upper() == 'C':

	p1,sy_U= userDetails("A")

	while True:
		
		dic =createBoard()

		if sy_U == 'X':
			sy_C = "O"
		else:
			sy_C = "X"
		i=0
		us_t= int(input("\tHead(1) or Tail(2)"))
		toss = random.randint(1,2)
		if toss == 1:
			print("\tToss won by ",p1.upper())
			print("\tGame Start with ",p1.upper())
			usW=1
		else:
			print("\tToss won by Computer")
			print("\tGame Start with Computer")
			usW = 0
		while len(temp)<=9:
			if usW==1:
				if(i%2==0):
					t =userTurn(sy_U,p1)
					if  t or len(temp) == 9:
						if not t:
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break		
				else: 
					r=compterTurn(sy_C)
					if len(temp) == 9 or r:
						if not r :
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break
				i+=1
			else:
				if(i%2!=0):
					t = userTurn(sy_U,p1)
					if len(temp) == 9 or t:
						if not t:
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break
				else: 
					t = compterTurn(sy_C)
					if t or len(temp) == 9:
						if not t:
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break

				i+=1	
		r=False	
		while True:	
			a = input("\tPlay Again(a) or Exit(q)")
			if a == 'a':
				dic =[]
				temp =[]
				r = True
				break
			elif a=="q":
				r= False
				break
			else:
				print("\tValid Value")
		if r == False:
			break
else:

	p1,sy_U = userDetails("A")
	p2= userDetails("B")
	while True:
		dic = createBoard()
		sy_C = p2[1]
		i=0
		us_t2= int(input("\t PlayerB choose Head(1) or Tail(2)"))
		toss = random.randint(1,2)
		if toss == us_t2:
			print("\tToss won by PlayerB :",p2)
			print("\tGame Start with ",p2[0])
			usW=1
		else:
			print("\tToss won by PlayerA :",p1.upper())
			print("\tGame Start with ",p1.upper())
			usW = 0
		while len(temp)<=9:
			if usW==1:
				if(i%2==0):
					t =userTurn(sy_U,p2[0])
					if  t or len(temp) == 9:
						if not t:
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break		
				else: 
					r=userTurn(sy_C,p1)
					if len(temp) == 9 or r:
						if not r :
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break
				i+=1
			else:
				if(i%2!=0):
					t = userTurn(sy_U,p1)
					if len(temp) == 9 or t:
						if not t:
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break
				else: 
					t = userTurn(sy_C,p2[0])
					if t or len(temp) == 9:
						if not t:
							print("\tOpps!!!! \n\t..MAtch Draw.......")
						break

				i+=1	
		r=False	
		while True:	
			a = input("\tPlay Again(a) or Exit(q)")
			if a == 'a':
				dic =[]
				temp =[]
				r = True
				break
			elif a=="q":
				r= False
				break
			else:
				print("\tValid Value")
		if r == False:
			break
print("........................ Thank You For Playing......................")