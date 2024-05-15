import http.server
import socketserver
from datetime import datetime

PORT = 9090
blockchain = []

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # Récupérer l'URL (chemin)
        url = self.path

        # Message de réponse par défaut
        message = "Bonjour ! Bienvenue sur IPIxel ;)"

        # Vérifier si l'URL contient "/verify"
        if url != "/verify":
            message = "UNKNOWN ACTION"
        # Envoyer le message de réponse
        self.wfile.write(message.encode('utf-8'))

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Le serveur est démarré sur le port {PORT}")
    httpd.serve_forever()

class Block:
    def __init__(self, id, previous_hash, timestamp, data, hash, nonce):
        self.id = id
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

def verify(block):
    if not block:
        message = "BLOCK_MISSING"
        self.wfile.write(message.encode('utf-8'))
        return
    if len(block.id) != 256:
        message = "BLOCK_INCORRECT"
        self.wfile.write(message.encode('utf-8'))
        return
    if len(block.prev_id) != 256:
        message = "BLOCK_INCORRECT"
        self.wfile.write(message.encode('utf-8'))
        return
    if not data:
        message = "BLOCK_INCORRECT"
        self.wfile.write(message.encode('utf-8'))
        return
    if len(block.nounce) != 256:
        message = "BLOCK_INCORRECT"
        self.wfile.write(message.encode('utf-8'))
        return
    if not isinstance(block.height, int):
        message = "BLOCK_INCORRECT"
        self.wfile.write(message.encode('utf-8'))
        return
    if not isinstance(block.timestsamp, int):
        message = "BLOCK_INCORRECT"
        self.wfile.write(message.encode('utf-8'))
        return
    message = "BLOCK VERIfIED"
    self.wfile.write(message.encode('utf-8'))
        
def verifytx(tx):
    if len(tx.addrSender) != 256
        message = "TX_NOK"
        self.wfile.write(message.encode('utf-8'))
        return
    if len(tx.addrRcpt) != 256 
        message = "TX_NOK"
        self.wfile.write(message.encode('utf-8'))
        return
    if len(tx.amount) != 256
        message = "TX_NOK"
        self.wfile.write(message.encode('utf-8'))
        return
    if not isinstance(tx.timestsamp, int):
        message = "TX_NOK"
        self.wfile.write(message.encode('utf-8'))
        return
    if not isinstance(tx.sig, str):
        message = "TX_NOK"
        self.wfile.write(message.encode('utf-8'))
        return
    message = "TX_OK"
    self.wfile.write(message.encode('utf-8'))

