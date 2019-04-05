function getInbox(){
    let token=localStorage.getItem('token');
    let output = "";
    fetch("http://127.0.0.1:5000/api/v2/messages/received",{
        method:'GET',
        headers:{
            Authorization:`Bearer ${token}`
        }
    })
    .then((response) => response.json())
    .then((data) => { 
        console.log(data)
        output = "Seems like you have not received any mails yet"
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