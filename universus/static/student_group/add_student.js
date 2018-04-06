
function addStudent(group_id, student_id) {
    alert("added student")
}

$(document).ready(function () {

    $("#search_student, #search_university, #search_department").on("keyup", function() {
        var student = $('#search_student').val().toLowerCase();
        var university = $('#search_university').val().toLowerCase();
        var department = $('#search_department').val().toLowerCase();
        $("#students tr").filter(function() {

            $(this).toggle(
                ($(this).children('.user-name').text().toLowerCase().indexOf(student) > -1) &&
                ($(this).children('.user-university').text().toLowerCase().indexOf(university) > -1)  &&
                ($(this).children('.user-university-department').text().toLowerCase().indexOf(department) > -1)
            )
            $(this).unhighlight();
            $(this).children('.user-name').highlight(student);
            $(this).children('.user-university').highlight(university);
            $(this).children('.user-university-department').highlight(department);
        });
    });


})