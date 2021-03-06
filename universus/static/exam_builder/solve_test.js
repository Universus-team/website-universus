
function sendToServer() {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(readExam()),
        dataType: 'text',
        success: function(result) {
            data = JSON.parse(result)
            if (data['success']) {
                window.location.href = '../../list/'
            }
        }
    });
}

function readExam() {
    tests = []
    $('.test').not('.template .test').each(function (i) {

        tests.push({
            question: $(this).find('.question').html().trim(),
            answers: []
        })

        $(this).find('.posible-answer').each(function () {
            tests[i].answers.push({
                content : $(this).find('.answer').text().trim(),
                correct : +$(this).find('input').is(':checked') + ''
            })
        })
    })
    return tests
}