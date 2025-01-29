(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

            form.classList.add('was-validated');
        }, false);
    });
})();

// Función para verificar si el teléfono es válido
const phoneField = document.getElementById('{{ form.telephone.id_for_label }}');
phoneField.addEventListener('input', function() {
    const phonePattern = /^[\+]?[0-9]{1,3}?[\.|\-| ]?[0-9]{4}[\.|\-| ]?[0-9]{4}$/;
    if (phonePattern.test(phoneField.value)) {
        phoneField.classList.remove('is-invalid');
        phoneField.classList.add('is-valid');
    } else {
        phoneField.classList.remove('is-valid');
        phoneField.classList.add('is-invalid');
    }
});

// Función para verificar si el email es válido
const emailField = document.getElementById('{{ form.email.id_for_label }}');
emailField.addEventListener('input', function() {
    if (emailField.validity.valid) {
        emailField.classList.remove('is-invalid');
        emailField.classList.add('is-valid');
    } else {
        emailField.classList.remove('is-valid');
        emailField.classList.add('is-invalid');
    }
});

// Función para verificar si las contraseñas coinciden
const passwordField = document.getElementById('{{ form.password.id_for_label }}');
const confirmPasswordField = document.getElementById('{{ form.password_confirm.id_for_label }}');

passwordField.addEventListener('input', validatePasswords);
confirmPasswordField.addEventListener('input', validatePasswords);

function validatePasswords() {
    if (passwordField.value == confirmPasswordField.value) {
        confirmPasswordField.setCustomValidity('');
        confirmPasswordField.classList.remove('is-invalid');
        confirmPasswordField.classList.add('is-valid');
    } else {
        confirmPasswordField.setCustomValidity('Las contraseñas no coinciden.');
        confirmPasswordField.classList.remove('is-valid');
        confirmPasswordField.classList.add('is-invalid');
    }
}
