
function formatDoc(sCmd, sValue) {
	console.log(sCmd)
	document.execCommand(sCmd, false, sValue);
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