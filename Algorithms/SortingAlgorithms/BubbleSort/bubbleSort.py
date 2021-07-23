
def bubbleSort(array):
   for j in range(len(array)-1):
      change = False
      for i in range(len(array)-1):
          if array[i] > array[i+1]:
              temp = array[i]
              array[i] = array[i+1]
              array[i+1] = temp
              change = True
      #print(array)
      if not change: return array    
   return array

#--testing--
arr = [1,3,4,4,3,3,2,2,1,1,1,1,1,0]
arr2 = bubbleSort(arr)
print(arr2)
