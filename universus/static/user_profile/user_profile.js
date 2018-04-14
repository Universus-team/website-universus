function saveChange() {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(readAccount()),
        dataType: 'text',
        success: function(result) {

        }
    });
}

function readAccount() {
    return {
        'name' : $('#name').text(),
        'surname' : $('#surname').text(),
        'patronymic' : $('#patronymic').text(),
        'phone' : $('#phone').val(),
        'address' : $('#address').val(),
        'birth_day' : $('#birth_day').val()
    }
}