import React, { useEffect, useState } from "react";
import API_URL from "..";
import axios from "axios";


const Form = ({ get_cinema }) => {
  // const [title, setTitle] = useState("");
  // const [starRating, setStarRating] = useState(0);
  // const [rating, setRating] = useState("NR");
  const [genre, setGenre] = useState([]);
  const [formData, setFormData] = useState({
    title: "",
    starRating: 0,
    rating: "R",
    genre: 1, // Updated to a string for the selected genre
    year: "2002-01-01",
    runTime: 1,
    cast: [1],
    iamge: "sdasdas",
  });

  const handleSubmit = (e) => {
    console.log(formData);
    e.preventDefault();
    if (!formData.title.trim()) {
      return;
    }
    
    console.log(JSON.stringify(formData));
    fetch(API_URL + "/movies/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.log(error))
      .finally(get_cinema);
    // setStarRating("");
    // setTitle("");
  };

  const getGenreList = () =>{
    axios
    .get(API_URL + "/genres")
    .then((response) => {
      console.log(response.data);
      setGenre(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };
  useEffect(getGenreList,[])
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          name="title"
          type="text"
          placeholder="Title"
          // autoComplete="off"
          value={formData.title}
          onChange={handleChange}
        />
        <input
          name="starRating"
          type="number"
          placeholder="Rating"
          autoComplete="off"
          value={formData.starRating}
          onChange={handleChange}
        />
         <div>
          <label>Genre:</label>
          <select name="genre" value={formData.genre} onChange={handleChange}>
            <option value="">Select a genre</option>
            {genre &&
          genre.map((genre) => (
            <option value={genre.id}>{genre.name}</option>
          ))}
         
            {/* <option value="1">Action</option> */}
            {/* <option value="2">Comedy</option> */}
            {/* Add more genre options as needed */}
          </select>
        </div>
        <button
          type="submit"
          className="bg-blue-400 text-white border-2 rounded-md px-3 border-blue-800 "
        >
          Добавить
        </button>
      </form>
    </div>
  );
};

export default Form;
