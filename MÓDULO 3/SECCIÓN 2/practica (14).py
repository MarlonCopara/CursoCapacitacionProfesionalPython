class QueueError(???):
    pass


class Queue:
    #
    # Código del laboratorio anterior.
    #


class SuperQueue(Queue):
    #
    # Escribe código nuevo aquí.
    #


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
    