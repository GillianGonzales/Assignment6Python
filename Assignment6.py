#
# Created By Gillian Gonzales
# Created On April 25 2018
#
# This program will find PI

n = 0
answer = 1

goodinput = False
while not goodinput:
    try:
        loopn = int(input('Enter a number: '))
        if loopn >= 0:
            goodinput = True
        else:
            print("that's not a positive number. Try again: ")
    except ValueError:
        print("that's not an integer. Try again: ")  

for loop in range (0,loopn) :
	n = n + 1
	answer = answer + ((-1)**n)/(2*n+1)
pass
answer = answer * 4
print(answer)




input("End Program")