"""
Demo Completo Simple - Sistema de Chat con Middleware
Este programa demuestra todos los conceptos básicos de una vez
"""
from broker import conectar_redis, enviar_mensaje, recibir_mensaje, limpiar_chat, contar_mensajes
import threading
import time

class ChatSimple:
    """Sistema de chat simple para demostrar middleware"""
    
    def __init__(self):
        self.client = None
        self.escuchando = False
        self.mensajes_enviados = 0
        self.mensajes_recibidos = 0
    
    def conectar(self):
        """Conecta al broker Redis"""
        print("🔌 Conectando al broker (middleware)...")
        self.client = conectar_redis()
        return self.client is not None
    
    def limpiar_chat(self):
        """Limpia mensajes anteriores"""
        if self.client:
            limpiar_chat(self.client)
    
    def enviar(self, usuario, mensaje):
        """Envía un mensaje al broker"""
        if self.client:
            enviar_mensaje(self.client, usuario, mensaje)
            self.mensajes_enviados += 1
    
    def escuchar_mensajes(self):
        """Hilo que escucha mensajes continuamente"""
        print("👂 Iniciando modo ESCUCHA...")
        
        while self.escuchando:
            try:
                mensaje = recibir_mensaje(self.client)
                if mensaje:
                    self.mensajes_recibidos += 1
                    # Solo mostrar si no es nuestro propio mensaje de demo
                    if not mensaje['usuario'].startswith('Demo'):
                        print(f"  💬 {mensaje['usuario']}: {mensaje['mensaje']}")
                time.sleep(0.1)
            except Exception as e:
                if self.escuchando:  # Solo mostrar error si seguimos escuchando
                    print(f"❌ Error escuchando: {e}")
                break
    
    def demo_completo(self):
        """Demostración completa del sistema"""
        print("\n🎭 DEMO SIMPLE - MIDDLEWARE Y MENSAJERÍA")
        print("="*60)
        
        # Paso 1: Conectar
        print("\n📍 PASO 1: Conectando al broker de mensajes...")
        if not self.conectar():
            print("❌ No se pudo conectar al broker")
            return
        
        input("Presiona ENTER para continuar...")
        
        # Paso 2: Limpiar
        print("\n📍 PASO 2: Limpiando mensajes anteriores...")
        self.limpiar_chat()
        
        input("Presiona ENTER para continuar...")
        
        # Paso 3: Demostrar conceptos
        print("\n📍 PASO 3: Demostrando conceptos básicos...")
        print("\n🔍 CONCEPTO: PRODUCER/CONSUMER")
        print("- PRODUCER: Quien ENVÍA mensajes")
        print("- CONSUMER: Quien RECIBE mensajes")
        print("- BROKER: El intermediario (Redis)")
        
        input("Presiona ENTER para ver en acción...")
        
        # Iniciar escucha en hilo separado
        self.escuchando = True
        hilo_escucha = threading.Thread(target=self.escuchar_mensajes, daemon=True)
        hilo_escucha.start()
        
        # Paso 4: Enviar mensajes de demostración
        print("\n📍 PASO 4: Enviando mensajes al broker...")
        
        mensajes_demo = [
            ("Alice", "¡Hola! ¿Alguien ahí?"),
            ("Bob", "¡Hola Alice! Sí, estoy aquí"),
            ("Alice", "¿Cómo funciona este sistema?"),
            ("Bob", "Simple: enviamos mensajes al broker (Redis)"),
            ("Alice", "¿Y luego qué pasa?"),
            ("Bob", "El broker los entrega a quien esté escuchando"),
            ("Alice", "¡Entiendo! Es como un cartero digital")
        ]
        
        for usuario, mensaje in mensajes_demo:
            print(f"\n📤 ENVIANDO: [{usuario}] {mensaje}")
            self.enviar(usuario, mensaje)
            time.sleep(2)  # Pausa para ver el efecto
        
        time.sleep(1)
        
        # Paso 5: Mostrar estadísticas
        print(f"\n📍 PASO 5: Estadísticas del demo")
        print("="*40)
        print(f"📤 Mensajes enviados: {self.mensajes_enviados}")
        print(f"📥 Mensajes recibidos: {self.mensajes_recibidos}")
        print(f"📊 Mensajes en el broker: {contar_mensajes(self.client)}")
        
        # Detener escucha
        self.escuchando = False
        
        input("\nPresiona ENTER para continuar...")
        
        # Paso 6: Explicar conceptos
        print("\n📍 PASO 6: ¿Qué acabamos de ver?")
        print("="*50)
        print("✅ MIDDLEWARE: Redis actuó como intermediario")
        print("✅ DESACOPLAMIENTO: Alice y Bob no se conocen directamente")
        print("✅ ASÍNCRONO: Los mensajes se envían sin esperar respuesta")
        print("✅ PERSISTENCIA: Los mensajes se guardan en el broker")
        print("✅ ESCALABILIDAD: Múltiples usuarios pueden participar")
        
        print("\n🎯 CONCEPTOS CLAVE DEMOSTRADOS:")
        print("1. PRODUCER → BROKER → CONSUMER")
        print("2. Comunicación indirecta a través del middleware")
        print("3. Los participantes están desacoplados")
        print("4. El broker actúa como buffer/almacén temporal")
        
        input("\nPresiona ENTER para terminar el demo...")
        print("\n✅ Demo completado exitosamente!")

def menu_principal():
    """Menú principal del demo"""
    chat = ChatSimple()
    
    while True:
        print("\n" + "="*50)
        print("🚀 SISTEMA DE CHAT SIMPLE")
        print("="*50)
        print("1. 🎭 Demo completo (recomendado)")
        print("2. 🧪 Probar broker")
        print("3. 📤 Solo enviar mensajes")
        print("4. 📥 Solo recibir mensajes")
        print("5. 🧹 Limpiar chat")
        print("6. 📊 Ver estado")
        print("7. ❌ Salir")
        print("="*50)
        
        try:
            opcion = input("Selecciona opción (1-7): ").strip()
            
            if opcion == "1":
                chat.demo_completo()
                
            elif opcion == "2":
                from broker import test_broker
                test_broker()
                
            elif opcion == "3":
                print("📤 Modo SENDER - Usa sender.py en otra terminal")
                input("Presiona ENTER cuando termines...")
                
            elif opcion == "4":
                print("📥 Modo RECEIVER - Usa receiver.py en otra terminal") 
                input("Presiona ENTER cuando termines...")
                
            elif opcion == "5":
                if chat.conectar():
                    chat.limpiar_chat()
                    
            elif opcion == "6":
                if chat.conectar():
                    cantidad = contar_mensajes(chat.client)
                    print(f"📊 Mensajes en el broker: {cantidad}")
                    
            elif opcion == "7":
                print("👋 ¡Hasta luego!")
                break
                
            else:
                print("❌ Opción inválida")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    menu_principal()