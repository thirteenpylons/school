"""
Define the Artist class with a constructor to initialize an artist's 
information and a print_info() method. The constructor should by default 
initialize the artist's name to "None" and the years of birth and death 
to 0. print_info() should display Artist Name, born XXXX if the year of 
death is -1 or Artist Name (XXXX-YYYY) otherwise.

Define the Artwork class with a constructor to initialize an artwork's 
information and a print_info() method. The constructor should by default 
initialize the title to "None", the year created to 0, and the artist 
to use the Artist default constructor parameter values.

Ex: If the input is:

Pablo Picasso
1881
1973
Three Musicians
1921
the output is:

Artist: Pablo Picasso (1881-1973)
Title: Three Musicians, 1921
If the input is:

Brice Marden
1938
-1
Distant Muses 
2000
the output is:

Artist: Brice Marden, born 1938
Title: Distant Muses, 2000
"""


class Artist:
    def __init__(self, name: str="None", birth_year: int=0, death_year: int=0):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
    
    def print_info(self) -> None:
        if self.death_year == -1:
            print(f"Artist: {self.name}, born {self.birth_year}")
        else:
            print(f"Artist: {self.name} ({self.birth_year}-{self.death_year})")

      
class Artwork:
    def __init__(self, title: str="None", year_created: int=0, artist: Artist = Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist
    
    def print_info(self) -> None:
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()
