function Soccer(){
    function shoot() {
        alert("Took Shot")
    }
    return(
        <>
            <button onClick={shoot}>Take Shot</button>
        </>
    )
  }

export default Soccer;