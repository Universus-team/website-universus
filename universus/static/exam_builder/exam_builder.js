

function addTest() {
    var test = $('.template .test')[0].cloneNode(true);
    var testContainer = $('#testContainer');
    var testId = "test_"+testContainer.children().length;
    test.id = testId;
    testContainer.append(test);
    addPosibleAnswer($(test).find('.container-posible-answers')[0]);
    $('[data-toggle="tooltip"]').tooltip({'placement': 'top', delay: {show:1000, hide:100}});
}

function addPosibleAnswer(container) {
    var testId = $(container).parents('.test')[0].id;
    var rbId = "rb_" + testId + "_" + $(container).children().length;
    var posibleAnswer = $('.template .posible-answer-single')[0].cloneNode(true);
    $(posibleAnswer).find("input")[0].id = rbId;
    $(posibleAnswer).find("input").attr('name', testId);
    $(posibleAnswer).find("label").attr('for', rbId);
	$(container).append(posibleAnswer)
}

function removeElement(elem) {
    parent = elem.parentNode;
    parent.removeChild(elem)
}

function formatDoc(sCmd, sValue) {
	console.log(sCmd)
	document.execCommand(sCmd, false, sValue); 
}


function readExam() {
    //считывает поля страницы в объект exam и возвращает этот объект
    var exam = {
        title : $('#title').text(),
        description : $('#description').text(),
        tests:[]
    }
    //not('.template .test') используется, чтобы не обрабатывать данные шаблона,
    //используемого для формирования конструктора тестов
    $('.test').not('.template .test').each(function (i) {
        exam.tests.push({
            question: $(this).find('.question-textarea').html(),
            answers: []
        })
        $(this).find('.posible-answer').each(function () {
            exam.tests[i].answers.push({
                content : $(this).find('textarea').val(),
                correct : +$(this).find('input').is(':checked') + ''
            })
        })
    })
    return exam;
}

function sendToServer() {
    //отправляет серверу в ajax данные об "тесте",
    //который был составлен в конструкторе тестов пользователя
    //если всё произошло удачно, выводит пользователю сообщение
    //о последнем времени сохранение теста
    $.ajax({
        url: '/exambuilder_body/',
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

document.addEventListener ("keydown", function (e) {
    if (e.ctrlKey   &&  e.altKey && e.keyCode === 82) { //CTRL+ALT+R
        e.preventDefault();
        formatDoc("forecolor", "red")
    } else if (e.ctrlKey   &&  e.altKey && e.keyCode === 89) { //CTRL+ALT+Y
        e.preventDefault();
        formatDoc("forecolor", "yellow")
    } else if (e.ctrlKey   &&  e.altKey && e.keyCode === 66) { //CTRL+ALT+B
        e.preventDefault();
        formatDoc("forecolor", "blue")
    } else if (e.ctrlKey   &&  e.altKey && e.keyCode === 71) { //CTRL+ALT+G
        e.preventDefault();
        formatDoc("forecolor", "green")
    } else if (e.ctrlKey   &&  e.altKey && e.keyCode === 75) { //CTRL+ALT+K
        e.preventDefault();
        formatDoc("justifyleft")
    } 
    /*hotkeys for align text left, right, center*/
    else if (e.ctrlKey && e.keyCode === 76) { //CTRL+L
        e.preventDefault();
        formatDoc("justifyleft")
    }else if (e.ctrlKey && e.keyCode === 69) { //CTRL+E
        e.preventDefault();
        formatDoc("justifycenter")
    }else if (e.ctrlKey && e.keyCode === 82) { //CTRL+R
        e.preventDefault();
        formatDoc("justifyright")
    } 
    /*hotkeys for bold, italic and underline formating text*/
    else if (e.ctrlKey  && e.keyCode === 66) { //CTRL+B
        e.preventDefault();
        formatDoc('bold')
    } else if (e.ctrlKey  &&   e.keyCode === 73) { //CTRL+I
        e.preventDefault();
    	formatDoc("italic")
    } else if (e.ctrlKey   &&  e.keyCode === 85) { //CTRL+U
        e.preventDefault();
    	formatDoc("underline")
    }
} );


window.onload = function() {
    addTest()
};

