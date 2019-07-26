# Analysis of Algorithms Answers

## Exercise I
a) This will run in O(n), linear, time. The `while` loop with run iteratively and dependent on a condition that `a < n^3`. By dividing the n^3 by n^2, we find that a becomes a factor n^3. This results in a being added by that factor and which is equal to n. 

b)

c) This is run in linear time. This function utilizes recursion and one stack is created for each recursive call. Each recursive call reduces the n by 1 until the stop condition is met. The function adds 2 + bunnyEars(n-1). bunnyEars(n-1) is called n times. 

## Exercise II
Because we have at least enough eggs for every floor, we can test floors in a way that allows for breaking multiple eggs. One can determine the correct floor in O(log(n)) time. Assume that we can 100 story building. There are 99 possible floors that can be the highest floor that can egg will not break. 
We can go to the middle floor, 50, and try it there. Assume that the target floor is 63. The egg will not break at floor 50, so we go higher. We try floor 75, and an egg breaks. We go to 62, and the egg doesn't break, so we go higher. We go to 68, and the egg breaks, so we go lower. The following floors are 64, then 62. Worst case is log(stories) base 2 number of steps. 

This approach is better than linear time and guessing on average. 

def floor_finder(floors):
    true_floor =  random.randint(1, floors)
    current_floor = floors//2
    print("True floor", true_floor)
    attempts = 0
    while( True ):
        attempts += 1
        time.sleep(0.5) 
        if( current_floor == true_floor ):
            break
        else:
            if( current_floor > true_floor ):
                current_floor = current_floor - ( true_floor - current_floor ) // 2 
            else:
                current_floor = current_floor + ( floors - current_floor ) // 2 
    print(attempts)
    return current_floor