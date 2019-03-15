// toggle between responsive class and top-navigation class
function myFunction(){
  var x = document.getElementById("myTopnav");
  if (x.className === "top-navigation") {
    x.className += " responsive";
  } else {
    x.className = "top-navigation";
  }
}