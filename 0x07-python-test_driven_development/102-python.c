#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    PyObject *type_obj, *type_name, *size_obj, *size, *value_obj, *value_str;

    if (!p || !PyString_Check(p)) {
        fprintf(stderr, "[.] invalid string object\n");
        return;
    }

    type_obj = PyObject_Type(p);
    type_name = PyObject_GetAttrString(type_obj, "__name__");
    size_obj = PyObject_Length(p);
    value_obj = PyObject_Str(p);

    if (!type_name || !size_obj || !value_obj) {
        PyErr_Print();
        return;
    }

    size = PyInt_AsLong(size_obj);
    value_str = PyUnicode_AsUTF8AndSize(value_obj, NULL);

    printf("[.] %s info\n", PyUnicode_AsUTF8(type_name));
    printf("  type: %s\n", PyUnicode_AsUTF8(type_name));
    printf("  length: %ld\n", size);
    printf("  value: %s\n", value_str ? value_str : "(unprintable)");

    Py_DECREF(type_obj);
    Py_DECREF(type_name);
    Py_DECREF(size_obj);
    Py_DECREF(size);
    Py_DECREF(value_obj);
    if (value_str)
        PyMem_Free(value_str);
}