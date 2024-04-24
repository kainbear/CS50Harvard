import emoji

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield emoji.emojize(":honeybee:" * i)

if __name__ == "__main__":
    main()

# ITERATORS !!!

""" 

!!! AND THIS IS CS 50 !!!
!!! Harvard !!!
!!! CS50’s Introduction to Programming with Python !!!
!!! Full University Course !!!

"""
