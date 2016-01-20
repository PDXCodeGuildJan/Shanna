#this function adds every number in a list iteratively
def sum(list):
   sum = 0
#find length of list
   for i in range(0, len(list)):
#updates sum to be sum plus the value at working index
      sum = sum + list[i]
   return sum

print(sum([5, 7, 3, 8, 10]))

#this function adds every number in a list recursively

def sum(list):
#if the length of the list is one item, return value at index 0
   if len(list) == 1:
      return list[0]
#if the length of the list is more than one item, return the value of item 
#plus next door neighbor from index position 1 through the end of the list.
   else:
      return list[0] + sum(list[1:])
#passes the variables to function sum, prints answer
print (sum([5,7,3,8,10]))

#this function calculates the factorial of a number n





