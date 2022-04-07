# Create a left rotation and a right rotation function that returns all the left rotations and right rotations of a string.
# leftRotations("abc") ➞ ["abc", "bca", "cab"]
# rightRotations("abc") ➞ ["abc", "cab", "bca"]


def leftRot(s1):
    b = []
    c = ""
    d = []
    e = []

    for i in range(len(s1)):
        b.append(s1[i])

    for j in range(len(b)):
        for k in range(len(b)):
            c += b[k]
        
        e.append(c)
        d = b[0]
        b.remove(b[0])
        b.append(d)
        c = ""

    print(f'left rotations = {e}')


def rightRot(s1):
    b = []
    c = ""
    d = []
    e = []

    for i in reversed(range(len(s1))):
        b.append(s1[i])

    for j in reversed(range(len(s1))):
        for k in reversed(range(len(s1))):
            c += b[k]
        
        e.append(c)
        d = b[0]
        b.remove(b[0])
        b.append(d)
        c = ""

    print(f'Right rotations = {e}')

leftRot('abcd')
rightRot('wxyz')