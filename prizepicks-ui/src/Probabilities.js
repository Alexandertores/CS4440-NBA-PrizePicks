import React from "react";
import axios from "axios";
import Graph from "./Graph";
import { useLocation } from 'react-router-dom';


const url = "http://localhost:3001/";


function Probabilities(props) {
  const [probabilities, setProbabilities] = React.useState(null);
  const [isLoading, setLoading] = React.useState(true);
  let { state } = useLocation();
  const date = state['date']
  const [probability, setProbability] = React.useState(state['probability'])

  console.log("state1" + JSON.stringify(state));
 


  React.useEffect(() => {
    if (isLoading === true) {
      console.log("fetching data");
  
      axios.get(url+"probabilities", {
        params: {
          stat: state["stat"],
          name: state["name"],
          startDate: props.startDate,
          endDate: props.endDate 
        }
      }).then((response) => {
        console.log("DATA")
        console.log(response.data)
        setProbabilities(response.data);
        setLoading(false);
        console.log(probabilities)
      });
    }
    
  }, [isLoading, probabilities, props, state, state.name]);

  const handleChange = (e) => {
    if (parseInt(e.target.value) > 2) {
      console.log("games"+e.target.value);

    axios.get(url+"probability", {
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

  if (isLoading) {
    return <div>Loading...</div>;
  }

  

  return (
    <><div style = {{maxWidth: "70%"}}><Graph data={probabilities} /> </div>

    <div style = {{alignItems: "left"}}><p></p>On {date}, based on the last <input type = "number" defaultValue={5} onChange={handleChange} /> games, {state["name"]} has a probability of {probability} of hitting the over.</div></>
  );
}
  
export default Probabilities;
