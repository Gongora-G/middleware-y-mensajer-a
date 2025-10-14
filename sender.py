"""
Sender (Emisor) - Programa para ENVIAR mensajes
Este es el PRODUCER: quien produce/envía mensajes al broker
"""
from broker import conectar_redis, enviar_mensaje, contar_mensajes

def menu_sender():
    """Menú simple para el emisor de mensajes"""
    print("\n" + "="*50)
    print("📤 SENDER - ENVIAR MENSAJES")
    print("="*50)
    print("Tú eres el PRODUCER (quien envía mensajes)")
    print("Los mensajes van al BROKER (Redis)")
    print("Otro programa (receiver) los recibirá")
    print("="*50)

def main():
    """Programa principal del sender"""
    menu_sender()
    
    # Conectar al broker
    client = conectar_redis()
    if not client:
        print("❌ No se pudo conectar al broker")
        return
    
    # Pedir el nombre del usuario
    print("\n👤 ¿Cuál es tu nombre?")
    nombre_usuario = input("Nombre: ").strip()
    
    if not nombre_usuario:
        nombre_usuario = "Usuario"
    
    print(f"\n¡Hola {nombre_usuario}! Ahora puedes enviar mensajes.")
    print("Escribe 'salir' para terminar")
    print("Escribe 'estado' para ver cuántos mensajes hay esperando")
    print("-" * 50)
    
    # Loop principal para enviar mensajes
    while True:
        try:
            # Pedir el mensaje
            mensaje = input(f"{nombre_usuario}: ").strip()
            
            if not mensaje:
                continue
                
            # Comandos especiales
            if mensaje.lower() == 'salir':
                print("👋 ¡Hasta luego!")
                break
                
            elif mensaje.lower() == 'estado':
                cantidad = contar_mensajes(client)
                print(f"📊 Hay {cantidad} mensajes esperando en el broker")
                continue
            
            # Enviar mensaje normal
            enviar_mensaje(client, nombre_usuario, mensaje)
            
        except KeyboardInterrupt:
            print("\n👋 Programa interrumpido. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()