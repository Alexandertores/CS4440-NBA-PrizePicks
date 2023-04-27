import React from "react";
import axios from "axios";
import Graph from "./Graph";

const url = "http://localhost:3001/probabilities";


function Probabilities(props) {
  const [probabilities, setProbabilities] = React.useState(null);
  const [isLoading, setLoading] = React.useState(true);

  React.useEffect(() => {
    console.log("fetching data");
    console.log(props.stat + props.name + props.startDate + props.endDate)
    axios.get(url, {
      params: {
        stat: props.stat,
        name: props.name,
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
  }, [probabilities, props]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  

  return (
    <div><Graph data={probabilities}  /> </div>
  );
}
  
export default Probabilities;