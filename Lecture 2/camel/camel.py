camel_case = input("camelCase: ")
snake_case = ""

if camel_case.islower():
    print("snake_case: " + camel_case)
else:
    for i in camel_case:
        if i.isupper():
            i = "_" + i.lower()
            snake_case += i
        else:
            snake_case += i
    print(snake_case)
