window.onload = function () {
  sign_in = document.getElementById('signin');
  sign_up = document.getElementById('signup');
  form = document.getElementById('myForm');
  sign_in.onclick = function () {
    form.action = "signin"
  }

  sign_up.onclick = function () {
   form.action = "/signup"
 }
}
