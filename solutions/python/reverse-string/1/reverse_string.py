def reverse(text):
    reverse_text = ""
    for letter in range(len(text)-1, -1, -1):
        reverse_text += text[letter]
    return reverse_text
