# 💬 Sistema de Chat Distribuido con Middleware

Sistema simple de mensajería que demuestra conceptos de **middleware** y **brokers de mensajes** en sistemas distribuidos.

## 🎯 Objetivos de Aprendizaje

- Entender qué es un **middleware/broker** de mensajes
- Implementar patrones **Producer/Consumer**
- Comunicación **asíncrona** entre componentes
- **Desacoplamiento** de sistemas
- Comunicación **distribuida** entre computadoras

## 🏗️ Arquitectura

```
[Usuario A] → [Redis Broker] → [Usuario B]
              (Middleware)
```

## 📁 Estructura del Proyecto

```
📦 Taller_Tema2/
├── 🔧 broker.py              # Configuración básica del broker Redis
├── 📤 sender.py              # Enviar mensajes (Producer)
├── 📥 receiver.py            # Recibir mensajes (Consumer) 
├── 🎮 demo_chat.py           # Demo completo interactivo
├── 🌐 broker_red.py          # Configuración para red local
├── 🌐 sender_red.py          # Sender para múltiples computadoras
├── 🌐 receiver_red.py        # Receiver para múltiples computadoras
├── 📋 requirements.txt       # Dependencias de Python
├── 📖 README_SIMPLE.md       # Documentación detallada
└── 👥 GUIA_PARA_COMPAÑERO.md # Guía para uso en red
```

## ⚡ Instalación Rápida

### 1. Instalar Redis (usando Docker)
```bash
docker run -d -p 6380:6379 --name redis-chat redis:latest
```

### 2. Instalar dependencias de Python
```bash
pip install redis
```

### 3. Probar el sistema básico
```bash
python demo_chat.py
```

## 🚀 Modos de Uso

### 📱 Modo 1: Chat Local (Una computadora)
Perfecto para entender los conceptos básicos:

```bash
# Terminal 1: Escuchar mensajes
python receiver.py

# Terminal 2: Enviar mensajes  
python sender.py
```

### 🌐 Modo 2: Chat en Red (Múltiples computadoras)
Para comunicación entre computadoras diferentes:

```bash
# Computadora 1 (Servidor): Ejecuta Redis
docker run -d -p 6380:6379 --name redis-network redis:latest redis-server --bind 0.0.0.0 --protected-mode no

# Computadora 2 (Cliente): Configura IP del servidor en broker_red.py
python sender_red.py  # o receiver_red.py
```

### 🎭 Modo 3: Demo Interactivo
Demostración completa con explicaciones:

```bash
python demo_chat.py
```

## 🔍 Conceptos Demostrados

| Concepto | Descripción | Implementación |
|----------|-------------|----------------|
| **Middleware** | Intermediario entre sistemas | Redis actúa como broker |
| **Producer** | Genera y envía mensajes | `sender.py` |
| **Consumer** | Recibe y procesa mensajes | `receiver.py` |
| **Desacoplamiento** | Sistemas independientes | No se conocen directamente |
| **Asíncrono** | Sin espera de respuesta | Mensajes en cola |
| **Distribuido** | Múltiples computadoras | Versión `*_red.py` |

## 🌐 Para Uso en Red Local

Ver **[GUIA_PARA_COMPAÑERO.md](GUIA_PARA_COMPAÑERO.md)** para instrucciones detalladas de configuración entre múltiples computadoras.

## 📚 Documentación Adicional

- **[README_SIMPLE.md](README_SIMPLE.md)**: Explicación detallada de conceptos
- **[GUIA_PARA_COMPAÑERO.md](GUIA_PARA_COMPAÑERO.md)**: Configuración para red local

## 🎓 Casos de Uso Reales

Este patrón se usa en:
- **WhatsApp, Telegram**: Mensajería instantánea
- **Discord, Slack**: Chat de equipos  
- **Apache Kafka**: Streaming de datos
- **RabbitMQ**: Comunicación entre microservicios
- **Redis Pub/Sub**: Notificaciones en tiempo real

## 🔧 Solución de Problemas

### ❌ Error de conexión a Redis
```bash
# Verificar que Redis esté ejecutándose
docker ps

# Reiniciar Redis si es necesario
docker restart redis-chat
```

### ❌ Problemas de red entre computadoras
1. Verificar que están en la misma red WiFi
2. Configurar IP correcta en `broker_red.py`
3. Verificar firewall de Windows
4. Usar versión de red: `*_red.py`

## 👨‍💻 Autor

Proyecto educativo para el curso de **Sistemas Distribuidos**  
Universidad: **[Tu Universidad]**  
Tema: **Middleware y Mensajería (Brokers de mensajería)**