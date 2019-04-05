let create_message = document.getElementById('submit');
create_message.addEventListener('click', CreateMessage);

function CreateMessage(e){
    let token=localStorage.getItem('token');
    let current_user=localStorage.getItem('email');

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
fetch("https://epicmailwabuluka.herokuapp.com/api/v2/messages",{
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
        document.getElementById('errors').innerHTML=data['errors'];
        if(data['message']==='The person you are sending the email to does not exist'){
            document.getElementById('errors').innerText=data.message;
            document.getElementById('errors').style.color="red";
            return false
        }
        else if(data['message']==='Message has been created successfully'){
            document.getElementById('errors').innerHTML=data['message'];
            window.location.replace('admin.html');
        }
        
    });

}