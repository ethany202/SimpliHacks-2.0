function addEvent(muscleName) {
    window.location.href="https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_trim"
    console.log(muscleName);
}

var click = false;
function clicked() {
    click = true;
}

function released() {
    if (click) {
        let result = document.getElementsByClassName('result');
        let data = [].map.call(result, element => element.textContent);

        for (let i = 0; i < data.length; i++) {
            result[i].style.display = "list-item";
        }
        click = false;
    }
    else {
        let result = document.getElementsByClassName('result');
        let data = [].map.call(result, element => element.textContent);

        for (let i = 0; i < data.length; i++) {
            result[i].style.display = "none";
        }
    }
}

function user_search() {
    let result = document.getElementsByClassName('result');
    let data = [].map.call(result, element => element.textContent);

    let input_value = document.getElementById('search').value.toLowerCase();  

    for (let i = 0; i < data.length; i++) {
        data[i].replace("\n", "");
        data[i] = data[i].trim();
        if (data[i].substring(0, input_value.length).toLowerCase() !== input_value) {
            result[i].style.display = "none";
        }
        else {
            result[i].style.display = "list-item";
        }
    }
}