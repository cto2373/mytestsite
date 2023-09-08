import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import API_URL from "../..";
import axios from "axios";

function MovieDetail() {
  const [movie, setMovie] = useState(null);
  const navigate = useNavigate();
  const { id } = useParams();

  function handleDelete(){
    axios
      .delete(API_URL + `/movie/${id}`)
      .then((response) => {
        console.log("Movie deleted:", response.data);
      })
      .catch((error) => {
        console.error("Error deleting movie:", error);
      });
      
  };

  useEffect(() => {
    axios
      .get(API_URL + `/movie/${id}`)
      .then((response) => {
        setMovie(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error("Error fetching movie details:", error);
      });
  }, [id]);

  if (!movie) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div className="bg-white flex my-8 justify-stretch mx-24 p-4">
        <div>
          <img
            src={movie.image}
            alt=""
            width="300"
            height="440"
            className="flex-none rounded-md  bg-slate-100"
          />
        </div>
        <h1 className="font-bold px-4 text-4xl">
          {movie.title} ({movie.year.slice(0, 4)})
        </h1>
      </div>
      <div>
        {/* Movie details */}
        <button onClick={handleDelete}>Delete Movie</button>
      </div>
    </div>
  );
}

export default MovieDetail;
