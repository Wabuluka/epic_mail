let create_group=document.getElementById('submit');

let token=localStorage.getItem('token');
let current_user=localStorage.getItem('email');
create_group.addEventListener('click', CreateGroup);

function CreateGroup(e){
    e.preventDefault();
    let group_name=document.getElementById('group_name').value;
    let role=document.getElementById('role').value;
    let createdby=current_user;

let data={
    group_name:group_name,
    role:role,
    createdby:createdby
};
fetch("http://127.0.0.1:5000/api/v2/groups",{
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
        if(data['message']==='You have successfully created a new group'){
            document.getElementById('m_error').innerHTML=data['message'];
            window.location.replace('groups.html');
        }
    });

}
