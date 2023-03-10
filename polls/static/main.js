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
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token,
            },
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit

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
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token,
            },
        method: 'PUT', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit

        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}


// I want to create a fn to post element to the API once the user pressed an element once it will create an order before adding element to the cart
// after that it will add the element to his cart
// an order is deleted manually 
// steps
// 1. gets data
// 2. get the url for the api request 
// 3. use POST method above