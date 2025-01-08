#python share code

def binary_search(arr, target):
    startIndex = 0 
    newLength = len(arr)
    while newLength != 2:
      middle = newLength//2
      if target == arr[middle]:
        IndexofTarget = middle
        print("Target Found")
        return target
      elif target < arr[middle]:
         print("less than mid")
         newLength = newLength//2   #
      else:
         newLength = newLength//2
         print("larger than mid")


#-------------------------------------------

input = "racecar"
def isPalindrome(input):
  input = input.lower()
  i = 0
  j = len(input)
  while i < j:
      if input[i] != input[j-1]:
        return False
      i += 1
      j -= 1
  return True

print(isPalindrome(input))
