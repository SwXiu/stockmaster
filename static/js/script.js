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

const passwordField = document.getElementById('passwordValidation');
const confirmPasswordField = document.getElementById('passwordConfirmValidation');

passwordField.addEventListener('input', validatePasswords);
confirmPasswordField.addEventListener('input', validatePasswords);

function validatePasswords() {
    if (passwordField.value === confirmPasswordField.value) {
        
        
        confirmPasswordField.setCustomValidity('');
        confirmPasswordField.classList.remove('is-invalid');
        confirmPasswordField.classList.add('is-valid');
    } else {
        confirmPasswordField.setCustomValidity('Las contraseñas no coinciden.');
        confirmPasswordField.classList.remove('is-valid');
        confirmPasswordField.classList.add('is-invalid');
    }
}
