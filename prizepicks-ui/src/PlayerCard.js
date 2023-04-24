import React from "react";


function PlayerCard(props) {

  return (
    <div>
      <div class="card mb-3" style={{maxWidth : '540px'}}>
        <div class="row g-0">
          <div class="col-md-4">
            <img src={props.data.image} class="img-fluid rounded-start" alt="..." />
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{props.data.data.name}</h5>
              <p class="card-text">Line: {props.data.line}</p>
              <p class="card-text">Prediction: {props.data.line}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
  
export default PlayerCard;