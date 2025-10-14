"""
Receiver (Receptor) - Programa para RECIBIR mensajes
Este es el CONSUMER: quien consume/recibe mensajes del broker
"""
from broker import conectar_redis, recibir_mensaje, contar_mensajes
import time

def menu_receiver():
    """Menú simple para el receptor de mensajes"""
    print("\n" + "="*50)
    print("📥 RECEIVER - RECIBIR MENSAJES")
    print("="*50)
    print("Tú eres el CONSUMER (quien recibe mensajes)")
    print("Los mensajes vienen del BROKER (Redis)")
    print("Otro programa (sender) los envía")
    print("="*50)

def main():
    """Programa principal del receiver"""
    menu_receiver()
    
    # Conectar al broker
    client = conectar_redis()
    if not client:
        print("❌ No se pudo conectar al broker")
        return
    
    print("\n🔄 Modo ESCUCHA activado")
    print("Esperando mensajes del broker...")
    print("Presiona Ctrl+C para salir")
    print("-" * 50)
    
    mensajes_recibidos = 0
    
    # Loop principal para recibir mensajes
    while True:
        try:
            # Verificar si hay mensajes esperando
            cantidad_esperando = contar_mensajes(client)
            if cantidad_esperando > 0:
                print(f"📊 Hay {cantidad_esperando} mensajes esperando...")
            
            # Intentar recibir un mensaje (espera 1 segundo)
            mensaje = recibir_mensaje(client)
            
            if mensaje:
                mensajes_recibidos += 1
                print(f"💬 {mensaje['usuario']}: {mensaje['mensaje']} ({mensaje['tiempo']})")
            else:
                # No hay mensajes, mostrar punto para indicar que estamos escuchando
                print(".", end="", flush=True)
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print(f"\n\n👋 Saliendo del modo escucha...")
            print(f"📊 Total mensajes recibidos: {mensajes_recibidos}")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()