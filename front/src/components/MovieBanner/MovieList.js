import React, { useEffect, useState } from "react";
import axios from "axios";
import Movies from "./Movies";
import Header from "../Header";
import Nav from "./Nav";
import NavItem from "./NavItem";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import API_URL from "../..";
import Form from "../Form";

export default function MovieList () {
  
  return(
    <>
    
      <Movies/>
      <Form/>
     </>
  )
}