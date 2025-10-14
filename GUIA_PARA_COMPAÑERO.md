# 💬 GUÍA RÁPIDA - CHAT ENTRE COMPUTADORAS

## 🎯 ¿Qué vamos a hacer?
Chatear entre **2 computadoras diferentes** usando **middleware** (Redis)

## 👥 ROLES SÚPER SIMPLES

### 🖥️ **PERSONA A (Servidor)** 
- Tiene Redis ejecutándose
- Su IP será algo como: `192.168.0.XX`

### 💻 **PERSONA B (Cliente)**
- Se conecta al Redis de la Persona A

---

## ⚡ PASOS SÚPER RÁPIDOS

### 📥 **1. DESCARGAR PROYECTO**
```bash
git clone https://github.com/Gongora-G/middleware-y-mensajer-a.git
cd middleware-y-mensajer-a
pip install redis
```

### 🔧 **2. CONFIGURAR (Solo Persona B)**
Abrir `broker_red.py` y cambiar **2 líneas**:
```python
REDIS_HOST = '192.168.0.XX'  # ← IP de la Persona A
MODO_SERVIDOR = False        # ← Cambiar a False
```

### 🚀 **3. EJECUTAR**

**Persona A (Servidor):**
```bash
python sender_red.py    # Para enviar
python receiver_red.py  # Para recibir (otra terminal)
```

**Persona B (Cliente):**
```bash
python sender_red.py    # Para enviar  
python receiver_red.py  # Para recibir (otra terminal)
```

---

## 🎮 ¡ESO ES TODO!

**Ya pueden chatear entre computadoras diferentes** 🎉

### 💬 Ejemplo:
```
[Ana desde 192.168.0.15]: ¡Hola Juan!
[Juan desde 192.168.0.23]: ¡Hola Ana! ¿Funciona?
[Ana desde 192.168.0.15]: ¡Sí! ¡Esto es increíble!
```

---

## 🧠 CONCEPTOS QUE APRENDEN (Para la clase)

- **🔄 Middleware**: Redis = cartero digital entre computadoras
- **📡 Sistema Distribuido**: 2 computadoras trabajando juntas  
- **⚡ Tiempo Real**: Mensajes instantáneos por la red
- **🎭 Desacoplamiento**: No se conectan directamente

---

## ❌ Si hay problemas:

1. **Misma WiFi** ✅
2. **IP correcta** en `broker_red.py` ✅  
3. **Redis ejecutándose** en Persona A ✅
4. **Firewall apagado** temporalmente ✅

**¡Listo para impresionar en clase!** 🎊