from serverManager import ServerManager

PORT = 9090


def main():
    server = ServerManager(PORT)
    server.run()


if __name__ == '__main__':
    main()
