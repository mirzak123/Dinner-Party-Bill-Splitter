# write your code here
import random


def lucky_one(ans):
    if ans == 'Yes':
        lucky_name = random.choice(list(names))
        print(lucky_name, "is the lucky one!")
        evenly_split_bill = total_bill / (len(names) - 1)
        for i in names:
            if i == lucky_name:
                names[i] = 0
            else:
                names[i] = round(evenly_split_bill, 2)
    else:
        print("No one is going to be lucky")


print("Enter the number of friends joining (including you):")
n = int(input())
if n <= 0:
    print("No one is joining for the party")
    quit()
names = dict()
print("Enter the name of every friend (including you), each on a new line:")
for _ in range(n):
    names[input()] = 0
print('Enter the total bill value: ')
total_bill = float(input())
evenly_split_bill = total_bill / len(names)
for i in names:
    names[i] = round(evenly_split_bill, 2)

print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
answer = input()
lucky_one(answer)
print(names)
