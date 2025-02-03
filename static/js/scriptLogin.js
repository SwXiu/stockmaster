function showNotification(message) {
    const notification = document.getElementById('notification2');
    notification.textContent = message;
    notification.classList.remove('hidden');
    notification.style.display = 'block';

    setTimeout(() => {
        notification.classList.add('hidden');
        notification.style.display = 'none';
    }, 2000);
}

document.addEventListener("DOMContentLoaded", function () {
    // Referencias a los campos del formulario
    const email = document.getElementById("id_email1");
    const password = document.getElementById("id_password");
    const submitBtn = document.getElementById("botonIniciarSesion");

    // Función para validar email con expresión regular
    function validateEmail(emailValue) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(emailValue);
    }

    // Validación de la contraseña (mínimo 6 caracteres)
    function validatePassword() {
        const passwordValid = password.value.length >= 3;
        return passwordValid;
    }

    // Habilita o deshabilita el botón de inicio de sesión
    function toggleSubmitBtn() {
        const emailValid = validateEmail(email.value);
        const passwordValid = validatePassword();
        submitBtn.disabled = !(emailValid && passwordValid);
    }

    // Eventos para validar mientras el usuario escribe
    email.addEventListener("input", function () {
        validateEmail(email.value);
        toggleSubmitBtn();
    });

    password.addEventListener("input", function () {
        validatePassword();
        toggleSubmitBtn();
    });

    // Manejar el formulario de inicio de sesión
    document.querySelector('.registration-form').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevenir la acción por defecto del formulario

        // Obtener los campos de correo y contraseña
        const password = document.getElementById('id_password');

        // Enviar los datos del formulario con fetch
        fetch('/user/login/', {
            method: 'POST',
            body: new FormData(this),
        })
            .then(response => {
                if (response.ok) {
                    // Si la autenticación es exitosa
                    return response.json().then(data => {
                        if (data.redirectUrl) {
                            // Redirigir a la URL proporcionada por el backend
                            window.location.href = data.redirectUrl;
                        }
                    });
                } else {
                    // Si la autenticación falla, manejar el error
                    return response.json().then(data => {
                        if (data.error) {
                            showNotification(data.error);  // Mostrar el mensaje de error en el frontend
                            password.value = "";  // Limpiar el campo de la contraseña
                        }
                    });
                }
            })
            .catch(error => {
                console.error('Error en el login:', error);
                showNotification("Hubo un problema al procesar tu solicitud.");
            });
    });
});

function togglePasswordVisibility(inputId, iconId) {
    const passwordInput = document.getElementById(inputId);
    const toggleIcon = document.getElementById(iconId);

    console.log('Antes de cambiar:', passwordInput.type, toggleIcon.classList);

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.classList.remove("bi-eye-slash");
        toggleIcon.classList.add("bi-eye");
    } else {
        passwordInput.type = "password";
        toggleIcon.classList.remove("bi-eye");
        toggleIcon.classList.add("bi-eye-slash");
    }

    console.log('Después de cambiar:', passwordInput.type, toggleIcon.classList);
}
document.getElementById("toggle-password").addEventListener("click", function () {
    togglePasswordVisibility("id_password", "toggle-password");
});

