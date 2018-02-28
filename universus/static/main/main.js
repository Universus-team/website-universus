

window.onload = function (ev) {
    obj = document.getElementById("main_content");
    obj.style.height = obj.contentWindow.document.body.scrollHeight +15+ 'px';
    setInterval(
        function () {
            obj.style.height = obj.contentWindow.document.body.scrollHeight +15+ 'px';
        },
        300
    )

}