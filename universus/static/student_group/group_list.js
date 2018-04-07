$(document).ready(function () {
    $("#search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#groups tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            $(this).unhighlight()
            $(this).highlight(value)
        });
    });
})