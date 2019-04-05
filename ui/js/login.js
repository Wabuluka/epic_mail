let login = document.getElementById('login');
login.addEventListener('click', loginUser);

function loginUser(e){
    e.preventDefault();

    let email=document.getElementById('email').value;
    let password=document.getElementById('password').value;

    if (email == ''){
        document.getElementById('errors').innerText = "Please provide an email to login";
        document.getElementById('errors').style.color="red";
        return false
    }
    else if (password == ''){
        document.getElementById('errors').innerText = "You did not provide a password";
        document.getElementById('errors').style.color="red";
        return false
    }

    let login_data={
        "email":email,
        "password":password
    };
    fetch("https://epicmailwabuluka.herokuapp.com/api/v2/auth/login", {
        method: 'POST',
        headers: {
            'Access': 'application/json, text/plain, */*',
            'Content-type': 'application/json'
        },
        body:JSON.stringify(login_data)
    })
    .then(data => data.json())
    .then(data =>  { 
        if(data.status === 200){
            token=data.token;
            localStorage.setItem('token', token)
            localStorage.setItem('email', login_data.email)
            console.log(token);
            window.location.replace('admin.html')
        }else{
            console.log('Not logged in')
        }
    })
}