arr = [100,200,300,400,500,600,700,800,900]
number = 3
maxi = 0

# if all array values were the same we'd have to have another consideration in partitioning the pages between scribes

for n in arr:
    maxi += n

def isValid(arr, barrier,n):
  writer = 1
  pages = 0
  for i in range(len(arr)):
    if barrier < arr[i]:
      return False
    if (pages + arr[i]) <= barrier:
      pages += arr[i]
    else:
      writer += 1
      pages = arr[i]
  if writer > n:
    return False
  return True
def defineBarrier(arr,init,final,n):
   i = init
   f = final
   barrier = -1
   while i <= f:
       medium  = (i+f) // 2
       if isValid(arr,medium,n) == True:
           barrier = medium
           f = medium - 1
       else:
           i = medium + 1
   aux = 0
   for pgs in arr:
     if aux + pgs <= barrier:
       aux += pgs
       print(pgs,end=" ")
     else:
       print("\\",end=" ")
       aux = pgs
       print(pgs,end=" ")
defineBarrier(arr,arr[0],maxi,number)