function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
  }
  
console.log('main js started');
// axios.defaults.headers.common['X-CSRFToken'] = csrf_token;
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const csrf_token =await getCookie('csrftoken');

    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token,
            },
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}

async function putData(url = '', data = {}) {
    // Default options are marked with *
    const csrf_token =await getCookie('csrftoken');

    const response = await fetch(url, {
        method: 'PUT', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token,
            },
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}


// function incrementValue(userID,restaurantID){
//     const data = {
//         user: userID,
//         restaurant: restaurantID
//     };

//     console.log(data)
//     postData('http://127.0.0.1:8000/api/addVotes', data)
//         .then((data) => { console.log(data); }) // JSON from `response.json()` call
//         .catch((error) => { console.error(error); });


// }

