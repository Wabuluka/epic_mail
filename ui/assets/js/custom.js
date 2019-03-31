// toggle between responsive class and top-navigation class
function myFunction(){
    var x = document.getElementById("myTopnav");
    if (x.className === "top-navigation") {
      x.className += " responsive";
    } else {
      x.className = "top-navigation";
    }
  }
  
  function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  } 

// let fetchAPI=function(url, method, data){
//   if(!('fetch' in window)){
//     console.log("The API is not found");
//     return;
//   }

//   const options={
//     method:method
//   }
// }