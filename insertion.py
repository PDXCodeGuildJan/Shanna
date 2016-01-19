
def main():
   sortedlist = insertsort([5, 21, 11, 93, 55])
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
