import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import './App.css';
import Navbar from './Navbar';
import Predictions from './Predictions';
import Probabilities from "./Probabilities";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={ <Predictions stat="points"/> } />
          <Route path="/rebounds" element={ <Predictions stat="rebounds"/> } />
          <Route path="/assists" element={ <Predictions stat="assists"/> } />
          <Route path="/probabilities" element={ <Probabilities startDate="2023-03-01" endDate="2023-03-28"/> } />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
