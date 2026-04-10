### 📁 El Estándar `.well-known` (RFC 8615)

El estándar **`.well-known`** define un directorio estandarizado dentro del dominio raíz de un sitio web. Su propósito es centralizar metadatos críticos, archivos de configuración e información sobre servicios, protocolos y mecanismos de seguridad del sitio.

Al utilizar la ruta fija `/.well-known/`, se facilita que navegadores, aplicaciones y herramientas de seguridad localicen información técnica de forma automática sin tener que adivinar nombres de archivos.

---

### 📋 Registro IANA y Reconocimiento con `.well-known`

La **IANA**`Internet Assigned Numbers Authority` mantiene un registro oficial de URIs bajo el estándar `.well-known`. Estos archivos permiten a los profesionales de seguridad mapear el panorama de seguridad de un objetivo de manera estructurada.

#### **Ejemplos Notables de la IANA**

|**Sufijo URI**|**Descripción**|**Referencia**|
|---|---|---|
|`security.txt`|Contacto para reportar vulnerabilidades.|RFC 9116|
|`change-password`|URL estándar para redirigir al cambio de contraseña.|W3C|
|`openid-configuration`|Detalles de configuración de OpenID Connect (OIDC).|OpenID Spec|
|`assetlinks.json`|Verificación de propiedad de apps asociadas al dominio.|Google Spec|
|`mta-sts.txt`|Política de seguridad para transporte de correo (MTA-STS).|RFC 8461|

---

#### **Caso de Estudio: `openid-configuration`**

Este archivo es parte del protocolo **OpenID Connect Discovery**. Al acceder a `https://dominio.com/.well-known/openid-configuration`, se obtiene un JSON con metadatos críticos del proveedor de identidad:

- **Endpoint Discovery:** Identifica las URLs exactas para autorización (`authorization_endpoint`), emisión de tokens (`token_endpoint`) e información de usuario (`userinfo_endpoint`).
    
- **JWKS URI:** Revela el **JSON Web Key Set**, que detalla las claves criptográficas públicas utilizadas para firmar los tokens.
    
- **Scopes y Algoritmos:** Permite conocer qué alcances se pueden solicitar (`openid`, `profile`, `email`) y qué algoritmos de firma se utilizan (ej. `RS256`).
    

---

```json
{
  "issuer": "https://example.com",
  "authorization_endpoint": "https://example.com/oauth2/authorize",
  "token_endpoint": "https://example.com/oauth2/token",
  "userinfo_endpoint": "https://example.com/oauth2/userinfo",
  "jwks_uri": "https://example.com/oauth2/jwks",
  "response_types_supported": ["code", "token", "id_token"],
  "subject_types_supported": ["public"],
  "id_token_signing_alg_values_supported": ["RS256"],
  "scopes_supported": ["openid", "profile", "email"]
}
```

La información obtenida de la `openid-configuration` El punto final ofrece múltiples oportunidades de exploración:

1. `Endpoint Discovery`:
    - `Authorization Endpoint`: Identificar la URL para solicitudes de autorización de usuario.
    - `Token Endpoint`: Encontrar la URL donde se emiten los tokens.
    - `Userinfo Endpoint`: Localizar el punto final que proporciona información al usuario.
2. `JWKS URI`: El `jwks_uri` revela el `JSON Web Key Set` (`JWKS`), detallando las claves criptográficas utilizadas por el servidor.
3. `Supported Scopes and Response Types`: Comprender qué alcances y tipos de respuesta son compatibles ayuda a mapear la funcionalidad y las limitaciones de la implementación de OpenID Connect.
4. `Algorithm Details`: La información sobre los algoritmos de firma compatibles puede ser crucial para comprender las medidas de seguridad implementadas.
---
#### **Oportunidades para el Reconocimiento Web**

Explorar estos endpoints estandarizados permite:

1. **Identificar vectores de ataque en OAuth/OIDC:** Al conocer los endpoints y métodos soportados.
    
2. **Mapear la superficie de autenticación:** Entender cómo se gestionan las identidades en la organización.
    
3. **Descubrir infraestructura oculta:** Los archivos de configuración a menudo apuntan a subdominios o servidores internos de autenticación.
    

[[web pentesting]]
