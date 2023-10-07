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
    let response = await fetch('https://amhep.pythonanywhere.com/grades');


    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    displayData(response);
}

async function fetchStudentGrade(name) {
    let response = await fetch('https://amhep.pythonanywhere.com/grades/'+name, {
        method: "GET",
    });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }
    displayData(response);
}

async function fetchDeleteStudentGrade(name) {
    let response = await fetch('https://amhep.pythonanywhere.com/grades/'+name, {
        method: "DELETE",
        });
    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        alert("Successfully Deleted Grade");
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    displayData(response);
}


async function fetchCreateGrade(name, grade) {
    // var x = document.getElementById("newStudentName").value;
    // var grade = document.getElementById("newStudentGrade").value;

    const data = {"name": name, "grade":grade};

    console.log(data)
    
    let response = await fetch('https://amhep.pythonanywhere.com/grades', {
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

    let response = await fetch('https://amhep.pythonanywhere.com/grades/'+name, {
        method: "PUT",
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    displayData(response);
}