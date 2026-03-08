## Casos seleccionados para automatizar (Autenticación > Registro)

Aplicando criterios de automatización (frecuencia, criticidad, assert claro, repetitividad, estabilidad y mantenimiento), se conservan únicamente los casos de mayor valor.

---

## TC-001 | [Autenticacion] | Validar registro de usuario con credenciales válidas

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Funcional / Smoke  
**Estado:** To automate

### Objetivo

Verificar que un usuario puede registrarse en el sistema con credenciales válidas.

### Precondiciones

- Navegador abierto en la página principal de OpenCart

### Pasos

| #   | Acción                                                 | Datos              | Resultado esperado                                                 |
| --- | ------------------------------------------------------ | ------------------ | ------------------------------------------------------------------ |
| 1   | Seleccionar en el menú superior la opción [My account] | —                  | Se despliega submenú con [Register] y [Login]                      |
| 2   | Hacer click en [Register]                              | —                  | El sistema redirige a `/register` y muestra formulario de registro |
| 3   | Ingresar nombre en "First Name"                        | manuel             | El dato se muestra correctamente                                   |
| 4   | Ingresar apellido en "Last Name"                       | hernandez          | El dato se muestra correctamente                                   |
| 5   | Ingresar email válido en "E-Mail"                      | test+new@test.test | El dato se muestra correctamente                                   |
| 6   | Ingresar contraseña válida en "Password"               | contrasenaReal12   | La contraseña se muestra oculta                                    |
| 7   | Seleccionar checkbox "Privacy Policy"                  | —                  | El checkbox queda seleccionado                                     |
| 8   | Click en [Continue]                                    | —                  | El sistema procesa el registro                                     |

### Resultado Esperado

- Usuario redirigido a `account/success`
- Se muestra pantalla de "Your Account Has Been Created!"

---

## TC-002 | [Autenticacion] | Validar error al dejar campo "First Name" vacío

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida y muestra error cuando el campo "First Name" está vacío.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                | Datos            | Resultado esperado                            |
| --- | ------------------------------------- | ---------------- | --------------------------------------------- |
| 1   | Dejar campo "First Name" vacío        | —                | Campo permanece vacío                         |
| 2   | Llenar "Last Name"                    | hernandez        | El dato se muestra correctamente              |
| 3   | Llenar "E-Mail"                       | test@test.test   | El dato se muestra correctamente              |
| 4   | Llenar "Password"                     | contrasenaReal12 | El dato se muestra correctamente              |
| 5   | Seleccionar checkbox "Privacy Policy" | —                | Checkbox queda seleccionado                   |
| 6   | Click en [Continue]                   | —                | Se muestra mensaje de error para "First Name" |

### Resultado Esperado

- Se muestra mensaje de error de validación para "First Name"
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-003 | [Autenticacion] | Validar error al dejar campo "Last Name" vacío

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida y muestra error cuando el campo "Last Name" está vacío.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                | Datos            | Resultado esperado                           |
| --- | ------------------------------------- | ---------------- | -------------------------------------------- |
| 1   | Llenar "First Name"                   | manuel           | El dato se muestra correctamente             |
| 2   | Dejar campo "Last Name" vacío         | —                | Campo permanece vacío                        |
| 3   | Llenar "E-Mail"                       | test@test.test   | El dato se muestra correctamente             |
| 4   | Llenar "Password"                     | contrasenaReal12 | El dato se muestra correctamente             |
| 5   | Seleccionar checkbox "Privacy Policy" | —                | Checkbox queda seleccionado                  |
| 6   | Click en [Continue]                   | —                | Se muestra mensaje de error para "Last Name" |

### Resultado Esperado

- Se muestra mensaje de error de validación para "Last Name"
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-004 | [Autenticacion] | Validar error al dejar campo "E-Mail" vacío

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida y muestra error cuando el campo "E-Mail" está vacío.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                | Datos            | Resultado esperado                        |
| --- | ------------------------------------- | ---------------- | ----------------------------------------- |
| 1   | Llenar "First Name"                   | manuel           | El dato se muestra correctamente          |
| 2   | Llenar "Last Name"                    | hernandez        | El dato se muestra correctamente          |
| 3   | Dejar campo "E-Mail" vacío            | —                | Campo permanece vacío                     |
| 4   | Llenar "Password"                     | contrasenaReal12 | El dato se muestra correctamente          |
| 5   | Seleccionar checkbox "Privacy Policy" | —                | Checkbox queda seleccionado               |
| 6   | Click en [Continue]                   | —                | Se muestra mensaje de error para "E-Mail" |

### Resultado Esperado

- Se muestra mensaje de error de validación para "E-Mail"
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-005 | [Autenticacion] | Validar error al dejar campo "Password" vacío

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida y muestra error cuando el campo "Password" está vacío.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                | Datos          | Resultado esperado                          |
| --- | ------------------------------------- | -------------- | ------------------------------------------- |
| 1   | Llenar "First Name"                   | manuel         | El dato se muestra correctamente            |
| 2   | Llenar "Last Name"                    | hernandez      | El dato se muestra correctamente            |
| 3   | Llenar "E-Mail"                       | test@test.test | El dato se muestra correctamente            |
| 4   | Dejar campo "Password" vacío          | —              | Campo permanece vacío                       |
| 5   | Seleccionar checkbox "Privacy Policy" | —              | Checkbox queda seleccionado                 |
| 6   | Click en [Continue]                   | —              | Se muestra mensaje de error para "Password" |

### Resultado Esperado

- Se muestra mensaje de error de validación para "Password"
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-006 | [Autenticacion] | Validar error al no seleccionar "Privacy Policy"

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida y muestra error cuando el checkbox "Privacy Policy" no está seleccionado.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                   | Datos            | Resultado esperado                 |
| --- | ---------------------------------------- | ---------------- | ---------------------------------- |
| 1   | Llenar "First Name"                      | manuel           | El dato se muestra correctamente   |
| 2   | Llenar "Last Name"                       | hernandez        | El dato se muestra correctamente   |
| 3   | Llenar "E-Mail"                          | test@test.test   | El dato se muestra correctamente   |
| 4   | Llenar "Password"                        | contrasenaReal12 | El dato se muestra correctamente   |
| 5   | NO seleccionar checkbox "Privacy Policy" | —                | Checkbox permanece sin seleccionar |
| 6   | Click en [Continue]                      | —                | Se muestra mensaje de error        |

### Resultado Esperado

- Se muestra mensaje de error: "You must agree to the Privacy Policy"
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-007 | [Autenticacion] | Validar error con formato de correo inválido

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema valida el formato del email y rechaza correos inválidos.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                | Datos            | Resultado esperado                     |
| --- | ------------------------------------- | ---------------- | -------------------------------------- |
| 1   | Llenar "First Name"                   | manuel           | El dato se muestra correctamente       |
| 2   | Llenar "Last Name"                    | hernandez        | El dato se muestra correctamente       |
| 3   | Ingresar email inválido en "E-Mail"   | testinvalid@     | El dato se muestra en el campo         |
| 4   | Llenar "Password"                     | contrasenaReal12 | El dato se muestra correctamente       |
| 5   | Seleccionar checkbox "Privacy Policy" | —                | Checkbox queda seleccionado            |
| 6   | Click en [Continue]                   | —                | Se muestra mensaje de error de formato |

### Resultado Esperado

- Se muestra mensaje de error de email inválido
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-008 | [Autenticacion] | Validar rechazo de correo ya registrado

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema no permite registrar un correo que ya existe.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Existe un usuario registrado con email: `existing@test.com`

### Pasos

| #   | Acción                                   | Datos             | Resultado esperado               |
| --- | ---------------------------------------- | ----------------- | -------------------------------- |
| 1   | Llenar "First Name"                      | newuser           | El dato se muestra correctamente |
| 2   | Llenar "Last Name"                       | prueba            | El dato se muestra correctamente |
| 3   | Ingresar email ya registrado en "E-Mail" | existing@test.com | El dato se muestra correctamente |
| 4   | Llenar "Password"                        | contrasenaReal12  | El dato se muestra correctamente |
| 5   | Seleccionar checkbox "Privacy Policy"    | —                 | Checkbox queda seleccionado      |
| 6   | Click en [Continue]                      | —                 | Se muestra mensaje de error      |

### Resultado Esperado

- Se muestra mensaje de error de email ya existente
- Formulario no se envía
- Usuario permanece en la página de registro

---

## TC-009 | [Autenticacion] | Validar error contraseña menor a 4 caracteres

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Validación / Funcional  
**Estado:** To automate

### Objetivo

Verificar que el sistema rechaza contraseñas con menos de 4 caracteres.

### Precondiciones

- Navegador abierto en la página de registro (`/register`)
- Formulario de registro visible

### Pasos

| #   | Acción                                   | Datos         | Resultado esperado               |
| --- | ---------------------------------------- | ------------- | -------------------------------- |
| 1   | Llenar "First Name"                      | manuel        | El dato se muestra correctamente |
| 2   | Llenar "Last Name"                       | hernandez     | El dato se muestra correctamente |
| 3   | Llenar "E-Mail"                          | test@test.com | El dato se muestra correctamente |
| 4   | Ingresar contraseña menor a 4 caracteres | abc           | El dato se muestra oculto        |
| 5   | Seleccionar checkbox "Privacy Policy"    | —             | Checkbox queda seleccionado      |
| 6   | Click en [Continue]                      | —             | Se muestra mensaje de error      |

### Resultado Esperado

- Se muestra mensaje de error por longitud mínima de contraseña
- Formulario no se envía
- Usuario permanece en la página de registro

---

## Casos removidos por baja rentabilidad de automatización

- Validaciones de solo espacios en nombre/apellido (alto mantenimiento, bajo impacto)
- Reglas de no permitir números en nombre/apellido (no críticas para el negocio)
- Límite exacto de 32 caracteres en nombre/apellido (baja frecuencia y menor criticidad)
- Caso de duplicidad nombre/apellido con email distinto (cobertura funcional ya implícita en flujo exitoso + email único)
