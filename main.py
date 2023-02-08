import time
import pandas as pdl
import matplotlib.pyplot as plt

total_money =100
wager_amount = 10
odds=2.50
tax_percentage= 0.20

fib=[0,1]
i=0

data={'Bet':[], 'outcome':[], 'winnings':[]}

while total_money>0:
    print("you have $" + str(total_money)+"remaining.")
    odds= float(input("enter the odds for the bet (e.g 2.50):"))
    print("wager amount : $" + str(wager_amount))
    bet_result= input("Enter 'w' for win or '1' for loss: ")

    if bet_result=="1":
        if wager_amount>total_money:
            print("you do not have enough money to place this bet.")
            break
        total_money-=wager_amount
        print("You lost $"+str(wager_amount)+".")
        data['Bet'].append(wager_amount)
        data['outcome'].append('loss')
        data['winnings'].append(0)
        i+=1
        if i >= len(fib):
            fib.append(fib[i-2])
        wager_amount=wager_amount+fib[i]
        if wager_amount>50:
            wager_amount=50
    elif bet_result=='w':
        winnings = wager_amount*odds
        tax =round(winnings*tax_percentage,2)
        total_money+=winnings-tax
        print("you won $"+ str(winnings)+"!(tax:$"+str(tax)+")")
        data['Bet'].append(wager_amount)
        data['outcome'].append('Win')
        data['winnings'].append(winnings-tax)
        wager_amount=10
        i=0
    time.sleep

print("You have no money")
df= pd.DataFrame(data)
print(df)

df.plot(kind='line')
plt.show()


