const url = 'http://51.250.110.185:8000/predict';

const input = document.getElementById('gen__input');
const result = document.getElementById('gen__result');

/** Make request with input's value to the url, set result's value to response */
function generateText() {
    if (input.value?.length > 0) {
        result.innerText = 'Loading...';
        fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: input.value })
        })
            .then((res) => res.json())
            .then((res) => {
                result.innerText = res[0]?.generated_text;
                console.log(res);
            })
            .catch((err) => {
                result.innerText = 'Что-то пошло не так';
                console.log(err);
             })
    } else {
        result.innerText = '';
    }
}
