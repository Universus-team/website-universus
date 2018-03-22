$(document).ready(function () {

    $("#search_teacher, #search_university, #search_department").on("keyup", function() {
        var teacher = $('#search_teacher').val().toLowerCase();
        var university = $('#search_university').val().toLowerCase();
        var department = $('#search_department').val().toLowerCase();
        $("#students tr").filter(function() {

            $(this).toggle(
                ($(this).children('.user-name').text().toLowerCase().indexOf(teacher) > -1) &&
                ($(this).children('.user-university').text().toLowerCase().indexOf(university) > -1)  &&
                ($(this).children('.user-university-department').text().toLowerCase().indexOf(department) > -1)
            )
            $(this).unhighlight();
            $(this).children('.user-name').highlight(teacher);
            $(this).children('.user-university').highlight(university);
            $(this).children('.user-university-department').highlight(department);
        });
    });


})