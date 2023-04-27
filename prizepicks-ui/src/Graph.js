import React from 'react';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';





function Graph(props) {

    var labels = []
    var points = []
    var input = JSON.parse(JSON.stringify(props.data))
    input.forEach(element => {
        labels.push(element.x);
        points.push(element.y);
    });
    const data = {
        labels: labels,
        datasets: [
          {
            data: points,
          }
        ]
      };


    console.log("PROPS1" + JSON.stringify(props.data))
    if (props.data != null) {
        return <Line data={data}></Line>
    }
    
}
  
export default Graph;