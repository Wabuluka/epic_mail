function getGroups(){
    let token=localStorage.getItem('token');
    let output = "";
    fetch("https://epicmailwabuluka.herokuapp.com/api/v2/groups/all",{
        method:'GET',
        headers:{
            Authorization:`Bearer ${token}`
        }
    })
    .then((response) => response.json())
    .then((data) => { 
        console.log(data)
        let received = data.data
        output=`
            <table style="width:100%">
            <tr>
                <th>Group Name</th>
                <th>Group Role</th>
                <th>Date Created</th>
            </tr>`;
        received.forEach(inbox => {
            console.log(received)
            output +=`
            
                <tr>
                    <td><a href="/view_group.html?id=${inbox.group_name}">${inbox.group_name}</a></td>
                    <td>${inbox.role}</td>
                    <td>${inbox.createdon}</td>
                </tr>
                
            `;
        });
        output +=`</table>`;
        document.getElementById('inboxing').innerHTML = output;
    }).catch(error =>{
        console.log(error)
    })
}