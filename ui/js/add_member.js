let token=localStorage.getItem('token');

function addMember(e){
    e.preventDefault();
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
        if(data['message']==='You have added a new member to the group'){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="green";
            window.location.replace('admin.html');
        }
        else if (data['message'] === "The user you are trying to add does not exist in the system"){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="red";
            return false
        }
        else if (data["message"] === "The member you are trying to add into the group already exists"){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="red";
            return false
        }
        else if (data["message"] === "You can not add a member to a group you did not create"){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="red";
            return false
        }
    });

}