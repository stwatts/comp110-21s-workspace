def main() -> None:
    b: list[str] = a
    f(a)
    g()
    print(b[0])

def f(a: list[str]) -> None:
    a[0] = "w"
    a = ["K", "j"]

def g() -> None:
    global a
    a[1] = "m"
    a = ["y", "p"]

    
a = ["u", "g"]

main()
