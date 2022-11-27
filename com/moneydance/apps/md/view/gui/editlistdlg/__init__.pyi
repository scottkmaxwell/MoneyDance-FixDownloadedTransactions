from typing import List
import com.moneydance.apps.md.view.gui


class EditCommandType('java.lang.Enum'):
    ADD = 'ADD'
    DELETE = 'DELETE'
    EDIT = 'EDIT'
    NONE = 'NONE'
    
    def __init__(self): ...
    
    @staticmethod
    def valueOf(s: str) -> 'EditCommandType': ...
    
    @staticmethod
    def values() -> List['EditCommandType']: ...
    
    
class EditStringListDialog(com.moneydance.apps.md.view.gui.SecondaryDialog, com.moneydance.apps.md.view.gui.OKButtonListener):
    pass
    
class EditStringListResult:
    def __init__(self): ...
    
    def getCommandType(self) -> EditCommandType: ...
    
    def getEditedText(self) -> str: ...
    
    def getOriginalText(self) -> str: ...
    
    def isInUse(self) -> List[str]: ...
    
    def toString(self) -> str: ...
    
    
