# variable
a = 10
b = 20
summe = a + b
print("Summe von", a, "+", b, "=", summe)

aktion = input("Welche Aktion willst du? (+/-/*/:)")
print("Aktion", aktion, "wird ausgeführt...")

if (aktion == "*"):
    print("Multiplikation ausgewählt.")

zahl = input("Welche Zahl wählst du?")
zahl = int(zahl)

zahl2 = int("23")

zahlA = "123"
zahlB = "456"
print(zahlA+zahlB)
# Ausgabe: 123456, weil es sich hier um einen STRING handelt!

zahlC = 987
text = str(zahlC)
