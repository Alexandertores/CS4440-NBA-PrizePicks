import React from "react";
import axios from "axios";
import Graph from "./Graph";
import { useLocation } from 'react-router-dom';


const probabilities_url = "http://localhost:3001/probabilities";
const over_unders_url = "http://localhost:3001/over_unders";

function PlayerInterface(props) {
    const [startDate, setStartDate] = React.useState("2023-02-23T00:00");
    const [endDate, setEndDate] = React.useState("2023-04-15T00:00");
    const [isLoading, setLoading] = React.useState(true);
    const [probabilities, setProbabilities] = React.useState(null);
    const [over_unders, setOverUnders] = React.useState(null);
    let { state } = useLocation();
    const date = state['date']
    const [probability, setProbability] = React.useState(state['probability'])


    React.useEffect(() => {
    console.log("fetching data");
    console.log(props.stat + " " + props.name + " " + startDate + " " + endDate)
    if (isLoading) {
        axios.get(probabilities_url, {
            params: {
              stat: props.stat,
              name: state["name"],
              startDate: startDate,
              endDate: endDate 
            }
          }).then((response) => {
            setProbabilities(response.data);
          });
        axios.get(over_unders_url, {
            params: {
              stat: props.stat,
              name: state["name"],
              startDate: startDate,
              endDate: endDate 
            }
          }).then((response) => {
            setOverUnders(response.data);
          });
        setLoading(false);
    }
  }, [isLoading, probabilities, over_unders, props]);

  const handleChange = (e) => {
    if (parseInt(e.target.value) > 2) {
      console.log("games"+e.target.value);

    axios.get("http://localhost:3001/probability", {
      params: {
        stat: state["stat"],
        name: state["name"],
        date: date, 
        games: e.target.value
      }
    }).then((response) => {
      console.log("DATA")
      console.log(response.data)
      setProbability(response.data);
    });
    }
    //setDate(e.target.value);
  };

  const handleStartDate = (event) => {
    setStartDate(event.target.value);
    console.log(startDate);
    setLoading(true);
}

const handleEndDate = (event) => {
    setEndDate(event.target.value);
    console.log(endDate);
    setLoading(true);
}

    if (isLoading) {
        return <div>Loading...</div>;
    }

    

    return (
        <div>
            <Graph data={probabilities} label="Probability of hitting over" canvas_id={"probabilities"} />
            <Graph data={over_unders} label="Over/under performance" canvas_id={"over_unders"} overunder={true} />
            <input type="datetime-local" value={startDate} onChange={handleStartDate}></input>
            <input type="datetime-local" value={endDate} onChange={handleEndDate}></input>
            <div style = {{alignItems: "left"}}><p></p>On {date}, based on the last <input type = "number" defaultValue={5} onChange={handleChange} /> games, {state["name"]} has a probability of {probability} of hitting the over.</div>

        </div>
    )
}

export default PlayerInterface