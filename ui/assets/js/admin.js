let create_message=document.getElementById('submit');
// retrieve the token from cache
let token=localStorage.getItem('token');
// get current user from browser
let current_user=localStorage.getItem('email');

let sender_mail=localStorage.getItem('user-email');
create_message.addEventListener('click', CreateMessage);

function CreateMessage(e){
    e.preventDefault();
    let address=document.getElementById('address').value;
    let subject=document.getElementById('subject').value;
    let message=document.getElementById('message').value;
    let sender=current_user;
    let status="sent";

let data={
    address:address,
    subject:subject,
    message:message,
    sender:sender,
    status:status
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
        document.getElementById('m_error').innerHTML=data['errors'];
        if(data['message']==='Message has been created successfully'){
            document.getElementById('m_error').innerHTML=data['message'];
            window.location.replace('/create.html');
        }
    });

}


// inbox for the user
window.onload = function getInbox(){
    fetch("http://127.0.0.1:5000/api/v2/messages/received", {
        method: 'GET',
        headers:{
            'Content-type':'application/json',
            Authorization: `Bearer ${token}`
        },
    })
    .then((response) => response.json())
    .then(function (data){
        if(data['msg']){
            let output
        }
    })
}