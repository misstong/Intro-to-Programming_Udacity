import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,
                 trailer_youtube,poster_image):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        print("parent called")

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

