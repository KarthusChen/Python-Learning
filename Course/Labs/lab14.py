class LabException(Exception):
    pass

try:
    raise LabException("This is the LabException!")
except LabException as LE:
    print("The Lab Exception:",LE,sep="\n")