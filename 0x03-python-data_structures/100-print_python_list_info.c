#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - A function that prints the python list info
 * @p: a python object pointer
 * Description: Using the python header, we use a c to print out
 * what goes on under the hood using c
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
