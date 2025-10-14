"""
Receiver para Red - Recibir mensajes desde cualquier computadora
"""
from broker_red import conectar_redis_red, recibir_mensaje_red, mostrar_info_conexion
import time
import socket

def obtener_nombre_computadora():
    """Obtiene el nombre de la computadora para identificación"""
    try:
        return socket.gethostname()
    except:
        return "PC-Desconocido"

def main():
    """Receiver que funciona en red"""
    print("\n" + "="*60)
    print("📥 RECEIVER DE RED - RECIBIR MENSAJES DE LA RED")
    print("="*60)
    print("🌐 Este programa escucha mensajes de todas las computadoras")
    print("="*60)
    
    # Mostrar información de conexión
    mostrar_info_conexion()
    
    # Conectar al broker
    client = conectar_redis_red()
    if not client:
        print("❌ No se pudo conectar al broker de red")
        input("Presiona ENTER para salir...")
        return
    
    nombre_pc = obtener_nombre_computadora()
    print(f"\n👂 Escuchando desde: {nombre_pc}")
    print("🔄 Modo ESCUCHA DE RED activado")
    print("💬 Recibirás mensajes de todas las computadoras conectadas")
    print("Presiona Ctrl+C para salir")
    print("-" * 60)
    
    mensajes_recibidos = 0
    computadoras_vistas = set()
    
    # Enviar mensaje de que nos conectamos
    try:
        from broker_red import enviar_mensaje_red
        enviar_mensaje_red(client, f"🔗{nombre_pc}", "se conectó para escuchar mensajes")
    except:
        pass
    
    # Loop principal para recibir mensajes
    while True:
        try:
            mensaje = recibir_mensaje_red(client)
            
            if mensaje:
                mensajes_recibidos += 1
                
                # Registrar nueva computadora
                ip_origen = mensaje.get('ip_origen', 'desconocida')
                if ip_origen != 'desconocida' and ip_origen not in computadoras_vistas:
                    computadoras_vistas.add(ip_origen)
                    print(f"🆕 Nueva computadora detectada: {ip_origen}")
                
                # Mostrar mensaje con formato especial para la red
                usuario = mensaje['usuario']
                texto = mensaje['mensaje']
                tiempo = mensaje['tiempo']
                
                if ip_origen != 'desconocida':
                    print(f"💬 [{ip_origen}] {usuario}: {texto} ({tiempo})")
                else:
                    print(f"💬 {usuario}: {texto} ({tiempo})")
                    
            else:
                # Mostrar actividad cada 5 segundos
                if mensajes_recibidos == 0:
                    print(".", end="", flush=True)
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n👋 Desconectando receiver de red...")
            print(f"📊 Estadísticas de la sesión:")
            print(f"   📥 Mensajes recibidos: {mensajes_recibidos}")
            print(f"   🖥️  Computadoras detectadas: {len(computadoras_vistas)}")
            if computadoras_vistas:
                print(f"   📍 IPs vistas: {', '.join(computadoras_vistas)}")
            
            # Enviar mensaje de desconexión
            try:
                from broker_red import enviar_mensaje_red
                enviar_mensaje_red(client, f"🔗{nombre_pc}", "dejó de escuchar mensajes")
            except:
                pass
                
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            time.sleep(2)
            print("🔄 Reintentando conexión...")

if __name__ == "__main__":
    main()