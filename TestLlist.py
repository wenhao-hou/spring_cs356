import imp

import unittest

from linkedList import linkedList

class TestLinked(unittest.TestCase):
    def  setUp(self):
        self.linked = linkedList()

def test_insertatbeg(self):
    mylist = linkedList()
    mylist = insertAtBeginning(1)
    list2 = linkedList()
    list2.inserAtBeginning(1)

    #comparing twp list 

    self.assertEqual(mylist,list2)
    # only works if we define __eq__method 

def test_insertatbeg2(self):
    mylist = linkedList()
    mylist = insertAtBeginning(1)
    res = mylist.find(1)
    self.assertEqual(res,1)
    self.assertEqual(mylist.traverse(), [1])
def test_traverse(self):
    mylist = linkedList()
    for i in range(8):
        mylist.insertAtBeginning(1)
    self.assertEqual(mylist.traverse(), [0,1,2,3,4,5,6,7])



def test_insert_del(self):
    mylist = [5,40,11,3]
    alist = helper[mylist]
    alist.insertAtEnd(5)
    alist.delFromEnd()
    self.assertEqual(alist.traverse(), mylist)    

def helper(self,datalist):
    mylist = linkedList
    for item in datalist:
        mylist.insertAtEnd()
    return mylist