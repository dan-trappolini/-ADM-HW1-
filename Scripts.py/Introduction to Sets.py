def average(array):
    n_array=sum(set(map(float,array)))
    l=len(set(array))
    return (n_array/l)
