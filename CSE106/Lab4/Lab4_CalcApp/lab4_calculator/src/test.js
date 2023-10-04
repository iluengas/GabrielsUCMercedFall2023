// function Car() {
//   return <h2>Hi, I am a car!</h2>;
// }

function Garage(props) {
    if (props.size === 2) {
      return (
        <>
        <h1>I'm a garage</h1>
        {/* How we do function calls */}
        <Car color="red" year="1989"/> 
        <Car color="blue" year="2000"/> 
        </>
      );
    }
    else {
      return(
        <>
          <h1>I'm an empty Garage</h1>
        </>
      )
    }
  }
  
  function Car(props) {
    return(
      <>
        <p>I'm a {props.color} car, made in {props.year}</p>
      </>
    )
  }


export default Garage;

