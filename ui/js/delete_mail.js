window.onclick = function(){
    let single_url = location.href
    let url = new URL(single_url)
    let message_id = url.searchParams.get('id')
    readMail(message_id)
    r = document.getElementById('address')
}

function deleteMail(id){
    token=localStorage.getItem('token')

    fetch(`https://epicmailwabuluka.herokuapp.com/api/v2/messages/${id}`,{
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