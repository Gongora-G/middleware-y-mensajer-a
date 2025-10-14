"""
Configuración de Red para Sistemas Distribuidos
Permite que múltiples computadoras se conecten al mismo broker Redis
"""
import redis
import json
import time
import socket

# CONFIGURACIÓN PARA RED LOCAL (CAMBIAR SEGÚN TU COMPUTADORA)
# =====================================================

# Opción 1: Si Redis está en TU computadora (tú eres el "servidor")
REDIS_HOST_LOCAL = 'localhost'  # Para ti mismo

# Opción 2: Si Redis está en la computadora de tu compañero
# REDIS_HOST_REMOTO = '192.168.1.100'  # IP del computador de tu compañero

# Opción 3: Configuración automática (detecta tu IP)
def obtener_mi_ip():
    """Obtiene la IP local de tu computadora en la red"""
    try:
        # Truco para obtener IP local sin conexión a internet
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# CONFIGURACIÓN PRINCIPAL
# =====================
REDIS_PORT = 6380
CHAT_CHANNEL = 'chat_distribuido'

# ¿Quién va a ser el servidor Redis?
MODO_SERVIDOR = True  # True si TU computadora tiene Redis, False si es la otra

if MODO_SERVIDOR:
    REDIS_HOST = 'localhost'  # Tu computadora es el servidor
    MI_IP = obtener_mi_ip()
else:
    # Cambiar por la IP del computador que tiene Redis
    REDIS_HOST = '192.168.1.XXX'  # IP del otro computador
    MI_IP = obtener_mi_ip()

def mostrar_info_conexion():
    """Muestra información para conectarse desde otras computadoras"""
    print("🌐 INFORMACIÓN DE CONEXIÓN")
    print("="*50)
    print(f"📍 Mi IP en la red local: {MI_IP}")
    print(f"🔌 Redis Host: {REDIS_HOST}:{REDIS_PORT}")
    print(f"📡 Canal de chat: {CHAT_CHANNEL}")
    
    if MODO_SERVIDOR:
        print("\n💡 INSTRUCCIONES PARA TU COMPAÑERO:")
        print("="*50)
        print("1. Abrir el archivo 'broker_red.py'")
        print("2. Cambiar la línea:")
        print(f"   REDIS_HOST = '{MI_IP}'")
        print("3. Cambiar MODO_SERVIDOR = False")
        print("4. Ejecutar el programa")
        print("\n⚠️  IMPORTANTE: Asegúrate que Redis permita conexiones externas")
    else:
        print(f"\n🔌 Conectando al servidor Redis en: {REDIS_HOST}")

def conectar_redis_red():
    """Conecta a Redis (local o remoto)"""
    try:
        print(f"🔌 Conectando a Redis en {REDIS_HOST}:{REDIS_PORT}...")
        
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True,
            socket_connect_timeout=5,  # Timeout de conexión
            socket_timeout=5
        )
        
        # Probar conexión
        client.ping()
        print(f"✅ Conectado exitosamente a Redis!")
        mostrar_info_conexion()
        return client
        
    except redis.ConnectionError as e:
        print(f"❌ Error de conexión a Redis:")
        print(f"   Host: {REDIS_HOST}:{REDIS_PORT}")
        print(f"   Error: {e}")
        print("\n🔧 POSIBLES SOLUCIONES:")
        if MODO_SERVIDOR:
            print("1. Verificar que Redis esté ejecutándose")
            print("2. Verificar que Redis acepte conexiones externas")
            print("3. Verificar firewall de Windows")
        else:
            print("1. Verificar la IP del otro computador")
            print("2. Verificar que Redis esté ejecutándose en el otro PC")
            print("3. Verificar que no haya firewall bloqueando")
        return None
    
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None

def enviar_mensaje_red(client, usuario, mensaje):
    """Envía un mensaje a través de la red"""
    try:
        mensaje_completo = {
            'usuario': usuario,
            'mensaje': mensaje,
            'tiempo': time.strftime("%H:%M:%S"),
            'ip_origen': MI_IP  # Para saber de qué computadora viene
        }
        
        mensaje_texto = json.dumps(mensaje_completo, ensure_ascii=False)
        client.lpush(CHAT_CHANNEL, mensaje_texto)
        print(f"📤 Mensaje enviado desde {MI_IP}: [{usuario}] {mensaje}")
        return True
        
    except Exception as e:
        print(f"❌ Error enviando mensaje: {e}")
        return False

def recibir_mensaje_red(client):
    """Recibe un mensaje a través de la red"""
    try:
        resultado = client.brpop(CHAT_CHANNEL, timeout=1)
        
        if resultado:
            canal, mensaje_texto = resultado
            mensaje = json.loads(mensaje_texto)
            
            # Mostrar de qué computadora viene el mensaje
            origen = mensaje.get('ip_origen', 'desconocida')
            print(f"📥 Mensaje de {origen}: [{mensaje['usuario']}] {mensaje['mensaje']} ({mensaje['tiempo']})")
            return mensaje
        
        return None
        
    except Exception as e:
        print(f"❌ Error recibiendo mensaje: {e}")
        return None

def test_conexion_red():
    """Prueba la conexión de red"""
    print("🧪 PROBANDO CONEXIÓN DE RED...")
    print("="*50)
    
    client = conectar_redis_red()
    if not client:
        return False
    
    # Enviar mensaje de prueba
    usuario_test = f"Test-{MI_IP}"
    mensaje_test = f"¡Hola desde {MI_IP}!"
    
    if enviar_mensaje_red(client, usuario_test, mensaje_test):
        print("✅ Envío de mensaje exitoso!")
        
        # Intentar recibir el mensaje
        print("🔄 Intentando recibir mensaje...")
        mensaje = recibir_mensaje_red(client)
        
        if mensaje:
            print("✅ Recepción de mensaje exitosa!")
            print("🎉 ¡Conexión de red funcionando correctamente!")
            return True
    
    print("❌ Problemas con la conexión de red")
    return False

if __name__ == "__main__":
    print("🌐 CONFIGURADOR DE RED PARA CHAT DISTRIBUIDO")
    mostrar_info_conexion()
    print("\n" + "="*50)
    test_conexion_red()