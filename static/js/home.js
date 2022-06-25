for (let i = 0; i < data.length; i++) {
    result[i].style.display = "none";
}

function clicked() {
    const input = document.getElementById('search'); 
    let result = document.getElementsByClassName('result');
    let data = [].map.call(result, element => element.textContent);

    input.addEventListener("click", () => {
        for (let i = 0; i < data.length; i++) {
            result[i].style.display = "list-item";
        }
    });
}

function user_search() {
    let result = document.getElementsByClassName('result');
    let data = [].map.call(result, element => element.textContent);

    let input_value = document.getElementById('search').value.toLowerCase();  

    for (let i = 0; i < data.length; i++) {
        if (data[i].substring(0, input_value.length).toLowerCase() !== input_value) {
            result[i].style.display = "none";
        }
        else {
            result[i].style.display = "list-item";
        }
    }
}