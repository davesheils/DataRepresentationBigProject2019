import discogs_client
import wikipedia

d = discogs_client.Client('davesApp/0.1')


release = d.release(6718132)

## trax = release.tracklist
# for track in trax:
#    print(track)

# get album title from discogs
title = release.title + " (Album)"
#  get artist .. bit of parsing required here as artist object is a list
artist = str(release.artists[0]).split("'")[1]
genres =""

for i, g in enumerate(release.genres):
    genres += g
    # i =+1
    if i < len(release.genres):
        g += ", "


summary = wikipedia.page(title).summary

print(title)
print(artist)
print(genres)
print(summary)
# print tracklist
for track in release.tracklist:
    song = str(track)