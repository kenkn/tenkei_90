def create_cumulative_sum_list(li):
    c_sum = [li[0]]
    for v in li:
        c_sum.append(c_sum[-1]+v)
    return c_sum