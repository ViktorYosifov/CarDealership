class InvQueue:

    def __init__(self):
        self._queue = []

    def add(self, item):
        if item:
            self._queue.append(item)
            return item
        else:
            return None

    def get(self):
        if not self.is_epmty():
            return self._queue.pop(0)
        else:
            return None

    def is_epmty(self):
        return len(self._queue) == 0

    def list(self):
        return self._queue

    def display_last(self):
        if not self.is_epmty():
            return self._queue[0]
        return None


if __name__ == "__main__":
    my_inv = InvQueue()
    my_inv.add('Item 1')
    my_inv.add('Item 2')
    print(my_inv.is_epmty())
    print(my_inv.get())
