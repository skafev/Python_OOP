class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        photos = photos_count // 4
        return cls(photos)

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return f"No more free spots"

    def display(self):
        result = ""
        for row in self.photos:
            result += f"-----------\n"
            if len(row) > 0:
                result += f"{' '.join(['[]' for el in row])}\n"
            else:
                result += '\n'
        result += f"-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())