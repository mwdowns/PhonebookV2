import pg

db = pg.DB(dbname = 'music_db')

# query = db.query('select artist.name, album.name from artist, album, featured where album_id = album.id and artist_id = artist.id group by artist.name, album.name;')
# print query

# db.insert('song', name='Highway 61 Revisited')
# db.insert('track', track_number=5)

# query = db.query("select song.name as song, track.track_number as track, album.name as album from song, track, album where track.song_id = song.id and track.album_id = album.id and album.name = 'Highway 61 Revisited' order by track.track_number desc")
# print query
# result_list = query.namedresult()
# for result in result_list:
#     print "Track %d on %s is %s." % (result.track, result.album, result.song)

db.delete('song', {'id': 65})
# db.delete('track', {'id': 65})
