a = "hellooooooooooo"

if ((length := len(a)) > 10):
    print(f"too long: {length} elements")


while (n := len(a)) > 1:
    print(a)
    a = a[:-1]