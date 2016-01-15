

def main():
   unsortedlist = [27, 89, 5, 11, 15]
   print(unsortedlist)
   sortedlist = selectionsort(unsortedlist)
   print(sortedlist)

def selectionsort(unsortedlist):
#Find the start of the unsorted list.
  
   position = 0 #index position of number we're working at, beginning of unsorted list. 
   numinlist = len(unsortedlist) #number of variables in list

   #this loop moves the start of the unsorted list one space forward 
   while position < numinlist: 
      #the lowest # is only gonna be the nownum the first iteration of the while
      #loop, so it needs to be outside the other while loop.

      nownumindex = position #temp variable to hold lowest found value thus far
      #always start looking for lowest at the start of the unsorted part of the 
      #list. position is the variable holding the start index of the unsorted list

      lowestindex = nownumindex #number we're checking the others against, value 
                                #of variable at position 

#This loop locates the smallest number and compares it against the remaining numbers
#It iterates until the index position we're working from is less than 
#length of unsorted part of list (numbers remaining).
# We have to slice the list to get only the unsorted part to the end.

#this line gets the length of the unsorted part of the list by slicing from position
#which is the variable holding the start index of the unsorted part, to the end.     
      while nownumindex < len(unsortedlist):
#if the variable stored at the address we're at (nownumIndex) is less than the 
#current lowest variable, which lives at lowestindex, the address of the newly 
#identified lowest variable becomes the new lowestindex. 
         if unsortedlist[nownumindex] < unsortedlist[lowestindex]:
            lowestindex = nownumindex

#now we have to move the value living at the lowestindex to temp variable switch
         nownumindex += 1 #everytime the loop runs, the index position increases

      #Swap smallest number with first number in the unsorted list.
      #Update the first number of the unsorted list to be the next number in the 
      #unsorted list.
      temp = unsortedlist[lowestindex] 
      unsortedlist[lowestindex] = unsortedlist[position]
      unsortedlist[position] = temp

      position += 1 #everytime the loop runs, the index position increases

   return unsortedlist
      
main()  


 




