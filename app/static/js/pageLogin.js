function Auth() {
    var user = document.getElementById('user')
    var pwd = document.getElementById('pwd')

    var utilisateur = {
        nom: "Sagalle",
        pwd: "Passer"
    }

    user = user.value.toString()
    pwd = pwd.value.toString()

    if (user == "" || pwd == "") {
        alert("Veuillez renseigner tous les champs!!!")

    } else {
        if (user != utilisateur.nom || pwd != utilisateur.pwd) {
            alert("nom ou mot de passe incorrect!!!");
        } else {
            window.location.href = "../templates/affiche_user.html";
        }
    }
}