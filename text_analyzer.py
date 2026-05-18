# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count
def total_letters(text):
    return count_consonants(text) + count_vowels(text)

def vowel_percentage(text):
    total = total_letters(text)
    if total == 0:
        return 0.0
    vowel = count_vowels(text)
    return round((vowel / total)* 100, 1)

def analyze_text(text):
    return f"V:{count_vowels(text)} C:{count_consonants(text)} T:{total_letters(text)} P:{vowel_percentage(text)}%"

