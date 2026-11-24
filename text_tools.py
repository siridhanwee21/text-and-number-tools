 # Text and Number Tools Project

def word_count(sentence):
    words = sentence.split()
    return len(words)


def longest_word(sentence):
    words = sentence.split()

    if not words:
        return "No words entered"

    return max(words, key=len)


def reverse_sentence(sentence):
    return sentence[::-1]


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Main program
sentence = input("Enter a sentence: ")
number = int(input("Enter a number: "))

print("\n--- Text Results ---")
print("Word count:", word_count(sentence))
print("Longest word:", longest_word(sentence))
print("Reversed sentence:", reverse_sentence(sentence))

print("\n--- Number Result ---")
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")