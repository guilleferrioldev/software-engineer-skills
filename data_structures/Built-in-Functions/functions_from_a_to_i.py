from typing import Any, Iterable, Callable, Tuple, List

###############
# ABS
###############
def Abs(number: int | float) -> int | float:
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError(f"bad operand type for abs(): '{type(number).__name__}'")
    
    if number < 0:
        number * (-1)
    
    return number


###############
# ALL
###############
def All(iterable: Iterable) -> bool:
    if not isinstance(iterable, list) and not isinstance(iterable, set) and not isinstance(iterable, dict)and not isinstance(iterable, tuple):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    
    for element in iterable:
        if not element:
            return False
    return True


###############
# ANY
###############
def Any(iterable: Iterable) -> bool:
    if not isinstance(iterable, list) and not isinstance(iterable, set) and not isinstance(iterable, dict)and not isinstance(iterable, tuple):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    
    for element in iterable:
        if element:
            return True
    return False


###############
# CALLABLE
###############
def Callable(obj: Callable) -> bool:
    return hasattr(obj, '__call__')


###############
# DIVMOD
###############
def Divmod(a: int | float, b: int | float):
    if not isinstance(a, int) and not isinstance(a, float) and not isinstance(b, int) and not isinstance(b, float):
        raise TypeError(f"unsupported operand type(s) for divmod(): '{type(a).__name__}' and '{type(b).__name__}'")
    
    quotient = a // b 
    remainder = a % b 
    return (quotient, remainder)

###############
# ENUMERATE
###############
def Enumerate(iterable: Iterable) -> List[Tuple[int, Any]]:
    if not isinstance(iterable, list) and not isinstance(iterable, set) and not isinstance(iterable, dict)and not isinstance(iterable, tuple):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")

    for i in range(len(iterable)):
        yield i, iterable[i]
        
        
###############
# FROZENSET
###############      
class Frozenset:
    def __init__(self, iterable: Iterable) -> None:
        if not isinstance(iterable, list) and not isinstance(iterable, set) and not isinstance(iterable, dict)and not isinstance(iterable, tuple):
            raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
        
        self.set = set(iterable)
        
    def __repr__(self) -> str:
        return f"Frozenset({self.set})"
  
  
###############
# ISINSTANCE
###############    
def Isinstance(obj: Any, type_: type) -> None:
    return type(obj) == type_