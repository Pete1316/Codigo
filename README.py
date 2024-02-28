import serial
import time

bluetooth_port = 'COM7'  # Reemplaza 'COM7' con el puerto COM que estés usando
baud_rate = 9600

try:
    ser = serial.Serial(bluetooth_port, baud_rate)
    print("Conexión establecida con éxito al dispositivo Bluetooth en el puerto:", bluetooth_port)
    time.sleep(2)  # Espera un momento para que se establezca la conexión
    
    while True:
        # Solicitar al usuario que ingrese el comando deseado
        comando = input("Ingrese '1' para encender el LED o '0' para apagarlo: ")
        
        # Verificar si el usuario ingresó un comando válido
        if comando == '1' or comando == '0':
            # Enviar el comando al Arduino a través de Bluetooth
            ser.write(comando.encode())
            print(f"Comando enviado: {'Encender' if comando == '1' else 'Apagar'} LED")
            
            # Salir del bucle si el comando es '0'
            if comando == '0':
                break
        else:
            print("Comando inválido. Por favor ingrese '1' o '0'.")
    
except serial.SerialException as e:
    print("Error al intentar establecer la conexión:", e)
except KeyboardInterrupt:
    # Manejar la interrupción del teclado para cerrar el puerto serial antes de salir
    print("\nInterrupción del usuario. Cerrando la conexión...")
finally:
    # Cerrar el puerto serial en el bloque finally para asegurarse de que siempre se cierre
    if 'ser' in locals():
        ser.close()
        print("Conexión cerrada.")
