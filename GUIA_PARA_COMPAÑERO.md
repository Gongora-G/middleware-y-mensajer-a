# 🌐 GUÍA PARA CHAT EN RED - PARA TU COMPAÑERO

## 🎯 Objetivo
Permitir que dos computadoras diferentes se comuniquen a través del chat usando Redis como broker de mensajes.

## 👥 Roles

### 🖥️ **COMPUTADORA 1 (Jhoan - Servidor)**
- **IP**: 192.168.0.23
- **Rol**: Tiene el Redis (servidor/broker)
- **Qué hace**: Ejecuta Redis y puede enviar/recibir mensajes

### 💻 **COMPUTADORA 2 (Tu compañero - Cliente)**
- **Rol**: Se conecta al Redis de Jhoan
- **Qué hace**: Se conecta remotamente y puede enviar/recibir mensajes

## 📋 PASOS PARA TU COMPAÑERO

### Paso 1: Conseguir los archivos
Tu compañero necesita estos archivos en su computadora:
- `broker_red.py`
- `sender_red.py` 
- `receiver_red.py`
- Y tener Python instalado con la librería `redis`

### Paso 2: Configurar la conexión
En el archivo `broker_red.py`, tu compañero debe cambiar estas líneas:

**ANTES:**
```python
REDIS_HOST = 'localhost'  # Para ti mismo
MODO_SERVIDOR = True  # True si TU computadora tiene Redis
```

**DESPUÉS:**
```python
REDIS_HOST = '192.168.0.23'  # IP de la computadora de Jhoan
MODO_SERVIDOR = False  # False porque no es el servidor
```

### Paso 3: Instalar dependencias
```bash
pip install redis
```

### Paso 4: Probar conexión
```bash
python broker_red.py
```

Debería mostrar: ✅ Conectado exitosamente a Redis!

## 🚀 CÓMO CHATEAR

### Opción 1: Jhoan envía, Compañero recibe
```bash
# En computadora de Jhoan
python sender_red.py

# En computadora del compañero  
python receiver_red.py
```

### Opción 2: Compañero envía, Jhoan recibe
```bash
# En computadora del compañero
python sender_red.py

# En computadora de Jhoan
python receiver_red.py
```

### Opción 3: Chat bidireccional
```bash
# Ambos ejecutan sender en una terminal y receiver en otra
# Terminal 1: python sender_red.py
# Terminal 2: python receiver_red.py
```

## 🔧 Solución de Problemas

### ❌ "Error de conexión"
1. **Verificar que están en la misma red WiFi**
2. **Jhoan**: Verificar que Redis esté ejecutándose
3. **Compañero**: Verificar la IP en `broker_red.py`
4. **Ambos**: Verificar firewall de Windows

### ❌ "No recibo mensajes"
1. Verificar que el receiver esté ejecutándose
2. Verificar que ambos usen el mismo canal (`chat_distribuido`)

### ❌ Firewall de Windows
Si hay problemas de conexión, Jhoan puede necesitar:
1. Ir a "Configuración de Firewall de Windows"
2. Permitir el puerto 6380 para Redis
3. O temporalmente desactivar el firewall para pruebas

## 🎮 COMANDOS ESPECIALES

En el sender:
- `salir` - Cerrar programa
- `quien` - Ver información de conexión

## 📱 EJEMPLO DE CONVERSACIÓN

```
[Jhoan desde 192.168.0.23] Hola compañero!
[Compañero desde 192.168.0.15] ¡Hola Jhoan! ¿Funciona el chat?
[Jhoan desde 192.168.0.23] ¡Sí! Estamos chateando entre computadoras diferentes
[Compañero desde 192.168.0.15] ¡Increíble! Esto es un sistema distribuido real
```

## ✅ VERIFICACIÓN EXITOSA

Si todo funciona correctamente, deberían ver:
- ✅ Conexiones exitosas
- 💬 Mensajes con IP de origen
- 🔄 Comunicación en tiempo real
- 📊 Estadísticas de mensajes

## 🧠 CONCEPTOS QUE ESTÁN APRENDIENDO

- **Sistema Distribuido**: Dos computadoras trabajando juntas
- **Broker/Middleware**: Redis actuando como intermediario
- **Comunicación en Red**: Usando IP y puertos
- **Producer/Consumer**: Enviando y recibiendo mensajes
- **Desacoplamiento**: Las computadoras no se conocen directamente