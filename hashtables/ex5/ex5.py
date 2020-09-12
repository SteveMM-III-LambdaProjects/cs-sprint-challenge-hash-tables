# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    
    dirs    = dict.fromkeys( queries )
    results = []
    
    for path in files:
        file = path.split( "/" )[ -1 ]

        if file in dirs:
            results.append( path )

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
