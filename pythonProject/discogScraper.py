import discogs_client

def getReleases(fileName,dis):
    f = open(fileName,"r")
    lines = f.readlines()
    f.close()
    releases = []
    sub1 = "release/"
    sub2 = "-"
    for line in lines:
        id = ''.join(line.split(sub1)[1].split(sub2)[0])
        releases.append(dis.release(id))
    return releases

def getTracks(releases):
    tracks = ""
    for release in releases:
        tracks += release.tracklist[0].title
        for track in release.tracklist[1:]:
            tracks += ".- " + str(track.title)
        tracks += "\n"
    f = open("titles.txt","w")
    f.write(tracks)
    f.close()



d = discogs_client.Client('my_user_agent/1.0', user_token='oZENLBNZAGdNfSaGNEncACkrSPFrdzZLvCTUGslh')
releases = getReleases("URL.txt",d)
getTracks(releases)
# print(trackList)
