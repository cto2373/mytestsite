import React, { useEffect, useState } from "react";
import MovieList from "./components/MovieBanner/MovieList";
import ActorDetail from "./components/Actor/ActorDetail";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Header from "./components/Header";
import MovieDetail from "./components/MovieDeteil/MovieDetail";


export default function App() {
  return (

      <Router>
        <Header>
        Home
        </Header>
        <Routes>
          <Route path="/actor/:id" element={<ActorDetail />} />
          <Route path="/movie/:id" element={<MovieDetail />} />
          
          <Route path="/" element={<MovieList  />}/>
        </Routes>
      </Router> 
  );
}

//             <p key={volute.rate_float}>
//               {volute.description}{": "}
//               <span dangerouslySetInnerHTML={{ __html: volute.symbol }}></span>{" "}
//               {volute.code} {volute.rate_float.toFixed(2)}{" "}
//             </p>
//           ))

// const [movies, setData] = useState([]);
// useEffect(() => get_cinema(), []);

// const get_cinema = () => {
//   axios
//     .get(API_URL + "pizza")
//     .then((response) => {
//       setData(response.data);
//     })
//     .catch((error) => {
//       console.log(error);
//     });
// };

// console.log(movies);
