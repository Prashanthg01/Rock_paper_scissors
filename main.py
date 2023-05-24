import random as rd
count = 0
win = 0
loss = 0
name = input("enter your name: ")
while True:
    count = count + 1
    n = input('choose: rock, paper or scissors: ')
    n = n.lower()
    x = rd.choice(['rock', 'paper', 'scissors'])
    print(f'The computer choise is {x}')
    print(f'number of chances remaining {count}')
    if n == x:
        print("You tied")
        count = count-1
        continue
    elif n == 'paper' and x == 'rock':
        win = win + 1
        print(f'You Win {win} times')
    elif n == 'rock' and x == 'scissors':
        win = win + 1
        print(f'You Win {win} times')
    elif n == 'scissors' and x == 'paper':
        win = win + 1
        print(f'You Win {win} times')
    else:
        print(f'You Loss try again {loss} times')
    loss = loss+1
    if count==5 and win>=3:
        count = 0
        print("you are the finall winner")
    if count==5 and win<3:
        count = 0
        print(f"{name} you loss")
