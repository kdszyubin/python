width = input()

item_width = input()
price_width = width - item_width

second = ''
l = []
first = raw_input()
while first != "end":
    second = raw_input()
    l.append([first, second])
    first = raw_input()

header_format = "%-*s%*s"
item_format = "%-*s%*s"
print '=' * width
print '-' * width
for i in l:
    print item_format % (item_width, i[0], price_width, i[1])
print '=' * width
