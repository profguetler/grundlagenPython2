# prime-numbers
# Funktion: check if given number is prime

def isPrime(n):
    # logik einbauen
    if (n <= 1):
        return False

    # gibt es eine Divison ohne Rest?
    # dann ist es keine Primzahl
    for p in range(2,n):
        if (n % p == 0):
            return False

    return True

print("Primzahlen-Checker")
z = input("Bitte die Zahl eingeben: ")
z = int(z)
if (isPrime(z)):
    print(z, "ist eine Primzahl")
else:
    print(z, "ist KEINE Primzahl")
