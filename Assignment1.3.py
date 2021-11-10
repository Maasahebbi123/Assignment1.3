#Don't go outside in odd days.
Days=(1,2,3,4,5,6,7,8,9,10,11,12,13)
even=0
odd=0
for i in Days:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print('Total number of even days: ',even)
print('Total number of odd days: ',odd ,end='')
print(' , Do not go outside.')
