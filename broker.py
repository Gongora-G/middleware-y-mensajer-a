"""
Broker Simple - Configuración básica de Redis para el chat
Este archivo tiene la configuración más simple posible para entender el concepto
"""
import redis
import json
import time

# Configuración súper simple de Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6380  # Puerto donde está nuestro Redis
CHAT_CHANNEL = 'chat_simple'  # Nome del canal de chat

def conectar_redis():
    """
    Función simple para conectar a Redis
    Redis es nuestro "cartero" que entrega mensajes
    """
    try:
        client = redis.Redis(
            host=REDIS_HOST, 
            port=REDIS_PORT, 
            decode_responses=True
        )
        client.ping()  # Verificar que funciona
        print("✅ Conectado al broker Redis (cartero)")
        return client
    except Exception as e:
        print(f"❌ Error conectando al broker: {e}")
        return None

def enviar_mensaje(client, usuario, mensaje):
    """
    Envía un mensaje al broker (cartero)
    
    Args:
        client: Conexión a Redis
        usuario: Quien envía el mensaje
        mensaje: Qué dice
    """
    # Crear un mensaje simple con timestamp
    mensaje_completo = {
        'usuario': usuario,
        'mensaje': mensaje,
        'tiempo': time.strftime("%H:%M:%S")
    }
    
    # Convertir a texto (JSON) para enviar
    mensaje_texto = json.dumps(mensaje_completo, ensure_ascii=False)
    
    # Enviar al broker usando LPUSH (poner al inicio de la lista)
    client.lpush(CHAT_CHANNEL, mensaje_texto)
    print(f"📤 Mensaje enviado al broker: [{usuario}] {mensaje}")

def recibir_mensaje(client):
    """
    Recibe un mensaje del broker (cartero)
    
    Args:
        client: Conexión a Redis
        
    Returns:
        Diccionario con el mensaje o None si no hay mensajes
    """
    try:
        # BRPOP espera hasta que hay un mensaje (bloquea por 1 segundo)
        resultado = client.brpop(CHAT_CHANNEL, timeout=1)
        
        if resultado:
            canal, mensaje_texto = resultado
            mensaje = json.loads(mensaje_texto)
            print(f"📥 Mensaje recibido: [{mensaje['usuario']}] {mensaje['mensaje']} ({mensaje['tiempo']})")
            return mensaje
        else:
            return None  # No hay mensajes
            
    except Exception as e:
        print(f"❌ Error recibiendo mensaje: {e}")
        return None

def contar_mensajes(client):
    """Cuenta cuántos mensajes hay esperando en el broker"""
    return client.llen(CHAT_CHANNEL)

def limpiar_chat(client):
    """Limpia todos los mensajes del chat"""
    client.delete(CHAT_CHANNEL)
    print("🧹 Chat limpiado")

# Función de prueba
def test_broker():
    """Prueba básica del broker"""
    print("🧪 Probando el broker...")
    
    client = conectar_redis()
    if not client:
        return
    
    # Limpiar mensajes anteriores
    limpiar_chat(client)
    
    # Enviar un mensaje de prueba
    enviar_mensaje(client, "Sistema", "¡Hola! El broker funciona correctamente")
    
    # Verificar que el mensaje está ahí
    cantidad = contar_mensajes(client)
    print(f"📊 Mensajes en el broker: {cantidad}")
    
    # Recibir el mensaje
    mensaje = recibir_mensaje(client)
    if mensaje:
        print("✅ Broker funcionando correctamente!")
    else:
        print("❌ Problema con el broker")

if __name__ == "__main__":
    test_broker()