def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def classify_number(n):
    if n == 0:
        return "zero"
    if is_positive(n):
        result = "positive"
    else:
        result = "negative"
    if is_even(n):
        return f"{result} even"
    else:
        return f"{result} odd" 
