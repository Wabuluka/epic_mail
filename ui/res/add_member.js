let add_member=document.getElementById('submit');

let token=localStorage.getItem('token');
let current_user=localStorage.getItem('email');
add_member.addEventListener('click', addMember);

function addMember(){
    // e.preventDefault();
    let group_name=document.getElementById('group_name').value;
    let member=document.getElementById('member').value;

let data={
    'group_name':group_name,
    'member':member
};
fetch("http://127.0.0.1:5000/api/v2/groups/users/members",{
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
        // document.getElementById('m_error').innerHTML=data['errors'];
        if(data['message']==='You have added a new member to the group'){
            // document.getElementById('m_error').innerHTML=data['message'];
            window.location.replace('/create.html');
            console.log("success")
        }
    });

}