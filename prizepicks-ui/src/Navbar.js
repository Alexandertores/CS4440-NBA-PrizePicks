import { Link } from "react-router-dom";

function Navbar() {
    return (
      <div className="App">
        <nav class="navbar navbar-expand-lg bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">PrizePicks Optimizer</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <Link class="nav-link active" aria-current="page" href="#" to="/">Points</Link>
                </li>
                <li class="nav-item">
                    <Link class="nav-link" to="rebounds">Rebounds</Link>
                </li>
                <li class="nav-item">
                    <Link class="nav-link" to="assists">Assists</Link>
                </li>
                <li class="nav-item">
                    <Link class="nav-link" to="topPlayers">Top Players</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    );
  }
  
  export default Navbar;