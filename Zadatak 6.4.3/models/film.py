from typing import List, Literal, Optional
from pydantic import BaseModel, Field

class Film(BaseModel):

    #Obavezni
    Title: str
    Year: str
    Rated: str
    Runtime: str
    Genre: str
    Language: str
    Country: str
    Actors: str
    Plot: str
    Writer: str

    Images: List[str] = []
    Type: Literal["movie", "series"]
    imdbID: str

    Director: Optional[str] = ""
    Released: Optional[str] = ""
    Awards: Optional[str] = ""
    Poster: Optional[str] = ""
    Metascore: Optional[str] = ""
    imdbRating: str 
    imdbVotes: str
    Response: Optional[str] = "True"
    totalSeasons: Optional[str] = None
    ComingSoon: Optional[bool] = False




