var me = {};

var you = {};

function formatDate(date) {
    return moment(date).format('HH:mm DD-MM-YYYY');
}

//-- No use time. It is a javaScript effect.
function insertChat(who, text, date_msg){
    var control = "";
    var date = formatDate(date_msg);

    if (who == "me" || who == 'я'){
        control = '<li style="width:100%;">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                  '</li>';

    }else{
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';
    }
    $("#messages").append(control);


}

function resetChat(){
    $("ul").empty();
}

function sendMessage(text) {
    if (text !== "") {
        $('#my_message').val('');
        $.ajax({
            url: window.location.href,
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'getNewMessages' : false,
                'getDialog' : false,
                'sendMessage' : true,
                'message' : text
            }),
            dataType: 'text',
            success: function(result) {
                data = JSON.parse(result)
                if (data['result_send']) {
                    insertChat("me",text, 0);
                    gotoBottom('messages')
                }

        }
    });
    }
}

function loadAllMessages(fromId, toId) {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'getNewMessages' : false,
            'getDialog' : true,
            'sendMessage' : false
        }),
        dataType: 'text',
        success: function(result) {
            var data = JSON.parse(result);
            if (data['dialog']) {
                count_msg = data['dialog'].length
                for (var i = 0; i < count_msg; i++) {
                    var item = data['dialog'][i];
                    if (item['From'] === fromId) {
                        var date = Date.parse(item['Date']);
                        insertChat('me', item['Message'], date)
                    } else {
                        var date = Date.parse(item['Date']);
                        insertChat('собеседник', item['Message'], date)
                    }
                }
                gotoBottom('messages')
            }
        }

    })
}

function loadNewMessages(fromId, toId) {
    $.ajax({
        url: window.location.href,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'getNewMessages' : true,
            'getDialog' : false,
            'sendMessage' : false
        }),
        dataType: 'text',
        success: function(result) {
            var data = JSON.parse(result);
            if (data['newMessage']) {
                count_msg = data['messages'].length
                for (var i = 0; i < count_msg; i++) {
                    var item = data['messages'][i];
                    if (item['From'] === fromId) {
                        var date = Date.parse(item['Date']);
                        insertChat('me', item['Message'], date)
                    } else {
                        var date = Date.parse(item['Date']);
                        insertChat('собеседник', item['Message'], date)
                    }
                }
                gotoBottom('messages')
            }
        }

    })
}

function gotoBottom(id){
   var element = document.getElementById(id);
   element.scrollTop = element.scrollHeight - element.clientHeight;
}

/*$('textarea').keydown(function (e) {
    console.log('keydown');
    if (e.keyCode === 13 && e.ctrlKey) {
        $(this).val(function(i,val){
            return val + "\n";
        });
    }
}).keypress(function(e){
    console.log('keypress');
    if (e.keyCode === 13 && !e.ctrlKey) {
        alert('submit');
        sendMessage($(this).val())
        return false;
    }
});*/



$(document).ready(function () {
    resetChat();
    loadAllMessages(+$('#fromUserId').text(), +$('#toUserId').text())
    setTimeout(function () {
        setInterval(function () {
            loadNewMessages(+$('#fromUserId').text(), +$('#toUserId').text())
        }, 3000)
    }, 10000)

})