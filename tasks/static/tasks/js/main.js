// var username = "admin";
// var password = "password123";
//
// $.ajaxSetup({
//     headers: ("Authorization": "Basic" + btoa(username + ":" + password))
// })

var $username = $('#username');
var $password = $('#password');
var $login = $('#login');

$login.click(function() {
    $.post('/api-auth/login/', {
        username: $username.val()
        password: $password.val()
    })
})


$.post('/api-auth/login', { username: "", password: ""})


$.get("api/tasks")
