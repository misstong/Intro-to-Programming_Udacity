import media
import fresh_tomatoes

utopia=media.Movie("utopia","animal love story",
                   "http://player.youku.com/player.php/sid/XMTQzNjc0MjU0OA==/v.swf",
                   "http://g.hiphotos.baidu.com/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=a333d2ae44166d222c7a1dc6274a6292/d439b6003af33a871f98557fc15c10385243b5da.jpg")
#utopia.show_trailer()

lion_king=media.Movie("Lion King","revenge",
                      "http://player.youku.com/player.php/sid/XMjMyMzkxODU2/v.swf",
                      "http://e.hiphotos.baidu.com/baike/c0%3Dbaike72%2C5%2C5%2C72%2C24/sign=537a9959c8fcc3cea0cdc161f32cbded/503d269759ee3d6d419192b043166d224f4ade71.jpg")

fight_club=media.Movie("Fight Club","fight",
                       "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                       "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTxAuj-TdaJsAS_i5c2ZVKwcJk4C1gAlOhoboZ9TsPX6sfmDtPk")

movies=[utopia,lion_king,fight_club]
fresh_tomatoes.open_movies_page(movies)
