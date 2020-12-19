# python-dynamic-programming
## Dynamic Programming 
   we use memoization 

## Fibonacci Series

   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,...etc.
Fibonacci Explanation 
   The first value should be added with the second value and second value added with the third value and so on.
Fibonacci Time Complexcity
   In normal we can find the fibonacci series ==> O(2**n)times, but in the case of dynamic programming 
   we can find the fibonacci value ==> O(n)times through dynamic programming we are removing 
   the dupilicate iteration by storing the data

## Grid Traverel
   you have a 3x3 dimention, now you are in the position (1,1). your destination is to go to the last position at (3,3).

Grid Explanation 
    you want find how many possible ways are there to reach the destination.

Grid Time Complexcity
    In normal we can find the Grid Traverel ==> O(2**n+m)times, but in the case of dynamic programming
    we can find the Grid value ==> O(n*n)times here also we are going to use the same memoization 
    method to reduce the time complexcity
