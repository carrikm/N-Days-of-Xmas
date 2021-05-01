#Carrik McNerlin
#The N Days of Christmas
#28 January 2020

#This program demonstrates that for a given number of days, N, we can use an inductive proof to discover the amount of total gifts given in the
#traditional song "12 Days of Christmas." We will prove it using a loop.
print('Hello. If you give me a day, I will do some quick calculations and show you how many gifts have been given by the end of that day in the 12 Days of Christmas song.')

N=int(input('What day of Christmas would you like to see the total gifts of?\n'))

running_total = 0


#loop up to day N
for i in range(N):
    
    day_total=0
    gift_cdown = i    #inner loop control
    day = i+1    #start at 1, not 0
    while gift_cdown > 0:
        day += gift_cdown   #ex (5 rings + 4 horns + 3 hens + 2 doves + 1 partridge)
        gift_cdown -= 1     #decrement for loop sake
        
    day_total += day
    running_total += day_total

print('Gifts for day: ' + str(day_total))
print('Total gifts: ' + str(running_total))

print('Total gifts (calculated another way): ' + str(int((N * (N+1) * (N+2))/6)))