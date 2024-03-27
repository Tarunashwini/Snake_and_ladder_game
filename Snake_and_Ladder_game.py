import random 
def dies_vlaue():
    die = random.randint(1,6)     
    return die             # Getting Random die to each player move


board = [" " for _ in range(1,1000)]
def print_board(icon,prev_pos,New_pos_A,New_pos_B):                               ## Printing Board
  if icon == "A":
    board[prev_pos] = " "
    board[New_pos_A] = "<A>"
  elif icon == "B":
    board[prev_pos] = " "
    board[New_pos_B] = "<B>"
  if(New_pos_A == New_pos_B):
    board[New_pos_A] = "<AB>"
     
## Printing Board 

  row10 = "|{}{}         |{}{}         |{}{}         |(<-0){}{}    |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |  ".format(100,board[100],99,board[99],98,board[98],97,board[97],96,board[96],95,board[95],94,board[94],93,board[93],92,board[92],91,board[91])

  row9 = "|{}{}          |{}{}         |{}{}         |[-3-]{}{}    |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |  ".format(81,board[81],82,board[82],83,board[83],84,board[84],85,board[85],86,board[86],87,board[87],88,board[88],89,board[89],90,board[90])

  row8 = "|{}{}          |{}{}         |{}{}         |{}{}         |{}{}         |(0->){}{}    |{}{}         |{}{}         |{}{}         |{}{}         |  ".format(80,board[80],79,board[79],78,board[78],77,board[77],76,board[76],75,board[75],74,board[74],73,board[73],72,board[72],71,board[71])

  row7 = "|{}{}          |{}{}         |(<-2){}{}    |{}{}         |{}{}         |(<-1){}{}    |{}{}         |{}{}         |{}{}         |{}{}         |  ".format(61,board[61],62,board[62],63,board[63],64,board[64],65,board[65],66,board[66],67,board[67],68,board[68],69,board[69],70,board[70])

  row6 = "|(2->){}{}     |{}{}         |{}{}         |{}{}         |[-3i-]{}{}   |{}{}         |{}{}         |[-2o-]{}{}   |(1->){}{}    |{}{}         |  ".format(60,board[60],59,board[59],58,board[58],57,board[57],56,board[56],55,board[55],54,board[54],53,board[53],52,board[52],51,board[51])

  row5 = "|{}{}          |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |(<-3){}{}    |{}{}         |{}{}         |{}{}         |  ".format(41,board[41],42,board[42],43,board[43],44,board[44],45,board[45],46,board[46],47,board[47],48,board[48],49,board[49],50,board[50])

  row4 = "|{}{}          |[-0o-]{}{}   |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |(<-4){}{}    |  ".format(40,board[40],39,board[39],38,board[38],37,board[37],36,board[36],35,board[35],34,board[34],33,board[33],32,board[32],31,board[31])

  row3 = "|{}{}          |{}{}         |{}{}         |{}{}         |(3->){}{}    |{}{}         |[-2o-]{}{}   |{}{}         |{}{}         |{}{}         |  ".format(21,board[21],22,board[22],23,board[23],24,board[24],25,board[25],26,board[26],27,board[27],28,board[28],29,board[29],30,board[30])

  row2 = "|{}{}          |{}{}         |{}{}         |{}{}         |(<-5){}{}    |{}{}         |{}{}         |(5->){}{}    |[-1o-]{}{}   |{}{}         |  ".format(20,board[20],19,board[19],18,board[18],17,board[17],16,board[16],15,board[15],14,board[14],13,board[13],12,board[12],11,board[11])

  row1 = "|{}{}           |{}{}         |[-0i-]{}{}    |(4->){}{}    |{}{}         |{}{}         |{}{}         |{}{}         |{}{}         |[-1i-]{}{}   |  ".format(1,board[1],2,board[2],3,board[3],4,board[4],5,board[5],6,board[6],7,board[7],8,board[8],9,board[9],10,board[10])

  print()
  print(row10)
  print(row9)
  print(row8)
  print(row7)
  print(row6)
  print(row5)
  print(row4)
  print(row3)
  print(row2)
  print(row1)
  print()
"""
def player_move_A(postion_A):                              #Tracing player A moves
    global die_A 
    print("Die value for A player is {}".format(die_A))
    postion_A = postion_A + dies_vlaue()
    if postion_A > 100:
      postion_A = postion_A - die_A
    
    postion_A = snakes("A",postion_A)
    print(f" pps A = {postion_A}")
    postion_A = Ladder("A",postion_A)
    return postion_A
"""

def player_move(icon,postion_A,postion_B):                              #Tracing player A moves
  global die_A 
  global die_B
  die_A = dies_vlaue()
  die_B = dies_vlaue()
  if icon == "A":
    print("Die value for {} player is {}".format(player_A_Name,die_A))
    postion_A = postion_A + die_A
    if postion_A > 100:
      postion_A = postion_A - die_A
    postion_A = snakes("A",postion_A)
    postion_A = Ladder("A",postion_A)
    print(f"First player your at {postion_A} postion")
    return postion_A

  elif icon == "B":               #Tracing player B move
    print("Die value for {} player is {}".format(player_B_Name,die_B))
    postion_B = postion_B + die_B

    if postion_B > 100:
      postion_B = postion_B - die_B
    postion_B = snakes("B",postion_B)
    postion_B = Ladder("B",postion_B)
    print(f"Second player your at {postion_B} postion")
    return postion_B


"""
       
def player_move_B(postion_B):                  #Tracing player B move
    global die_B 
    die_B = dies_vlaue()
    print("Die value for B player is {}".format(die_B))
    postion_B = postion_B + die_B
    if postion_B > 100:
      postion_B = postion_B - die_B
    postion_B = snakes("B",postion_B)
    postion_B = Ladder("B",postion_B)
    return postion_B
"""
# Snake commands
s = {97:75,66:52,63:60,47:25,31:4,16:13}
def snakes(icon,postion):
  if postion in s:
    if icon == "A":
      play = player_A_Name
    else:
      play =player_B_Name
    key = postion
    postion = s[key]
    print("Uff ! player {}, Your are bitten by the snake so your postion was reduced to {}".format(play,postion))
    
  return postion 

"""
def snakes(icon,postion): 
  if postion == 97:
    postion = 75
    print("Uff ! {} Snake a bite you have reduced to postion {}".format(icon,postion))
  elif postion == 66:
    postion = 52
    print("Uff ! {} Snake a bite you have reduced to postion {}".format(icon,postion))
  elif postion == 63:
    postion = 60
    print("Uff ! {} Snake a bite you have reduced to postion {}".format(icon,postion))
  elif postion == 47:
    postion = 25
    print("Uff ! {} Snake a bite you have reduced to postion {}".format(icon,postion))
  elif postion == 31:
    postion = 4
    print("Uff ! {} Snake a bite you have reduced to postion {}".format(icon,postion))
  elif postion == 16:
    postion = 13
    print("Uff ! {} Snake a bite you have reduced to postion {}".format(icon,postion))
  return postion
"""

# Ladder Commands
L = {3:39,10:12,27:53,56:84}
def Ladder(icon,postion):
  if postion in L:
    if icon == "A":
      play = player_A_Name
    else:
      play =player_B_Name
    key = postion
    postion = L[key]
    print(f"postion is {postion} ")
    print("Hey! player {}, You have got A Ladder. You have raises to the postion = {}".format(play,postion))
  return postion

"""
def Ladder(icon,postion):
  if postion == 3:
    postion = 39
    print("Hurry ! You have got a ladder now you are shifted to postion {}".format(postion))
  elif postion == 10:
    postion = 12
    print("Hurry ! You have got a ladder now you are shifted to postion {}".format(postion))
  elif postion == 27:
    postion = 53
    print("Hurry ! You have got a ladder now you are shifted to postion {}".format(postion))
  elif postion == 56:
    postion = 84
    print("Hurry ! You have got a ladder now you are shifted to postion {}".format(postion))
  return postion

   """
   
   


# Any one player winning checking

def winning_codition(postion):
    if( postion == int(100)):
        return True
    else:
        return False


#Critical postions checking

def critical_conditions(icon,postion):
    
    if postion == 95 and (die_A >= 5 or die_B >= 5):
        return postion
    elif postion == 96 and (die_A >= 4 or die_B >= 4):
      return postion
    elif postion == 97 and (die_A >= 3 or die_B >= 3):
      return postion
    elif postion == 98 and (die_A >=2 or die_B >= 2):
        return postion
    elif postion == 99 and (die_A >= 1 or die_B >= 1):
        return postion
    elif postion > 100: 
      if icon == "A":
        postion = postion - die_A
      elif icon == "B":
        postion = postion - die_B
      return postion
    else:
        return postion

# All GLobal Initalizations

postion_A = 0
postion_B = 0
prev_pos = 0

#Instructions

print()
print("Before starting the Game please Read the Notations carefuly ")
print("* (<-0) ---->   mouth of first snake." ) 
print("* (0->) ----> tail of first snake")
print("* Similarlly to all numbers of snakes")
print("* [-1i-] first ladder in" )
print("* [-1o-] ----> first ladder out")
print()
print()

player_A_Name = input("Player A Please enter your name:   ").strip()
player_B_Name = input("Player B Please enter your name:   ").strip()


                                # Code starts from 
## int main()             
while True:
  
  A = input("{}, Press any key to roll your die  : ".format(player_A_Name))
  prev_pos = postion_A
  postion_A = player_move("A",postion_A,postion_B)
  print_board("A",prev_pos,postion_A,postion_B)
  print("Player A is at postion {}".format(postion_A))
  postion_A = critical_conditions("A",postion_A)
 
  if winning_codition(postion_A):
    print("Congrates {}! You won the Game".format(player_A_Name))
    break
  print("__________________________________________________________________________")



  B = input("{},Please any key to roll your die  : ".format(player_B_Name)) 
  prev_pos = postion_B    
  postion_B = player_move("B",postion_A,postion_B)
  print("Player B is at postion {}".format(postion_B))
  print_board("B",prev_pos,postion_A,postion_B)
  print("Player B, You are at postion {}".format(postion_B))
  postion_B = critical_conditions("B",postion_B)
  if winning_codition(postion_B):
    print("Congrates {} ! You won the Game".format(player_B_Name))
    break
  print("___________________________________________________________________________")



