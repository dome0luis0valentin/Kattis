import sys

def factorial(n,fact):
    for i in range(len(fact),n+1):
        fact.append(fact[-1]*i)


def main():


    fact = [1]
    for word in sys.stdin:
        letters = {}
        word = word.strip()
        n = len(word)
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        factorial(n,fact)
        ans = fact[n]
        for let in letters:
            ans //= fact[letters[let]]
        print (ans)

if __name__ == '__main__':
    main()
