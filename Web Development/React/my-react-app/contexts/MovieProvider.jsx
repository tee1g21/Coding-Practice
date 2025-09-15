import { useState, useEffect } from "react";
import MovieContext from "./MovieContext";

const MovieProvider = ({ children }) => {
  const [favourites, setFavourites] = useState([]);

  useEffect(() => {
    try {
      const storedFavs = localStorage.getItem("favourites");
      if (storedFavs) setFavourites(JSON.parse(storedFavs));
    } catch {
      // ignore storage errors
    }
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem("favourites", JSON.stringify(favourites));
    } catch {
      // ignore storage errors
    }
  }, [favourites]);

  const addToFavourites = (movie) => {
    setFavourites((prev) => [...prev, movie]);
  };

  const removeFromFavourites = (movieId) => {
    setFavourites((prev) => prev.filter((movie) => movie.id !== movieId));
  };

  const isFavourite = (movieId) => favourites.some((movie) => movie.id === movieId);

  const value = { favourites, addToFavourites, removeFromFavourites, isFavourite };

  return (
    <MovieContext.Provider value={value}>{children}</MovieContext.Provider>
  );
};

export default MovieProvider;
