
//подстраивает высоту фрейма по высоту его содержимого
function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
}