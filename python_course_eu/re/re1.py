import re

# s = "Regular expressions easily explained!"
# "easily" in s

# def isREmatched(t):
#     if t:
#         print("matched and its return value is:", t)
#     else:
#         print("did not match and its return value is:", t)

# str = "A cat and a rat can't be friends."

# x = re.search("cat",str)
# isREmatched(x)

# x = re.search("go", str)
# isREmatched(x)

# x = re.search(r" .at ",str)
# x

# x = re.search(r"[-a-z]",str)
# x


# from urllib.request import urlopen
# with urlopen('https://www.python-course.eu/simpsons_phone_book.txt') as fh:
#     for line in fh:
#         # line is a byte string so we transform it to utf-8:
#         line = line.decode('utf-8').rstrip() 
#         if re.search(r"J.*Neu",line):
#             print(line)


s1 = "Mayer is a very common Name"

s2 = "He is called Meyer but he isn't German."
print(re.search(r"^M[ae][iy]er",s1))

s = s1 + s2
print(re.search(r"^M[ae][iy]er",s))

