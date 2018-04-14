$(document).ready(function () {
    $("#search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#exams tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });

    $('td:has( > .not-complete)').css('font-weight', 'bold').css('background-color', '#79aec8')
    $('td:has( > .not-pass)').css('font-weight', 'bold').css('background-color', '#E86A41')
    $('td:has( > .pass)').css('font-weight', 'bold').css('background-color', '#7ec87f')
})