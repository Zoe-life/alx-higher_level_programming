# include <stdio.h>
# include <stdlib.h>
# include <stdarg.h>
# include <limits.h>  // For INT_MAX

# if defined(__FreeBSD__) || defined(__APPLE__)
# include <floatingpoint.h>
# endif

/**
* print_python_list - Prints basic info about a Python list object
* @ p: A pointer to the Python object
*/
void print_python_list(PyObject * p)
{
    Py_ssize_t size, i
    PyObject * item

    if (PyList_Check(p) == 0)
    {
        printf("[.] not a list\n")
        return
    }

    size = PyList_Size(p)
    printf("[*] Python list info\n")
    printf("[*] Size of the Python List = %zd\n", size)
    printf("[*] Allocated = %zd\n", PyList_GetAlloc(p))

    for (i=0
         i < size
         i++)
    {
        item = PyList_GetItem(p, i)
        printf("  Element %zd: ", i)

        / * Try to print a string representation * /
        if (PyUnicode_Check(item))
        {
            PyObject * obj_str = PyUnicode_AsUTF8String(item)

            if (obj_str)
            {
                char * str = PyBytes_AsString(obj_str)
                printf("[Unicode] %s\n", str)
                Py_DECREF(obj_str)
            }
            else
            {
                PyErr_Clear()
                printf("[UNKNOWN]\n")
            }
        }
        else if (PyBytes_Check(item))
        {
            print_python_bytes(item)
        }
        else if (PyLong_Check(item))
        {
            printf("[Long] %ld\n", PyLong_AsLong(item))
        }
        else if (PyFloat_Check(item))
        {
            # if defined(__FreeBSD__) || defined(__APPLE__)
            double val = PyFloat_AsDouble(item)
            if (isnan(val) | | isinf(val))
            {
                printf("[NaN] ")
            }
            else
            {
                printf("[Float] %g\n", val)
            }
            # else
            printf("[Float] %f\n", PyFloat_AsDouble(item))
            # endif
        }
        else
        {
            printf("[UNKNOWN]\n")
        }
    }
}

/**
* print_python_bytes - Prints basic info about a Python bytes object
* @ p: A pointer to the Python object
*/
void print_python_bytes(PyObject * p)
{
    Py_ssize_t size, i
    char * str

    if (PyBytes_Check(p) == 0)
    {
        printf("[.] not a bytes object\n")
        return
    }

    size = PyBytes_Size(p)
    printf("[.] bytes object info\n")
    printf("  size: %zd\n", size)

    printf("  trying string: ")
    str = PyBytes_AsString(p)
    for (i=0
         i < size & & i < 10
         i++)
    {
        printf("%02x", (unsigned char)str[i])
        if (i < size - 1)
        printf(" ")
    }
    if (size > 10)
    printf(" ...")
    printf("\n")
}
