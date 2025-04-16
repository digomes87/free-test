import unittest
from tentando import ExceptionDemo


class TestExceptionDemo(unittest.TestCase):

    def assertRaisesWithMessage(self, exception_class, func):
        with self.assertRaises(exception_class):
            func()


    def test_arithmetic_error(self):
        self.assertRaisesWithMessage(ArithmeticError, ExceptionDemo.arithmetic_error)

    
    def test_floating_point_error(self):
        self.assertRaisesWithMessage(FloatingPointError, ExceptionDemo.floating_point_error)

    
    def test_overflow_error(self):
        self.assertRaisesWithMessage(OverflowError, ExceptionDemo.overflow_error)


    def test_zero_division_error(self):
        self.assertRaisesWithMessage(ZeroDivisionError, ExceptionDemo.zero_division_error)


    def test_assertion_error(self):
        self.assertRaisesWithMessage(AssertionError, ExceptionDemo.assertion_error)

    
    def test_attribute_error(self):
        self.assertRaisesWithMessage(AttributeError, ExceptionDemo.attribute_error)


    def test_buffer_error(self):
        self.assertRaisesWithMessage(BufferError, ExceptionDemo.buffer_error)


    def test_eof_error(self):
        self.assertRaisesWithMessage(EOFError, ExceptionDemo.eof_error)


    def test_import_error(self):
        self.assertRaisesWithMessage(ImportError, ExceptionDemo.import_error)


    def test_module_not_found_error(self):
        self.assertRaisesWithMessage(ModuleNotFoundError, ExceptionDemo.module_not_found_error)


    def test_index_error(self):
        self.assertRaisesWithMessage(IndexError, ExceptionDemo.index_error)


    def test_key_error(self):
        self.assertRaisesWithMessage(KeyError, ExceptionDemo.key_error)


    def test_lookup_error(self):
        self.assertRaisesWithMessage(LookupError, ExceptionDemo.lookup_error)


    def test_memory_error(self):
        self.assertRaisesWithMessage(MemoryError, ExceptionDemo.memory_error)


    def test_name_error(self):
        self.assertRaisesWithMessage(NameError, ExceptionDemo.name_error)


    def test_unbound_local_error(self):
        self.assertRaisesWithMessage(UnboundLocalError, ExceptionDemo.unbound_local_error)



if __name__ == "__main__":
    unittest.main()
