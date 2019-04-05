let add_member=document.getElementById('submit');
let token=localStorage.getItem('token');
add_member.addEventListener('click', addMember);

window.onload = function(){
    let single_url = location.href
    let url = new URL(single_url)
    let message_id = url.searchParams.get('id')
    getGroupMembers(message_id)
    addMember(message_id)
    // deleteUser(message_id)
}

function getGroupMembers(id){
    token=localStorage.getItem('token')
    fetch(`https://epicmailwabuluka.herokuapp.com/api/v2/groups/members/${id}`,{
        method: 'GET',
        headers:{
            Authorization:`Bearer ${token}`
        }
    }).then((response) => response.json())
    .then((data) => { 
        console.log(data)
        let received = data.data
        output=
            `
            <table style="width:100%">
            <tr>
                <th>ID</th>
                <th>Subject</th>
                <th>Date Received</th>
                <th>Actions</th>
            </tr>`;
            received.forEach(inbox => {
                // console.log('id', message_id)
                
                output +=`
                
                    <tr>
                        <td id="member_id">${inbox.member_id}</td>
                        <td>${inbox.member}</td>
                        <td>${inbox.createdon}</td>
                        <td><button onclick="deleteUser('${id}', ${inbox.member_id})">Delete</button></td>
                        
                    </tr>`;
            });
            output +='</table>';
        document.getElementById('inboxing').innerHTML = output;
    });
}

function addMember(message_id){
    let member=document.getElementById('member').value;

let data={
    'group_name': message_id,
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
            window.location.reload;
            console.log("success")
        }
    });

}

function deleteUser(id, number){
    token=localStorage.getItem('token')
    console.log('group_name', id)
    console.log('number', number)
    // let member_identification = getGroupMembers.received['member_id'];
    // let member_identification = document.getElementById("member_id")
    // console.log('id', member_identification)
    fetch(`https://epicmailwabuluka.herokuapp.com/api/v2/groups/${id}/users/${number}`,{
        method: 'DELETE',
        headers:{
            Authorization:`Bearer ${token}`
        }
    }).then((response) => response.json())
    .then((data) =>{
        if (data.status === 200){
            console.log("deleted")
        }
    });
}