document.getElementById('inbox').addEventListener('click', getRecievedMessages);
function getRecievedMessages() {
    let recieveUrl = 'http://127.0.0.1:5000/api/v2/messages';
    token = localStorage.getItem('token');
    if (token === null) {
        alert('please login');
        window.location.replace('UI/index.html');
    };
    fetch(recieveUrl, {
        headers: {
            'Authorization': `Bearer ${token}`
        } 
    })
    .then(res => res.json())
    .then(response => {
        if (response.error != "you have no recieved messages")
         {let output = `
        
            <p>you have no recieved messages</p>
        `
        document.getElementById('no_mail').innerHTML = output;
        } 
        {let output = `
        <tr class="titles">
            <th>created-on</th>
            <th>subject</th>
            <th>sender_email</th>
        </tr>`
        for(let k in response){
            console.log(response[k].item);
            output += `
            <tr class="orders">
                <td>${response[k].created-on}</td>
                <td>${response[k].subject}</td>
                <td>${response[k].sender_email}</td>`

            console.log(output);
        }
        document.getElementById('recieved').innerHTML = output;};
        
    })
}

function getPosts(){
    fetch('https://jsonplaceholder.typicode.com/posts')
    .then((res) => res.json())
    .then((data) => {
        let output = '<h2> Posts </h2';
            data.forEach(function(post){
                output +=`
                <div>
                    <h3>${post.title}</h3>
                    <p>${post.body}</p>
                </div>
                `;
            });
            document.getElementById('output').innerHTML = output;
    })
}