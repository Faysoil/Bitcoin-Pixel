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

#Pour verifier la validite d'un block
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

#Pour verifier la validite d'une transaction
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

class Transaction:
    def __init__(self, addrSender, addrRcpt, amount, timestamp, sig):
        self.addrSender = addrSender  # Adresse de l'émetteur
        self.addrRcpt = addrRcpt      # Adresse du destinataire
        self.amount = amount          # Montant de la transaction
        self.timestamp = timestamp    # Horodatage de la transaction
        self.sig = sig                # Signature de la transaction

#Verification + Validation
def new_transaction(tx):
    # Vérifier si la transaction est valide en appelant verifytx
    if verifytx(tx):
        # Vérifier si l'émetteur a un solde suffisant
        if check_balance(tx.addrSender, tx.addrRcpt):
            # Ajouter la transaction à la blockchain (a voir)
            
            return "Transaction valide et ajoutée à la blockchain."
        else:
            return "Solde insuffisant pour effectuer la transaction."
    else:
        return "Transaction invalide."

def check_balance(sender, amount):
    # Vérifier le solde de l'émetteur en parcourant la blockchain
    balance = 0
    for block in blockchain:
        for transaction in block.data:
            if transaction.addrSender == sender:
                balance -= transaction.amount
            if transaction.addrRcpt == sender:
                balance += transaction.amount
                
    # Si le solde est suffisant pour la transaction actuelle, retourner True, sinon False
    return balance >= amount
