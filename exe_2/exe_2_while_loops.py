numb = 2
multiple = 1
while numb < 13:
    print("   [", numb, "]")
    while multiple < 13:
        print(numb, " * ", multiple, " = ", numb * multiple)
        multiple = multiple + 1
    print("----------------")
    print()
    numb = numb + 1
    multiple = 1