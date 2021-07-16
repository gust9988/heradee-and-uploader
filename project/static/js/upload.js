// SLIDE IMAGE UPLOAD AND PREVIEW

$(function() {
    $("#filename").on('change', function() {
        readURL(this);
    });
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $("#preImage").attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}


// IMAGE DP

function printimgWH(img) {
    var w = document.getElementById(img).clientWidth;
    var h = document.getElementById(img).clientWidth;
}
