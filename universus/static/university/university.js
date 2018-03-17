$(document).ready(function () {

    $("#search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#departments tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });

    $('#edit-mode').change(function() {
        if ($(this).prop('checked')) {
            $('.field').attr('contenteditable', 'true').css('background-color', '#fff992')
        } else {
            $('.field').attr('contenteditable', 'false').css('background-color', '')
        }
    })
})

