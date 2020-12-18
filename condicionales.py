x = 3

while True:
    if x == 3:
        print("one time")
        break
    else:
        print("Sorry is not Equal")
        break

while x < 5:
    print(x, "inside the loop")
    x = x + 1

y = 6
while y < 5:
    print(y, "inside the loop again")
    break

my_list = [1, 2, 3, 4]

while len(my_list) > 3:
    if len(my_list) >= 5:
        print("Length: ", len(my_list))
        break
    else:
        print("List Length is not complete the requirement.")



