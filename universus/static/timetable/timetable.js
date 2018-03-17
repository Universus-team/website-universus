dayOfWeak = [
    {Name : 'Sunday', Id : 0},
    {Name : 'Monday', Id : 1},
    {Name : 'Tuesday', Id : 2},
    {Name : 'Wednesday', Id : 3},
    {Name : 'Thursday', Id : 4},
    {Name : 'Friday', Id : 5},
    {Name : 'Saturday', Id : 6},


]

/*timetableData = [
    {"Day":1, "Class number" : 1, "Subject" : "Java", "Teacher" : "John", "Location" : "anywhere"},
    {"Day":1, "Class number" : 2, "Subject" : "Java", "Teacher" : "John", "Location" : "anywhere"},
    {"Day":2, "Class number" : 2, "Subject" : "C#", "Teacher" : "John", "Location" : "anywhere"},
    {"Day":2, "Class number" : 3, "Subject" : "Java", "Teacher" : "John", "Location" : "anywhere"},
    {"Day":3, "Class number" : 1, "Subject" : "C#", "Teacher" : "John", "Location" : "anywhere"},
]*/

$(function() {

    $("#timetable").jsGrid({
        height: "550px",
        width: "100%",
        inserting: true,
        editing: true,
        sorting: true,
        filtering: true,
        // data:timetableData,
        deleteConfirm: "Do you really want to delete the client?",
        fields: [
            { name: "Day", type: "select", items: dayOfWeak, valueField: "Id", textField: "Name", width: 40 },
            { name: "Class number", type: "number", width: 30 },
            { name: "Subject", type: "text", width: 100 },
            { name: "Teacher", type: "text", width: 75 },
            { name: "Location", type: "text", width: 50 },
            { type: "control" },

        ],
        controller: {
            loadData:  function(filter) {
                        var d = $.Deferred();
                        $.ajax({
                            type: "GET",
                            url: "/timetable_body/get",
                            data: filter
                        }).done(function(result) {
                            d.resolve($.map(result, function(item) {
                                return $.extend(item.fields, { id: item.pk });
                            }));
                        });
                        return d.promise();
                    },
        }
    });

});