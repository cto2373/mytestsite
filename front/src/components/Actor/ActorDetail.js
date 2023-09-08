import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import API_URL from "../..";
import axios from "axios";
import Movies from '../MovieBanner/Movies';


function ActorDetail() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [actor, setActor] = useState(null);


  useEffect(() => {
    // Fetch actor details using the actor ID from route params
    axios.get(API_URL + `/actor/${id}`)
      .then(response => {
        setActor(response.data);
        console.log(response.data);
      })
      .catch(error => {
        console.error('Error fetching actor details:', error);
      });
    
  }, [id]);

  if (!actor) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      
      <p className=" flex pr-8 bg-slate-900 text-white"> {actor.first_name} {actor.last_name}</p>
      <Movies id={id}/>
    </div>
  );
}

export default ActorDetail;
