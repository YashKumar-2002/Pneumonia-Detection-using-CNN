function resetImage() {
    document.getElementById('image').value = '';
}

// function previewImage() {
//     var input = document.getElementById('imageInput');
//     var preview = document.getElementById('imagePreview');

//     var file = input.files[0];
//     var reader = new FileReader();

//     reader.onload = function (e) {
//         preview.src = e.target.result;
//     };

//     if (file) {
//         reader.readAsDataURL(file);
//     } else {
//         preview.src = '';
//     }
// }