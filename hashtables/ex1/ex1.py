def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i, weight in enumerate( weights ):
        # check cache for value, return if found
        if limit - weight in cache:
            return ( i, cache[ limit - weight ] )
        # wasn't in cache
        cache[ weight ] = i

    # doesn't exist
    return None