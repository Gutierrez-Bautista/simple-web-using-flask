const form = document.getElementById('test-form')
const input = document.getElementById('user-id')
const submitBtn = document.getElementById('submit-btn')

const allUsers = document.getElementById('get-all-users')

function showUserInfo (data, whereInsert) {
    const fragment = document.createDocumentFragment()
    
    for (key in data) {
        let inf = document.createElement('P')
        inf.innerHTML = `${key}: <span class="bold">${data[key]}</span>`
        fragment.appendChild(inf)
    }

    whereInsert.appendChild(fragment)
}

submitBtn.addEventListener('click', (evt) => {
    evt.preventDefault()

    const getUser = async () => {
        let url = `http://localhost:5000/api/v1/user?user_id=${input.value}`;
        const response = await fetch(url);
        const data = await response.json();

        
        if (data["status"]) {
            return Promise.reject(data)
        }
        
        return Promise.resolve(data)
    }


    const userSection = document.getElementById('user-info')
    userSection.innerHTML = ''
    getUser()
        .then(res => showUserInfo(res, userSection))
        .catch(error => userSection.innerHTML = `<p>User Not Found</p>`)
})

allUsers.addEventListener('click', (evt) => {
    fetch('http://localhost:5000/api/v1/users')
        .then(response => response.json())
        .then(data => {
            const userSection = document.getElementById('user-info')
            userSection.innerHTML = ''
            data.forEach(element => {
                showUserInfo(element, userSection)
            });
        })
    }
)