
# for find duplicate items in array(list) by O(n) time complexity (by hash table)
# Dictionary in python created by hashtable data structure
def find_duplicate(array):
    hash_table = {}
    print("The duplicate items are: ")
    for i in array:  # time complexity = O(n)
        tbl_len = len(hash_table)  # time complexity = O(1)
        hash_table[i] = i
        if tbl_len == len(hash_table):
            print(i)


# for find sum of two numbers by O(nlgn) complexity time
def find_sum(array, number):
    s = 0
    e = len(array) - 1
    sorted_arr = sorted(array)  # sort the array by O(nlgn)
    while e > s:  # find numbers by O(n)
        if sorted_arr[s] + sorted_arr[e] == number:
            return sorted_arr[s], sorted_arr[e]
        elif sorted_arr[s] + sorted_arr[e] < number:
            s += 1
        else:
            e -= 1


if __name__ == '__main__':
    # find duplicate items
    arr = [2, 3, 32, 32, 4, 5, 34, 45, 45, 4]
    find_duplicate(arr)

    # find sum of two numbers
    my_arr = [1, 2, 45, 3, 67, 10, 200, 167]
    num = 210
    print(f"The result is : {find_sum(my_arr, num)}")
