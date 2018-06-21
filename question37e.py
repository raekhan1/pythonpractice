def doesExist(number):

    current = self.firstnode
    if current.value == number:
        return True

    while current.next is not None:
        if current.next.value == number:
            return True

        else:
            current = current.next

    return False
