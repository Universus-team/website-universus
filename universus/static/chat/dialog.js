var me = {};

var you = {};

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time = 0){
    var control = "";
    var date = formatAMPM(new Date());

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
    setTimeout(
        function(){
            $("ul").append(control);

        }, time);

}

function resetChat(){
    $("ul").empty();
}

function sendMessage(text) {
    if (text !== "") {
        insertChat('Я', text);
        $('#my_message').val('');
    }

}

$('textarea').keydown(function (e) {
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
});


//-- Clear Chat
resetChat();

//-- Print Messages
insertChat("Trinity", "Wake up, Neo...", 0);
insertChat("Trinity", "The Matrix has you...",2000);
insertChat("Trinity", "Knock, knock, Neo.",4000);
insertChat("Trinity", "Follow the white rabbit.",6000);
insertChat("me", "Фига себе травка о.О",9000);



//-- NOTE: No use time on insertChat.