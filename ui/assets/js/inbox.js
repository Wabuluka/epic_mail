// inbox for the user
let get_inbox=document.getElementById('inbox');;
get_inbox.addEventListener('click', getInbox);

let token=localStorage.getItem('token');
// get current user from browser
let current_user=localStorage.getItem('email');
function getInbox(){
    document.getElementById('inboxing').innerHTML = "output";
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
        let received = data.data
        received.forEach(inbox => {
            console.log(received)
            output +=`
            <div>
                <h3>${inbox.subject}</h3>
                <p>${inbox.message}</p>
            </div>
            `;
        });
        document.getElementById('inboxing').innerHTML = output;
    }).catch(error =>{
        console.log(error)
    })
}