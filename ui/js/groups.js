function getGroups(){
    let token=localStorage.getItem('token');
    let output = "";
    fetch("http://127.0.0.1:5000/api/v2/groups/all",{
        method:'GET',
        // cache:'no-cache',
        headers:{
            Authorization:`Bearer ${token}`
        }
    })
    .then((response) => response.json())
    .then((data) => { 
        console.log(data)
        let received = data.data
        received.forEach(inbox => {
            console.log(received)
            output=`<div id="tab3" class="tab-content">
            <table style="width:100%">
            <tr>
                <th>Group ID</th>
                <th>Group Name</th>
                <th>Group Role</th>
                <th>Date Created</th>
            </tr>`;
            output +=`
            
                <tr>
                    <td>${inbox.group_id}</td>
                    <td><a href="/get_one.html?id=${inbox.group_name}">${inbox.group_name}</a></td>
                    <td>${inbox.role}</td>
                    <td>${inbox.createdon}</td>
                </tr>
                </table>
            </div>
            `;
        });
        document.getElementById('inboxing').innerHTML = output;
    }).catch(error =>{
        console.log(error)
    })
}