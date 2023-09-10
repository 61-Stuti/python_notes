def bubble(lst):
    n = len(lst)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        for j in range(0,n-i-1):
        # since after each pass largest number is at right end

            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

                Swapped = True
            if(Swapped == False):            #all the elements are sorted
                break

    
lst= [64, 34, 25, 12, 22, 11, 90]
print("Sorted list: ")
bubble(lst)
for i in lst:
    print(i, end=" ")


#OR

# Optimized Python program for implementation of Bubble Sort


def bubbleSort(arr):
	n = len(arr)
	
	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already in place
		for j in range(0, n-i-1):
			print(i,j)

			# Traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
				print(arr)
		if (swapped == False):
			break


# Driver code to test above
if __name__ == "__main__":
	arr = [64, 34, 25, 12, 22, 11, 90]

	bubbleSort(arr)

	print("Sorted array:")
	for i in range(len(arr)):
		print("%d" % arr[i], end=" ")

# This code is modified by Suraj krushna Yadav


		