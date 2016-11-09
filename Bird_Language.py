VOWELS = "aeiouy"

def translate(phrase):
    result = ""
    i = 0
    while i < len(phrase) - 1:
        result += phrase[i]
        if phrase[i] == " ":
            i += 1
        elif phrase[i] not in VOWELS:
            i += 2
        else:
            i += 3
    return result