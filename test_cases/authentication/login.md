## Casos seleccionados para automatizar (Autenticación > Login OrangeHRM)

---

## TC-001 | [Autenticacion] | Validar login exitoso con credenciales válidas de administrador

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Funcional / Smoke  
**Estado:** ✅ Automated

### Objetivo

Verificar que un usuario administrador puede iniciar sesión en OrangeHRM con credenciales válidas y acceder al dashboard.

### Precondiciones

- La aplicación OrangeHRM está disponible
- El usuario `testAdmin1!` existe y está habilitado
- Navegador abierto en la página de login de OrangeHRM

### Pasos

| #   | Acción                                         | Datos         | Resultado esperado                                 |
| --- | ---------------------------------------------- | ------------- | -------------------------------------------------- |
| 1   | Navegar a la página de login                   | `/auth/login` | El sistema muestra el formulario de autenticación  |
| 2   | Ingresar username válido                       | testAdmin1!   | El dato se visualiza correctamente en el campo     |
| 3   | Ingresar password válida                       | testAdmin1!   | El dato se muestra oculto                          |
| 4   | Hacer click en el botón `Login`                | —             | El sistema autentica al usuario                    |
| 5   | Validar redirección posterior al inicio sesión | —             | El usuario es redirigido al dashboard de OrangeHRM |

### Resultado Esperado

- La URL final contiene `/dashboard/index`
- El usuario accede correctamente al dashboard
- La sesión queda iniciada

---

## TC-002 | [Autenticacion] | Validar login con credenciales vacías

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** ✅ Automated

### Objetivo

Verificar que OrangeHRM no permite iniciar sesión cuando los campos de username y password están vacíos.

### Precondiciones

- Navegador abierto en la página de login de OrangeHRM
- Formulario de login visible

### Pasos

| #   | Acción                                  | Datos | Resultado esperado                                      |
| --- | --------------------------------------- | ----- | ------------------------------------------------------- |
| 1   | Navegar a la página de login            | —     | El formulario de autenticación se muestra correctamente |
| 2   | Dejar vacío el campo username           | —     | El campo permanece vacío                                |
| 3   | Dejar vacío el campo password           | —     | El campo permanece vacío                                |
| 4   | Hacer click en el botón `Login`         | —     | El sistema bloquea el inicio de sesión                  |
| 5   | Validar mensajes de campos obligatorios | —     | Se muestran mensajes `Required` para ambos campos       |

### Resultado Esperado

- La URL permanece en `/auth/login`
- Se muestran 2 mensajes de validación obligatoria
- El usuario no inicia sesión

---

## TC-003 | [Autenticacion] | Validar login con username inválido

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Seguridad / Funcional  
**Estado:** ✅ Automated

### Objetivo

Verificar que OrangeHRM rechaza el inicio de sesión cuando el username es inválido y la contraseña tiene un formato válido.

### Precondiciones

- Navegador abierto en la página de login de OrangeHRM
- Formulario de login visible

### Pasos

| #   | Acción                          | Datos       | Resultado esperado                          |
| --- | ------------------------------- | ----------- | ------------------------------------------- |
| 1   | Navegar a la página de login    | —           | El formulario de autenticación se muestra   |
| 2   | Ingresar username inválido      | invalidUser | El dato se visualiza correctamente          |
| 3   | Ingresar password               | testAdmin1! | El dato se muestra oculto                   |
| 4   | Hacer click en el botón `Login` | —           | El sistema rechaza la autenticación         |
| 5   | Validar mensaje de error        | —           | Se muestra el mensaje `Invalid credentials` |

### Resultado Esperado

- La URL permanece en `/auth/login`
- Se muestra el mensaje `Invalid credentials`
- El usuario no accede al dashboard

---

## TC-004 | [Autenticacion] | Validar login con password inválida

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Seguridad / Funcional  
**Estado:** ✅ Automated

### Objetivo

Verificar que OrangeHRM rechaza el inicio de sesión cuando el username es válido pero la contraseña es incorrecta.

### Precondiciones

- El usuario `testAdmin1!` existe en el sistema
- Navegador abierto en la página de login de OrangeHRM

### Pasos

| #   | Acción                          | Datos       | Resultado esperado                          |
| --- | ------------------------------- | ----------- | ------------------------------------------- |
| 1   | Navegar a la página de login    | —           | El formulario de autenticación se muestra   |
| 2   | Ingresar username válido        | testAdmin1! | El dato se visualiza correctamente          |
| 3   | Ingresar password inválida      | invalidPass | El dato se muestra oculto                   |
| 4   | Hacer click en el botón `Login` | —           | El sistema rechaza la autenticación         |
| 5   | Validar mensaje de error        | —           | Se muestra el mensaje `Invalid credentials` |

### Resultado Esperado

- La URL permanece en `/auth/login`
- Se muestra el mensaje `Invalid credentials`
- El usuario no accede al dashboard
