#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: A pointer to a Python object.
 *
 * Description:
 *   This function prints the size (allocated and actual) and the type
 *   of each element of a Python list.
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    size_t i, allocated;

    if (!PyList_Check(p))
    {
        printf("[*] Not a Python list\n");
        return;
    }

    list = (PyListObject *)p;
    allocated = list->ob_alloc;
    printf("[*] Size of the Python List = %zu\n", PyList_GET_SIZE(list));
    printf("[*] Allocated = %zu\n", allocated);

    for (i = 0; i < PyList_GET_SIZE(list); i++)
    {
        PyObject *element = PyList_GET_ITEM(list, i);
        printf("  Element %zu: %s\n", i, Py_TYPE(element)->tp_name);
    }
}