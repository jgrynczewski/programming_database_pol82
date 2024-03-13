# fluent interface (płynny interfejs)
class HouseBuilder:
    def __init__(self, name):
        self.name = name

    def build_walls(self):
        print("Stawiam ściany")
        return self

    def mount_windows(self):
        print("Montuje okna")
        return self

    def mount_doors(self):
        print("Montuje drzwii")
        return self


b = HouseBuilder("Bob")
# fluent interface
b.build_walls().mount_windows().mount_doors()

# Lub tak
# HouseBuilder("Bob").\
#     build_walls().\
#     mount_windows().\
#     mount_doors()
