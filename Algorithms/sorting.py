#Locate smallest number in the unsorted list. 
#Swap smallest number with first number in the unsorted list.
#Update the first number of the unsorted list to be the next number in the unsorted list. 
#Repeat 1-3 until there are no more numbers in the unsorted list.

unsortedlist = []
def selection_sort(unsortedlist):
   smallnum = min([unsortedlist])
   
   unsortedlist.insert(0, smallnum)



