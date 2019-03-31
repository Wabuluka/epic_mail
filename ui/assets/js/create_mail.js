let create_message=document.getElementById('submit');

// retrieve the token from cache
let token=localStorage.getItem('access_token');

create_message.addEventListener('click', CreateMessage);

function CreateMessage(e){
    e.preventDefault();

    let address=document.getElementById('address').value;
    let subject=document.getElementById('subject').value;
    let message=document.getElementById('message').value;
    let sender=document.getElementById('sender').values;
    let status=document.getElementById('status').value;
};

let data={
    "address":address,
    "subject":subject,
    "message":message,
    "sender":sender,
    "status":status
};
fetch("http://127.0.0.1:5000/api/v2/messages",{
        method:'POST',
        headers:{
            'Application':'application/json, text/plain,*/*',
            'Content_type':'application/json',
            Authorization:`Bearer ${token}`
        },
        body:JSON.stringify(data)
    })
    .then((response) => response.json())
    .then(function(data){
        
    });