var $tasks = $('#tasks');
var $title = $('input[name="title"]');
var $status = $('input[name="status"]');
var $priority = $('input[name="priority"]');


$.get('http://localhost:8000/api/tasks/', function(tasks){
  abilities.results.forEach(function(task) {
    console.log(task)
    var $li = $('<li>');
    $li.text(task.title)
    $li.appendTo($tasks);
  })
})

$task.submit(function() {
  console.log('Form submitted!');

  $.ajax({
    method: 'post',
    url: 'http://localhost:8000/api/tasks/',
    username: 'admin',
    password: 'password123',
    data: {
      title: $title.val(),
      status: $status.val(),
      priority: $priority.val()
    },
    success: function(newTask) {
      console.log(newTask)
      var $li = $('<li>');
      $li.text(newTask.name)
      $li.appendTo($tasks);
    }
  });

  return false;
});
