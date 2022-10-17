""" Module: advanced Python
Assignment #5 (October 18, 2021)


--- Goal
Write a class to handle a sequence of voltage measurements at different times.

--- Specifications
- the class name must be VoltgeData
- the class must be initialized with two generic iterables of the same length
  holding the numerical values of times and voltages
- alternatively the class can be initialized from a text file
- the class must expose two attributes: 'times' and 'voltages', each returning
  a numpy array of type numpy.float64 of the corresponding quantity.
- the values should be accessible with the familiar square parenthesis syntax:
  the first index must refer to the entry, the second selects time (0) or
  voltage (1). Slicing must also work.
- calling the len() function on a class instance must return the number of
  entries
- the class must be iterable: at each iteration, a numpy array of two
  values (time and voltage) corresponding to an entry in the file must be
  returned
- the print() function must work on class instances. The output must show one
  entry (time and voltage), as well as the entry index, per line.
- the class must also have a debug representation, printing just the values
  row by row
- the class must be callable, returning an interpolated value of the tension
  at a given time
- the class must have a plot() method that plots data using matplotlib.
  The plot function must accept an 'ax' argument, so that the user can select
  the axes where the plot is added (with a new figure as default). The user
  must also be able to pass other plot options as usual
- [optional] rewrite the run_tests() function in sandbox/test_voltage_data.py
  as a sequence of proper UnitTests
- [optional] support a third optional column for the voltage errors """

import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

class VoltageData:
    """Class to process a sequence of voltages at different times"""

    def __init__(self, times, voltages):
        """Constructor"""
        assert len(times) == len(voltages)
        t_array = np.array(times, dtype=np.float64)
        v_array = np.array(voltages, dtype=np.float64)
        self._data = np.column_stack((t_array, v_array))
        self.spline = scipy.interpolate.InterpolatedUnivariateSpline(t_array, v_array, k=3)

    def __len__(self):
        return len(self._data)

    @property
    def times(self):
        """Time array getter"""
        return self._data[:, 0]

    @property
    def voltages(self):
        """Voltage array getter"""
        return self._data[:, 1]

    def __getitem__(self, index):
        return self._data[index]

    @classmethod
    def from_file(cls, path):
        """Alternative constructor from file"""
        t_array, v_array = np.loadtxt(path, unpack=True)
        return cls(t_array, v_array)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return str(self._data)

    def __str__(self):
        rows=[]
        for i, element in enumerate(self):
            rows.append(f'INDEX:{i}, TIME: {element[0]}, VOLTAGE: {element[1]} ')
        return '\n'.join(rows)

    def __call__(self, timestamp):
        return self.spline(timestamp)

    def plot(self, ax=None, fmt='-g', **optional_args):
        """Plot function using mathplotlib.pyplot"""
        if ax is None:
            ax = plt.figure('Voltage vs Time')
        else:
            plt.sca(ax)
        plt.plot(self.times, self.voltages, fmt, **optional_args)
        plt.xlabel('Time[s]')
        plt.ylabel('Voltage[V]')
        plt.grid(True)
