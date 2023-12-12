window.onload = function() {
    if(document.getElementById("alert")) {
        setTimeout(function() {
            document.getElementById("alert").style.display = 'none';
        }, 5000);
    }
};
