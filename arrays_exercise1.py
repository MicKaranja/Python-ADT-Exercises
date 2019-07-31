"""1. You have been given an array of distinct integer values, No number in the array is repeated. 
It also gives you a separate integer value that represents a target sum. Write a function that is 
going to find whether or not there is a pair of numbers in the array given, that sums up to the target sum.
[3, 5, -4, 8, 11, 1, -1, 6]  target sum  = 10"""

def pair_sum_is_n(arr, n):
    """Check if there are any two elements in array "arr" that sums up to a given target "n".
    
    Args:
        arr (list): a list of integers or floats..
        n (int): the desired target sum.
    
    Returns:
        2-element list if the two numbers exist, otherwise empty list.
    Run time:
        linear time: O(N)
    """
    arr = set(arr)
    for i in arr: # i is one part of the pair
        if n - i in arr: # n-i is the second part of the pair; checking if it exists
            return [i, n-i]
    return []

#print(pair_sum_is_n([3, 5, -4, 8, 11, 1, -1], 17))

"""
2.  You have been given an array of distinct integer values, No number in the array is repeated. 
It also gives you a separate integer value that represents a target sum write  a function that 
will find all the possible triplets in the array, that sum up to the target sum
    [12, 3, 1, 2, -6, 5, -8, 6] target sum  = 0

"""
def triplet_sum_is_n(arr, n): 
    """
    find all the possible triplets in the array "arr", that sum up
     to a given target sum "n".
    
    Args:
        arr (list): an array of integers.
        target (int): an array of integers.
    
    Returns:
        a list of tuples with triplets that add to target.
    Run time:
        quadratic time : O(N^2) 
    """
    for i in range(0, len(arr)): 
        # Find pair in subarray arr[i + 1..n-1]  
        # with sum equal to sum - arr[i] 
        s = set() # ensuring no duplicates
        current_sum = n - arr[i] 
        for j in range(i + 1, len(arr)): 
            if (current_sum - arr[j]) in s: 
                return True
            s.add(arr[j]) 
            print("Triplet:", arr[i],  
                        ", ", arr[j], ", ", current_sum-arr[j])
    return False

#print(triplet_sum_is_n([12, 3, 1, 2, -6, 5, -8, 6], 15))


"""
3.  You have two arrays of integer values. Write a function to find the pair 
of numbers where one number comes from the first array,
and another number comes from the second array with the smallest difference.
Array A = [-1, 5, 10, 20, 28, 3]
Array B = [26, 134, 135, 15, 17]"""

def smallest_difference_pair(arr1, arr2): 
    """
    find the pair of numbers where one number comes from the first array,
     and another number comes from the second array with the smallest difference.
    
    Args:
        arr1 (array): array of integer values.
        arr2 (array): array of integer values.
    
    Returns:
        tuple: pair of ints with the smallest  difference.
    Run time:
            linear time: O(N)  
    """
    # sorting the arrays 
    arr1.sort() 
    arr2.sort() 
    
    res_min = 0; res_max = 0 # To store resultant 2 numbers 

    i, j = 0,0  # pointers to arr1, arr2, 
    # Loop until one array reaches to its end 
    # Find the smallest difference. 
    diff = 2147483647 # max size for a 32-bit system (sys.maxsize)
    while (i < len(arr1) and j < len(arr1)): 
        maxi = max(arr1[i], arr2[j])  # maximum number 
        mini = min(arr1[i], arr2[j]) # Find minimum and increment its index.
        if (mini == arr1[i]): 
            i += 1
        else: 
            j += 1
        # Comparing new difference with the 
        # previous one and updating accordingly 
        if (diff > (maxi - mini)): 
            diff = maxi - mini
            res_max = maxi
            res_min = mini
    return res_max, res_min

#print(smallest_difference_pair([-1, 5, 10, 20, 29, 3], [26, 134, 135, 15, 19]))

"""
4. You have been given an array of distinct integer values, No number in the array is repeated. 
It also gives you a separate integer value that represents a target sum. write  a function that 
will find all the possible quadruplets in the array, that sum up to the target number.
[7, 6, 4, -1, 1, 2] target sum  = 16 """

def quadruplets_sum_to_target(arr, n): 
    """
    find all the possible quadruplets in the array "arr",
     that sum up to the target number "n".
   
    Args:
        arr (list): an array of integers. 
        n (int): target sum.
    
    Returns:
        True after printing a list of quadruplets.

    Run time:
        cubic time = O(N^3)
    """ 
    # Fix the first element and find  
    # other three 
    for i in range(0,len(arr)-3): 
          
        # Fix the second element and  
        # find other two 
        for j in range(i+1,len(arr)-2): 
              
            # Fix the third element  
            # and find the fourth 
            for k in range(j+1,len(arr)-1): 
                if n - (arr[i] + arr[j] + arr[k]) in arr: # finding if the remainder exists
                    print("Quadruplet:", arr[i], arr[j], arr[k], n - (arr[i] + arr[j] + arr[k]) )

#print(quadruplets_sum_to_target([ 7, 6, 4, -1, 1, 2, 8, 8, 0, 0], 16))
