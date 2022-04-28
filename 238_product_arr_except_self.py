def find_product(arr):
    # Write your code here
    left = [0] * len(arr)
    product = [0] * len(arr)
    
    leftProd = 1

    for i, val in enumerate(arr):
        left[i] = leftProd
        leftProd *= val
    
    rightProd = 1
    i = len(arr)-1

    while i >= 0:
        product[i] = left[i]*rightProd
        rightProd *= arr[i]
        i -= 1
    
    return product

print(find_product([1, 2, 3, 4]))