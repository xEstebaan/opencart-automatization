## Casos seleccionados para automatizar (Autenticación > Logout)

---

## TC-010 | [Autenticacion] | Validar cierre de sesión desde opción Logout

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Funcional / Smoke  
**Estado:** To automate

### Objetivo

Verificar que el usuario autenticado puede cerrar sesión y que el sistema finaliza su sesión correctamente.

### Precondiciones

- Usuario autenticado en OpenCart
- Usuario ubicado en cualquier página con menu

### Pasos

| #   | Acción                       | Datos | Resultado esperado                                                |
| --- | ---------------------------- | ----- | ----------------------------------------------------------------- |
| 1   | Abrir menú My Account        | —     | Se despliega submenú de cuenta                                    |
| 2   | Hacer click en opción Logout | —     | El sistema procesa cierre de sesión                               |
| 3   | Validar URL luego del cierre | —     | El usuario es redirigido a la pantalla de logout (account/logout) |
| 4   | Navegar a Login              | —     | El sistema muestra formulario de inicio de sesión (/login)        |

### Resultado Esperado

- La sesión del usuario queda cerrada
- El usuario no permanece autenticado
- Al ir a login, se muestra pantalla de inicio de sesión

---

## TC-011 | [Autenticacion] | Validar acceso a /wishlist sin sesión activa

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Seguridad / Funcional  
**Estado:** To automate

### Objetivo

Verificar que una ruta privada requiere autenticación y redirige al login cuando no existe sesión activa.

### Precondiciones

- Usuario sin sesión activa
- Navegador abierto en OpenCart

### Pasos

| #   | Acción                                    | Datos     | Resultado esperado                          |
| --- | ----------------------------------------- | --------- | ------------------------------------------- |
| 1   | Ingresar directamente la URL protegida    | /wishlist | El sistema intercepta acceso no autenticado |
| 2   | Validar redirección                       | —         | El sistema redirige a la página de login    |
| 3   | Validar mensaje o estado de autenticación | —         | Se solicita iniciar sesión para continuar   |

### Resultado Esperado

- Usuario no autenticado no puede acceder a /wishlist
- El sistema solicita iniciar sesión
- Usuario permanece en flujo de autenticación hasta loguearse
