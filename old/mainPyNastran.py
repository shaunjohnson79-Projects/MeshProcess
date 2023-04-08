import pyNastran
#print (pyNastran.__file__)
#print (pyNastran.__version__)
#pkg_path = pyNastran.__path__[0]

from pyNastran.bdf.bdf import BDF, read_bdf
from pyNastran.utils import object_attributes, object_methods

def main():
    print("Hello World!")
    fileName="nastran_input.nas"
    
    # create the BDF object
    bdf = BDF()

    # read the file from the GUI
    # don't cross-reference
    bdf.read_bdf(fileName, xref=False)
    
    print(object_attributes(bdf))
    #   print(object_methods(bdf))
    
    print("attributes = [%s]\n" % ', '.join(bdf.object_attributes()))
    print("methods = [%s]\n" % ', '.join(bdf.object_methods()))

    print(bdf.get_bdf_stats())
    print("card_count = %s\n" % bdf.card_count)
    print("reject_count = %s" % bdf.reject_count)

if __name__ == "__main__":
    main()
