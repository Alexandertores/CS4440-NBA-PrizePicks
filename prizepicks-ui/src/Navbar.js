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
                  <a class="nav-link active" aria-current="page" href="#">Points</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Rebounds</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Assists</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    );
  }
  
  export default Navbar;