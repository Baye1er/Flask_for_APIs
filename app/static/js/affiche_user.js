const usersList = document.querySelector('.user-body');
let output = '';
const table = document.querySelector('.table')
const url = 'http://127.0.0.1:5000/users';
const urlupdate = 'http://127.0.0.1:5000/users/';
var idUser = ""
var detai_user_btn
fetch(url)
    .then(reponse => reponse.json())
    .then(data => {
        data.forEach(user => {
            output +=
                `<tr class="user">
                <td ><input value=${user.id} type='hidden' class="btn"></td>
              <td><input value=${user.name} readonly class="btn"></td>
              <td><input value=${user.username} readonly class="btn"></td>
              <td><input value=${user.email} readonly class="btn"></td>
              <td> <input type="checkbox" class='checkbox'></td>
              <td>
              <button class="edit" onclick = "updateUser()"> Edit
              </button>
              <td>
              <button class="detailuser" onclick="detailUserFuction()"> Detail
              </button>
              </td>
              <td>
              <button class="delet" href="#"> Delete
              </button>
              </td>
            </tr>`;
        });
        usersList.innerHTML = output;

        detai_user_btn = document.querySelectorAll('.detailuser')


        const buttons = document.querySelectorAll(".btn")
            // console.log(buttons.parentNode.parentNode);
        const checkbox = document.querySelectorAll(".checkbox")
        const users = document.querySelectorAll('.user')
        var cpt = 0
            // users.forEach((user) => {
        checkbox.forEach((check) => {
            check.addEventListener('click', (e) => {
                // console.log(check.parentNode.parentNode.id);
                // console.log(e.target.parentNode.parentNode.id);
                let id_tr_even = e.target.parentNode.parentNode.id
                let id_tr_check = check.parentNode.parentNode.id
                buttons.forEach((button) => {
                    let id_tr_input = button.parentNode.parentNode.id
                    if (id_tr_check == id_tr_even && id_tr_input == id_tr_even && cpt < 4) {
                        button.removeAttribute("readonly")
                        cpt += 1
                    }
                })
                console.log("apres click " + cpt);

                buttons.forEach((button) => {
                    button.addEventListener('dblclick', () => {
                        button.removeAttribute("readonly")
                    })

                })
            })

        })
        cpt = 0


        // users.forEach((user) => {
        //     let detai_user_btn = document.querySelector('.detailuser')
        //     detai_user_btn.addEventListener('click', () => {
        //         console.log(user);
        //     })
        // })
        let name = document.getElementById('name')
        let username = document.getElementById('username')
        let email = document.getElementById('email')
        let phone = document.getElementById('phone')
        let website = document.getElementById('website')
        let address = document.getElementById('address')
        let suite = document.getElementById('suite')
        let city = document.getElementById('city')
        let zipcode = document.getElementById('zipcode')
        let company_name = document.getElementById('company_name')
        let catchPhrase = document.getElementById('catchPhrase')
        let bs = document.getElementById('bs')

        // -- -- -- -- -- -- -- --Delet User -- -- -- -- -- -- -- --
        let delet_btn = document.querySelector('.delet')
        delet_btn.addEventListener('click', (e) => {
            let id = e.target.parentNode.parentNode.children[0].children[0].value
            fetch(urlupdate + id, {
                method: 'DELETE',
                headers: { 'Content-Type': 'appliction/json' }
            })
        })

        // -- -- -- -- -- -- -- --Detail User Show-- -- -- -- -- -- -- --

        var detai_user_btn = document.querySelectorAll('.detailuser')
        for (detail_btn of detai_user_btn) {
            detail_btn.addEventListener('click', (e) => {
                idUser = (e.target.parentNode.parentNode.children[0].children[0].value);
                fetch(urlupdate + idUser)
                    .then(response => response.json())
                    .then(user => {
                        name.value = user.name
                        username.value = user.username
                        email.value = user.email
                        phone.value = user.phone
                        website.value = user.website
                        address.value = user.address.street
                        suite.value = user.address.suite
                        city.value = user.address.city
                        zipcode.value = user.address.zipcode
                        company_name.value = user.company.company_name
                        catchPhrase.value = user.company.catchPhrase
                        bs.value = user.company.bs
                    })
            })
        }

        // -- -- -- -- -- -- -- --Edit User Show-- -- -- -- -- -- -- --

        var edit_user_btn = document.querySelectorAll('.edit')
        for (edit_btn of edit_user_btn) {
            edit_btn.addEventListener('click', (e) => {
                let edit_register = document.querySelector('.edit_register')
                edit_register.style.display = 'block'
                idUser = (e.target.parentNode.parentNode.children[0].children[0].value);
                fetch(urlupdate + idUser)
                    .then(response => response.json())
                    .then(user => {
                        name.value = user.name
                        username.value = user.username
                        email.value = user.email
                        phone.value = user.phone
                        website.value = user.website
                        address.value = user.address.street
                        suite.value = user.address.suite
                        city.value = user.address.city
                        zipcode.value = user.address.zipcode
                        company_name.value = user.company.name
                        catchPhrase.value = user.company.catchPhrase
                        bs.value = user.company.bs
                        edit_register.addEventListener('click', () => {
                            var user_editer = {
                                name: name.value,
                                username: username.value,
                                email: email.value,
                                phone: phone.value,
                                website: website.value,
                                address: address.value,
                                suite: suite.value,
                                city: city.value,
                                street: 'medina',
                                zipcode: zipcode.value,
                                lat: 3.4,
                                lng: 3.8,
                                company_name: company_name.value,
                                catchPhrase: catchPhrase.value,
                                bs: bs.value
                            }
                            fetch(urlupdate + idUser, {
                                method: 'PATCH',
                                headers: { 'Content-Type': 'appliction/json' },
                                body: JSON.stringify(user_editer)
                            })
                            window.location.href = "../templates/affiche_user.html";
                        })
                    })
            })
        }












        // var cpt = 0
        // const checkbox = document.querySelectorAll('.checkbox')
        // const buttons = document.querySelectorAll(".btn")
        // buttons.forEach((button) => {
        // checkbox.forEach((check) => {
        // check.addEventListener('click', () => {
        // let position = check.getBoundingClientRect()
        // console.log("" + check.getBoundingClientRect().top)
        // })
        // 
        // })
        // 
        // button.addEventListener('dblclick', (e) => {
        // button.removeAttribute("readonly")
        // let position = button.getBoundingClientRect()
        // console.log(button.getBoundingClientRect().top);
        // })
        // checkbox.addEventListener('click', (e) => {

        // if (cpt < 4) {
        // console.log(button.firstChild) 
        // button.removeAttribute('readonly')
        // cpt += 1
        // }
        // })
        // })

        // cpt = 0
        // const user = document.querySelector('.user')
        // console.log(user);
    });



// -- -- -- -- --Post New user -- -- -- -- --
let name = document.querySelector('.name')
let username = document.querySelector('.username')
let email = document.querySelector('.email')
let phone = document.querySelector('.phone')
let website = document.querySelector('.website')
let address = document.querySelector('.address')
let suite = document.querySelector('.suite')
let city = document.querySelector('.city')
let zipcode = document.querySelector('.zipcode')
let company_name = document.querySelector('.company_name')
let catchPhrase = document.querySelector('.catchPhrase')
let bs = document.querySelector('.bs')
addNewUser_btn = document.querySelector('.addNewUser_btn')
addNewUser_btn.addEventListener('click', async(e) => {
    new_user = {
        name: name.value,
        username: username.value,
        email: email.value,
        phone: phone.value,
        website: website.value,
        address: address.value,
        suite: suite.value,
        city: city.value,
        street: 'medina',
        lat: '12',
        lng: '12',
        zipcode: zipcode.value,
        company_name: company_name.value,
        catchPhrase: catchPhrase.value,
        bs: bs.value
    }

    e.preventDefault()
    await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(new_user)
    })
    window.location.href = "../templates/affiche_user.html";
})

// -- -- -- -- --New user formulaire-- -- -- -- --

//show
function addNeuwUserFuction() {
    const addNewUser = document.querySelector('.newUser')
    addNewUser.style.top = "280px"
}

//hidden
function annulNeuwUserFuction() {
    document.querySelector('.newUser').style.top = "-1000px"
    document.querySelector('.newUser').style.transition = "0.5s"
}


// -- -- -- -- --Détail user formulaire-- -- -- -- --

//show
function detailUserFuction() {
    let edit_user = document.querySelector('.edit_user')
    let detail_user = document.querySelector('.detail_user')
    let edit_register = document.querySelector('.edit_register')
    edit_register.style.display = 'none'
    edit_user.style.display = 'none'
    detail_user.style.display = 'block'
    const detailUser = document.querySelector('.detailUserDiv')
    detailUser.style.top = "280px"
    const detailUser_btn = document.querySelectorAll('.detail_btn')
    for (edit of detailUser_btn) {
        edit.addEventListener('click', (e) => {
            console.log(e.target.parentNode.children[0]);
            e.target.parentNode.children[0].style.input = "readonly"
        })
    }
}

//hidden
function annulDetailUserFuction() {
    document.querySelector('.detailUserDiv').style.top = "-1000px"
    document.querySelector('.detailUserDiv').style.transition = "0.8s"
    const detailUser_btn = document.querySelectorAll('.detail_btn')
        // for (edit of detailUser_btn) {
        //     edit.addEventListener('click', (e) => {
        //         console.log(e.target.parentNode.children[0]);
        //         e.target.parentNode.children[0].setAttribute("readonly")
        //     })
        //     location.reload()
        // }
}

//edit user
function updateUser() {
    let detail_user = document.querySelector('.detail_user')
    let edit_user = document.querySelector('.edit_user')
    const detailUser_btn = document.querySelectorAll('.detail_btn')
    const detailUser = document.querySelector('.detailUserDiv')
    detail_user.style.display = 'none'
    edit_user.style.display = 'block'
    detailUser.style.top = "280px"
    for (edit of detailUser_btn) {
        edit.addEventListener('click', (e) => {
            e.target.parentNode.children[0].removeAttribute("readonly")
        })

    }


}


// -- -- -- -- -- --update users-- -- -- -- -- --

// function updateUser(id) {
//     id = String(id)
//     fetch(urlupdate + id).then(reponse => reponse.json())
//         .then(data => {
//             console.log(data);
//         })
// }