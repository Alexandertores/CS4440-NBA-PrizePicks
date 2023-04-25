import React from "react";
import axios from "axios";
import PlayerCard from "./PlayerCard";

const url = "http://localhost:3001";




function Predictions(props) {
  const [lines, setLines] = React.useState(null);
  const [isLoading, setLoading] = React.useState(true);

  React.useEffect(() => {
    console.log("fetching data");
    axios.get(url, {
      params: {
        stat: props.stat 
      }
    }).then((response) => {
      setLines(response.data);
      setLoading(false);
    });
  }, [props]);

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      {lines.map((line, index) => {
        if (line.probability != null) {
          return <PlayerCard data={line} />
        }
      })}
    </div>

  );
}
  
export default Predictions;