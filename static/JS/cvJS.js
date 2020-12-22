

//updating the date automatically
function date(){

var date = new Date();

var months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
document.getElementById("year").innerHTML = months[date.getMonth()] + ' ' + date.getFullYear();

}


function validate(){
  var name = document.getElementById("name").value;
  var phone = document.getElementById("phone").value;
  var email = document.getElementById("email").value;
  var error_message = document.getElementById("error_message");
  

  if(name.length < 5){
    text = "please enter full name";
    error_message.innerHTML = text;
    return false;
   
  }
 
  if(isNaN(phone) || phone.length < 10){
    text = "please enter a valid phone number";
    error_message.innerHTML = text;
    return false;
    
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "please enter a valid mail adress";
    error_message.innerHTML = text;
    return false;
    
    
  }
 
  alert("the message has been sent");
  document.getElementById("subbtn").value="MESSAGE HAS BEEN SENT!";
   return false;

}
