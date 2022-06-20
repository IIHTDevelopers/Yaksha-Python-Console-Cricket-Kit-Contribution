import unittest
from usecase import Purchase
from myexception import InvalidWholeSaleError
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_whole_sale_error(self):
        test_obj = TestUtils()
        try:
            obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,helmet,1500.00,4,vickets,1500.00,2")
            test_obj.yakshaAssert("TestWholeSaleError", False, "exception")
            print("TestWholeSaleError = Failed")
        except InvalidWholeSaleError as e:
            test_obj.yakshaAssert("TestWholeSaleError", True, "exception")
            print("TestWholeSaleError = Passed")
    def test_value_error(self):
        test_obj = TestUtils()
        try:
            obj=Purchase.obtain_purchase_with_amount("101abc,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
            test_obj.yakshaAssert("TestValueError", False, "exception")
            print("TestValueError = Failed")
        except InvalidWholeSaleError as e:
            test_obj.yakshaAssert("TestValueError", True, "exception")
            print("TestValueError = Passed")
