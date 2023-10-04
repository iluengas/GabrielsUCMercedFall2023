import { useState } from "react";

function Banana(){
    const [color, setColor] = useState("yellow");
    const [year, setYear] = useState(1900);
    //Use json as a const/useState
    const [attributes, setAttributes] = useState({make:"Toyota", model:"Corrola"});
  
    //Function to change color state through setColor func
  
    function changeColor(){
      if (color === "yellow") {
        setColor("brown")
      } else if (color === "brown") {
        setColor("black")
      } 
  
    }
  
    function incrementyear(){
        setYear(year+1)
    }

    function upgrade(){
        //Spread operator to separate and edit attributes individually
        setAttributes(previousState => {
                return {...previousState, model:"Prius"};
        });
    }

    function reset(){
      setColor("yellow")
    }
  
    return(
      <>
        <h1 id='2'>I'm a banana colored {color}, born in {year}</h1>
        <button onClick={changeColor}>Press to change Color</button>
        <button onClick={reset}>Reset</button>
        <br/>
        <button onClick={incrementyear}>Press to change year</button>
        <br/>
        <h1>I am a {attributes.make}, {attributes.model}</h1>
        <button onClick={upgrade}>Press to upgrade</button>

      </>
    );
  }

export default Banana;