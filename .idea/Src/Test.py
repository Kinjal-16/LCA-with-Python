from Insertion import *
import unittest

class LcaTest(unittest.TestCase):

    def test_LCA1(self):
        a = [15, 10, 25, 8, 12, 20, 30, 6, 9, 18, 22];
        r = Node(a[0])
        a.pop(0);
        for x in a:
            r = insert(r, x)
        self.assertEquals(lca(r, 6, 12),10)
        self.assertEquals(lca(r, 10, 15), 15)
        self.assertEquals(lca(r, 22, 30), 25)
        self.assertEquals(lca(r, 10, 12), 10)

    def test_LCA2(self):
        b= [3,10,16,29]
        q = Node(b[0])
        b.pop(0);
        for x in b:
            q = insert(q,x)
        self.assertEquals(lca(q, 16, 29),16)
        self.assertEquals(lca(q, 10, 10), 10)
