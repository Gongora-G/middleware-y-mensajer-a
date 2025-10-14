# Ejemplo Simple: Sistema de Chat con Middleware

## 🎯 Objetivo
Entender los conceptos básicos de middleware y mensajería con un ejemplo súper simple: un sistema de chat.

## 🔧 Conceptos Básicos que Aprenderemos

### 1. ¿Qué es un Broker/Middleware?
- Es como un **cartero** que recibe mensajes y los entrega
- Los usuarios no se hablan directamente, hablan a través del cartero (Redis)

### 2. Producer vs Consumer
- **Producer**: Quien envía mensajes (usuario escribiendo)
- **Consumer**: Quien recibe mensajes (usuario leyendo)

### 3. Cola de Mensajes
- Es como un **buzón** donde se guardan los mensajes
- Los mensajes esperan hasta que alguien los lea

## 🏗️ Arquitectura Simple

```
[Usuario A] → [Redis Broker] → [Usuario B]
              (Cartero)
```

## 📁 Estructura del Ejemplo Simple
```
simple_chat/
├── README_SIMPLE.md   # Esta documentación
├── broker.py          # Configuración simple de Redis
├── sender.py          # Enviar mensajes (Producer)
├── receiver.py        # Recibir mensajes (Consumer)
└── demo_chat.py       # Demo completo
```