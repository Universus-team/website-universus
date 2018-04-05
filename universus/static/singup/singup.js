

$(document).ready(function () {

    $('#universities').on('change', function() {
        univer_id = +(this.value)
        if (univer_id !== 0) {
            $.ajax({
                url: window.location.href+'departments/',
                type: 'POST',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify({'university_id' : univer_id}),
                dataType: 'text',
                success: function(result) {
                    $('#departments').empty();
                    departments = JSON.parse(result)
                    $.each(departments, function (i, item) {

                        $('#departments').append($('<option>', {
                            value: item.Id,
                            text : item.Name
                        }));
                    });
                }
            });
        }

    })


})