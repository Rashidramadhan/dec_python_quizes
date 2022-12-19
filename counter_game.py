# Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of 2.
# If it is, they divide it by 2. If not, they reduce it by the next lower number which is a power of 2.
# Whoever reduces the number to 1 wins the game. Louise always starts. we have Given an initial value,
# determine who wins the game.

def counter_game(n):
    set_bits = bin(n-1).count('1')
    if set_bits % 2 == 1:
        print('Louise')
    else:
        print('Richards')
counter_game(6)
