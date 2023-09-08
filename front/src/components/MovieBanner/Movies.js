import { useEffect, useState } from "react";
import Nav from "./Nav.js";
import NavItem from "./NavItem.js";
import List from "./List.js";
import { FilterButton } from "./FilterButton.js";
import ListItem from "./ListItem.js";
import axios from "axios";
import API_URL from "../..";


export default function Movies({id}) {
  const [searchText, setSearchText] = useState("");
  const [movies, setMovies] = useState([]);
  const [filter, setFilter] = useState("All");
  const [genre, setGenre] = useState([]);
  const [sort, setSort] = useState("-year");
  let genreList = ["All"];

  function get_movies ()  {
    axios
      .get(API_URL + "/movies", {
        params: {
          genre: filter,
          sort:  sort,
          cast_id: id,
        },
      })
      .then((response) => {
        setMovies(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  
  genre.map((genre) => genreList.push(genre.name));
  
  const getGenreList = () =>{
    axios
    .get(API_URL + "/genres",{
      params:{
        actor_id:id,
      }
    })
    .then((response) => {
      console.log(response.data);
      setGenre(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
  };
  
  useEffect(get_movies, [filter, sort, id]);
  useEffect(getGenreList, [id]);
  
  return (
    <div className="divide-y divide-black">
      <input
        placeholder="Search"
        className="outline-none pl-1 rounded mx-6"
        type="text"
        onChange={(e) => setSearchText(e.target.value)}
      />
      <Nav>
        {genreList &&
          genreList.map((name) => (
            <FilterButton
              key={name}
              name={name}
              isPressed={name === filter}
              setFilter={setFilter}
            />
          ))}
         
      </Nav>
      <List>
        {movies && movies.map((movie) => {
          if (
            movie.title
              .toLowerCase()
              .indexOf(searchText.trim().toLowerCase()) === -1
          ) {
            return;
          }
          return <ListItem key={movie.id} movie={movie} />;
        })}
      </List>

    </div>
  );
};
