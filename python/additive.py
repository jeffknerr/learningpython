"""
write additive program
J. Knerr
Spring 2024

12122436 could be 12+12=24, 12+24=36

break into segments, no segment starts with 0,
must be at least 3 segments in number, segment can
be any number of digits, and each two segments must
add to the next segment
"""


def main():
    start = 5000
    end = 15560
    for i in range(start, end):
        if isadd(i):
            print(i, "IS ADDITIVE!!")
    assert(isadd(15520) is True)
    assert(isadd(121224) is True)

    assert(isadd(5793150) is True)
    assert(isadd(12090210) is True)


def isadd(n):
    """helper function to set up the recursion"""
    nstr = str(n)
    length = len(nstr)
    ndigits = length - 2   # number of digits to make 3 numbers
    ipos = length - 1      # everything to right of this already good
    # ex: 11235813
    # length = 8
    # ndigits = 6  (235813), so 3 numbers are 1 1 235813
    # ipos = 7 (just starting)
    # once we find out that 5 + 8 = 13, adjust and recur:
    # recadd(nstr, 4, 5)
    # so 3 numbers now are 1 1 2358
    # and ipos = 5 (digits in positions 6 and 7 are already done/good)
    return recadd(nstr, ndigits, ipos)


def recadd(nstr, ndigits, ipos):
    """recursive function to return True if number is additive"""
    # ex: subs="18", nstr="9918", return True  9+9=18
    # ex: subs="28", nstr="9928", return False 9+9!=28
    # ex: subs="24", nstr="121224", return True  12+12=24
    # ex: subs="5", nstr="11235", return True  1+1=2, 1+2=3, 2+3=5
    # base case...when to quit
    if ndigits == 0:
        return False
    # handle 3-number case first
    if ndigits+2 == len(nstr):
        a = nstr[0]
        b = nstr[1]
        c = nstr[2:]
        # check for illegal substrings...
        if a == "0" or b == "0" or c[0] == "0":
            return recadd(nstr, ndigits-1, ipos)
        # now see if they add up...
        if (int(nstr[0])+int(nstr[1]) == int(nstr[2:])):
            return True
        else:
            # keep going, but try smaller initial substring
            return recadd(nstr, ndigits-1, ipos)
    else:
        # try all possible 2 numbers from up to 2*ndigits back
        # ex: if string is abcdefghijklm, and ndigits is 4 (so jklm)
        # then we want to look at all combinations of
        # 8 digits back bcdefghi
        # 7 digits back cdefghi
        # 6 digits back cdefghi
        # and so on
        # can probably stop at some point, but let's do all for now
        start = ipos + 1 - ndigits
        end = ipos + 1
        substr = nstr[start:end]
        back = ndigits * 2
        if ndigits + back > len(nstr):
            back = len(nstr) - ndigits
        for i in range(back, 1, -1):
            consider = nstr[start-back:start]
            for j in range(back-1):
                a = consider[0:j+1]
                b = consider[j+1:]
                if strsum(a, b, substr):
                    if len(a) + len(b) + len(substr) == len(nstr):
                        # we are done!!!
                        return True
                    # move over and recur
                    ipos = ipos - ndigits
                    newend = len(nstr) - ndigits
                    newstr = nstr[:newend]
                    ndigits = back - j - 1
                    return recadd(newstr, ndigits, ipos)
        return recadd(nstr, ndigits-1, ipos)


def strsum(a, b, c):
    """given 3 string ints, return True if they add up"""
    return int(a) + int(b) == int(c)


main()
