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