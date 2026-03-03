# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """
    myFunction(arg1, arg2=None) --> Doesn't really do anything

    Parameters:
        arg1: the first arg
        arg2: 2nd arg.  Defaults to none.

    Returns:

    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
