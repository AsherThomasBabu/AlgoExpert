# You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible IP addresses that can be
# created by inserting threes in the string. sequence of four positive
# An IP address is a
# 0255
# Inclusive.
# integers that are separated by s, where each individual integer is within the range
# An IP address isn't valid If any of the individual integers contains leading s. For example, "192.168.0.1" is a valid IP address, but "192.168.06.1" and "192.168.0.01" aren't, because they contain "e" and 01 respectively. Another example of a valid IP
# address is 99.1.1.10" conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.
# Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can be created from the string, your function should return an empty list.
# Note: check out our Systems Design Fundamentals on SystemsExpert to learn more about IP addresses!


# https://leetcode.com/problems/restore-ip-addresses/discuss/31211/Adding-a-python-solution-also-requesting-for-improvement

# The Input is always fixed, so no matter what number of nested loops, it will always run in constant time :)

def validIPAddresses(string):
    IPAddressesFound = []

    for i in [1, 2, 3]:
        for j in [i+1, i+2, i+3]:
            for k in [j+1, j+2, j+3]:
                if k >= len(string):
                    continue
                s1 = string[:i]
                s2 = string[i:j]
                s3 = string[j:k]
                s4 = string[k:]

                tempList = [s1, s2, s3, s4]
                if isValidString(tempList):
                    IPAddressesFound.append(".".join(tempList))

    return IPAddressesFound


def isValidString(list):
    for i in list:
        if i[0] == "0" and i != "0":
            return False
        if int(i) > 255:
            return False
    return True
