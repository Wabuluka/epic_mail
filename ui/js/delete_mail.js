window.onclick = function(){
    let single_url = location.href
    let url = new URL(single_url)
    let message_id = url.searchParams.get('id')
    readMail(message_id)
    r = document.getElementById('address')
}

function deleteMail(id){
    token=localStorage.getItem('token')

    fetch(`http://127.0.0.1:5000/api/v2/messages/${id}`,{
        method: 'DELETE',
        headers:{
            Authorization:`Bearer ${token}`
        }
    }).then((response) => response.json())
    .then((data) =>{
        if (data.status === 200){
            // var one_mail = data.data;
            console.log("deleted")
            // let result = ``;
            // let email = ``;

            // document.getElementById("from").innerHTML = `${one_mail.createdby}`;
            // document.getElementById("to").innerHTML = `${one_mail.address}`;
            // document.getElementById("message").innerHTML = `${one_mail.message}`;
            // document.getElementById("subject").innerHTML = `${one_mail.subject}`;

            // one_mail.forEach((mail) => {
            

            // document.
            // });
        }
    });
}