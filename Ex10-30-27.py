# Exercise 10.30.27

# Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
# test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
#
# s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
# test(replace(s, 'om', 'am'),
#       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')
#
# test(replace(s, 'o', 'a'),
#       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')


def replace(s, old, new):
    lst = s.split(" ")
    newstr = []
    for n in lst:
        ind = 0
        newn = []
        while ind < len(n):
            if n[ind:(ind+len(old))] == old:
                newn += new
                ind += len(old)
            else:
                newn += n[ind]
                ind += 1
        newstr.append(newn)
    return " ".join(["".join(n) for n in newstr])

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print(replace(s, 'om', 'am'))
