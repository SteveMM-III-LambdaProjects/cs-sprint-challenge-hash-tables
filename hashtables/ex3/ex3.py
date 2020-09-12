def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache  = {}
    result = []

    # nested fors counting ocurrs
    for ray in arrays:
        for itm in ray:
            if itm not in cache:
                cache[ itm ]  = 1
            else:
                cache[ itm ] += 1
    
    # check cache, if in all should == len arrays
    for key in cache:
        if cache[ key ] == len( arrays ):
            result.append( key )

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
