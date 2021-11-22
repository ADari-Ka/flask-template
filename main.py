"""from threading import Thread"""

from app import app

app.run()

"""   
server_thread = Thread(target=app.run, daemon=True, kwargs={'port': 8080,
                                                            'threaded': True}).start()
"""
