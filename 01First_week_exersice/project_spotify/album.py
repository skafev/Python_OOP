from project_spotify.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [song for song in songs]
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        filtered_songs = [x for x in self.songs if x == song]
        if filtered_songs:
            return "Song is already in the album."
        elif not filtered_songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        filtered_songs = [x for x in self.songs if x.name == song_name]
        if not filtered_songs:
            return "Song is not in the album."
        song_to_remove = filtered_songs[0]
        self.songs.remove(song_to_remove)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        res = f"Album {self.name}\n"
        for s in self.songs:
            res += f"== {s.get_info()}\n"
        return res


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())