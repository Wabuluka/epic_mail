let submit = document.getElementById('submit');
submit.addEventListener('click', registerUser);


function registerUser(e){
    e.preventDefault();

    let firstname=document.getElementById('firstname').value;
    let lastname=document.getElementById('lastname').value;
    let email=document.getElementById('email').value;
    let password=document.getElementById('password').value;

    // validation of data submitted
    // firstname input
    if (firstname == ''){
        document.getElementById('errors').innerText = "You have not provided your first name.";
        document.getElementById('errors').style.color="red";
        return false
    }
    // lastname input
    else if (lastname == ''){
        document.getElementById('errors').innerText = "You have not provided your last name.";
        document.getElementById('errors').style.color="red";
        return false
    }
    // email input
    else if (email == ''){
        document.getElementById('errors').innerText = "You have not provided you email address.";
        document.getElementById('errors').style.color="red";
    }
    else if(password== ''){
        document.getElementById('errors').innerText="You have not provided your password";
        document.getElementById('errors').style.color="red";
        return false
    }

    // to the db
    let data={
        "firstname":firstname,
        "lastname":lastname,
        "email":email,
        "password":password
    };
    fetch("http://127.0.0.1:5000/api/v2/auth/signup",{
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json'
        },
        body:JSON.stringify(data)
    })
    .then((response) => response.json())
    .then(function(data){
        console.log(data['message']);
        if (data['message']==='You have successfully created an account'){
            window.location.replace('login.html');
        }
        else if(data['message']==='User already exists'){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="red";
            return false
        }
        else if (data['message']==='Do not use special characters and numbers on a name'){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="red";
            return false
            // window.location.replace('index.html');
        }
        else if (data['message']==='Your password must at least contain an uppercase character'){
            document.getElementById('errors').innerHTML=data.message;
            document.getElementById('errors').style.color="red";
        }
    });

}