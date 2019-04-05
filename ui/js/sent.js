function getSent(){
    let token=localStorage.getItem('token');
    let output = "";
    fetch("https://epicmailwabuluka.herokuapp.com/api/v2/messages/sent",{
        method:'GET',
        headers:{
            Authorization:`Bearer ${token}`
        }
    })
    .then((response) => response.json())
    .then((data) => { 
        if (data["status"] !== 200 ){
            document.getElementById('errors').innerHTML="You do not have any mails here yet";
            document.getElementById('errors').style.color="red";
            return false
        }else if (data["status"] === 200){
            output="You have not sent any mails"
            let received = data.data
            output=`
                <table style="width:100%">
                <tr>
                    <th>Message ID</th>
                    <th>Subject</th>
                    <th>Date Received</th>
                    <th>To</th>
                </tr>`;
            received.forEach(inbox => {            
                output +=`            
                    <tr>
                        <td>${inbox.message_id}</td>
                        <td><a href="/get_one.html?id=${inbox.message_id}">${inbox.subject}</a></td>
                        <td>${inbox.createdon}</td>
                        <td>${inbox.address}</td>
                    </tr>
                `;
            });
            output +=`</table>`;
            document.getElementById('inboxing').innerHTML = output;
        }
    }).catch(error =>{
        console.log(error)
    })
}