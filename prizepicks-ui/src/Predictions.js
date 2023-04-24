import React from "react";
import axios from "axios";
import PlayerCard from "./PlayerCard";

const url = "http://localhost:3001";




function Predictions() {
  const [lines, setLines] = React.useState(null);
  const [isLoading, setLoading] = React.useState(true);

  React.useEffect(() => {
    axios.get(url).then((response) => {
      setLines(response.data);
      setLoading(false);
    });
  }, []);
  console.log(lines);

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