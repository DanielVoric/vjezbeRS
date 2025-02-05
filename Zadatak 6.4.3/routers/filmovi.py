
from fastapi import APIRouter, HTTPException, Query
from typing import List, Literal, Optional
import json
from pathlib import Path

from models.film import Film

router = APIRouter()

#Iskreno, bo
DATA_FILE = Path(__file__).parent.parent / "lista_filmova.json"
with open(DATA_FILE, "r", encoding="utf-8") as f:
    films_data = json.load(f)
filmovi: List[Film] = [Film(**film) for film in films_data]








@router.get("/films", response_model=List[Film])
async def get_films(
    min_year: Optional[int] = Query(None,ge=1900,description="Min godina, veća od 1900."
    ),
    max_year: Optional[int] = Query(None,ge=1900,description="Max god, veća od 1900."
    ),
    min_rating: Optional[float] = Query(None,ge=0,le=10,description="Min rating."
    ),
    max_rating: Optional[float] = Query(None,ge=0,le=10,description="Max rating."
    ),
    film_type: Optional[Literal["movie", "series"]] = Query(None,description="Tip mora bit movie ili series."
    )
):
    filtered_films = filmovi

    if min_year is not None:
        filtered_films = [
            film for film in filtered_films
            if int(film.Year) >= min_year
        ]
    if max_year is not None:
        filtered_films = [
            film for film in filtered_films
            if int(film.Year) <= max_year
        ]
    



    if min_rating is not None:
        filtered_films = [
            film for film in filtered_films
            if film.imdbRating != "N/A" and float(film.imdbRating) >= min_rating
        ]
    if max_rating is not None:
        filtered_films = [
            film for film in filtered_films
            if film.imdbRating != "N/A" and float(film.imdbRating) <= max_rating
        ]
    




    if film_type is not None:
        filtered_films = [
            film for film in filtered_films
            if film.Type == film_type
        ]

    return filtered_films



@router.get("/{imdb_id}", response_model=Film)
async def dohvati_film_ID(imdb_id: str):
    for film in filmovi:
        if film.imdbID == imdb_id:
            return film
    raise HTTPException(status_code=404, detail="Film s tim id-em ne postoji")

@router.get("/title/{title}", response_model=Film)
async def dohvati_film_naslov(title: str):

    for film in filmovi:
        if film.Title.lower() == title.lower():
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")