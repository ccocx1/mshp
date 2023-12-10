def count_elements(lst):
    if lst == []:
        return 0
    return 1 + count_elements(lst[1:])
my_list = [1, 2, 3, 4, 5]
count = count_elements(my_list)
print(count)



def find_max(lst):
    if not lst:
        return
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))
