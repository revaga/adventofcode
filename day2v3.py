
arr = []
with open('input2.txt', 'r') as file:
    for line in file:
        temparr = []
        # Strip whitespace and split the line into two numbers
        parts = line.strip().split()
        for num in parts:
            temparr.append(int(num))
        
        arr.append(temparr)

def check_row(arr):
    decr = True
    incr = True
    safe = True
    for j in range(len(arr)-1):
        if j < len(arr) - 1:
            next = arr[j+1]
        if next > arr[j]:
            decr = False
        elif next < arr[j]:
            incr = False
        if incr == False and decr == False:
            remove_arr = arr[0:j] + arr[j+1:]
            if check_helper_row(remove_arr) == True:
                return True
            else:
                safe = False
        else:
            if abs(next - arr[j]) < 1 or abs(next - arr[j]) > 3:
                if check_helper_row(arr[0:j] + arr[j+1:]) == True:
                    return True
                else:
                    safe = False
    #edge cases
    if check_helper_row(arr[1:]) == True:
            return True
    if check_helper_row(arr[:-1]) == True:
            return True
    return safe


def check_helper_row(arr):
    decr = True
    incr = True
    safe = True
    for j in range(len(arr)-1):
        if j < len(arr) - 1:
            next = arr[j+1]
        if next > arr[j]:
            decr = False
        elif next < arr[j]:
            incr = False
        if incr == False and decr == False:
            safe = False
        else:
            if abs(next - arr[j]) < 1 or abs(next - arr[j]) > 3:
                safe = False
    return safe


temp_arr = [4,2,5,7,8]
print(check_helper_row(temp_arr))
print(check_row(temp_arr))


safe_arr = []
for i in arr:
    safe_arr.append(check_row(i)) #use check_helper_row to get value of safe without removing any numbers

print(safe_arr.count(True))
