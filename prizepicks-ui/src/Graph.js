import React from "react";
import { Line } from "react-chartjs-2";

function Graph(props) {
    return <Line data={props.data}></Line>
}
  
export default Graph;