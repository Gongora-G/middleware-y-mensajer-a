# 📝 TALLER RÁPIDO: CHAT DISTRIBUIDO CON MIDDLEWARE

**Objetivo:** Crear chat entre 2 computadoras usando Redis como middleware
**Tiempo:** 20 minutos

---

## 🚀 PASO 1: PREPARACIÓN
```bash
# Verificar Python
python --version

# Instalar Redis para Python
pip install redis

# Crear carpeta
mkdir chat_simple
cd chat_simple
```

---

## 🔧 PASO 2: CREAR BROKER
**Archivo:** `broker.py`
```python
import redis, json, time

# Configuración
REDIS_HOST = 'localhost'  # Cambiar por IP si es remoto
REDIS_PORT = 6380
COLA = 'chat'

def conectar():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    client.ping()
    print("✅ Broker conectado")
    return client

def enviar(client, usuario, mensaje):
    data = {'usuario': usuario, 'mensaje': mensaje, 'hora': time.strftime("%H:%M")}
    client.lpush(COLA, json.dumps(data, ensure_ascii=False))
    print(f"📤 {usuario}: {mensaje}")

def recibir(client):
    resultado = client.brpop(COLA, timeout=1)
    if resultado:
        data = json.loads(resultado[1])
        print(f"📥 {data['usuario']}: {data['mensaje']} ({data['hora']})")
        return data
    return None
```

---

## 📤 PASO 3: CREAR EMISOR
**Archivo:** `emisor.py`
```python
from broker import conectar, enviar

client = conectar()
nombre = input("Tu nombre: ")

while True:
    mensaje = input(f"{nombre}: ")
    if mensaje == 'salir':
        break
    enviar(client, nombre, mensaje)
```

---

## 📥 PASO 4: CREAR RECEPTOR
**Archivo:** `receptor.py`
```python
from broker import conectar, recibir
import time

client = conectar()
print("🔄 Escuchando mensajes... (Ctrl+C para salir)")

try:
    while True:
        recibir(client)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("👋 Saliendo...")
```

---

## 🧪 PASO 5: INSTALAR REDIS
```bash
# Con Docker (recomendado)
docker run -d -p 6380:6379 redis:latest
```

---

## ✅ PASO 6: PROBAR LOCAL
```bash
# Terminal 1
python receptor.py

# Terminal 2  
python emisor.py
```

---

## 🌐 PASO 7: PARA MÚLTIPLES PCs

**En la PC cliente, cambiar en `broker.py`:**
```python
REDIS_HOST = '192.168.0.XX'  # IP de la PC servidor
```

**En la PC servidor, Redis con acceso externo:**
```bash
docker run -d -p 6380:6379 redis:latest redis-server --bind 0.0.0.0 --protected-mode no
```

---

## 🎯 ¡LISTO!

**¿Qué lograste?**
- ✅ **Middleware**: Redis coordina mensajes
- ✅ **Producer**: `emisor.py` envía
- ✅ **Consumer**: `receptor.py` recibe  
- ✅ **Distribuido**: Funciona entre PCs diferentes

**Misma tecnología que WhatsApp, Discord, Netflix** 🚀

---

## ❌ PROBLEMAS COMUNES
- **Python no funciona**: Instalar con "Add to PATH"
- **pip falla**: Usar `python -m pip install redis`  
- **No se conecta**: Verificar IP y firewall
- **Redis no funciona**: Verificar que Docker esté ejecutándose

**¡Felicidades! Creaste un sistema distribuido real** 🎉