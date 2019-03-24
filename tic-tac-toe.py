#tic tac toe

board=[['-','-','-'],['-','-','-'],['-','-','-']]

def resetboard():
    board=[['-','-','-'],['-','-','-'],['-','-','-']]

def printboard():
    for lt in board :
        print(lt)

def iswon(r,c,symbol):
    if board[0][c] == symbol and board[1][c] == symbol and board[2][c] == symbol:
        return (True)

    if board[r][0] == symbol and board[r][1] == symbol and board[r][2] == symbol:
        return (True)

    if r==1 and c == 1 :
        if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
            return (True)
        if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
            return (True)  



    if(r == 0 and c== 0)or (r==2 and c == 2):
        if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
            return (True)
    if (r == 0 and c== 2) or (r==2 and c == 0):
        if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
            return (True)  
    return (False)   

p1='X'
p2='O'
printboard()

for i in range(9):
    while True :
     try : 

    
      if i % 2== 0 :
        print("Player 1 turn (X),enter valid row and column index space separated")
        symbol='X'
      else:
        print("Player 2 turn (O),enter valid row and column index space separated")
        symbol='O'
      lt =[int(x) for x in input().split()]
      r=lt[0]
      c=lt[1]
      if(r < 0 or r>2):
          print("Enter valid row and column (0 to 2) and unoccupied")
          continue
      if(c < 0 or c>2):
          print("Enter valid row and column (0 to 2) and unoccupied")
          continue
      if board[r][c]== '-' :
          break
      else:
          print("Enter unoccupied row and column")
     except ValueError  :
         print("Enter only numbers in the range 0 to 2 ")
     except IndexError :
         print("Enter two space separateed numbers eg: 1 2 ")
     
       

    board[r][c]=symbol
    printboard()
    if iswon(r,c,symbol) :
        print("Player ",symbol," Won the game") 
        break
else:
    print("Game Draw")
