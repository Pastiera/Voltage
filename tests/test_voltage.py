import unittest
import os
import numpy as np
import matplotlib.pyplot as plt

from Voltage.Voltage import VoltageData

class TestVoltageData(unittest.TestCase):

    def setUp(self, lenght = 12):
        """ Test setup"""
        self.lenght = lenght
        self.t = np.linspace(0., 3., lenght)
        self.v = np.random.rand(lenght)
        self.load_file = os.path.abspath("data/sample_data_file.txt")

    def load_data(self):
        """Utility function to generate the test object"""
        test_data = VoltageData(self.t, self.v)
        return test_data

    def test_constructor(self):
        """Tests that the shape of the object is as expected"""
        test_data = self.load_data()
        self.assertEqual(test_data._data.shape, (self.lenght, 2))

    def test_alt_contructor(self):
        """Test for the alternate constructor loading data from a file.txt"""
        v_data = VoltageData.from_file(self.load_file)

    def test_type(self):
        """Tests the type for times and voltages columns."""
        test_data = self.load_data()
        self.assertTrue(isinstance(test_data.times, np.ndarray))
        self.assertTrue(isinstance(test_data.voltages, np.ndarray))

    def test_num_rows(self):
        """Test to check the number of rows"""
        test_data = self.load_data()
        self.assertEqual(np.size(test_data, 0), self.lenght)

    def test_num_col(self):
        """Test to check the number of columns"""
        test_data = self.load_data()
        self.assertEqual(np.size(test_data, 1), 2)


    def test_getitem(self):
        """Tests the __getitem__ method by direct
        access to the values using square parenthesis syntax."""
        test_data = self.load_data()
        self.assertEqual(test_data[3,0], self.t[3])
        self.assertEqual(test_data[2,1], self.v[2])
        #Slicing test
        self.assertEqual(test_data[1:6,:].shape, (5,2))

    def test_iteration(self):
        """Tests __iter__ method."""
        test_data = self.load_data()
        for element in test_data.times:
            self.assertTrue(isinstance(element, np.float64))

    def test_print(self):
        """Tests __str__ and __repr__ method."""
        test_data = self.load_data()
        print(test_data)
        print(repr(test_data))

    def test_plotting(self):
        test_data = self.load_data()
        plt.figure('Test_plot')
        ax = plt.gca()
        test_data.plot(ax)
        plt.show()




if __name__ == '__main__':
    unittest.main()
