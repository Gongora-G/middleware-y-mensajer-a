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

## ⚡ INSTALACIÓN SÚPER RÁPIDA

### 🐍 **Requisitos:**
- **Python 3.8+** → https://www.python.org/downloads/ 
- ✅ Marcar "Add Python to PATH" durante instalación

### 🎯 **Para PROBAR el concepto (1 computadora):**
```bash
git clone https://github.com/Gongora-G/middleware-y-mensajer-a.git
cd middleware-y-mensajer-a
pip install redis
python demo_chat.py  # ← Demo completo con explicaciones
```

### 🌐 **Para CHAT EN RED (2 computadoras):**
```bash
# Paso 1: Descargar
git clone https://github.com/Gongora-G/middleware-y-mensajer-a.git
cd middleware-y-mensajer-a  

# Paso 2: Instalar dependencias
pip install redis

# Paso 3: Configurar red (ver GUIA_PARA_COMPAÑERO.md)
```

---

## 🚀 MODOS DE USO

### 🎮 **Modo 1: Demo Educativo** 
```bash
python demo_chat.py
```
✅ Perfecto para **explicar conceptos** en clase  
✅ Muestra **paso a paso** cómo funciona el middleware

### 💻 **Modo 2: Chat Local**
```bash
python receiver.py  # Terminal 1: escuchar
python sender.py    # Terminal 2: enviar
```  
✅ Entender **Producer/Consumer** básico

### 🌍 **Modo 3: Chat Distribuido** (¡LO MÁS GENIAL!)
```bash
python receiver_red.py  # Persona A
python sender_red.py    # Persona B (otra computadora)
```
✅ **Sistema distribuido REAL** entre computadoras  
✅ Perfecto para **impresionar** en presentaciones

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