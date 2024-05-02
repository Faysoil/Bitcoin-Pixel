import http.server
import socketserver

PORT = 9090

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Récupérer l'URL demandée (chemin)
        url = self.path

        # Créer le message de réponse incluant l'URL demandée
        message1 = f"Bonjour! Vous avez atteint la fonction 'hello' de ce serveur."
        
        self.wfile.write(message1.encode('utf-8'))
        self.wfile.write(url.encode('utf-8'))

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Le serveur est démarré sur le port {PORT}")
    httpd.serve_forever()
