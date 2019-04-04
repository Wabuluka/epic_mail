let create_group_msg=document.getElementById('submit');

let token=localStorage.getItem('token');
let current_user=localStorage.getItem('email');
create_group_msg.addEventListener('click', CreateGroupMsg)

function CreateGroupMsg(){
    // e.preventDefault();
    let group_name=document.getElementById('group_name').value;
    let subject=document.getElementById('subject').value;
    let message=document.getElementById('message').value;
    let status="sent";

let data={
    'group_name':group_name,
    'subject':subject,
    'message':message,
    'status':status
};
fetch("http://127.0.0.1:5000/api/v2/groups/messages",{
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
        if(data['message']==='Group messages successfully created.'){
            window.location.replace('admin.html');
        }
    });

}