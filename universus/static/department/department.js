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