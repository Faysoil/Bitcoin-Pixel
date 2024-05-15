import http.server
import socketserver
from datetime import datetime
from flask import Flask

app = Flask(__name__)

PORT = 9090
blockchain = []

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        genesis = create_genesis_block()
        blockchain.append(genesis)
        print(blockchain)
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
@app.route('/verify')
def verify(block):
    if not block:
        message = "BLOCK_MISSING"
        print(message.encode('utf-8'))
        return false
    if len(block.id) != 256:
        message = "BLOCK_INCORRECT"
        print(message.encode('utf-8'))
        return false
    if len(block.prev_id) != 256:
        message = "BLOCK_INCORRECT"
        print(message.encode('utf-8'))
        return false
    if not block.data:
        message = "BLOCK_INCORRECT"
        print(message.encode('utf-8'))
        return false
    if len(block.nounce) != 256:
        message = "BLOCK_INCORRECT"
        print(message.encode('utf-8'))
        return false
    if not isinstance(block.height, int):
        message = "BLOCK_INCORRECT"
        print(message.encode('utf-8'))
        return false
    if not isinstance(block.timestsamp, int):
        message = "BLOCK_INCORRECT"
        print(message.encode('utf-8'))
        return false
    for i in range(len(block.data)):
        if not verifytx(block.data[i])
            message = "TX_NOK"
            print(message.encode('utf-8'))
            return false
    message = "BLOCK VERIfIED"
    print(message.encode('utf-8'))
    return true

#Pour verifier la validite d'une transaction
def verifytx(tx):
    if len(tx.addrSender) != 256:
        message = "TX_NOK"
        print(message.encode('utf-8'))
        return false
    if len(tx.addrRcpt) != 256: 
        message = "TX_NOK"
        print(message.encode('utf-8'))
        return false
    if len(tx.amount) != 256:
        message = "TX_NOK"
        print(message.encode('utf-8'))
        return false
    if not isinstance(tx.timestsamp, int):
        message = "TX_NOK"
        print(message.encode('utf-8'))
        return false
    if not isinstance(tx.sig, str):
        message = "TX_NOK"
        print(message.encode('utf-8'))
        return false
    message = "TX_OK"
    print(message.encode('utf-8'))
    return true

class Transaction:
    def __init__(self, addrSender, addrRcpt, amount, timestamp):
        self.addrSender = addrSender  # Adresse de l'émetteur
        self.addrRcpt = addrRcpt      # Adresse du destinataire
        self.amount = amount          # Montant de la transaction
        self.timestamp = timestamp    # Horodatage de la transaction
        

#Verification + Validation
@app.route('/newtx')
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
    
@app.route('/newblock')
def new_block(bloc):
    tmp = 0
    i = bloc.height
    length = len(bloc)
    while i < len(blockchain):
        tmp += len(blockchain[i].data)
        i=i+1
    if tmp < length:
        return "Bloc ajouté"
        #Transaction ajouté à la blockchain
    return "Bloc non ajouté"

def calculate_hash(block):
    block_string = str(block.id) + str(block.previous_hash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return hashlib.sha256(block_string.encode()).hexdigest()

# Creation bloc genesis
def create_genesis_block():
    
    genesis_transaction = Transaction("genesis_sender", "genesis_recipient", 1000, time.time())

    genesis_block_data = [genesis_transaction]

    genesis_id = 0
    genesis_previous_hash = "0"
    genesis_timestamp = time.time()
    genesis_nonce = 0

    genesis_hash = calculate_hash(Block(genesis_id, genesis_previous_hash, genesis_timestamp, genesis_block_data, genesis_nonce))

    genesis_block = Block(genesis_id, genesis_previous_hash, genesis_timestamp, genesis_block_data, genesis_hash, genesis_nonce)

    return genesis_block

# Test
genesis_block = create_genesis_block()
print("Genesis Block ID:", genesis_block.id)
print("Genesis Block Previous Hash:", genesis_block.previous_hash)
print("Genesis Block Timestamp:", genesis_block.timestamp)
print("Genesis Block Data:", genesis_block.data)
print("Genesis Block Hash:", genesis_block.hash)
print("Genesis Block Nonce:", genesis_block.nonce)
