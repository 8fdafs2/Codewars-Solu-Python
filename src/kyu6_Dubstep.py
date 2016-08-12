class Solution():
    def __init__(self):
        self.song_decoder = self.song_decoder_01

    def song_decoder_01(self, song):
        return ' '.join(song.replace('WUB', ' ').split())

    def song_decoder_02(self, song):
        return ' '.join([_f for _f in song.split('WUB') if _f])

    def song_decoder_03(self, song):
        return ' '.join([word for word in song.split('WUB') if word])
