function getInbox(){
    let token=localStorage.getItem('token');
    let output = "";
    fetch("https://epicmailwabuluka.herokuapp.com/api/v2/messages/received",{
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
        output=
            `
            <table style="width:100%">
            <tr>
                <th>Subject</th>
                <th>Date Received</th>
                <th>From</th>
                <th>Actions</th>
            </tr>`;
        received.forEach(inbox => {
            console.log(received)
            
            output +=`
            
                <tr>
                    <td><a href="/get_one.html?id=${inbox.message_id}">${inbox.subject}</a></td>
                    <td>${inbox.createdon}</td>
                    <td>${inbox.createdby}</td>
                    <td><a href="#" onclick="deleteMail(${inbox.message_id})">Delete</a></td>
                    
                </tr>
            `;
        });
        output+=`</table>`;
        document.getElementById('inboxing').innerHTML = output;
    }).catch(error =>{
        console.log(error)
    })
}