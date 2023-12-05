async function likePost(postID){
    let response = await fetch('/likePost/'+postID, {method: 'post'});

    if (response.ok) { // if HTTP-status is 200-299
        let newLikeTotal = await response.json();
        console.log(response);
        let placehold = document.getElementById("likeButton"+postID);  //Selects field with likeButton

        placehold.innerHTML = newLikeTotal;  //plug new data into dom element 
        
    } else {
        alert("HTTP-Error: " + response.status);
    }
}

async function dislikePost(postID){
    let response = await fetch('/dislikePost/'+postID, {method: 'post'});

    if (response.ok) { // if HTTP-status is 200-299
        let newDislikeTotal = await response.json();
        console.log(response);
        let placehold = document.getElementById("dislikeButton"+postID);  //Selects field with likeButton

        placehold.innerHTML = newDislikeTotal;  //plug new data into dom element 
        
    } else {
        alert("HTTP-Error: " + response.status);
    }
}

async function fetchAllClasses_Student() {
    let response = await fetch('http://127.0.0.1:5000/mCS', { method: 'get', mode: 'cors' });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    console.log(response)
}


async function fetchCourseList(){
    let response = await fetch('http://127.0.0.1:5000/courseList', { method: 'get', mode: 'cors' });

    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    console.log(response)


}

async function fetchAllGrades() {

    //Await fetch response (make sure url matches local host and route we want to use in backend), define method 
    let response = await fetch('http://127.0.0.1:5000/grades', { method: 'GET'});


    //Error handling 
    if (response.ok) { // if HTTP-status is 200-299
        console.log(response);
        
    } else {
        alert("HTTP-Error: " + response.status);
    }

    //Send response data json to displayFunction to print it to the page 
    displayData(response);
}