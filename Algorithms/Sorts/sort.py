#make a place (empty list) to hold the unsorted variables
#make a place (empty list) to hold the sorted variables. Not sure if this is 
#necessary.
unsortedlist = [117, 48, 5, 22, 4, 0, 87] 

sortedlist = [] #current state every iteration except first


#defines sort function and tells it to expect the unsorted list of variables
def selection_sort (unsortedlist):
 
#computer finds out how many items in list 
   numinlist = len(unsortedlist)
#create variable for smallest number
#computer finds smallest number in that list
   smallest = min([unsortedlist])
#remove smallest number from list
   unsortedlist.remove(smallest)
#insert smallest number at index 0
   unsortedlist.insert(0, smallest)
#number that used to be at index 0 has been shifted one to the right, to index 1
#computer looks at the number living at index 1

#computer loops to check for next smallest number

# computer moves that number to index 1.  

#former index 1 number swapped out where second smallest number used to live, 
#ad nauseum.
   

#calls function and passes it the unsortedlist
selection_sort(unsortedlist)
   






   

sorted=selection_sort([])
   print (sorted)
