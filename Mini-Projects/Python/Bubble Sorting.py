'''
Implementation of Binary Search Algorithm in Python
'''

# defining a function for bubble sort
# def bubble_sort(my_list):

#                 # len() to find total no of elements in list
#                 length   =  len(my_list)
#                 print(f"Original List : {my_list}")

#                 # traversing through the list with for loop
#                 for i in range(length - 1): 
#                         for j in range(length - i - 1):
#                                 #  checking and swapping values if the element is found larger
#                                 if my_list[j] > my_list[j+1]:
#                                         my_list[j],  my_list[j+1] = my_list[j+1],  my_list[j]

#                 print(f"After sorting list is :  {my_list}")

# # creating a list through user input
# my_list = []
# num = int(input("Enter total no of elements =  "))
# for i in range(num):
#         x = int(input("Enter no :  "))
#         my_list.append(x)

# # function call
# bubble_sort(my_list)

def bubblesort(arr):
        n = len(arr)
        print("original list:",arr)
        for i in range (n-1):
                for j in range(0,n-i-1):
                        if arr[j] > arr[j+1]:
                                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("sorted list:",arr)
arr = []
num = int(input("enter number of elements:"))
for i in range(num):
        ele = int(input("enter elements:"))
        arr.append(ele)
bubblesort(arr)
                

