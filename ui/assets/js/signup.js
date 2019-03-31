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
        document.getElementById('e_firstname').innerText = "You have not provided your first name.";
        document.getElementById('e_firstname').style.color="red";
        return false
    }
    // lastname input
    else if (lastname == ''){
        document.getElementById('e_lastname').innerText = "You have not provided your last name.";
        document.getElementById('e_lastname').style.color="red";
        return false
    }
    // email input
    else if (email == ''){
        document.getElementById('e_email').innerText = "You have not provided you email address.";
        document.getElementById('e_email').style.color="red";
    }
    else if(password== ''){
        document.getElementById('e_password').innerText="You have not provided your password";
        document.getElementById('e_password').style.color="red";
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
            alert('You have successfully created an account');
            window.location.replace('login.html');
        }
        else if(data['message']==='User already exists'){
            document.getElementById('e_error').innerHTML=data['message'];
            document.getElementById('e_email').style.color="red";
            return false
        }
        else{
            window.location.replace('/index.html');
        }
    });

}