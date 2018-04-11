
function sendToServer() {
    //отправляет серверу в ajax данные об "тесте",
    //который был составлен в конструкторе тестов пользователя
    //если всё произошло удачно, выводит пользователю сообщение
    //о последнем времени сохранение теста
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(readExam()),
        dataType: 'text',
        success: function(result) {
            data = JSON.parse(result)
            $('#saveMessage').text(data.message)
        }
    });
}



window.onload = function() {
    addTest()
};

