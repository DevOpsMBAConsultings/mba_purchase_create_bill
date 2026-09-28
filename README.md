# Botón Crear Factura en Compras (MBA Consultings)

Micro-módulo complementario para **Odoo 19.0 Community** desarrollado por **MBA Consultings** para restablecer el flujo ágil de creación directa de facturas de proveedor en órdenes de compra.

---

## 🚀 Problemática y Solución

En **Odoo 19**, la vista de orden de compra (`purchase.order.form`) reemplazó el botón tradicional de creación de facturas por el widget `purchase_file_uploader`, obligando a los usuarios a subir un archivo PDF/XML o entrar por flujos alternos.

Este micro-módulo resuelve ese inconveniente de usabilidad:
- **Restablece el botón directo "Crear factura":** Coloca el botón principal `Crear factura` (`action_create_invoice`) destacado (`oe_highlight`) en el encabezado de la orden de compra antes del widget de subida de archivos.
- **Acceso rápido con hotkey:** Atajo de teclado `Alt + W` (o `Ctrl/Cmd + Alt + W`) para crear la factura de proveedor de forma inmediata.
- **Condición nativa:** Solo visible cuando la orden está confirmada (`purchase`, `done`) y tiene líneas pendientes de facturar.

---

## 📦 Dependencias

* `purchase` (Odoo Core)

---

## 🛠️ Instalación

1. Clonar o colocar la carpeta `mba_purchase_create_bill` dentro de los addons de Odoo 19.
2. Actualizar la lista de aplicaciones en Odoo con modo desarrollador activo.
3. Buscar e instalar **`mba_purchase_create_bill`**.

---

## 📄 Licencia y Autor
* **Autor:** MBA Consultings (Brooks Gonzalez)
* **Licencia:** LGPL-3
* **Repositorio:** [https://github.com/DevOpsMBAConsultings/mba_purchase_create_bill](https://github.com/DevOpsMBAConsultings/mba_purchase_create_bill)
