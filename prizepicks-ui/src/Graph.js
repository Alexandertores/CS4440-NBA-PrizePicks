import React, { useRef, useEffect } from 'react';
import { Chart } from 'chart.js/auto';


function Graph(props) {

  const chartRef = useRef(null);
  const previousChartRef = useRef(null);

  console.log("PROPS1" + JSON.stringify(props.data))
  useEffect(() => {
    if (props.data) {
      if (previousChartRef.current) {
        previousChartRef.current.destroy();
      }
      const ctx = chartRef.current.getContext("2d");

      var labels = []
      var points = []
      var input = JSON.parse(JSON.stringify(props.data))
      var zero = []
      input.forEach(element => {
        labels.push(element.x);
        points.push(element.y);
        if (props.overunder) {
          zero.push(0)
        }
        
      });
      var newChartInstance
      if (props.overunder) {
        newChartInstance = new Chart(ctx, {
          type: "line",
          data: {
            labels: labels,
            datasets: [
              {
                data: points,
                label: props.label || ''
              },
              {
                data: zero,
                label: props.label || ''
              }
            ]
          }
        });
      } else {
        newChartInstance = new Chart(ctx, {
          type: "line",
          data: {
            labels: labels,
            datasets: [
              {
                data: points,
                label: props.label || ''
              }
            ]
          }
        });
      }
      
      previousChartRef.current = newChartInstance;
      return () => {
        newChartInstance.destroy();
      };
    }
  }, [props.data, props.canvas_id]);

  return <canvas id={props.canvas_id} ref={chartRef}/>
}
  
export default Graph;