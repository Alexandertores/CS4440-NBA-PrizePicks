import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import './App.css';
import Navbar from './Navbar';
import Predictions from './Predictions';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={ <Predictions stat="points"/> } />
          <Route path="/rebounds" element={ <Predictions stat="rebounds"/> } />
          <Route path="/assists" element={ <Predictions stat="assists"/> } />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
