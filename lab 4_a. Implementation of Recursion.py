def max_elemnt(gven_lst, len_lst):
    if len_lst == 1:
        return gven_lst[0]
    return max(gven_lst[len_lst - 1], max_elemnt(gven_lst, len_lst - 1))


def min_elemnt(gven_lst, len_lst):
    if len_lst == 1:
        return gven_lst[0]
    return min(gven_lst[len_lst-1], min_elemnt(gven_lst, len_lst-1))


gven_lst = list(map(int, input( 'Enter the Elements of the List separated by spaces = ').split()))
len_lst = len(gven_lst)
print("The Maximum element in a given list",
      gven_lst, "=", max_elemnt(gven_lst, len_lst))
print("The Minimum element in a given list",
      gven_lst, "=", min_elemnt(gven_lst, len_lst))