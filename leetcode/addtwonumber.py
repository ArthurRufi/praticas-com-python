# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Obter os valores atuais dos nós ou 0 se não houver nós
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calcular a soma dos valores atuais e do transporte
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Adicionar um novo nó com o dígito à lista resultante
            current.next = ListNode(digit)
            current = current.next
            
            # Avançar para o próximo nó em ambas as listas se disponível
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Retornar a lista resultante, ignorando o nó inicial
        return dummy_head.next
