from testdomain import testRezervare
from testCRUD import test_adauga_rezervare, test_sterge_rezervare
from testlogic import testReducere, testUpperClass, testMaximPeClase, testOrdonare, testSumaPreturi
from testundoredo import test_undo_redo


def runAllTests():
    testRezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    testReducere()
    testMaximPeClase()
    testUpperClass()
    testOrdonare()
    testSumaPreturi()
    test_undo_redo()