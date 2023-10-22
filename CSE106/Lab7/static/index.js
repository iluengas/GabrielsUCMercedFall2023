async function displayData(responseData) {

    const grades = await responseData.json();
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

async function fetchAllGrades() {
    let response = await fetch('http://127.0.0.1:5000/grades', { method: 'get', mode: 'cors' });


    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    displayData(response);
}

async function fetchStudentGrade(name) {
    let response = await fetch('http://localhost:5000/grades/'+name, {
        method: "GET",
        mode: 'cors'
    });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status + "\n Student Not Found");
    }
    displayData(response);
}

async function fetchDeleteStudentGrade(name) {
    let response = await fetch('http://localhost:5000/grades/'+name, {
        method: "DELETE",
        mode: 'cors'
        });
    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Deleted Grade");
        
    } else {
        alert("HTTP-Error: " + response.status + "\n Student Not Found");
    }

    displayData(response);
}


async function fetchCreateGrade(name, grade) {
    // var x = document.getElementById("newStudentName").value;
    // var grade = document.getElementById("newStudentGrade").value;

    const data = {"name": name, "grade":grade};

    console.log(data)
    
    let response = await fetch('http://localhost:5000/grades', {
        method: "POST",
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Created Grade");
    } else {
        alert("HTTP-Error: " + response.status);
    }

    displayData(response);

}

async function fetchEditGrade(name, newGrade) {
    const data = {"grade": newGrade};

    console.log(data);

    let response = await fetch('http://localhost:5000/grades/'+name, {
        method: "PUT",
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Edited Grade");
        
    } else {
        alert("HTTP-Error: " + response.status + "\n Student Not Found");
    }

    displayData(response);
}