#this function multiplies all numers in a list

def multiply(numbers):
   total = 0
#for as many times as there are numbers in the list
   for x in numbers:
#the new total = total * x 
      total *=x
   return total
print(multiply((8,2,3,0,7)))
   
