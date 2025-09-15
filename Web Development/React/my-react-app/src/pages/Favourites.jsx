import "../css/Favourites.css"
import { useMovieContext } from "../../contexts/MovieContexts"
import MovieCard from "../components/MovieCard"

function Favourites() {
    const {favourites} = useMovieContext

    if (favourites) {
        return (
        <div className="favorites">
            <h2>Your Favourites</h2>
        <div className="movies-grid"> 
            {favourites.map((movie) => (
                <MovieCard movie={movie} key={movie.id}/>
            ))}
        </div>
        </div>
        )
    }
    return (
        <div className="favourites-empty">
            <h2>No Favourite movies yet</h2>
            <p>Start adding favourites to appear here</p>
        </div>
    
    )
}

export default Favourites