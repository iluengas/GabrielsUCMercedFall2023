
//Function that intakes json and parses it into html to add to table
    //Use async functions so page can handle other operations while awaiting a response from server 
    //Not necessary, but could improve page speed and usability 
    //If an async function is used, all functions must also be async
async function displayData(responseData) {

    //Await response data 
    const grades = await responseData.json();
    //Log response data 
    console.log(grades);

    let placehold = document.querySelector("#grades");  //Selects field with grades id 
    var x = "";     //output string

    for (studentName in grades) {   //iterate through each key in json obj
        //Append table elements to plug back into table
        x += `<tr>               
                <td>
                    ` + studentName + `
                </td>
                <td>
                    ` + grades[studentName] + `
                </td>
            </tr>`
    }
    placehold.innerHTML = x;  //plug new rows and data into table 
}

//Request to fetch all grades in db
async function fetchAllGrades() {

    //Await fetch response (make sure url matches local host and route we want to use in backend), define method 
    let response = await fetch('http://127.0.0.1:5000/grades', { method: 'get', mode: 'cors' });


    //Error handling 
    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    //Send response data json to displayFunction to print it to the page 
    displayData(response);
}


//Function to fetch a student grade based on name received through name field on front-end html
async function fetchStudentGrade(name) {

    //Await fetch response -> plug name argument variable into url to send var to backend route  
    let response = await fetch('http://localhost:5000/grades/'+name, {
        method: "GET",
        mode: 'cors'
    });

        //Error handling 
    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status + "\n Student Not Found");
    }
    displayData(response);
}


//Function to delete student from db
    //Receive name variable from field in front-end
async function fetchDeleteStudentGrade(name) {

    //await fetch request with name variable plugged into URL
    let response = await fetch('http://localhost:5000/grades/'+name, {
        method: "DELETE",
        mode: 'cors'
        });

        //Error handling 
    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Deleted Grade");
        
    } else {
        alert("HTTP-Error: " + response.status + "\n Student Not Found");
    }

    displayData(response);
}


//Function to create a new entry in our DB 
    //Name and grade vars from HTML input field
async function fetchCreateGrade(name, grade) {

    //Create data dictionary with data from our argument variabes 
    const data = {"name": name, "grade":grade};

    //Log data being sent 
    console.log(data)
    
    //Create request with data in to body to send to back-end 
    let response = await fetch('http://localhost:5000/grades', {
        method: "POST",
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", 
        headers: {
            'Content-Type': 'application/json', //Define what kind of data we are including in request body 
        },
        body: JSON.stringify(data), //Send JSON data through the body of the request 
    });

    //Error Handling 

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Created Grade");
    } else {
        alert("HTTP-Error: " + response.status);
    }

    displayData(response);

}


//Function to edit a grade in the gradebook
    //newName and newGrade vars are from HTML input field 
async function fetchEditGrade(name, newGrade) {

    //Initialize and define data dict 
    const data = {"grade": newGrade};

    //Console log data dict
    console.log(data);

    //Create/await a fetch request 
        //Inlcude name in URL path to send as a variable 
    let response = await fetch('http://localhost:5000/grades/'+name, {
        method: "PUT",
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), //Json stringify data dict to send to back end 
    });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Edited Grade");
        
    } else {
        alert("HTTP-Error: " + response.status + "\n Student Not Found");
    }

    displayData(response);
}