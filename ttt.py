import itertools
board=[0,1,2,3,4,5,6,7,8]
def play_game():
    input1=[]
    input2=[]
    win=0
    show_board()
    winset=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    while(True):
        if(len(input1)<=5):
            inputuser1=int(input("enter position to occupy by user1"))
            if inputuser1 not in input2:
                input1.append(inputuser1)
                input1=sorted(input1)
                board[inputuser1]="X"
                show_board()
                print("input1:",input1)
                if len(input1)>=3:
                    lst=[]
                    s=[]
                    for i in itertools.combinations(input1,3):
                        lst.append(i)
                        for j in lst:
                            if j not in s:
                                s.append(j)
                                if list(j) in winset:
                                    win=1
                                    print("winner is user1")
                                    break
        else:
            break
        if win==1:
                break
        if(len(input1)<5):
            inputuser2=int(input("enter position to occupy by user2"))
            if inputuser2 not in input1:
                input2.append(inputuser2)
                input2=sorted(input2)
                board[inputuser2]="O"
                show_board()
                print("input2:",input2)
                if len(input2)>=3:
                    lst1=[]
                    s1=[]
                    for i in itertools.combinations(input2,3):
                        lst1.append(i)
                    for j in lst1:
                        if j not in s1:
                            s1.append(j)
                            if list(j) in winset:
                                win=1
                                print("winner is user2")
                                break
        else:
            print("match draw")
            break
def show_board():
    c=0
    for i in range(3):
        for j in range(3):
            print(board[c],sep="|",end="|")
            c+=1
        print("\n")
play_game()
