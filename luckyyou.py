3  # -*-coding:utf8;-*-
# qpy:console

# This program generate lotto numbers

from random import randint as rt


class luckyYou:
    def __init__(self):
        pass

    # 2-Sure method
    def twoSure(self):
        nums = set()
        numSet = list()
        while True:
            while len(nums) < 2:
                nums.add(rt(1, 90))
            if len(nums) == 2:
                numSet.append(nums)
                nums = set()
            if len(numSet) == 10:
                return numSet

    # Perm5 method
    def perm5(self):
        digits = set()
        digitSet = list()
        while True:
            while len(digits) < 5:
                digits.add(rt(1, 90))
            if len(digits) < 10:
                digitSet.append(digits)
                digits = set()
            if len(digitSet) == 10:
                return digitSet

    # Closing message
    def close(self):
        print("\nThank you for coming around!")
        print("\nSee you next time.")
        print("\nExiting...\n\n")




















