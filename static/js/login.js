var x = "cadastro"


function loginb(){
    // x = "login"
    // console.log(x)
    const left = document.getElementsByClassName("left")[0];
    const right = document.getElementsByClassName("right")[0];
    const leftTitle = document.querySelector(".left h1");
    const rightTitle = document.querySelector(".title");
    const formLeft = document.querySelector("#form-left");
    const formData = new FormData(formLeft);
    leftTitle.classList.remove("fade-in");
    rightTitle.classList.remove("fade-in");
    console.log(left.classList.contains("left_expand"));  

    if(!left.classList.contains("left_expand")){
        // formLeft.action = "{{ url_for('login.autenticar') }}"
        // colocando e removendo classes
        left.classList.remove("left_retract");
        right.classList.remove("right_expand");
        left.classList.add("left_expand");
        right.classList.add("right_retract");

        // tirando e adiconando elementos   
        document.getElementsByClassName("logoleft")[0].classList.add("disappear");
        setTimeout(() => {
            document.getElementsByClassName("logoleft")[0].style.display = "none";
            document.getElementsByClassName("logoleft")[0].classList.remove("show");
            document.getElementById("lfi").classList.remove("disappear"); 
            document.getElementById("lfi").classList.add("show"); 
        }, 1000); 
        
        document.getElementById("rgi").classList.add("disappear");
        setTimeout(() => {
            document.getElementById("rgi").style.display = "none";
            document.getElementById("rgi").classList.remove("show");
            document.getElementsByClassName("logoright")[0].classList.remove("disappear"); 
            document.getElementsByClassName("logoright")[0].classList.add("show"); 
        }, 1000); 
        // Trocando so titulos
        leftTitle.classList.add("fade-out");
        rightTitle.classList.add("fade-out");
        
        setTimeout(() => {
            leftTitle.innerHTML = "Faça login";
            rightTitle.innerHTML = "BEM VINDO DE VOLTA!";
            leftTitle.classList.remove("fade-out");
            rightTitle.classList.remove("fade-out");
            leftTitle.classList.add("fade-in");
            rightTitle.classList.add("fade-in");
    
        }, 1000);

    } else {
        document.querySelector('.base_input[name="usuariologin"]').focus(); 

        fetch('/login/dados') 
        .then(response => response.json())
        .then(users => {
            const formData = new FormData(document.querySelector('#form-left'));
            const usuario = formData.get('usuariologin');
            const senha = formData.get('passwlogin');
            if (usuario != "" && senha != ""){
                if (users[usuario] && users[usuario] === senha) {
                    console.log("Login bem-sucedido");
                    formLeft.submit();
                } else {
                    showSnackbar("Usuário ou senhas incorretos")
                }
            } else {
                showSnackbar("Preencha todos os campos");
            }
        })
        .catch(error => console.error('Erro ao obter dados:', error));
}
}

function cadb() {
    const left = document.getElementsByClassName("left")[0];
    const right = document.getElementsByClassName("right")[0];
    const leftTitle = document.querySelector(".left h1");
    const rightTitle = document.querySelector(".title");
    const formRight = document.querySelector("#form-right");
    leftTitle.classList.remove("fade-in");
    rightTitle.classList.remove("fade-in");
    console.log(left.classList.contains("left_expand"));  

    if (left.classList.contains("left_expand")) {
        // Remove as classes de expansão
        left.classList.remove("left_expand");
        right.classList.remove("right_retract");

        // Adiciona as classes para reverter as animações
        left.classList.add("left_retract");
        right.classList.add("right_expand");

        //adicionando e removendo elementos

        document.getElementById("lfi").classList.add("disappear");
        setTimeout(() => {
            document.getElementById("lfi").style.display = "none";
            document.getElementById("lfi").classList.remove("show");
            document.getElementsByClassName("logoleft")[0].classList.remove("disappear"); 
            document.getElementsByClassName("logoleft")[0].classList.add("show"); 
        }, 1000); 
        
        document.getElementsByClassName("logoright")[0].classList.add("disappear"); 
        
        setTimeout(() => {
            document.getElementsByClassName("logoright")[0].style.display = "none";
            document.getElementsByClassName("logoright")[0].classList.remove("show"); 
            document.getElementById("rgi").classList.remove("disappear");
            document.getElementById("rgi").classList.add("show");
        }, 1000); 
        //trocando titulos
        leftTitle.classList.add("fade-out");
        rightTitle.classList.add("fade-out");
        
        setTimeout(() => {
            leftTitle.innerHTML = "BEM-VINDO!";
            rightTitle.innerHTML = "Crie uma conta";
            leftTitle.classList.remove("fade-out");
            rightTitle.classList.remove("fade-out");
            leftTitle.classList.add("fade-in");
            rightTitle.classList.add("fade-in");
        }, 1000);
    } else {
        formRight.submit();
    }
}

function showSnackbar(message) {
    const snackbar = document.getElementById("snackbar");
    snackbar.innerText = message;
    snackbar.className = "snackbar show";
    
    // Remova a snackbar após 3 segundos
    setTimeout(() => {
        snackbar.className = snackbar.className.replace("show", "");
    }, 4000);

    // Foca no input de usuário ao exibir um erro
    if (message.includes("incorretos")) {
        document.querySelector('.base_input[name="usuariologin"]').focus();
    }
}
