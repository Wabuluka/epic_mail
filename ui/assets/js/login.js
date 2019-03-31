let login = document.getElementById('login');
login.addEventListener('click', loginUser);

function loginUser(e){
    e.preventDefault();

    let email=document.getElementById('email').value;
    let password=document.getElementById('password').value;

    let data={
        "email":email,
        "password":password
    };

    fetch("http://127.0.0.1:5000/api/v2/auth/login", {
        method: 'POST',
        headers: {
            'Access': 'application/json, text/plain, */*',
            'Content-type': 'application/json'
        },
        body:JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => {
        if (data['access_token'] === data['access_token']){
            window.location.replace('/admin.html');
            let token = data['access_token'];

            // browser cache
            localStorage.setItem('access_token', token);
        }
        else{
            document.getElementById('l_error').innerText=data['message'];
            document.getElementById('l_error').style.color="red";
            window.location.replace('//signup.html');
            return false
        }
    });
}