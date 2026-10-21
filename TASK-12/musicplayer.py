class MusicPlayer:
    def play(self):
        print("Playing music")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")


m = MusicPlayer()
m.play()

s = Spotify()
s.play()