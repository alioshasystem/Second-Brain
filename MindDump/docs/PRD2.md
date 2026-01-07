# Product Requirements Document (PRD)

## MindDump — Cognitive Notes App

**Versión:** 0.2 (Scope redefinido)
**Plataforma:** iOS (Swift)
**Dispositivo objetivo:** iPhone

---

## 1. Overview

### 1.1 Propósito

MindDump es una aplicación móvil de notas diseñada para **pensar**, no solo para escribir. Su objetivo es ayudar al usuario a capturar ideas rápidamente y permitir que el sistema procese esas notas para **extraer estructura cognitiva**: conceptos, intenciones y pendientes (to‑do’s), que evolucionan con el tiempo.

La app funciona como un **segundo cerebro**, donde el valor no está únicamente en cada nota individual, sino en las relaciones que emergen entre ellas.

---

### 1.2 Propuesta de Valor

* Captura rápida de ideas (texto y voz)
* Procesamiento automático de notas para:

  * conceptos personales
  * intenciones cognitivas
  * to‑do’s
* Organización emergente sin fricción manual
* Priorización implícita mediante bookmarks
* Asociación visual mediante imágenes/pinturas

---

### 1.3 Usuario Objetivo

Personas que:

* piensan escribiendo o hablando
* generan ideas dispersas a lo largo del día
* quieren claridad, no carpetas manuales
* valoran estructura emergente más que organización rígida

---

## 2. User Journey (Alto Nivel)

1. **Onboarding / Tutorial**
   Introduce el valor de la app y cómo el sistema ayuda a pensar mejor.

   > *El contenido del tutorial falta por definirse en esta versión del PRD.*

2. **Autenticación**
   Inicio de sesión mediante:

   * Google
   * Email / método tradicional

3. **Vista Principal — Todas las Notas**
   Acceso al sistema completo de notas y navegación a vistas derivadas.

4. **Exploración Cognitiva**
   Navegación entre:

   * Conceptos
   * Intenciones
   * To‑do’s

---

## 3. Entidades Principales del Sistema

### 3.1 Nota

La **nota** es la unidad central del sistema.

* Se representa como un **JSON estructurado**
* Puede contener:

  * texto
  * bloques (futuro)
  * metadatos
* Es **editable**
* Es la **fuente única de verdad**

Cada vez que una nota:

* se crea
* se edita
* se elimina
* se marca o desmarca como bookmark

→ el sistema vuelve a ejecutar el pipeline de procesamiento que se hara en el backend.

---

### 3.2 Concepto

* Entidad **generada automáticamente** por el sistema
* Representa agrupaciones semánticas personales
* Por el momento no es editable por el usuario en esta versión
* Puede:

  * agrupar múltiples notas
  * evolucionar con el tiempo

> El comportamiento multi‑idioma de los conceptos queda **fuera de definición** en este PRD.

---

### 3.3 Intención

* Categoría cognitiva **predefinida**
* Set finito controlado por el sistema
* Cada nota tiene **exactamente una intención**

Ejemplos:

* Acción
* Aprender
* Planear
* Crear
* Reflexionar

Las intenciones se usan principalmente para:

* lógica backend
* vistas de utilidad
* flujos futuros

De momomento solo es una columna mas en la base de datos.

---

### 3.4 To‑do

* Derivado automáticamente del contenido de una nota
* No existe de forma independiente
* Vive y muere con la nota

Características:

* Referencia siempre a su nota origen
* Editable solo indirectamente (editando la nota)

---

## 4. Funcionalidades (Scope Actual)

### 4.1 Autenticación

* Login obligatorio después del tutorial
* Métodos:

  * Google
  * Email

---

### 4.2 Gestión de Notas

* Crear nota:

  * texto
  * voz (dictado)
* Editar nota
* Eliminar nota
* Marcar / desmarcar bookmark

**Bookmark**:

* Se presenta como un favorito simple
* Internamente incrementa el peso semántico de la nota
* No se explica al usuario como funcionalidad avanzada

---

### 4.3 Procesamiento Automático

Cada nota es procesada para extraer:

* intención
* conceptos relacionados
* to‑do’s
* embedding semántico

El procesamiento es:

* reactivo
* eventual (no realtime)

---

### 4.4 Vistas Principales

#### 4.4.1 Vista — Todas las Notas

* Lista cronológica de notas
* Acciones:

  * abrir nota
  * bookmark
  * eliminar

---

#### 4.4.2 Vista — Nota Individual

* Contenido completo de la nota
* Pintura de fondo (estética)
* Acceso a:

  * conceptos asociados
  * intención
  * to‑do’s derivados

---

#### 4.4.3 Vista — Conceptos

* Lista de conceptos generados
* Cada concepto muestra:

  * imagen de fondo
  * notas asociadas

---

#### 4.4.4 Vista — Intenciones

* Lista fija de intenciones
* Al seleccionar una:

  * se muestran las notas correspondientes

---

#### 4.4.5 Vista — To‑do’s

* Lista de pendientes activos
* Cada to‑do:

  * referencia su nota origen

---

### 4.5 Pinturas / Imágenes

* Pueden asociarse a:

  * notas
  * conceptos
* Se pueden:

  * generar automáticamente
  * seleccionar manualmente
* Función puramente estética

---

### 4.6 Settings

Opciones disponibles:

* Idioma (afecta procesamiento futuro)
* Preferencias visuales (pinturas)

---

### 4.7 Widgets y Quick Actions

* Widgets para:

  * crear nota rápida
* Acciones rápidas:

  * grabación de voz

Toda entrada por widget se trata como **una nota normal**.

---

## 5. Requerimientos Técnicos

### 5.1 Plataforma

* Swift
* iOS
* Mobile only

---

### 5.2 Arquitectura

* Frontend desacoplado del backend
* Contratos de datos claros:

  * Note JSON
  * Concept JSON
  * To‑do projection
  * Intention enum

---

### 5.3 Persistencia

* Backend con almacenamiento de:

  * notas
  * resultados derivados
* Auth obligatoria

---

## 6. Fuera de Alcance (Explícito)

* Edición manual de conceptos
* Fusión / renombrado de conceptos
* Definición multi‑idioma semántica
* Colaboración
* Sync multi‑dispositivo avanzado
* AI avanzada explicable al usuario

---

## 7. Futuro (No implementado)

* Control total del usuario sobre conceptos
* Re‑procesamiento manual
* Edición rica de notas (bloques, headers, estilos)
* To‑do management avanzado
* Inteligencia multi‑idioma

---

## 8. Principios de Diseño del Producto

* La nota es la verdad
* Todo lo demás es derivado
* El sistema piensa, el usuario decide
* Simplicidad en UI, complejidad en backend
* Evolución progresiva, no magia inmediata

---

*Este PRD define el sistema mínimo coherente para construir MindDump sin contradicciones ni deuda conceptual temprana.*
