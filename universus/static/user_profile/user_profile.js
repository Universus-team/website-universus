function saveChange() {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(readAccount()),
        dataType: 'text',
        success: function(result) {
            data = JSON.parse(result)
            $('#saveMessage').text(data.message)
        }
    });
}

function readAccount() {
    return {
        
    }
}