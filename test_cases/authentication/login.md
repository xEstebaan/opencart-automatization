## Casos seleccionados para automatizar (Autenticación > Login)

---

## TC-001 | [Autenticacion] | Validar login exitoso con credenciales válidas

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Funcional / Smoke  
**Estado:** To automate

### Objetivo

Verificar que un usuario registrado puede iniciar sesión con credenciales válidas y acceder a su cuenta.

### Precondiciones

- Usuario registrado en el sistema
- Navegador abierto en la página principal de OpenCart

### Pasos

| #   | Acción                     | Datos          | Resultado esperado                                |
| --- | -------------------------- | -------------- | ------------------------------------------------- |
| 1   | Ir a My Account > Login    | —              | El sistema muestra formulario de login            |
| 2   | Ingresar correo válido     | test@email.com | El dato se muestra correctamente                  |
| 3   | Ingresar contraseña válida | Test1234!      | El dato se muestra oculto                         |
| 4   | Click en "Login"           | —              | El sistema autentica y redirige al área de cuenta |

### Resultado Esperado

- Usuario redirigido a `/account/account` o `/account`
- Se muestra pantalla de cuenta del usuario
- La sesión queda iniciada

---

## TC-002 | [Autenticacion] | Validar que el correo exige formato válido

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el campo de correo no acepta formato inválido al intentar iniciar sesión.

### Precondiciones

- Navegador abierto en la página de login
- Formulario de login visible

### Pasos

| #   | Acción                          | Datos        | Resultado esperado                |
| --- | ------------------------------- | ------------ | --------------------------------- |
| 1   | Ir a My Account > Login         | —            | El formulario de login se muestra |
| 2   | Ingresar correo con mal formato | testinvalid@ | El dato se muestra en el campo    |
| 3   | Ingresar contraseña cualquiera  | Test1234!    | El dato se muestra oculto         |
| 4   | Click en "Login"                | —            | El sistema rechaza autenticación  |

### Resultado Esperado

- Usuario no puede iniciar sesión con correo inválido
- Se muestra mensaje de error de autenticación/validación
- Usuario permanece en la página de login

---

## TC-003 | [Autenticacion] | Validar login con contraseña incorrecta y correo correcto

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Seguridad / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema impide iniciar sesión cuando el correo es correcto pero la contraseña es incorrecta.

### Precondiciones

- Existe un usuario registrado con correo válido
- Navegador abierto en la página de login

### Pasos

| #   | Acción                         | Datos               | Resultado esperado                |
| --- | ------------------------------ | ------------------- | --------------------------------- |
| 1   | Ir a My Account > Login        | —                   | El formulario de login se muestra |
| 2   | Ingresar correo registrado     | registered@test.com | El dato se muestra correctamente  |
| 3   | Ingresar contraseña incorrecta | WrongPass123        | El dato se muestra oculto         |
| 4   | Click en "Login"               | —                   | El sistema rechaza autenticación  |

### Resultado Esperado

- Se muestra mensaje de credenciales inválidas
- Usuario no accede al área privada
- Usuario permanece en la página de login

---

## TC-004 | [Autenticacion] | Validar login con campos vacíos

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida campos obligatorios cuando se intenta iniciar sesión sin correo y sin contraseña.

### Precondiciones

- Navegador abierto en la página de login
- Formulario de login visible

### Pasos

| #   | Acción                     | Datos | Resultado esperado                      |
| --- | -------------------------- | ----- | --------------------------------------- |
| 1   | Ir a My Account > Login    | —     | El formulario de login se muestra       |
| 2   | Dejar campo correo vacío   | —     | Campo permanece vacío                   |
| 3   | Dejar campo password vacío | —     | Campo permanece vacío                   |
| 4   | Click en "Login"           | —     | El sistema muestra error y no autentica |

### Resultado Esperado

- Se muestra mensaje de error de autenticación/validación
- Usuario no inicia sesión
- Usuario permanece en la página de login
