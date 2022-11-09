# $Id: app.py,v 1.1 2022/11/09 18:17:12 heiko Exp $
#
# $Log: app.py,v $
# Revision 1.1  2022/11/09 18:17:12  heiko
# Initial revision
#

phrase = "Giraffe Academy"
print(len(phrase))    # 15

print(phrase[0])      # G
print(phrase[3])      # a

print(phrase.index("G"))    # 0
print(phrase.index("a"))    # 3

print(phrase.index("Acad")) # 8

print(phrase.replace("Giraffe", "Elephant"))
