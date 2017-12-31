window.onload = function () {
  sign_in = document.getElementById('signin');
  sign_up = document.getElementById('signup');
  username = document.getElementById('username');
  pswd = document.getElementById('pswd')
  sign_in.onclick = function () {

  }

  sign_up.onclick = function () {
    var fetchAction =  require('fetch');
    var url = "https://auth.analogically97.hasura-app.io/v1/signup";
    var requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        }
    };

    var body = {
        "provider": "username",
        "data": {
            "username": username,
            "password": pswd
        }
    };

    requestOptions.body = JSON.stringify(body);

    fetchAction(url, requestOptions)
    .then(function(response) {
    	return response.json();
    })
    .then(function(result) {
    	console.log(result);
    	// To save the auth token received to offline storage
    	var authToken = result.auth_token
    	window.localStorage.setItem('HASURA_AUTH_TOKEN', authToken);
    })
    .catch(function(error) {
    	console.log('Request Failed:' + error);
    });
  }
}
