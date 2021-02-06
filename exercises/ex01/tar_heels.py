"""An exercise in remainders and boolean logic."""

__author__ = "720332576"


# Begin your solution here...

print("please input an integer")
y = input()
z = int(y)

a = z % 2
b = z % 7

if a == 0 and b == 0:
    print("TAR HEELS")
else:
    if a == 0:
        print("TAR")
    else:
        if b == 0:
            print("HEELS")
        else:
            print("CAROLINA")