import React, {useMemo, useRef, useState} from "react";
import axios from "axios";
import MaterialReactTable from 'material-react-table';
import { Link } from "react-router-dom";


const url = "http://localhost:3001";





function Predictions(props) {
  const [lines, setLines] = React.useState(null);
  const [isLoading, setLoading] = React.useState(true);

  const [date, setDate] = useState("2023-04-07");
  const dateInputRef = useRef(null);

  React.useEffect(() => {
    console.log("fetching data");
    axios.get(url, {
      params: {
        stat: props.stat,
        date: date
      }
    }).then((response) => {
      console.log(response)
      var newLines = Array.from(response.data);
      
      var index = 0;
      while (index < (newLines.length)) {
        if (newLines[index].probability == null) {
          newLines.splice(index, 1);
        } else if (newLines[index].data.name === "Jayson Tatum" && newLines[index].date > new Date("2023-04-01")){
          newLines.splice(index, 1);
        }else {
          index++;
        }
      }
      
      // newLines.forEach(element => {
      //   console.log(element.data.name);
      //   if (element.probability == null) {
      //     console.log(element);
      //     console.log(newLines.indexOf(element));
          
      //   }        
      // });
      console.log(newLines);
      setLines(newLines);
      setLoading(false);
    });
  }, [props, date]);
  

  

  const columns = useMemo(
    () => [
    {
      accessorKey: 'image', //normal accessorKey
      header: 'Player Image',
      Cell: ({cell}) => (<span><img src = {cell.getValue()} alt = ""/></span>)
    },
    {
      accessorKey: 'data.name', //access nested data with dot notation
      header: 'Name',
      Cell: ({cell}) => (<span><Link class="nav-link" to="http://localhost:3000/probabilities" state={{name:cell.getValue(), stat: props.stat, date: date, probability:cell.row.original.probability}}>{cell.getValue()}</Link></span>)
    },
    {
      accessorKey: 'line',
      header: 'Line',
    },
    {
      accessorKey: 'probability', //normal accessorKey
      header: 'Prediction'
    }
],
[],);

  const handleChange = (e) => {
    setDate(e.target.value);
    //setDate(e.target.value);
    console.log(date);
  };



  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (

    <div>
      <div style = {{textAlign: "left", marginLeft: "5%"}}>Choose a Date's Predictions <br /><input type="date" onChange={handleChange} ref={dateInputRef} defaultValue = "2023-04-07"/></div>
      <MaterialReactTable columns = {columns} data = {lines} />
      {/* {lines.map((line, index) => {
        if (line.probability != null) {
          return <PlayerCard data={line} />
        }
      })} */}
    </div>

  );
}
  
export default Predictions;