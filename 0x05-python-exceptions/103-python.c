#include <stdio.h>
#include < ctypes.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about a Python list object.
 * @p: A pointer to the PyObject to print.
 **/
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", PyList_GetAlloc(p));

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("  Element %zd: ", i);
        print_python_object(item);
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object.
 * @p: A pointer to the PyObject to print.
 **/
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);

    if (Py_SAFE_DOWNCAST(size, Py_ssize_t, 10) >= 0)
    {
        printf("  trying string: ");
        for (i = 0; i < size && string[i] != '\0'; i++)
        {
            if (isprint(string[i]))
                printf("%c", string[i]);
            else
                printf("\\x%02x", string[i]);
        }
        printf("\n");
    }
    else
    {
        printf("  [WARNING] Truncating the string\n");
        for (i = 0; i < 10; i++)
        {
            if (isprint(string[i]))
                printf("%c", string[i]);
            else
                printf("\\x%02x", string[i]);
        }
        printf("...\n");
    }

    printf("  first %zd bytes: ", Py_MIN(size, (Py_ssize_t)10));
    for (i = 0; i < Py_MIN(size, (Py_ssize_t)10); i++)
    {
        printf("%02x ", (unsigned char)string[i]);
    }
    printf("\n");
}

/**
 * print_python_float - Prints basic info about a Python float object.
 * @p: A pointer to the PyObject to print.
 **/
void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %g\n", value);
}