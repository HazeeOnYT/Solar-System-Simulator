from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import turtle

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            with open('index.html', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/turtle.js':
            with open('turtle.js', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/javascript')
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/styles.css':
            with open('styles.css', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server running on port 8000')
    httpd.serve_forever()

# Run the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Turtle code
def turtle_draw():
    screen = turtle.Screen()
    turtle.speed(2)
    turtle.hideturtle()

    def draw_planet(planet_name):
        turtle.reset()
        turtle.penup()
        turtle.goto(0, -100)
        turtle.write(planet_name, align="center", font=("Arial", 12, "normal"))
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.circle(50)

    def spin_planet():
        turtle.right(10)

    screen.onkey(spin_planet, 's')
    screen.listen()

    turtle.mainloop()

# Start Turtle drawing
turtle_thread = threading.Thread(target=turtle_draw)
turtle_thread.start()
