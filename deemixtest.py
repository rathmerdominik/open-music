from deemix.utils import deezer as deezer_login, formatListener
from deemix import downloader
import deemix
import deezer


class LogListener:
    @classmethod
    def send(cls, key, value=None):
        logString = formatListener(key, value)
        if logString:
            print(logString)


acc_token = deezer_login.getAccessToken("xxx", "xxxx")
arl = deezer_login.getArlFromAccessToken(acc_token)
deezer_client = deezer.Deezer()
print(arl)
if deezer_client.login_via_arl(arl):
    deezer_api = deezer.API(
        deezer_client.session,
        {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/79.0.3945.130 Safari/537.36"
        },
    )
    track = deezer_api.search_track("its late")
    track = track["data"][0]
    print(track["link"])
    download_object = deemix.generateDownloadObject(
        deezer_client, "https://www.deezer.com/en/track/478233122", 1
    )
    downloader.Downloader(
        deezer_client,
        download_object,
        {
            "downloadLocation": "/home/xxxx/Music/",
            "tracknameTemplate": "%artist% - %title%",
            "albumTracknameTemplate": "%tracknumber% - %title%",
            "playlistTracknameTemplate": "%position% - %artist% - %title%",
            "createPlaylistFolder": True,
            "playlistNameTemplate": "%playlist%",
            "createArtistFolder": False,
            "artistNameTemplate": "%artist%",
            "createAlbumFolder": True,
            "albumNameTemplate": "%artist% - %album%",
            "createCDFolder": True,
            "createStructurePlaylist": False,
            "createSingleFolder": False,
            "padTracks": True,
            "paddingSize": "0",
            "illegalCharacterReplacer": "_",
            "queueConcurrency": 3,
            "maxBitrate": 1,
            "feelingLucky": False,
            "fallbackBitrate": False,
            "fallbackSearch": False,
            "fallbackISRC": False,
            "logErrors": True,
            "logSearched": False,
            "overwriteFile": "n",
            "createM3U8File": False,
            "playlistFilenameTemplate": "playlist",
            "syncedLyrics": False,
            "embeddedArtworkSize": 800,
            "embeddedArtworkPNG": False,
            "localArtworkSize": 1400,
            "localArtworkFormat": "jpg",
            "saveArtwork": True,
            "coverImageTemplate": "cover",
            "saveArtworkArtist": False,
            "artistImageTemplate": "folder",
            "jpegImageQuality": 90,
            "dateFormat": "Y-M-D",
            "albumVariousArtists": True,
            "removeAlbumVersion": False,
            "removeDuplicateArtists": True,
            "featuredToTitle": "0",
            "titleCasing": "nothing",
            "artistCasing": "nothing",
            "executeCommand": "",
            "tags": {
                "title": True,
                "artist": True,
                "artists": True,
                "album": True,
                "cover": True,
                "trackNumber": True,
                "trackTotal": False,
                "discNumber": True,
                "discTotal": False,
                "albumArtist": True,
                "genre": True,
                "year": True,
                "date": True,
                "explicit": False,
                "isrc": True,
                "length": True,
                "barcode": True,
                "bpm": True,
                "replayGain": False,
                "label": True,
                "lyrics": False,
                "syncedLyrics": False,
                "copyright": False,
                "composer": False,
                "involvedPeople": False,
                "source": False,
                "rating": False,
                "savePlaylistAsCompilation": False,
                "useNullSeparator": False,
                "saveID3v1": True,
                "multiArtistSeparator": "default",
                "singleAlbumArtist": False,
                "coverDescriptionUTF8": False,
            },
        },
        LogListener(),
    ).start()

else:
    print("succ")
