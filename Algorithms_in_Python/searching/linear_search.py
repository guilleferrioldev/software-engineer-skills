# Unordered linear search

def search(unordered_list, term):
    for i, item in enumerate(unordered_list):
        if term == unordered_list[i]:
            return i
    return None


# Ordered linear search

def search_ordered(ordered_list, term):
    ordered_list_size = len(ordered_list)
    
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None
    return None
