print("\t\t\tArea calculator\n\n")

# a, b = input("Enter Length and With of the room: ").split() # this is multi input input type str
a, b = map(float, input("Enter Length and Width of the room in meter: ").split()) # multi input type selectable
# print(type(a))
# print(type(b))
area = float(a) * float(b)

print("\t\t\tArea of room: {}meters or {}feets ".format(area, area*3.28084))





