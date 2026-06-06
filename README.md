# PFO 3 - Rediseño como Sistema Distribuido (Cliente-Servidor)

## Alumna: Sofía Trucco

---

## Descripción del proyecto

Este proyecto implementa una arquitectura distribuida basada en el modelo cliente-servidor utilizando sockets TCP en Python.

El sistema permite que uno o varios clientes envíen tareas de procesamiento de texto a un servidor central. El servidor distribuye dichas tareas mediante una cola de mensajes a un conjunto de workers ejecutados en hilos independientes, los cuales procesan la información y devuelven los resultados al cliente correspondiente.

---

## Objetivo

Aplicar conceptos de sistemas distribuidos mediante:

* Comunicación cliente-servidor mediante sockets.
* Procesamiento concurrente utilizando hilos.
* Distribución de tareas mediante una cola de mensajes.
* Diseño de una arquitectura escalable inspirada en entornos productivos.

---

## Arquitectura del sistema

El diseño propuesto incluye los siguientes componentes:

* Clientes (Web, Móvil o Consola)
* Balanceador de carga (Nginx / HAProxy)
* Servidor principal
* Cola de mensajes (RabbitMQ)
* Workers con pool de hilos
* PostgreSQL
* Amazon S3

En la implementación práctica se desarrolló el cliente y el servidor solicitados por la consigna. La cola de mensajes fue representada mediante `queue.Queue()` de Python para simplificar el desarrollo manteniendo el mismo concepto arquitectónico.

---

## Tecnologías utilizadas

* Python
* Socket
* Threading
* Queue
* Git / GitHub

---

## Estructura del proyecto

PFO3/

├── servidor.py

├── cliente.py

└── README.md

└── PFO3-Diagrama.jpg

---

## Funcionamiento

### Servidor

El servidor:

* Escucha conexiones entrantes mediante sockets TCP.
* Mantiene una cola de tareas compartida.
* Crea un pool de workers ejecutados en hilos.
* Distribuye las tareas recibidas entre los workers disponibles.

### Cliente

El cliente:

* Se conecta al servidor.
* Envía textos para procesar.
* Recibe los resultados generados por los workers.
* Permite enviar múltiples tareas durante la misma conexión.

---

## Ejecución

### Iniciar servidor

```bash
python servidor.py
```

### Iniciar cliente

En otra terminal:

```bash
python cliente.py
```

---

## Ejemplo de uso

Entrada:

```text
Hola mundo
```

Salida:

```text
Procesado por Worker 1

Texto original: Hola mundo
Mayúsculas: HOLA MUNDO
Palabras: 2
Caracteres: 10
```

---

## Conceptos aplicados

### Sockets TCP

Permiten la comunicación entre clientes y servidor a través de la red.

### Pool de Workers

Los workers ejecutan tareas concurrentemente utilizando hilos independientes.

### Cola de Mensajes

La cola desacopla la recepción de tareas de su procesamiento, permitiendo una distribución más eficiente de la carga.

### Balanceo y Escalabilidad

La arquitectura propuesta contempla el uso de balanceadores, múltiples workers y almacenamiento distribuido para facilitar la escalabilidad del sistema.

---

## Conclusión

El proyecto demuestra la implementación de una arquitectura cliente-servidor distribuida utilizando sockets, hilos y colas de tareas, aplicando conceptos fundamentales de concurrencia, comunicación en red y procesamiento distribuido.
