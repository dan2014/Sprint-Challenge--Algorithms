import random
import time

# def floor_finder(floors):
#     true_floor =  random.randint(1, floors)
#     current_floor = floors//2
#     print("True floor", true_floor)
#     attempts = 0
#     while( True ):
#         attempts += 1
#         time.sleep(0.5) 
#         if( current_floor == true_floor ):
#             break
#         else:
#             if( current_floor > true_floor ):
#                 current_floor = current_floor - ( true_floor - current_floor ) // 2 
#             else:
#                 print( ( floors - current_floor ) // 2  )
#                 current_floor = current_floor + ( floors - current_floor ) // 2 

#     print(f"{attempts} Attempts")
#     return current_floor

    
# print(floor_finder(11))

def alg(n):
    sum = 0
    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1
    return sum

print(alg(10))