# -*-coding:utf8;-*-
# qpy:console

import luckyyou

play = luckyyou.luckyYou()

print("\n\nLuckYou in action... We Wish You GoodLuck!\n")

while True:
    print("\nWhat kind of numbers do you want?")
    print("\t1. Generate Two-Sure lucky numbers")
    print("\t2. Generate Perm-5 lucky numbers")
    print("\t3. Stop generating numbers")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        print("\n\t2-Sure Numbers\n")
        twoSureNums = play.twoSure()
        for i in twoSureNums:
            print("\t", i)

        print("\nGenerate new numbers?")
        print("\t1. Yes\n\t2. No")
        repeat = input("\nEnter your choice: ")
        if repeat == "1":
            pass
        elif repeat == "2":
            play.close()
            break
        else:
            print("Wrong entry")
            pass
    elif choice == "2":
        print("\n\tPerm 5 numbers\n")
        perm5Nums = play.perm5()
        for i in perm5Nums:
            print("\t", i)

        print("\nGenerate new numbers?")
        print("\t1. Yes\n\t2. No")
        repeat = input("\nEnter your choice: ")
        if repeat == "1":
            pass
        elif repeat == "2":
            play.close()
            break
        else:
            print("Wrong entry")
    elif choice == "3":
        play.close()
        break
    else:
        print("Wrong entry")

