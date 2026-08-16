---
title: Naming Standard
document_id: BHG-MIG-52D57B6334D2
document_type: Standard
version: 0.1.0
status: Draft
governance_level: Standard
owner: BHG Governance Council
approval_authority: BHG Governance Council
created: '2026-07-06'
last_updated: '2026-07-06'
effective_date: null
classification: Internal
language: en
repository: BHG-GOVERNANCE
extensions:
  normalization:
    baseline: 8685abae60b176dcb3042400ebacc01b7dea97a5
    performed: '2026-08-16'
    mode: controlled_reconciliation
governed_by: []
governs: []
depends_on: []
related_to: []
---

# Naming Standard

> Estándar Corporativo de Nomenclatura de Breto's Holding Group

---

# Estado

Versión: 1.0.0

Estado: Activo

Nivel Normativo: Estándar Corporativo (S0)

---

# Propósito

Este estándar establece las reglas oficiales de nomenclatura para todos los activos del ecosistema BHG.

Su finalidad es garantizar uniformidad, reducir ambigüedades y facilitar la comprensión humana y el procesamiento automatizado.

---

# Principios

Toda nomenclatura deberá ser:

* Única.
* Descriptiva.
* Consistente.
* Escalable.
* Legible.
* Estable.
* Predecible.
* Internacionalizable cuando sea necesario.

---

# Idioma

Los nombres técnicos oficiales deberán utilizar inglés.

Podrán utilizarse nombres comerciales o marcas registradas en su idioma correspondiente.

Ejemplos:

* `REPOSITORY_STANDARD.md`
* `DOCUMENT_POLICY.md`
* `BEiA`
* `ZIVA Latam`

---

# Archivos

Los documentos normativos utilizarán:

```text
UPPER_SNAKE_CASE.md
```

Ejemplos:

* `AUTHORITY_MODEL.md`
* `NAMING_STANDARD.md`
* `AI_POLICY.md`

---

# Carpetas

Las carpetas utilizarán:

```text
kebab-case
```

cuando representen componentes técnicos.

Las carpetas de gobernanza podrán utilizar la convención ya definida por el ecosistema, por ejemplo:

```text
00-CONSTITUTION
01-POLICIES
02-STANDARDS
```

---

# Repositorios

Formato recomendado:

```text
bhg-governance
bhg-knowledge
ziva-backend
bregpersonal-app
```

Características:

* minúsculas;
* palabras separadas por guiones;
* sin espacios;
* sin caracteres especiales.

---

# APIs

Recursos:

```text
/api/users
/api/projects
/api/documents
```

Endpoints:

```text
kebab-case
```

---

# Variables de entorno

Formato obligatorio:

```text
UPPER_SNAKE_CASE
```

Ejemplos:

```text
DATABASE_URL
JWT_SECRET
SUPABASE_ANON_KEY
```

---

# Bases de datos

Tablas:

```text
snake_case
```

Columnas:

```text
snake_case
```

Claves primarias:

```text
id
```

Claves foráneas:

```text
<tabla>_id
```

---

# Código

Se aplicarán las convenciones del lenguaje de programación utilizado.

Cuando existan varios estándares posibles, prevalecerá el estándar oficial del lenguaje.

---

# Empresas

Las empresas utilizarán su denominación oficial registrada.

Ejemplos:

* Breto's Holding Group
* ZIVA Latam
* Frecuencia Latina
* BREGPersonal

---

# Productos

Los productos podrán utilizar nombres comerciales siempre que estén documentados y aprobados.

---

# IA

Los asistentes especializados seguirán una estructura uniforme.

Ejemplos:

* BEiA Core
* BEiA Finance
* BEiA Engineering
* BEiA HR
* BEiA Legal

---

# Evitar

No deberán utilizarse:

* abreviaturas ambiguas;
* nombres genéricos;
* nombres temporales como `test`, `nuevo`, `final2`, `tmp`;
* versiones en el nombre del archivo cuando exista control de versiones.

---

# Compatibilidad con BKOs

BKOs utilizará este estándar para:

* localizar activos;
* relacionar conceptos;
* detectar duplicados;
* identificar inconsistencias de nomenclatura.

---

# Compatibilidad con BEiA

BEiA deberá respetar este estándar al:

* generar nuevos documentos;
* crear proyectos;
* sugerir nombres;
* producir código.

---

# Auditoría

El incumplimiento de este estándar podrá ser detectado automáticamente por el Corporate Compliance Engine (CCE).

---

# Principio Final

Un buen nombre reduce la complejidad antes de que exista.

La nomenclatura consistente es uno de los pilares fundamentales del conocimiento organizado.

