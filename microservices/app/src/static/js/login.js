window.onload = function () {
  sign_in = document.getElementById('signin');
  sign_up = document.getElementById('signup');
  username = document.getElementById('username');
  pswd = document.getElementById('pswd')
  sign_in.onclick = function () {
    document.getElementById("myForm").action = "/signin";
  }

  sign_up.onclick = function () {
   document.getElementById("myForm").action = "/signup";
 }
}
