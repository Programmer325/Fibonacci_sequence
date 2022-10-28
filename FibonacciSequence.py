from re import A


def fibonacci_sequence(fibonacci_sequence_length):
    a = 0
    b = 1
    i = 1
    while i <= fibonacci_sequence_length:
        print(str(i) + ". == " + str(b))
        b = a + b
        a = b - a
        i+=1




print("ENG: Fibonacci Sequence || PL: Ciag Fibonacciego")
print("ENG: Enter the length of the list || PL: Podaj ilosc elementow ciagu")
fibonacci_sequence_length = int(input(": "))

fibonacci_sequence(fibonacci_sequence_length)