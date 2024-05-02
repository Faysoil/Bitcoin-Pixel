import http.server
import socketserver
from datetime import datetime

PORT = 9090

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


# class Block:
#     def __init__(self, id, prev_id, data, height, timestamp):
#         self.prev_id = prev_id
#         self.data = data
#         self.height = height
#         self.nonce = randomNounce()
          # Getting the current date and time
#         dt = datetime.now()
          # getting the timestamp
#         ts = datetime.timestamp(dt)
#         self.timestamp = ts
          # Calculer l'identifiant du bloc
#         self.id = self.calculate_hash()
    
    # def randomNounce():
    #     number_of_strings = 5
    #     length_of_string = 8
    #     for x in range(number_of_strings):
    #         return (
    #             "".join(
    #                 random.choice(string.ascii_letters + string.digits)
    #                 for _ in range(length_of_string)
    #             )
    #         )

    #def calculate_hash(self):
    #   block_string = json.dumps({
    #      "prev_id": self.prev_id,
            "data": self.data,
            "height": self.height,
            "nonce": self.nonce,
            "timestamp": self.timestamp
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
