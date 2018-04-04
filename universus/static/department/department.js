$(document).ready(function () {

    $("#search_department").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#departments tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });

    $("#search_student_group").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#student_groups tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });


})

function saveChange() {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(readDepartment()),
        dataType: 'text',
        success: function(result) {
            data = JSON.parse(result)
            $('#saveMessage').text(data.message)
        }
    });
}

function readDepartment() {
    return {
        'name' : $('#name').text(),
        'description' : $('#description').text(),
        'dean_name' : $('#dean').text(),
         csrfmiddlewaretoken: '{{ csrf_token }}'
    }
}