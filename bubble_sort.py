
def bubble_sort(L):

    swapped = True # set flag True to repeat sorting

    while swapped:
        swapped = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                # swap the element
                L[i], L[i+1] = L[i+ 1], L[i]
                # set the flag to True so we'll loop again
                swapped = True

    return L


numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))

