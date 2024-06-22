import itertools

prefixes = [
    "032", "033", "034", "035", "036", "037", "038", "039", "086", "096", 
    "097", "098", "070", "076", "077", "078", "079", "089", "090", "093", 
    "081", "082", "083", "084", "085", "088", "091", "094"
]

def generate_phone_numbers():
    for prefix in prefixes:
        for suffix in itertools.product("0123456789", repeat=7): 
            yield prefix + "".join(suffix)

with open("vie-phonenumber_main.txt", "w", newline="\n") as file:
    for phone_number in generate_phone_numbers():
        file.write(phone_number + "\n")
