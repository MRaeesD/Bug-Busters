if k < num_less:
    return kth(below, k)
elif k == num_less: # Change made here
    return pivot
else:
    return kth(above, k - num_lessoreq) # Change made here
