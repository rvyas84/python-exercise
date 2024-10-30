forStar = 30
for num in range(100):
    if num < forStar:
        print(f"{num} *")
    elif num in range(30, 61):
        print(f"{num} R")
    elif num in range (61,91):
        print(f"{num} M")
    else:
        print(f"{num} V")

stringData = "Hello Paython!"
i = 0

for charc in stringData:
    print(f'Characters "{charc}" in "{stringData}" is at {i}')
    i += 1