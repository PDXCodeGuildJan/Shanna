"""Search functions, including Binary. """
#from module/docname import nameoffunction
from insertion import insertsort

def main():
   #makes the list to look through, and the targetvalue to look for
   unsortedlist = ['E', 'T', 'B' , 'S' , 'W']
   targetvalue = 'S'

   #call the search function, catch what it returns, which is a tuple
   sortedlist, targetindex = binary_search(unsortedlist, targetvalue)

   #print out our solutions
   print(sortedlist, 'I found', targetvalue, 'It is at ', targetindex, '.')

def binary_search(thelist, targetvalue): 
   """Implements the Binary Search Algorithm"""

   sortedlist = insertsort(thelist)
   #Search for the target value

   #Find length of current segment. 
   length = len(sortedlist)
#initialize start and end variables
   start = 0
   end = length
   #If length >=1, look for target
   while length >= 1:
     
      #Find the middle of the part of the list being searched.
      middle = start + (length //2)
   #if equal, we've found it, return middle. More efficient to look for best case
   #first (we found it!), then suboptimal situations, then worst. The worst case 
   #situation is if there's a list of only one item, with no middle.

   #determine if middle value is greater or less than or equal to targetvalue
   #if equal, we found it, return middle
      if sortedlist[middle] == targetvalue: 
         return (sortedlist, middle)
   #if greater than, reduce segment to left half from middle, repeat loop. Start
   # to middle. NEw end point is now the middle
      elif sortedlist[middle] > targetvalue:
         end = middle
   #if less than, reduce segment to right half from middle, repeat loop
      elif sortedlist[middle] < targetvalue:
         start = middle + 1
   #updates length value to be the length of the list from the start to the new 
   #end. length of the new segment
      length = len(sortedlist[start: end])

#remember to handle what happens when searched-for element isn't there
#traditionally, we return -1 if we can't find the index.
#   return (sortedlist, -1)
#tuple is a group of related elements, a chunk of related information
if __name__ =="__main__":
   main()



