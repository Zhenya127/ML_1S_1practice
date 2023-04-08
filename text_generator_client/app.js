const url = 'http://127.0.0.1:8000/';

const input = document.getElementById('gen__input');
const result = document.getElementById('gen__result');

const teamList = document.getElementById('team__list');

const genContainer = document.getElementById('gen-container');
const teamContainer = document.getElementById('team-container');

/** Make request with input's value to the url, set result's value to response */
function generateText() {
    if (input.value?.length > 0) {
        result.innerText = 'Loading...';
        fetch(url + 'predict', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: input.value })
        })
            .then((res) => res.json())
            .then((res) => {
                result.innerText = res[0]?.generated_text;
                console.log(res);
            });
    } else {
        result.innerText = '';
    }
}

/** Get team information and switch view */
function getTeamInfo() {
    fetch(url + 'about-team', {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then((res) => res.json())
        .then((res) => {
            console.log(res);
            // clear old elements
            teamList.replaceChildren([]);
            // add team members
            res?.members.forEach((el) => {
                const node = document.createElement('li');
                node.classList.add('team__list-item');

                const textNode = document.createTextNode(
                    el.full_name + ' - ' + el.role
                );
                node.appendChild(textNode);

                teamList.appendChild(node);
            });
            // switch view
            genContainer.classList.add('--hidden');
            teamContainer.classList.remove('--hidden');
        });
}

/** Switch view to app */
function showApp() {
    teamContainer.classList.add('--hidden');
    genContainer.classList.remove('--hidden');
}
