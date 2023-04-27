import React from "react";
import axios from "axios";
import Graph from "./Graph";
import { useLocation } from 'react-router-dom';


const url = "http://localhost:3001/probabilities";


function Probabilities(props) {
  const [probabilities, setProbabilities] = React.useState(null);
  const [isLoading, setLoading] = React.useState(true);
  let { state } = useLocation();
  console.log("state1" + JSON.stringify(state));
 


  React.useEffect(() => {
    if (isLoading === true) {
      console.log("fetching data");
  
      axios.get(url, {
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

  if (isLoading) {
    return <div>Loading...</div>;
  }

  

  return (
    <><div style = {{maxWidth: "70%"}}><Graph data={probabilities} /> </div>
    <div><p></p><input type = "number" defaultValue={5}/></div></>
  );
}
  
export default Probabilities;