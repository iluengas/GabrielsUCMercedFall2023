document.addEventListener('DOMContentLoaded', function () {
    var sourcePage = document.referrer;
    if (sourcePage.includes('changePassword')) {
        // Trigger HTML alteration here
        // For example, change the content of an element
        alert("Password has Succesfully been changed")
    }
});