
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

#def bubbleSort(alist):
 #   for passnum in range(len(alist)-1,0,-1):
 #       for i in range(passnum):
 #           if alist[i]>alist[i+1]:
 #               temp = alist[i]
 #               alist[i] = alist[i+1]
 #               alist[i+1] = temp

#alist = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)
#print(alist)
         

#MAKE INSERTION SORT FOR THE WEEKEND AND HAVE IT WORKING
#read chapter 5-8, 13

#TURN SWAP INTO A FUNCTION
#Swaps the values in the two passed indexes of the passed list
def swap(unsortedlist, index1, index2):
   temp = unsortedlist[index1]
   unsortedlist[index1] = unsortedlist[index2]
   unsortedlist[index2] = temp

   unsortedlist=swap(unsortedlist, index1, index2)
      
   unsort_len -=1  
   return unsortedlist

main()

def swap(unsortedlist):
   unsortedlist[index1], unsortedlist[index2] = unsortedlist[index2], unsortedlist[index1]
   
   return unsortedlist



#x-1 passes to sort x values

#INSERTION SORT
#Find the start of the unsorted list.
#Begins at index 1, the start of the unsorted list.
#Compare working number with number at the beginning of the unsorted list.
#If working number > number at start of unsorted list,
#  insert in numerical order in sorted list
#     which means you have to compare the first pair
#        # if workingval > neighbor 

# What values do we need?
#  Beginning of unsorted list = position
#  Length of full list = numinlist (to tell when to stop iterating)
#  

#  Value of variable stored at position = workingval 
#  Which should be compared to the value of variable stored nextdoor, position -1 


def main():
   sortedlist = insertionsort(5, 21, 11, 93, 55)
   print(sortedlist)

def swap (thelist, index1, index2): 
#swaps two items in a list
   thelist[index1], thelist[index2] = thelist[index2], thelist[index1]
   return thelist

def insertsort(thelist):
 
#this loop moves the start of the unsorted list one index forward
    for startindex, value in enumerate(thelist): 

#temp variable for the index of the thing we're currently sorting
      lostindex = startindex
      lostvalue = value

#while the value stored at the lostindex < the value stored at the lostindex -1, the neighbor, AND the lost_index <1, keep 
      while (lostvalue < thelist[lostindex - 1] and lostindex > 0):
#swapping the lostvalue with its adjacent value
         thelist = swap(thelist, lostindex, lostindex -1)
         
# the lostindex moves left one space with each iteration  
         lostindex -=1

    return thelist

main()

     

 




