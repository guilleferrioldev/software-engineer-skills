from typing import Any, Iterable, Callable, Tuple, List

###############
# LEN
###############
def Len(iterable: Iterable) -> int:
    if not isinstance(iterable, list) and not isinstance(iterable, set) and not isinstance(iterable, dict) and not isinstance(iterable, tuple):
        raise TypeError(f"object of type '{type(iterable).__name__}' has no len()")
    
    count = 0 
    for _ in iterable:
        count += 1
    return count


###############
# MAX
###############
def Max(iterable: Iterable, *iterables: Iterable, key: Callable = None, default: Any = None) -> Any:
    if len(iterables) > 0:
        iterable = (iterable,) + iterables
    
    if not iterable:
        if default is not None:
            return default
        else:
            raise ValueError("max() arg is an empty sequence")
    
    if key is None: # If a key function is not provided
        max_value = iterable[0]  # We assume that the first element is the maximum
        for item in iterable[1:]: # We start from the second element
            if item > max_value: # We compare the resulting keys
                max_value = item
        return max_value
    else: # If a key function is provided
        max_item = iterable[0]
        max_key = key(iterable[0])
        for item in iterable[1:]:  # We start from the second element
            current_key = key(item)
            if current_key > max_key: # We compare the resulting keys
                max_item = item
                max_key = current_key
        return max_item


###############
# MIN
###############
def Min(iterable: Iterable, *iterables: Iterable, key: Callable = None, default: Any = None):
    if len(iterables) > 0:
        iterable = (iterable,) + iterables

    if not iterable:  # Handling the case where no iterable is provided
        if default is not None:
            return default
        else:
            raise ValueError("min() arg is an empty sequence")

    if key is None: # If a key function is not provided
        min_value = iterable[0] # We assume that the first element is the minimum
        for item in iterable[1:]: # We start from the second element
            if item < min_value:  # We directly compare the elements
                min_value = item
        return min_value
    else:  # If a key function is provided
        min_item = iterable[0] 
        min_key = key(iterable[0]) 
        for item in iterable[1:]: # We start from the second element
            current_key = key(item)
            if current_key < min_key: # We compare the resulting keys
                min_item = item
                min_key = current_key
        return min_item


###############
# RANGE
###############
class Range:
    """A class that mimic s the built-in range class."""
    def __init__(self, start: int, stop: int = None, step: int = 1) -> None:
        """Initialize a Range instance. Semantics is similar to built-in range class."""
        if step == 0:
            raise ValueError("step cannot be 0")
       
        if stop is None: # special case of range(n)
            start, stop = 0, start # should be treated as if range(0,n)
            
        # calculate the effective length once
        self.length = max(0, (stop - start + step - 1) // step)
        
        # need knowledge of start and step (but not stop) to support getitem
        self.start = start
        self.step = step
        self.stop = stop
          
    def __len__ (self) -> int:
        """Return number of entries in the range."""
        return self.length
    
    def __contains__(self, value: int) -> bool:
        """Return if the value exists"""
        current = self.start
        while (self.step > 0 and current < self.stop) or (self.step < 0 and current > self.stop):
            if current == value: 
                return True
            current += self.step   
        return False
    
    def __getitem__ (self, index: int) -> int:
        """Return entry at index (using standard interpretation if negative)."""
        if index < 0:
            index += len(self) # attempt to convert negative index
            
        if not 0 <= index < self. length:
            raise IndexError("index out of range")
        
        return self.start + index * self.step
    
    def __iter__(self) -> Iterable[int]:
        current = self.start
        while (self.step > 0 and current < self.stop) or (self.step < 0 and current > self.stop):
            yield current
            current += self.step
        
    def __repr__(self):
        return f'Range({self.start}, {self.stop}, {self.step})'
   
    
###############
# SUM
###############
def Sum(iterable: Iterable, start: Any = 0) -> Any:
    result = start
    for element in iterable:
        result += element
    return result


###############
# VARS
###############
def Vars(obj: object) -> dict:
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    elif hasattr(obj, '__slots__'):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        raise AttributeError("The object has no directly accessible attributes")


###############
# ZIP
###############
def Zip(iterable_1: Iterable, iterable_2: Iterable) -> List[Any]:
    smaller = iterable_1 if iterable_1 < iterable_2 else iterable_2
    largest = iterable_1 if iterable_1 > iterable_2 else iterable_2
    
    for index in range(len(smaller)):
        yield smaller[index], largest[index]