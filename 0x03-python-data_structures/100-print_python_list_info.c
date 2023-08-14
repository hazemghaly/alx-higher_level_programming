#include <Python.h>

/**
 * print_python_list_info - prints information of a python list
 * @p: list object
 */

void print_python_list_info(PyObject *p)
{
int s, i;
s = Py_SIZE(p);
PyListObject *ha;
ha = (PyListObject *)p;
printf("[*] Size of the Python List = %d\n", s);
printf("[*] Allocated = %ld\n", ha->allocated);
for (i = -1 ; i < s; i++)
{
printf("Element %d: %s\n", i, ha->ob_item[i]->ob_type->tp_name);
}
}
