import http.server
import socketserver

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
            message = "unknown action."
        # Envoyer le message de réponse
        self.wfile.write(message.encode('utf-8'))

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Le serveur est démarré sur le port {PORT}")
    httpd.serve_forever()


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


# class Block:
#     def __init__(self, prev_id, data, height):
#         self.prev_id = prev_id
#         if not isinstance(data, list) or len(data) == 0:
#             raise ValueError("Data must be a non-empty list") 
#         self.data = data
#         self.height = height
#         self.nonce = randomNounce()
#         self.id = sha256()
