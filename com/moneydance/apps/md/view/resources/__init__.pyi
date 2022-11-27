from typing import List, TypeVar
import com.infinitekind.moneydance.model
import com.infinitekind.util
import com.moneydance.apps.md.controller
import com.moneydance.apps.md.view.gui

T = TypeVar("T")


class DisplayableChoice:
    def __init__(self, mDResourceProvider: 'MDResourceProvider', t: 'T'): ...
    
    def equals(self, o: object) -> bool: ...
    
    def getValue(self) -> 'T': ...
    
    def hashCode(self) -> int: ...
    
    def toString(self) -> str: ...
    
    
class BalanceTypeChoice(DisplayableChoice):
    def __init__(self, mDResourceProvider: 'MDResourceProvider', c: com.moneydance.apps.md.controller.BalanceType): ...
    
    
class DisplayableObject:
    def __init__(self): ...
    
    def getResourceKey(self) -> str: ...
    
    
class InitialAccountsLoader:
    def __init__(self): ...
    
    @staticmethod
    def readAccountsFromTable(c: com.infinitekind.moneydance.model.AccountBook, c2: com.moneydance.apps.md.view.gui.MDStrings, c3: com.infinitekind.moneydance.model.CurrencyTable, c4: com.infinitekind.moneydance.model.Account, c5: com.infinitekind.util.StreamVector, c6: com.infinitekind.moneydance.model.CurrencyType) -> None: ...
    
    
class MDResourceProvider:
    def __init__(self): ...
    
    def getIcon(self, s: str) -> 'javax.swing.Icon': ...
    
    def getImage(self, s: str) -> 'java.awt.Image': ...
    
    def getResources(self) -> 'Resources': ...
    
    def getStr(self, s: str) -> str: ...
    
    def strings(self) -> com.moneydance.apps.md.view.gui.MDStrings: ...
    
    
class Resources('java.util.ResourceBundle'):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def containsKey(self, s: str) -> bool: ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    def getAccountType(self, s: str) -> str: ...
    
    def getBalanceType(self, s: str) -> str: ...
    
    def getCalendarFieldString(self, c: com.infinitekind.moneydance.model.PeriodType) -> str: ...
    
    def getCheckNumberList(self, c: com.infinitekind.moneydance.model.Account) -> List[str]: ...
    
    def getColorLabel(self, s: str) -> str: ...
    
    def getDebtPaymentSpec(self, s: str) -> str: ...
    
    def getDefaultCheckNumberSettings(self) -> com.infinitekind.moneydance.model.CheckNumSettings: ...
    
    def getKeys(self) -> 'java.util.Enumeration': ...
    
    def getLocale(self) -> 'java.util.Locale': ...
    
    def getRateAdjustmentOption(self, c: com.infinitekind.moneydance.model.RateAdjustmentOption) -> str: ...
    
    def getShortAccountType(self, s: str) -> str: ...
    
    def getSortFieldName(self, c: com.infinitekind.moneydance.model.TxnSortOrder) -> str: ...
    
    def labelify(self, s: str) -> str: ...
    
    def setLocale(self, j: 'java.util.Locale') -> None: ...
    
    def strings(self) -> com.moneydance.apps.md.view.gui.MDStrings: ...
    
    
class Resources_af(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_cn(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_cs(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_da(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_de(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_el(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    
class Resources_en(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    
class Resources_en_UK(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    
class Resources_en_AU(Resources_en_UK):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    
class Resources_en_GB(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    
class Resources_es(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_fa(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_fr(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_hr(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_it(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_ja(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_jp(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_ko(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_nl(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_no(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_pt_BR(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_pt_PT(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_ru(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_ua(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_uk(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
class Resources_zh(Resources):
    OVERRIDE_DICTIONARY = None
    
    def __init__(self): ...
    
    def convertNumberToText(self, i: int, c: com.infinitekind.moneydance.model.CurrencyType) -> str: ...
    
    
