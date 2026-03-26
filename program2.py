arr = list(map(int, input().split()))
if len(arr) != 0:
    print("Invalid input")
else:
    if all (x == arr[0] for x in arr):
        print("Perfect Array")
    else:
        print("Not Perfect")