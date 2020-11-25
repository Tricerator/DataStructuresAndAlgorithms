#!/usr/bin/env python3


class Node:

    def __init__(self, value):
        self.value = value
        self.descendant = None


class LinkedList(object):

    def __init__(self, value=None):

        if value is None:
            self.root = None
            return
        if type(value).__name__ == 'list':
            if len(value) == 0:
                self.root = None
            else:
                self.root = Node(value[0])
                for i in value[1:]:
                    self.Add(i)


        else:
            self.root = Node(value)

    def AddToBeginning(self, value):
        node = Node(value)
        node.descendant = self.root
        self.root = node

    def Add(self, value):
        node = self.root
        while node.descendant is not None:
            node = node.descendant
        node.descendant = Node(value)

    def PrintList(self):
        print(self.createList())

    def createList(self):
        myList = []
        myNode = self.root

        while myNode is not None:
            myList.append(myNode.value)
            myNode = myNode.descendant
        return myList

    def Search(self, value):
        myNode = self.root

        while myNode is not None:
            if myNode.value == value:
                return True
            myNode = myNode.descendant
        return False

    def RemoveValue(self, value):
        node = self.root
        if node.value == value:
            self.root = self.root.descendant
            return True
        previousNode = node
        node = node.descendant
        while node is not None:
            if node.value == value:
                previousNode.descendant = node.descendant
                return True
            previousNode = node
            node = node.descendant
        return False

    def RemoveAllPositionsOfValue(self, value):
        a = True
        while a:
            a = self.RemoveValue(value)
