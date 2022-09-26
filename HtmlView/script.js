document.getElementById('myForm').addEventListener('submit', handleSubmit);
document.getElementById('image').addEventListener('change', handleImage);


let myImage = null;

function handleImage(e) {
    myImage = e.target.files[0];
    console.log(myImage);
};

function handleSubmit(e) {
    e.perventDefault();
    let user = document.getElementById('user').value;
    let content = document.getElementById('content').value;
    let form_data = new FormData();
    form_data.append('user', user);
    form_data.append('content', content);
    form_data.append('image', myImage);


    for (var [key, value] of form_data.entries()) {
        console.log(key, ': ', value);
    };
};