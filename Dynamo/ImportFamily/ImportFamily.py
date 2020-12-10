import clr
import System.IO

# Import DesignScript Grometry Library
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

from System.Collections.Generic import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# 이 노드에 대한 입력값은 IN 변수에 리스트로 저장됩니다.
dataEnteringNode = IN

# 코드를 이 선 아래에 배치
def GetFamily(Rfa_FileFullPath):

    family = None
    
    familyname = System.IO.Path.GetFileNameWithoutExtension(Rfa_FileFullPath)
    collector = FilteredElementCollector(doc).OfClass(Family).ToElements()
    for f in collector:
        if f.Name == familyname:
            family = f
            break
            
    if family != None:
        return family

    else:
    
        TransactionManager.Instance.EnsureInTransaction(doc)
        
        success, f = doc.LoadFamily.Overloads.Functions[0](Rfa_FileFullPath)
        
        TransactionManager.Instance.TransactionTaskDone()

        return f

def GetDefaultFamilySymbol(family):
    if family == None:
        return None
    else:
    	
        symbols_id = family.GetFamilySymbolIds().GetEnumerator()
        symbols_id.MoveNext()
        symbol = doc.GetElement(symbols_id.Current)
        return symbol
        

rfafile = IN[0]

family = GetFamily(rfafile)

OUT = GetDefaultFamilySymbol(family).ToDSType(True)