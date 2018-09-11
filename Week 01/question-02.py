"""""
Write a function that prints the song "99 bottles of beer on the wall". The formatting, paragraphing and punctuation
should be same as the lyrics in the link below. Use as many loops as possible. The question will be marked according to
the number of lines used for the solution. Less lines of code, more points.
"""""

def song_lyrics():
    for bottles in range(99, 2, -1):
        print("%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottles of beer on the wall.\n\n" % (bottles, bottles, bottles - 1))
    print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n\n")
    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\n")
    print("No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.\n")

song_lyrics()