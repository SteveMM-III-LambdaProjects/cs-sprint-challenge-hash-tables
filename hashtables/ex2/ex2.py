#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = [ None ] * length

    # cache tickets
    for ticket in tickets:
        cache[ ticket.source ] = ticket.destination

    #print( cache )
    
    # NONE for first
    cur = cache[ 'NONE' ]

    # loop through with each dest as next source
    for i in range( length ):
        route[ i ] = cur
        cur = cache[ cur ]

    return route
