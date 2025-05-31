# lib/main.py

from song import Song

song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")

print(Song.count)          # => 2
print(Song.genres)         # => ["Rap", "Pop"]
print(Song.artist_count)   # => {"Jay-Z": 1, "Beyonce": 1}
