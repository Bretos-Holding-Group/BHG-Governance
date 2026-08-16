---
title: Testing Standard
document_id: BHG-MIG-3D56813EDF52
document_type: Engineering Standard
version: 0.1.0
status: Draft
governance_level: Engineering
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
---

# Testing Standard

> Estándar Corporativo de Pruebas de Breto's Holding Group

---

# Estado

Versión: 1.0.0

Estado: Activo

Nivel Normativo: Estándar de Ingeniería (E2)

---

# Propósito

Este estándar establece los principios y requisitos para las actividades de verificación y validación del software desarrollado dentro del ecosistema BHG.

Su objetivo es reducir riesgos, aumentar la confianza en los cambios y preservar la estabilidad de los sistemas durante todo su ciclo de vida.

---

# Alcance

Aplica a:

* aplicaciones;
* APIs;
* servicios;
* bibliotecas;
* automatizaciones;
* agentes de IA;
* BKOs;
* BEiA;
* cualquier componente de software desarrollado por el Holding.

---

# Principios

Toda estrategia de pruebas deberá ser:

* Planificada.
* Repetible.
* Automatizable cuando sea posible.
* Trazable.
* Documentada.
* Proporcional al riesgo.
* Mantenible.

---

# Objetivo de las pruebas

Las pruebas buscan proporcionar evidencia de que el sistema cumple los requisitos establecidos.

No pueden demostrar la ausencia absoluta de errores.

---

# Pirámide de pruebas

La estrategia de pruebas priorizará, cuando sea aplicable:

1. Pruebas unitarias.
2. Pruebas de integración.
3. Pruebas de sistema.
4. Pruebas de aceptación.

El equilibrio entre niveles dependerá de la naturaleza del proyecto.

---

# Automatización

Las pruebas automatizadas serán la opción preferente para verificaciones repetitivas.

Las pruebas manuales se reservarán principalmente para escenarios exploratorios, de experiencia de usuario o cuando la automatización no sea viable.

---

# Cobertura

La cobertura de pruebas es un indicador útil, pero no constituye por sí sola una medida suficiente de calidad.

Se priorizará la calidad de las pruebas sobre el porcentaje de cobertura.

---

# Gestión de defectos

Todo defecto identificado deberá:

* registrarse;
* clasificarse según su impacto;
* corregirse o aceptarse mediante una decisión documentada;
* verificarse antes de su cierre.

---

# Pruebas antes de producción

Todo cambio deberá superar las pruebas definidas para el nivel de riesgo correspondiente antes de su despliegue en producción.

---

# Regresión

Siempre que sea posible deberán existir pruebas que detecten regresiones provocadas por cambios futuros.

---

# Integración continua

Las pruebas automatizadas deberán integrarse en los procesos de integración continua cuando sea técnicamente viable.

---

# Integración con BKOs

BKOs conservará el conocimiento relacionado con estrategias de prueba, incidencias, resultados y lecciones aprendidas para facilitar la evolución futura de los sistemas.

---

# Integración con BEiA

BEiA podrá asistir en:

* generación de casos de prueba;
* revisión de cobertura;
* análisis de riesgos;
* identificación de escenarios faltantes;
* interpretación de resultados.

La aprobación final corresponderá siempre a la autoridad competente.

---

# Cumplimiento

Todo activo de software deberá cumplir este estándar antes de considerarse apto para producción.

---

# Principio Final

Las pruebas no existen para demostrar que un sistema es perfecto.

Existen para generar la confianza necesaria que permita evolucionarlo de forma segura, controlada y sostenible.

