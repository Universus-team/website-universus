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

$(document).ready(function () {

    $("#search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#departments tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });
})

function readUniversity() {
    return {
        'ShortName' : $('#ShortName').text(),
        'FullName' : $('#FullName').text(),
        'Description' : $('#Description').text(),
        'Address' : $('#Address').text(),
        'WebSite' : $('#WebSite').val()
    }
}