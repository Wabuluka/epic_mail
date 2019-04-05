let token=localStorage.getItem('token');

function addMember(e){
    e.preventDefault();
    let group_name=document.getElementById('group_name').value;
    let member=document.getElementById('member').value;

let data={
    'group_name':group_name,
    'member':member
};
fetch("https://epicmailwabuluka.herokuapp.com/api/v2/groups/users/members",{
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
        if(data['message']==='You have added a new member to the group'){
            window.location.replace('admin.html');
            console.log("success")
        }
    });

}