lorem = (
    "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz "
    "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później "
    "zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w "
    "latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z "
    "zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach "
    "osobistych, jak Aldus PageMaker "
)

first_name = "Oskar"

last_name = "Majewski"

lorem_output = (
    f"W tekście jest {lorem.lower().count(first_name[2].lower())} liter "
    f"{first_name[2].lower()} oraz {lorem.lower().count(last_name[3].lower())} liter {last_name[3].lower()}"
)

print(lorem_output)
