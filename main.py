# This is a sample Python script.
from BST import BST
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    myBST = BST()
    print(myBST)
    myBST.add("middle")
    myBST.add("left")
    myBST.add("right")

    print(myBST)
    myBST.root.print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
