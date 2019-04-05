window.onload = function(){
    let single_url = location.href
    let url = new URL(single_url)
    let message_id = url.searchParams.get('id')
    readMail(message_id)
}
function readMail(id){
    token=localStorage.getItem('token')
    fetch(`https://epicmailwabuluka.herokuapp.com/api/v2/messages/${id}`,{
        method: 'GET',
        headers:{
            Authorization:`Bearer ${token}`
        }
    }).then((response) => response.json())
    .then((data) =>{
        if (data.message === "Mail not found"){
            document.getElementById('inboxing').innerHTML = response.message;
        }else if (data.status === 200){
            var one_mail = data.data;
            console.log(one_mail)
            document.getElementById("from").innerHTML = `${one_mail.createdby}`;
            document.getElementById("to").innerHTML = `${one_mail.address}`;
            document.getElementById("message").innerHTML = `${one_mail.message}`;
            document.getElementById("subject").innerHTML = `${one_mail.subject}`;
        }
    });
}