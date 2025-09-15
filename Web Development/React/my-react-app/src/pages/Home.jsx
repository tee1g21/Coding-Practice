import MovieCard from "../components/MovieCard"
import { useState, useEffect } from "react"
import "../css/Home.css"
import {getPopularMovies, searchMovies} from "../services/api";

function Home() {
    const [searchQuery, setSearchQuery] = useState("");
    const [movies, setMovies] = useState([]);
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const loadPopularMovies = async () => {
            try { 
                const popularMovies = await getPopularMovies()
                setMovies(popularMovies)
            } catch (err) {
                console.log(err)
                setError("Failed to load movies...")
            } 
            finally {
                setLoading(false)
            }
        }

        loadPopularMovies()
    }, [])

    
    const handleSearch = async (e) => {
        e.preventDefault();
        console.log("Form submitted with query:", searchQuery);

        if (!searchQuery.trim()) {
            console.log("Empty query, returning early");
            return;
        }
        if (loading) {
            console.log("Still loading, skipping");
            return;
        }

        setLoading(true);
        try {
            const searchResults = await searchMovies(searchQuery);
            console.log("API raw results:", searchResults);

            setMovies(searchResults);
            setError(null)
            console.log("Movies state updated!");
            
        } catch (err) {
            console.error("Search failed:", err);
            setError("Failed to search movies...");
        } finally {
            setLoading(false);
        }
    };

    return <div className="home">
        <form onSubmit={handleSearch} className="search-form">
            <input 
                type="text" 
                placeholder="Search for movies..." 
                className="search-input"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
            />
            <button type="submit" className="search-button">Search</button>
        </form>

        {error && <div className="error-message">{error}</div>}

        {loading ? (
         <div className="loading">Loading...</div>
        ) : ( 
        <div className="movies-grid"> 
            {movies.map((movie) => (
                <MovieCard movie={movie} key={movie.id}/>
            ))}
        </div>) }        
    </div>
}

export default Home