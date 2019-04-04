function getInbox(){
    let token=localStorage.getItem('token');
    let output = "";
    fetch("http://127.0.0.1:5000/api/v2/messages/received",{
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
            output=
            `           
            <div id="tab3" class="tab-content">
            <table style="width:100%">
            <tr>
                <th>Message ID</th>
                <th>Subject</th>
                <th>Date Received</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>`;
            output +=`
            
                <tr>
                    <td>${inbox.message_id}</td>
                    <td><a href="/get_one.html?id=${inbox.message_id}">${inbox.subject}</a></td>
                    <td>${inbox.createdon}</td>
                    <td>${inbox.status}</td>
                    <td><a href="#" onclick="deleteMail(${inbox.message_id})">Delete</a></td>
                    
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