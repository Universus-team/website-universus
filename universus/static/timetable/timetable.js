dayOfWeak = [
    {Name : 'Sunday', Id : 0},
    {Name : 'Monday', Id : 1},
    {Name : 'Tuesday', Id : 2},
    {Name : 'Wednesday', Id : 3},
    {Name : 'Thursday', Id : 4},
    {Name : 'Friday', Id : 5},
    {Name : 'Saturday', Id : 6},


]

$(function() {

    $("#timetable").jsGrid({
        height: "550px",
        width: "100%",
        filtering: true,
        editing: true,
        inserting: true,
        sorting: true,
        deleteConfirm: "Do you really want to delete the client?",
        fields: [
            { type: "control" },
            { name: "Day", type: "select", items: dayOfWeak, valueField: "Id", textField: "Name", width: 40 },
            { name: "Class number", type: "number", width: 30 },
            { name: "Subject", type: "text", width: 100 },
            { name: "Teacher", type: "text", width: 75 },
            { name: "Location", type: "text", width: 50 },

        ]
    });

});