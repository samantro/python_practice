# genrator for infinite even numbers

def infinite_even_numbers():
    num = 0
    while True:
        yield num
        num += 2

# [x**3 for x in range(1, 20) if x%2 == 0]

def even_cubes_up_to(n):
    for x in range(1, n):
        if x % 2 == 0:
            yield x ** 3

def sentence_to_word(sentence):
    words = sentence.split(' ')
    for word in words:
        yield word.title()