
arr = []
with open('input2.txt', 'r') as file:
    for line in file:
        temparr = []
        # Strip whitespace and split the line into two numbers
        parts = line.strip().split()
        for num in parts:
            temparr.append(int(num))
        
        arr.append(temparr)


def func(arr):
    safe = [True] * len(arr)

    for i in range(len(arr)):
        decr = True
        incr = True
        for j in range(len(arr[i])-1):
            if j < len(arr[i]) - 1:
                next = arr[i][j+1]
            print(arr[i][j], next)
            if next > arr[i][j]:
                decr = False
            elif next < arr[i][j]:
                incr = False
            if incr == False and decr == False:
                safe[i] = False
                break

            else:
                if abs(next - arr[i][j]) < 1 or abs(next - arr[i][j]) > 3:
                    safe[i] = False
                    break

    print(safe.count(True))

