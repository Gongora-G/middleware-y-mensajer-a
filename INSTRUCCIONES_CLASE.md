# 🚀 INSTRUCCIONES PARA COMPAÑEROS DE CLASE

## 🎯 ¿Qué vamos a hacer?
**Chatear entre 2 computadoras diferentes** para demostrar **sistemas distribuidos**

---

## ⚡ PASOS SÚPER FÁCILES

### � **1. VERIFICAR/INSTALAR PYTHON**
- ¿Tienes Python? Prueba: `python --version`
- Si no: https://www.python.org/downloads/ 
- **¡IMPORTANTE!** ✅ Marcar "Add Python to PATH"

### �📥 **2. DESCARGAR PROYECTO**
```bash
git clone https://github.com/Gongora-G/middleware-y-mensajer-a.git
cd middleware-y-mensajer-a
```

### 📦 **3. INSTALAR DEPENDENCIAS**
```bash
pip install redis
```
*Si no funciona: `python -m pip install redis`*

### 👥 **4. DECIDIR ROLES**
- **🖥️ PERSONA A**: Su computadora será el "servidor" (tiene Redis)
- **💻 PERSONA B**: Su computadora será el "cliente" (se conecta)

### 🔧 **5. CONFIGURAR (Solo Persona B)**
Abrir archivo `broker_red.py` y cambiar:
```python
REDIS_HOST = '192.168.0.XX'  # ← Poner IP de Persona A aquí
MODO_SERVIDOR = False        # ← Cambiar a False
```

### 🚀 **6. EJECUTAR**
**Ambas personas ejecutan:**
```bash
python sender_red.py    # Para escribir mensajes
python receiver_red.py  # Para ver mensajes (otra terminal)
```

---

## 🎉 ¡YA ESTÁN CHATEANDO!

**Ejemplo de conversación:**
```
💬 [María desde 192.168.0.10]: ¡Hola Carlos!
💬 [Carlos desde 192.168.0.15]: ¡Hola María! ¿Funciona el middleware?
💬 [María desde 192.168.0.10]: ¡Sí! ¡Sistemas distribuidos en acción!
```

---

## 🧠 CONCEPTOS QUE ESTÁN VIENDO

- **🔄 MIDDLEWARE**: Redis actúa como "cartero" entre las computadoras
- **📡 SISTEMA DISTRIBUIDO**: 2 computadoras trabajando juntas  
- **⚡ TIEMPO REAL**: Los mensajes llegan al instante por la red
- **🎭 DESACOPLAMIENTO**: Las computadoras no se conocen directamente

---

## ❌ SOLUCIÓN DE PROBLEMAS

### 🐍 **Problemas con Python:**
- **`python` no reconocido**: Reinstalar Python con "Add to PATH" ✅
- **`pip` no funciona**: Usar `python -m pip install redis` ✅
- **Versión vieja**: Python 3.8+ requerido ✅

### 🌐 **Problemas de red:**
1. **Misma WiFi** ✅
2. **IP correcta** en `broker_red.py` ✅  
3. **Redis ejecutándose** en Persona A ✅
4. **Firewall apagado** temporalmente ✅

### 🔍 **Verificar instalación:**
```bash
python --version    # Debe mostrar 3.8+
pip --version      # Debe funcionar
pip show redis     # Debe mostrar la librería instalada
```

---

## 🔥 ¿Por qué esto es INCREÍBLE?

**¡Es la misma tecnología que usan WhatsApp, Discord, Netflix!**
- Computadoras separadas físicamente
- Comunicándose a través de un broker (Redis)
- En tiempo real por la red

**¡Felicidades! Ya saben crear sistemas distribuidos** 🎊