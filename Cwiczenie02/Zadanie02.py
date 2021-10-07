data = "To jest tekst hej"


def fuuuun(data):
    dict1 = {
        "lenght": len(data),
        "letters": list(data),
        "big_letters": data.upper(),
        "small_letters": data.lower(),
    }
    return dict1


print(fuuuun(data))
