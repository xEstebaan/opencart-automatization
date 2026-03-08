## TC-001 | Login exitoso con credenciales válidas

**Módulo:** Autenticación  
**Prioridad:** Alta  
**Tipo:** Funcional / Smoke  
**Estado:** Automatizado ✅

### Objetivo
Verificar que un usuario registrado puede iniciar sesión 
con credenciales válidas y es redirigido a su cuenta.

### Precondiciones
- Usuario registrado en el sistema
- Navegador abierto en la página principal de OpenCart

### Pasos
| # | Acción | Datos |
|---|--------|-------|
| 1 | Ir a My Account > Login | — |
| 2 | Ingresar email | test@email.com |
| 3 | Ingresar contraseña | Test1234! |
| 4 | Click en "Login" | — |

### Resultado Esperado
- Usuario redirigido a `/account/account`
- Se muestra el mensaje "My Account"
- El header muestra el nombre del usuario

### Caso de prueba relacionado en código
`tests/test_login.py::test_successful_login`