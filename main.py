"""from threading import Thread"""

from app import app

if __name__ == '__main__':
    app.run(port='8080')

    """   
    server_thread = Thread(target=app.run, daemon=True, kwargs={'port': 8080,
                                                            'threaded': True}).start()
    """
