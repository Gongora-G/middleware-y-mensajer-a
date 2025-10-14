"""
Sender para Red - Enviar mensajes desde cualquier computadora
"""
from broker_red import conectar_redis_red, enviar_mensaje_red, mostrar_info_conexion
import socket

def obtener_nombre_computadora():
    """Obtiene el nombre de la computadora para identificar usuarios"""
    try:
        return socket.gethostname()
    except:
        return "PC-Desconocido"

def main():
    """Sender que funciona en red"""
    print("\n" + "="*60)
    print("📤 SENDER DE RED - ENVIAR MENSAJES A TRAVÉS DE LA RED")
    print("="*60)
    print("🌐 Este programa puede conectarse a Redis en otra computadora")
    print("="*60)
    
    # Mostrar información de conexión
    mostrar_info_conexion()
    
    # Conectar al broker (puede estar en otra computadora)
    client = conectar_redis_red()
    if not client:
        print("❌ No se pudo conectar al broker de red")
        input("Presiona ENTER para salir...")
        return
    
    # Identificación automática del usuario
    nombre_pc = obtener_nombre_computadora()
    print(f"\n👤 Tu computadora: {nombre_pc}")
    
    # Pedir nombre del usuario (opcional)
    nombre_usuario = input("¿Cuál es tu nombre? (o presiona ENTER para usar nombre de PC): ").strip()
    
    if not nombre_usuario:
        nombre_usuario = nombre_pc
    
    print(f"\n🚀 ¡Hola {nombre_usuario}!")
    print("💬 Ahora puedes chatear con computadoras en la red")
    print("Comandos especiales:")
    print("- 'salir' para terminar")
    print("- 'quien' para ver información de conexión")
    print("-" * 60)
    
    # Loop principal para enviar mensajes
    while True:
        try:
            mensaje = input(f"{nombre_usuario}: ").strip()
            
            if not mensaje:
                continue
                
            # Comandos especiales
            if mensaje.lower() == 'salir':
                # Enviar mensaje de despedida
                enviar_mensaje_red(client, nombre_usuario, "se ha desconectado 👋")
                print("👋 ¡Hasta luego!")
                break
                
            elif mensaje.lower() == 'quien':
                mostrar_info_conexion()
                continue
            
            # Enviar mensaje normal
            if enviar_mensaje_red(client, nombre_usuario, mensaje):
                pass  # Mensaje enviado exitosamente
            else:
                print("❌ Error enviando mensaje. ¿Perdiste la conexión?")
                
        except KeyboardInterrupt:
            print(f"\n👋 {nombre_usuario} se desconecta...")
            try:
                enviar_mensaje_red(client, nombre_usuario, "se desconectó inesperadamente 😵")
            except:
                pass
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()