
#
def main():
#displays unsorted list
   unsortedlist = [27, 89, 5, 11, 15]
   print(unsortedlist)
#displays sorted list
   sortedlist = bubblesort(unsortedlist)
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
      


#BUBBLE SORT

#if the first value in the unsorted list isn't the last, continue
#if the current value in the unsorted list is the last value in the unsorted list,
#stop

#     locate first value in unsorted list
#     compare found value w/value in index to right
#        if left value > right value:
#        swap
#        if left value < right value:
#        move one index to the left
#        repeat

   
#this loop moves the 
def bubblesort(unsortedlist):
   
   #number of variables in unsortedlist
   unsort_len = len(unsortedlist)
   #length of the full list
   length = len(unsortedlist)

   while unsort_len > 1 :
      #value stored at the index we are currently looking at, beginning of unsortedlist
      workingind = 0

      while workingind < unsort_len-1:

         workingval = unsortedlist[workingind] 
         neighbor = unsortedlist[workingind +1] 
         
         if workingval > neighbor:
       
            temp = unsortedlist[workingind]
            unsortedlist[workingind] = unsortedlist[workingind +1]
            unsortedlist[workingind +1] = temp

         workingind += 1
         
      
      unsort_len -=1  
   return unsortedlist

main()
     

 




