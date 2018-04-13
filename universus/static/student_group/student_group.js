$(document).ready(function () {

    $("#search_student").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#students tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });

    $("#search_teacher").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#teachers tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });


})

function sendMessage() {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'sendMessage': true,
            'message': $('#share_message').val()
        }),
        dataType: 'text',
        success: function(result) {
            data = JSON.parse(result)
            if (data['no students']) {
                $('#msg_result').text('Нет студентов')
            } else if (data['send']) {
                $('#msg_result').text('Сообщение отправлено')
                $('#share_message').val('')
            } else {
                $('#msg_result').text('Сообщение НЕ отправлено')
            }
        }
    });
}

function saveChange() {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(readUniversity()),
        dataType: 'text',
        success: function(result) {
            data = JSON.parse(result)
            $('#saveMessage').text(data.message)
        }
    });
}