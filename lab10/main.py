import websocket
import time

def on_message(ws, message):
    print(f"Otrzymano wiadomość: {message}")

def on_error(ws, error):
    print(f"Błąd: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Połączenie zamknięte")

def on_open(ws):
    print("Połączenie otwarte")
    ws.send("Hello, WebSocket!")
    time.sleep(1)
    ws.close()

ws = websocket.WebSocketApp("ws://echo.websocket.org",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
