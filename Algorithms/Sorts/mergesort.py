___author__= "Shanna Louise"
"""Implements the merge sort algorithm, recursively, in Python"""

#mumbling about how a merge_sort works
      #split list in two halves
      #sort the first half using merge_sort = first_sorted
      #sort the second half using merge_sort = second_sorted
      #merge the two halves back together in a merged list
      #return the mergedsorted list
def main():
   """take a random list and use merge_sort to sort it.""" 
   unsorted = [11, 5, 15, 90, 29, 3]
   sorted_list = merge_sort(unsorted)
   print(sorted_list)

def merge_sort(a_list): 
   """Implement the merge sort algorithm.""" 
#merge_sort
   #if list has one item (base case)
   if len(a_list) <= 1:
   #it's sorted, return the list
      return a_list
   #if list has more than one item
   else:
      #find the middle 
      middle = len(a_list)//2
      #split the list (take a slice from the left to middle and one from middle to right
      #merge_sort the new left and right slices by re-feeding them to merge_sort
      #(recursively invoke merge sort on both new halves)
      left = merge_sort(a_list[:middle])
      right = merge_sort(a_list[middle:]) 
      #returning the merged list is essential to the recursion    
      return merge(left, right)
#when the parts are sorted, merge is performed
def merge(left, right):
   """Given two lists, merge them together into a third list, which is sorted.""" 
   #list to hold our freshy merges   
   temp_list = []
   #tracks length of lists, so we know how long to loop
   right_length, left_length = len(right), len(left)
   #we need to track the indices of left and right, so we can extract the values
   #can initialize them both with a tuple
   left_index, right_index = 0, 0
   #loop until there are still items in at least one list
   while left_length > left_index and right_length > right_index:
      #take the smallest value from two lists 
      if left[left_index] <= right[right_index]:
         #and pop it into the new list
         temp_list.append(left[left_index])
         #increments the left index
         left_index += 1 
      else:
         temp_list.append(right[right_index])
         #increments the right index
         right_index += 1
   #if the length is longer than the left index, we have elements left
   if left_length >= left_index:
      #pass a slice from left index to end, adds it to the end of temp list
      temp_list.extend(left[left_index:])
   #if the length is longer than the right index, we have elements left
   if right_length >= right_index:
      #pass a slice from right index to end, add it to end of temp list
      temp_list.extend(right[right_index:])

   return temp_list
if __name__== '__main__':
   main()

