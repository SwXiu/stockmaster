document.addEventListener("DOMContentLoaded", function () {
    // Selector de interfaz
    const interfaceSelector = document.getElementById("interfaceSelector");
    const warehouseList = document.getElementById("warehouseList");
    const kardexTotal = document.getElementById("kardexTotal");

    // Cambiar entre vistas
    interfaceSelector.addEventListener("change", function () {
        if (this.value === "warehouseList") {
            warehouseList.style.display = "block";
            kardexTotal.style.display = "none";
        } else {
            warehouseList.style.display = "none";
            kardexTotal.style.display = "block";
        }
    });

    // Manejar los modales al hacer clic en un almacén
    document.querySelectorAll(".warehouse-card").forEach(function (card) {
        card.addEventListener("click", function () {
            let almacenId = this.getAttribute("data-id");
            let modalId = `#warehouseModal${almacenId}`;
            $(modalId).modal("show");
        });
    });
});
