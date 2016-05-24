var $tasks = $('#tasks');

$.get('/api/tasks/', function(tasks){
    if (tasks.results != undefined) {
        tasks.results.forEach(for_function);
    }
})

function for_function(task) {
        console.log(task);
        var $li = $('<li>');
        $li.text(task.title);
        $li.appendTo($tasks);
}

var $task = $('#task');
var $title = $('input[name="title"]');
var $status = $('input[name="status"]');
var $priority = $('input[name="priority"]');

$task.submit(function() {
  console.log('Form submitted!');

  $.ajax({
    {% csrf_token %}
    method: 'post',
    url: '/api/tasks/',
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
