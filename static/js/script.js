function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.classList.remove('hidden');
    notification.style.display = 'block';

    // Ocultar la notificación después de 3 segundos
    setTimeout(() => {
        notification.classList.add('hidden');
        notification.style.display = 'none';
    }, 3000);
}

flatpickr("#id_birth_date", {
    dateFormat: "d/m/Y",
    altInput: true,
    altFormat: "d/m/Y",
    locale: "es",
    maxDate: "today",
});

const provinces = [
    "Álava", "Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz", "Barcelona", "Burgos", "Cáceres",
    "Cádiz", "Cantabria", "Castellón", "Ciudad Real", "Córdoba", "Cuenca", "Girona", "Granada", "Guadalajara", "Gipuzkoa",
    "Huelva", "Huesca", "Islas Baleares", "Jaén", "Madrid", "Málaga", "Murcia", "Navarra", "Ourense", "Palencia", "Las Palmas",
    "Pontevedra", "La Rioja", "Salamanca", "Segovia", "Sevilla", "Soria", "Tarragona", "Santa Cruz de Tenerife", "Teruel",
    "Toledo", "Valencia", "Valladolid", "Vizcaya", "Zamora", "Zaragoza"
];

const addressInput = document.getElementById('id_address');
const suggestionsBox = document.getElementById('suggestions');

function showSuggestions() {
    const query = addressInput.value.toLowerCase();
    suggestionsBox.innerHTML = '';
    suggestionsBox.style.display = 'none';

    if (query.length > 0) {
        const filteredProvinces = provinces.filter(province => province.toLowerCase().startsWith(query));

        if (filteredProvinces.length > 0) {
            suggestionsBox.style.display = 'block';

            filteredProvinces.forEach(province => {
                const suggestionItem = document.createElement('div');
                suggestionItem.textContent = province;
                suggestionItem.classList.add('suggestion-item');

                suggestionItem.addEventListener('click', function () {
                    addressInput.value = province;
                    suggestionsBox.innerHTML = '';
                    suggestionsBox.style.display = 'none';
                });

                suggestionsBox.appendChild(suggestionItem);
            });
        }
    } else {

        suggestionsBox.style.display = 'block';
        provinces.forEach(province => {
            const suggestionItem = document.createElement('div');
            suggestionItem.textContent = province;
            suggestionItem.classList.add('suggestion-item');

            suggestionItem.addEventListener('click', function () {
                addressInput.value = province;
                suggestionsBox.innerHTML = '';
                suggestionsBox.style.display = 'none';
            });

            suggestionsBox.appendChild(suggestionItem);
        });
    }
}


addressInput.addEventListener('focus', function () {
    showSuggestions();
});


addressInput.addEventListener('input', function () {
    showSuggestions();
});


addressInput.addEventListener('blur', function () {
    setTimeout(() => {
        suggestionsBox.style.display = 'none';
    }, 200);
});

document.addEventListener('DOMContentLoaded', function () {
    // Referencias a los campos del formulario
    const username = document.getElementById('id_username');
    const email = document.getElementById('id_email');
    const telephone = document.getElementById('id_telephone');
    const address = document.getElementById('id_address');
    const birthDate = document.getElementById('id_birth_date');
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    const submitBtn = document.querySelector('.btn-primary');

    // Función para validar email con una expresión regular básica
    function validateEmail(emailValue) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(emailValue);
    }

    // Función para validar la fecha de nacimiento en formato DD-MM-YY
    function validateBirthDate(dateValue) {
        // Comprueba que el formato sea exactamente DD/MM/YY
        const re = /^\d{2}\/\d{2}\/\d{4}$/;
        return re.test(dateValue);
    }

    // Función auxiliar que cambia el color del borde del contenedor del campo según la validez
    function validateField(field, isValid) {
        const container = field.closest('.input-container');
        if (container) {
            container.style.borderColor = isValid ? 'green' : 'red';
        }
    }

    function validateUsername() {
        const usernameValid = username.value.trim() !== '' && checkFieldExists(username, "username");
        validateField(username, usernameValid);
        return usernameValid;
    }

    function validateEmailField() {
        const emailValid = validateEmail(email.value) && checkFieldExists(email, "email");
        validateField(email, emailValid);
        return emailValid;
    }

    function validateTelephone() {
        const telephoneValid = telephone.value.trim() !== '' && checkFieldExists(telephone, "telephone");
        validateField(telephone, telephoneValid);
        return telephoneValid;
    }

    // Función para validar el campo address
    function validateAddress() {
        const addressValid = address.value.trim() !== '';
        validateField(address, addressValid);
        return addressValid;
    }

    // Función para validar el campo birthDate
    function validateBirthDateField() {
        const birthDateValid = validateBirthDate(birthDate.value.trim());
        validateField(birthDate, birthDateValid);
        return birthDateValid;
    }

    function validatePassword1() {
        const password1Valid = password1.value.length >= 6;
        validateField(password1, password1Valid);
        return password1Valid;
    }

    function validatePassword2() {
        const password2Valid = (password2.value === password1.value && password2.value !== '' && password2.value.length >= 6);
        validateField(password2, password2Valid);
        return password2Valid;
    }

    function checkFieldExists(field, fieldType) {
        return fetch(`/user/check-field/?value=${encodeURIComponent(field.value.trim())}&type=${fieldType}`)
            .then(response => response.json())
            .then(data => {
                if (data.exists) {
                    validateField(field, false);
                    showNotification(`El ${fieldType} ya está en uso`);
                    return false;
                } else {
                    validateField(field, true);
                    console.log(`${fieldType} disponible.`);
                    return true;
                }
            })
            .catch(error => {
                console.error("Error en la verificación AJAX:", error);
                return false;
            });
    }


    function toggleSubmitBtn() {
        submitBtn.disabled = !(validateUsername() && validateEmailField() && validateTelephone() && validateAddress() && validateBirthDateField() && validatePassword1() && validatePassword2());
    }

    username.addEventListener('input',async  function () {
        await validateUsername();
        toggleSubmitBtn();
    });

    email.addEventListener('input',async  function () {
        await validateEmailField();
        toggleSubmitBtn();
    });

    telephone.addEventListener('input',async  function () {
        await validateTelephone();
        toggleSubmitBtn();
    });

    address.addEventListener('input', function () {
        validateAddress();
        toggleSubmitBtn();
    });

    birthDate.addEventListener('input', function () {
        validateBirthDateField();
        toggleSubmitBtn();
    });

    password1.addEventListener('input', function () {
        validatePassword1();
        validatePassword2()
        toggleSubmitBtn();
    });

    password2.addEventListener('input', function () {
        validatePassword2();
        toggleSubmitBtn();
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

document.getElementById("toggle-password1").addEventListener("click", function () {
    togglePasswordVisibility("id_password1", "toggle-password1");
});
document.getElementById("toggle-password2").addEventListener("click", function () {
    togglePasswordVisibility("id_password2", "toggle-password2");
});