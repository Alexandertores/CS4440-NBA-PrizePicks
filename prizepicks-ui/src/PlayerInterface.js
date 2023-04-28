import React from "react";
import axios from "axios";
import Graph from "./Graph";

const probabilities_url = "http://localhost:3001/probabilities";
const over_unders_url = "http://localhost:3001/over_unders";

function PlayerInterface(props) {
    const [startDate, setStartDate] = React.useState("2023-02-23T00:00");
    const [endDate, setEndDate] = React.useState("2023-04-15T00:00");
    const [isLoading, setLoading] = React.useState(true);
    const [probabilities, setProbabilities] = React.useState(null);
    const [over_unders, setOverUnders] = React.useState(null);

    React.useEffect(() => {
    console.log("fetching data");
    console.log(props.stat + " " + props.name + " " + startDate + " " + endDate)
    if (isLoading) {
        axios.get(probabilities_url, {
            params: {
              stat: props.stat,
              name: props.name,
              startDate: startDate,
              endDate: endDate 
            }
          }).then((response) => {
            setProbabilities(response.data);
          });
        axios.get(over_unders_url, {
            params: {
              stat: props.stat,
              name: props.name,
              startDate: startDate,
              endDate: endDate 
            }
          }).then((response) => {
            setOverUnders(response.data);
          });
        setLoading(false);
    }
  }, [isLoading, probabilities, over_unders, props]);

    if (isLoading) {
        return <div>Loading...</div>;
    }

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

    return (
        <div>
            <Graph data={probabilities} label="Probability of hitting over" canvas_id={"probabilities"} />
            <Graph data={over_unders} label="Over/under performance" canvas_id={"over_unders"} />
            <input type="datetime-local" value={startDate} onChange={handleStartDate}></input>
            <input type="datetime-local" value={endDate} onChange={handleEndDate}></input>
        </div>
    )
}

export default PlayerInterface