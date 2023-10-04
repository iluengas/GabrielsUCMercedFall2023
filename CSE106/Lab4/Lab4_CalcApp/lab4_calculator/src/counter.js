import { useState, useEffect } from "react";

function Counter(){
    //Js obj containing css - can call from anywhere
    const myStyle = {
      color: "white",
      backgroundColor: "red", 
      fontFamily: "Sans-Serif"
    }
  
    const[count, setCount] = useState(0);
    const[calculation, setCalculation] = useState(0);
  
            //Pass in funtion w/ NO Arguments  ** useEffect Hook watches count and performs calculation when count is changed 
    useEffect(() =>{
      if (count === 3){
        setCalculation(() => count*3); // Conditional to anazlyze given attributes
      } else {
        setCalculation(() => count*2); // Call setCalc Function to return multi by 2
      }
    }, [count]); //Whenever Count is changed 
    
  
    return (
      <>
        {/* Inline css *remember to use camelCasing - obj w/ 1 attribute */}
        <p style={{backgroundColor: "blue"}}>Count: {count}</p>
        {/* Empty function to call setCount and make it equal to Count +1 */}
        <button onClick={() => setCount((c) => c+1)}>+</button>
        {/* Use js obj to style */}
        <p style = {myStyle}>Calculation: {calculation}</p>
      </>
    )
  }

export default Counter;