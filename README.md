# README
DSA FUNDAMENTALS - TASK 4:

D1 : count how many times 'l' appears in "hello world":

im just iterating the string and checking if each letter is equal to 'l', if yes then im incrementing the counter


#D2 : find the smallest value in an array of 8 integers:

first im taking inputs for the array, then im setting the min variable value as the first element of the array in the beggining then i itterate every element in the array and if the element is lesser than the current min variable value then the lesser element will be the new value for min variable

#D3 : manually find the 2nd largest number in an array

To find the second largest number in an array, I start by taking user input for all the elements. I then initialize two variables: max and sec. I set their initial values by comparing the first two elements of the array.

After that, I iterate through the rest of the array (starting from the third element). During each step, I check if the current element is greater than max or if it's smaller than max but greater than sec. This two-part check ensures that max and sec are always updated correctly. The sec variable will have the second largest number at the end of the loop, which I then print.
