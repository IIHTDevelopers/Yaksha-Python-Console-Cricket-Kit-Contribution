import unittest
from usecase import Purchase
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_object_type_purchase(self):
        obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
        test_obj = TestUtils()
        if type(obj)==type(Purchase(1,'2-3-2021','venu',200)):
            test_obj.yakshaAssert("TestObjectTypePurchase", True, "functional")
            print("TestObjectTypePurchase = Passed")
        else:
            test_obj.yakshaAssert("TestObjectTypePurchase", False, "functional")
            print("TestObjectTypePurchase = Failed")

    def test_object_type(self):
        obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
        test_obj = TestUtils()
        if type(obj)!=type(None):
            test_obj.yakshaAssert("TestObjectType", True, "functional")
            print("TestObjectType = Passed")
        else:
            test_obj.yakshaAssert("TestObjectType", False, "functional")
            print("TestObjectType = Failed")
