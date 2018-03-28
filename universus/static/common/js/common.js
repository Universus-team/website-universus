$(document).ready(function () {

    $('#edit-mode').change(function() {
        if ($(this).prop('checked')) {
            $('.field:not(input)').attr('contenteditable', 'true').css('background-color', '#fff992')
            $('input.field').removeAttr('readonly').css('background-color', '#fff992')
        } else {
            $('.field:not(input)').attr('contenteditable', 'false').css('background-color', '')
            $('input.field').attr('readonly', '').css('background-color', '')
        }
    })

    $('.field:not(input)').attr('contenteditable', 'false').css('background-color', '')
    $('input.field').attr('readonly', '').css('background-color', '')
})