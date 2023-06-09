import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import './App.css';
import Navbar from './Navbar';
import Predictions from './Predictions';
import PlayerInterface from "./PlayerInterface";
import TopPlayers from "./TopPlayers";
import React from "react";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={ <Predictions stat="points"/> } />
          <Route path="/rebounds" element={ <Predictions stat="rebounds"/> } />
          <Route path="/assists" element={ <Predictions stat="assists"/> } />
          <Route path="/probabilities" element={ <PlayerInterface stat="points" /> } />
          <Route path="/topPlayers" element={ <TopPlayers/> } />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
