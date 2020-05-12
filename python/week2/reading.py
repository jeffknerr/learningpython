"""
reading log -- show use of for loop

J. Knerr
Spring 2020
"""

def main():
    pages = int(input(" pages to read? "))
    days  = int(input("days until due? "))
    print()   # a blank line

    total = 0
    for i in range(1,days+1):
        read = int(input("Pages for day %d: " % (i)))
        total = total + read
        print("You've read %d out of %d pages..." % (total, pages))
        left = pages - total
        print("\n** You've got %d pages left and %d days to go." % (left, days-i))
        if days-i > 0:
            avg = left/(days-i)
            print("** I suggest %d pages per day...\n" % (avg))

main()
