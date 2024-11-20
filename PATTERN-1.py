#PATTERN 1
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

n = 5
half_pyramid(n)

print()
#PATTERN 2
def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")

n = 5
inverted_half_pyramid(n)

#PATTERN 3
def numpat(n): 
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("")

n = 5
numpat(n)

#PATTERN 4
def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)

def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)

def print_pyramid(n, current_row=1):
    if current_row > n:
        return
    spaces = n - current_row
    stars = 2 * current_row - 1
    print_space(spaces)
    print_star(stars)
    print()
    print_pyramid(n, current_row + 1)
n = 5

print_pyramid(n)
