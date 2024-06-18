class QueueError(???):  # Eligir la clase base para la nueva excepción.
    #
    #  Escribe el código aquí.
    #


class Queue:
    def __init__(self):
        #
        # Escribe el código aquí.
        #

    def put(self, elem):
        #
        # Escribe el código aquí.
        #

    def get(self):
        #
        # Escribe el código aquí.
        #


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    