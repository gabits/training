def find_outlier(integers):
    for o in integers:
        copied_list = integers.copy()
        copied_list.remove(o)
        if o % 2 != (copied_list[0] % 2) and (o % 2) != (copied_list[1] % 2):
            return o
