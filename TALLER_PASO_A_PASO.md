# 📝 TALLER: SISTEMA DE CHAT DISTRIBUIDO CON MIDDLEWARE

**Objetivo:** Crear un sistema de mensajería entre 2 computadoras usando Redis como middleware/broker

**Tiempo estimado:** 30-45 minutos

**Conceptos que aprenderás:**
- Middleware y Brokers de mensajería
- Sistemas distribuidos
- Comunicación Producer/Consumer
- Desacoplamiento de sistemas

---

## 🎯 PARTE 1: PREPARACIÓN DEL ENTORNO

### PASO 1: Verificar Python
**¿Qué hacer?** Verificar que tienes Python instalado
```bash
python --version
```
**Resultado esperado:** Debe mostrar Python 3.8 o superior
**Si no funciona:** Instalar Python desde https://www.python.org/downloads/
⚠️ **IMPORTANTE:** Marcar "Add Python to PATH" durante la instalación

### PASO 2: Instalar dependencias
**¿Qué hacer?** Instalar la librería Redis para Python
```bash
pip install redis
```
**Si no funciona, intenta:**
```bash
python -m pip install redis
```

### PASO 3: Crear carpeta del proyecto
**¿Qué hacer?** Crear una carpeta para nuestros archivos
```bash
mkdir chat_distribuido
cd chat_distribuido
```

---

## 🔧 PARTE 2: CREAR EL BROKER (MIDDLEWARE)

### PASO 4: Crear archivo de configuración
**Archivo:** `broker.py`
**¿Qué hace?** Configura la conexión a Redis (nuestro middleware)

**CÓDIGO COMPLETO:**
```python
"""
Configuración del Broker Redis - El middleware de nuestro sistema
"""
import redis
import json
import time

# Configuración del broker Redis
REDIS_HOST = 'localhost'  # Cambiar por IP del servidor si es remoto
REDIS_PORT = 6380         # Puerto donde corre Redis
CHAT_QUEUE = 'chat_cola'  # Nombre de nuestra cola de mensajes

def conectar_broker():
    """Conecta al broker Redis"""
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )
        client.ping()  # Probar conexión
        print("✅ Conectado al broker Redis")
        return client
    except Exception as e:
        print(f"❌ Error conectando al broker: {e}")
        return None

def enviar_mensaje(client, usuario, mensaje):
    """Envía un mensaje al broker"""
    mensaje_completo = {
        'usuario': usuario,
        'mensaje': mensaje,
        'hora': time.strftime("%H:%M:%S")
    }
    mensaje_json = json.dumps(mensaje_completo, ensure_ascii=False)
    client.lpush(CHAT_QUEUE, mensaje_json)
    print(f"📤 Enviado: [{usuario}] {mensaje}")

def recibir_mensaje(client):
    """Recibe un mensaje del broker"""
    try:
        resultado = client.brpop(CHAT_QUEUE, timeout=1)
        if resultado:
            _, mensaje_json = resultado
            mensaje = json.loads(mensaje_json)
            print(f"📥 Recibido: [{mensaje['usuario']}] {mensaje['mensaje']} ({mensaje['hora']})")
            return mensaje
        return None
    except Exception as e:
        print(f"❌ Error recibiendo: {e}")
        return None

# Función de prueba
if __name__ == "__main__":
    print("🧪 Probando conexión al broker...")
    client = conectar_broker()
    if client:
        print("✅ Broker funcionando correctamente")
    else:
        print("❌ Problema con el broker")
```

### PASO 5: Probar el broker
**¿Qué hacer?** Ejecutar el archivo para verificar que funciona
```bash
python broker.py
```
**Resultado esperado:** "✅ Broker funcionando correctamente"

---

## 📤 PARTE 3: CREAR EL PRODUCER (EMISOR)

### PASO 6: Crear el programa emisor
**Archivo:** `emisor.py`
**¿Qué hace?** Permite enviar mensajes al broker

**CÓDIGO COMPLETO:**
```python
"""
Emisor de mensajes - PRODUCER
Este programa envía mensajes al broker Redis
"""
from broker import conectar_broker, enviar_mensaje

def main():
    print("📤 EMISOR DE MENSAJES")
    print("="*40)
    
    # Conectar al broker
    client = conectar_broker()
    if not client:
        print("❌ No se pudo conectar al broker")
        return
    
    # Pedir nombre del usuario
    nombre = input("¿Cuál es tu nombre? ").strip()
    if not nombre:
        nombre = "Usuario"
    
    print(f"¡Hola {nombre}! Escribe mensajes (o 'salir' para terminar)")
    print("-" * 40)
    
    # Loop para enviar mensajes
    while True:
        mensaje = input(f"{nombre}: ").strip()
        
        if mensaje.lower() == 'salir':
            print("👋 ¡Hasta luego!")
            break
            
        if mensaje:
            enviar_mensaje(client, nombre, mensaje)

if __name__ == "__main__":
    main()
```

---

## 📥 PARTE 4: CREAR EL CONSUMER (RECEPTOR)

### PASO 7: Crear el programa receptor
**Archivo:** `receptor.py`
**¿Qué hace?** Escucha y recibe mensajes del broker

**CÓDIGO COMPLETO:**
```python
"""
Receptor de mensajes - CONSUMER
Este programa escucha mensajes del broker Redis
"""
from broker import conectar_broker, recibir_mensaje
import time

def main():
    print("📥 RECEPTOR DE MENSAJES")
    print("="*40)
    
    # Conectar al broker
    client = conectar_broker()
    if not client:
        print("❌ No se pudo conectar al broker")
        return
    
    print("🔄 Escuchando mensajes...")
    print("Presiona Ctrl+C para salir")
    print("-" * 40)
    
    mensajes_recibidos = 0
    
    # Loop para recibir mensajes
    while True:
        try:
            mensaje = recibir_mensaje(client)
            if mensaje:
                mensajes_recibidos += 1
            else:
                print(".", end="", flush=True)  # Indicar que está escuchando
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print(f"\n👋 Saliendo... Mensajes recibidos: {mensajes_recibidos}")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
```

---

## 🧪 PARTE 5: PROBAR EL SISTEMA LOCALMENTE

### PASO 8: Instalar y ejecutar Redis
**¿Qué hacer?** Necesitamos Redis como nuestro broker

**Opción A - Con Docker (recomendado):**
```bash
docker run -d -p 6380:6379 --name chat-redis redis:latest
```

**Opción B - Sin Docker:**
- Descargar Redis desde: https://github.com/microsoftarchive/redis/releases
- Instalar y ejecutar

### PASO 9: Probar chat local
**¿Qué hacer?** Probar que el sistema funciona en una sola computadora

**Terminal 1 (Receptor):**
```bash
python receptor.py
```

**Terminal 2 (Emisor):**
```bash
python emisor.py
```

**¿Qué debe pasar?**
1. El receptor debe mostrar "🔄 Escuchando mensajes..."
2. El emisor debe permitir escribir mensajes
3. Los mensajes del emisor deben aparecer en el receptor

---

## 🌐 PARTE 6: CONFIGURAR PARA MÚLTIPLES COMPUTADORAS

### PASO 10: Modificar para red (Solo Computadora Cliente)
**¿Qué hacer?** Si quieres conectar desde otra computadora

**En el archivo `broker.py` de la computadora CLIENTE, cambiar:**
```python
# ANTES:
REDIS_HOST = 'localhost'

# DESPUÉS:
REDIS_HOST = '192.168.0.XX'  # IP de la computadora que tiene Redis
```

**¿Cómo saber la IP del servidor?**
En la computadora servidor ejecutar:
```bash
ipconfig  # Windows
```
Buscar la IP que empiece con 192.168.0.X

### PASO 11: Configurar Redis para conexiones externas
**¿Qué hacer?** Permitir que otras computadoras se conecten

**Si usas Docker:**
```bash
docker stop chat-redis
docker rm chat-redis
docker run -d -p 6380:6379 --name chat-redis redis:latest redis-server --bind 0.0.0.0 --protected-mode no
```

### PASO 12: Probar chat distribuido
**¿Qué hacer?** Chatear entre computadoras diferentes

**Computadora A (Servidor):**
- Tiene Redis ejecutándose
- Ejecuta: `python receptor.py` o `python emisor.py`

**Computadora B (Cliente):**
- Modificó `broker.py` con la IP de A
- Ejecuta: `python emisor.py` o `python receptor.py`

---

## 🎉 VERIFICACIÓN FINAL

### ¿Qué debes ver si todo funciona?

**En el receptor:**
```
📥 RECEPTOR DE MENSAJES
========================================
🔄 Escuchando mensajes...
Presiona Ctrl+C para salir
----------------------------------------
📥 Recibido: [Juan] Hola María! (14:30:25)
📥 Recibido: [María] ¡Hola Juan! ¿Funciona? (14:30:32)
```

**En el emisor:**
```
📤 EMISOR DE MENSAJES
========================================
¿Cuál es tu nombre? Juan
¡Hola Juan! Escribe mensajes (o 'salir' para terminar)
----------------------------------------
Juan: Hola María!
📤 Enviado: [Juan] Hola María!
```

---

## 🧠 CONCEPTOS APRENDIDOS

### ¿Qué acabas de crear?
1. **Middleware/Broker:** Redis actúa como intermediario
2. **Producer:** El programa `emisor.py` produce mensajes
3. **Consumer:** El programa `receptor.py` consume mensajes
4. **Sistema Distribuido:** Computadoras separadas comunicándose
5. **Desacoplamiento:** Los programas no se conocen directamente

### ¿Por qué es importante?
- **WhatsApp, Telegram:** Usan este mismo patrón
- **Netflix, YouTube:** Para coordinar sus sistemas
- **Bancos:** Para procesar transacciones
- **E-commerce:** Para manejar pedidos

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Python no funciona
- Reinstalar Python marcando "Add to PATH"
- Usar `python3` en lugar de `python`

### pip no funciona
- Usar `python -m pip install redis`
- Verificar conexión a internet

### Redis no se conecta
- Verificar que Redis esté ejecutándose
- Verificar IP correcta en `broker.py`
- Verificar firewall (temporalmente desactivar)

### No recibo mensajes
- Ambas computadoras deben usar la misma cola (`chat_cola`)
- Verificar que receptor esté ejecutándose
- Verificar conexión de red

---

## 📋 ARCHIVOS FINALES

Tu proyecto debe tener estos archivos:
- `broker.py` - Configuración del middleware
- `emisor.py` - Producer de mensajes
- `receptor.py` - Consumer de mensajes

**¡Felicidades! Has creado un sistema distribuido real** 🎊

---

**NOTA PARA EL INSTRUCTOR:**
Este taller demuestra los conceptos fundamentales de middleware y brokers de mensajería de forma práctica. Los estudiantes pueden experimentar con sistemas distribuidos reales sin complejidad excesiva.