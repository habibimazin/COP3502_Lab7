import sys

arguments = sys.argv  # converts input into a list
from heifer_generator import HeiferGenerator

def list_cows(cows):
    print("Cows available:", end= " ")
    for cow in cows:
        print(cow.get_name(), end= " ")


def find_cow(name, cows):  # Given a name and a Python list of Cow objects, return the Cow object with the specified name.
    for cow in cows:
        if name == cow.get_name():
            return cow
    return None


if __name__ == "__main__":

    me_moo_moos = HeiferGenerator.get_cows()
    if sys.argv[1] == "-l":
        (list_cows(me_moo_moos))

    elif sys.argv[1] == "-n":  # Prints out the MESSAGE using the specified COW #Prints specified cow
        me_moo_moos = find_cow(sys.argv[2], me_moo_moos)
        if me_moo_moos is None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            for word in sys.argv[3:]:
                print(word, end=" ")
            print()
            print(me_moo_moos.get_image())

    elif sys.argv[1] != "-l" or sys.argv[1] != "-n":
        for word in sys.argv[1:]:
            print(word, end=" ")
            print()
        print(me_moo_moos[0].get_image())
