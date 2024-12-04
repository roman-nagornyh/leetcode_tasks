class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)  # Создаем "пустой" узел для упрощения
    current = dummy_head
    carry = 0  # Перенос

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Получаем значение из первого списка или 0
        val2 = l2.val if l2 else 0  # Получаем значение из второго списка или 0

        # Суммируем значения и перенос
        total = val1 + val2 + carry
        carry = total // 10  # Обновляем перенос
        current.next = ListNode(total % 10)  # Создаем новый узел с остатком
        current = current.next  # Переходим к следующему узлу

        # Переходим к следующему узлу в списках, если они не пустые
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next  # Возвращаем следующий узел после "пустого" узла