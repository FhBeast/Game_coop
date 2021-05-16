from game import Game
from Server.serverManager import ServerManager
import threading


def main():
    while True:
        show_menu()
        answer = int(input("Enter: "))
        if answer == 0:
            port = int(input("Enter port: "))
            thread_server = threading.Thread(target=run_server, args=(port,))
            thread_server.start()
            break
        elif answer == 1:
            port = int(input("Enter port: "))
            break
    run_client(port)


def show_menu():
    print("0 - Run server\n"
          "1 - Connect to server")


def run_client(port):
    game = Game(1400, 900, port)
    game.run_game()


def run_server(port):
    server = ServerManager(port)
    server.run()


if __name__ == '__main__':
    main()
