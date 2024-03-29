#include "Python.h"

/**
 * print_python_string - This Prints all information about Python strings.
 * @p: A PyObject string object.
 * Returns : Nothing to be returned
 */
void print_python_string(PyObject *p)
{
	long int longer;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	longer = ((PyASCIIObject *)(p))->longer;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", longer);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &longer));
}
