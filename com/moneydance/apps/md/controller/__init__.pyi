from typing import Callable, Dict, Iterator, List, Sequence, Set
import com.infinitekind.moneydance.model
import com.infinitekind.util
import com.moneydance.apps.md.extensionapi
import com.moneydance.apps.md.view
import com.moneydance.apps.md.view.gui
import com.moneydance.apps.md.view.gui.editlistdlg
import com.moneydance.apps.md.view.resources
import com.moneydance.security
import olb
import sync


class AccountBookWrapper:
    CRYPTO_LEVEL_KEY = u'md.crypto_level'
    LOCAL_SETTINGS_FILENAME = u'settings'
    PASSWD_CACHE_KEY = u'gen.passwd_cache'
    SAFE_SUBFOLDER_NAME = u'safe'
    SAFE_TMP_SUBFOLDER_NAME = u'safe/tmp'
    STORE_PINS_KEY = u'store_passwords'
    STORE_PINS_PARAM = u'store_passwords'
    
    def __init__(self): ...
    
    @staticmethod
    def createProvisionalWrapper(j: 'java.io.File') -> 'AccountBookWrapper': ...
    
    @staticmethod
    def createWrapperForNewFolder(j: 'java.io.File') -> 'AccountBookWrapper': ...
    
    def getBook(self) -> com.infinitekind.moneydance.model.AccountBook: ...
    
    def getEncryptionHint(self) -> str: ...
    
    def getEncryptionKey(self) -> str: ...
    
    def getEncryptionLevel(self) -> str: ...
    
    def getPublicMetaInfo(self) -> com.infinitekind.util.StreamTable: ...
    
    def getSyncEncryptionPassword(self) -> str: ...
    
    def getSyncFolder(self) -> sync.AbstractSyncFolder: ...
    
    def getUUIDResetFlag(self) -> bool: ...
    
    def isMasterSyncNode(self) -> bool: ...
    
    def isSyncingEnabled(self) -> bool: ...
    
    def loadDataModel(self, c: com.moneydance.security.SecretKeyCallback) -> bool: ...
    
    def loadLegacyFile(self, j: 'java.io.File', i: 'io.FileOpeningContext') -> bool: ...
    
    def loadLocalStorage(self, c: com.moneydance.security.SecretKeyCallback) -> bool: ...
    
    def promoteFromProvisionalFile(self, s: str) -> None: ...
    
    def resetDirtyFlags(self) -> None: ...
    
    def setEncryptionHint(self, s: str) -> None: ...
    
    def setEncryptionKey(self, s: str, s2: str) -> None: ...
    
    def setIsMasterSyncNode(self, b: bool) -> None: ...
    
    def setNeedsResetFromSyncFolder(self) -> None: ...
    
    def setPublicMetaInfo(self, c: com.infinitekind.util.StreamTable) -> None: ...
    
    def setSyncEncryptionPassword(self, s: str) -> None: ...
    
    def setSyncFolder(self, s: sync.AbstractSyncFolder) -> None: ...
    
    def setUUIDResetFlag(self, b: bool) -> None: ...
    
    def toString(self) -> str: ...
    
    @staticmethod
    def wrapperForFolder(j: 'java.io.File') -> 'AccountBookWrapper': ...
    
    @staticmethod
    def wrapperForName(s: str) -> 'AccountBookWrapper': ...
    
    
class AccountFilter:
    def __init__(self, s: str): ...
    
    def addAllowedType(self, s: str) -> None: ...
    
    def addIncludedAccounts(self, c: com.infinitekind.moneydance.model.AccountBook, list: List[str]) -> None: ...
    
    def buildIncludedAccountList(self, c: com.infinitekind.moneydance.model.AccountBook) -> List[com.infinitekind.moneydance.model.Account]: ...
    
    def equals(self, o: object) -> bool: ...
    
    def exclude(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def excludeAllOfType(self, s: str) -> bool: ...
    
    def excludeFromFilter(self, c: com.infinitekind.moneydance.model.AccountBook, c2: com.infinitekind.moneydance.model.AcctFilter) -> None: ...
    
    def excludeId(self, i: int) -> None: ...
    
    def filter(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def filterId(self, i: int) -> bool: ...
    
    def filterType(self, s: str) -> bool: ...
    
    @staticmethod
    def getAccountName(c: com.infinitekind.moneydance.model.AccountBook, s: str) -> str: ...
    
    def getAcctSearch(self) -> com.infinitekind.moneydance.model.AcctFilter: ...
    
    def getAllDisplayResourceKey(self) -> str: ...
    
    def getAllIncluded(self) -> Sequence[str]: ...
    
    def getAllIncludedCollapsed(self) -> Sequence[str]: ...
    
    def getAllowedTypes(self) -> Set[str]: ...
    
    def getDisplayString(self, c: com.infinitekind.moneydance.model.AccountBook, c2: com.moneydance.apps.md.view.resources.MDResourceProvider) -> str: ...
    
    def getFullList(self) -> 'FullAccountList': ...
    
    def getIncludedCount(self) -> int: ...
    
    def hashCode(self) -> int: ...
    
    def include(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def includeAllOfType(self, s: str) -> bool: ...
    
    def includeID(self, s: str) -> None: ...
    
    @staticmethod
    def isAccountNumOrTypeHack(s: str) -> bool: ...
    
    def isAllAccounts(self) -> bool: ...
    
    def isAllowedType(self, s: str) -> bool: ...
    
    def reset(self) -> None: ...
    
    def setFullList(self, fullAccountList: 'FullAccountList') -> None: ...
    
    
class AppEventListener:
    def __init__(self): ...
    
    def handleEvent(self, s: str) -> None: ...
    
    
class AppEventManager:
    ACCOUNT_SELECTED = u'md:account:select'
    APP_EXITING = u'md:app:exiting'
    BUDGET_SELECTED = u'md:viewbudget'
    FILE_AFTER_SAVE = u'md:file:postsave'
    FILE_BEFORE_SAVE = u'md:file:presave'
    FILE_CLOSED = u'md:file:closed'
    FILE_CLOSING = u'md:file:closing'
    FILE_OPENED = u'md:file:opened'
    FILE_OPENING = u'md:file:opening'
    GRAPH_REPORT_SELECTED = u'md:graphreport'
    HOME_SELECTED = u'md:account:root'
    LICENSE_UPDATED = u'md:licenseupdated'
    REMINDERS_SELECTED = u'md:viewreminders'
    
    def __init__(self): ...
    
    def addAppEventListener(self, appEventListener: AppEventListener) -> None: ...
    
    def fireEvent(self, s: str) -> None: ...
    
    def removeAppEventListener(self, appEventListener: AppEventListener) -> bool: ...
    
    
class AppSource:
    def __init__(self): ...
    
    def getAppName(self) -> str: ...
    
    def getAppVersion(self) -> str: ...
    
    def getBottomPanelColorFrom(self) -> int: ...
    
    def getBottomPanelColorTo(self) -> int: ...
    
    def getBundledExtensionIDs(self) -> List[str]: ...
    
    def getCanChangeLocale(self) -> bool: ...
    
    def getCheckPrintingEnabled(self) -> bool: ...
    
    def getDefaultThemeID(self) -> str: ...
    
    def getDirectOFXEnabled(self) -> bool: ...
    
    def getDirectPurchaseURL(self) -> str: ...
    
    def getExcludedExtensions(self) -> List[str]: ...
    
    def getExtensionsEnabled(self) -> bool: ...
    
    def getGUIBackground(self) -> int: ...
    
    def getGUIForeground(self) -> int: ...
    
    def getGradientPanelsEnabled(self) -> bool: ...
    
    def getIconResource(self) -> str: ...
    
    def getLicenseResource(self) -> str: ...
    
    def getLicenseWindowEnabled(self) -> bool: ...
    
    def getMultiCurrencyEnabled(self) -> bool: ...
    
    def getNetworkPreferencesEnabled(self) -> bool: ...
    
    def getOverrideDictionary(self) -> str: ...
    
    def getOverrideResource(self) -> str: ...
    
    def getPurchaseURL(self) -> str: ...
    
    def getRatingURL(self) -> str: ...
    
    def getRegistrationEnabled(self) -> bool: ...
    
    def getSourceID(self) -> str: ...
    
    def getSourceKey(self, s: str, s2: str) -> str: ...
    
    def getSourceName(self) -> str: ...
    
    def getSplashScreenResource(self) -> str: ...
    
    def getStartPageColor(self) -> int: ...
    
    def getStartPageGraphicResource(self) -> str: ...
    
    def getSupportURL(self) -> str: ...
    
    def getTopPanelColorFrom(self) -> int: ...
    
    def getTopPanelColorMiddle(self) -> int: ...
    
    def getTopPanelColorTo(self) -> int: ...
    
    def getUpdatesEnabled(self) -> bool: ...
    
    def getUpgradePurchaseURL(self) -> str: ...
    
    def getUserGuideURL(self) -> str: ...
    
    def getVendorURL(self) -> str: ...
    
    
class AssetTypeGroup:
    def __init__(self, s: str, c: com.infinitekind.moneydance.model.CurrencyType, i: int): ...
    
    def addAccount(self, c: com.infinitekind.moneydance.model.Account, i: int) -> None: ...
    
    def getAccountList(self) -> List[com.infinitekind.moneydance.model.Account]: ...
    
    def getBalance(self, c: com.infinitekind.moneydance.model.Account) -> int: ...
    
    def getPercent(self, c: com.infinitekind.moneydance.model.Account) -> float: ...
    
    def getTotalBalance(self) -> int: ...
    
    
class PreferencesListener:
    def __init__(self): ...
    
    def preferencesUpdated(self) -> None: ...
    
    
class BackgroundOpsThread(AppEventListener, PreferencesListener, 'java.lang.Thread'):
    MAX_PRIORITY = 10
    MIN_PRIORITY = 1
    NORM_PRIORITY = 5
    
    def __init__(self, main: 'Main'): ...
    
    def handleEvent(self, s: str) -> None: ...
    
    def isRunning(self) -> bool: ...
    
    def preferencesUpdated(self) -> None: ...
    
    def run(self) -> None: ...
    
    def runOnBackgroundThread(self, callable: Callable) -> None: ...
    
    def scheduleAutoSaveInSecondsFromNow(self, i: int) -> None: ...
    
    def scheduleNetSync(self) -> None: ...
    
    def stopRunning(self) -> None: ...
    
    def waitForAllTasksToFinish(self) -> None: ...
    
    
class BalanceType('java.lang.Enum', com.moneydance.apps.md.view.resources.DisplayableObject):
    BALANCE = 'BALANCE'
    CLEARED_BALANCE = 'CLEARED_BALANCE'
    CONFIRMED_BALANCE = 'CONFIRMED_BALANCE'
    CURRENT_BALANCE = 'CURRENT_BALANCE'
    DEFAULT = 'CURRENT_BALANCE'
    UNCONFIRMED_TOTAL = 'UNCONFIRMED_TOTAL'
    
    def __init__(self): ...
    
    @staticmethod
    def fromInt(i: int) -> 'BalanceType': ...
    
    @staticmethod
    def fromStandardBalanceType(s: str) -> 'BalanceType': ...
    
    def getConfigKey(self) -> str: ...
    
    def getResourceKey(self) -> str: ...
    
    def standardBalanceType(self) -> str: ...
    
    @staticmethod
    def valueOf(s: str) -> 'BalanceType': ...
    
    @staticmethod
    def values() -> List['BalanceType']: ...
    
    
class BuildInfo:
    def __init__(self): ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    
class Common:
    ACCOUNT_BOOK_ATTACHMENTS_SUBDIR = u'attach'
    ACCOUNT_BOOK_CHECKPOINT_SUBDIR = u'checkpt'
    ACCOUNT_BOOK_EXTENSION = u'.moneydance'
    ARCHIVE_FILE_EXTENSION = u'.moneydancearchive'
    ATTACHMENT_TAG_PREFIX = u'attach.'
    AUTO_SAVE_INTERVAL_IN_SECONDS = '20'
    COUNTRY_NAME_TABLE = "{u'CAN': u'Canada', u'CHE': u'Switzerland', u'USA': u'United States of America', u'ESP': u'Spain', u'FRA': u'France', u'DEU': u'Germany', u'GBR': u'Great Britain', u'ITA': u'Italy', u'NLD': u'Netherlands', u'BEL': u'Belgium'}"
    DEFAULT_SECURITY_DEC_PLACES = 5
    EXTENSION_LIST_DEBUG_URL = u'https://infinitekind.com/app/md.debug/extensions.dct'
    EXTENSION_LIST_URL = u'https://infinitekind.com/app/md/extensions.dct'
    FMODULE_URI_PREFIX = u'moneydance:fmodule:'
    HELP_RSRC = u'/com/moneydance/modules/features/palmsync/help_en.html'
    LICENSE_RSRC = u'/com/moneydance/apps/md/etc/license.txt'
    LOOKUP_FI_ALTERNATE_BASE_URL = u'https://infinitekind.com/app/md.debug/'
    LOOKUP_FI_BASE_URL = u'https://infinitekind.com/app/md/'
    LOOKUP_FI_FILENAME = u'fi2004.dict'
    LOOKUP_FI_SIG_FILENAME = u'fi2004.sig'
    NEXT_CHECKNUM_PREFIX = u'<'
    NEXT_CHECKNUM_SUFFIX = u'>'
    OFX_COUNTRY_CODES = '[BEL, CAN, CHE, DEU, ESP, FRA, GBR, ITA, NLD, USA]'
    OLD_FILE_EXTENSION = u'.md'
    PRINT_CHECKNUM_PREFIX = u'{'
    PRINT_CHECKNUM_SUFFIX = u'}'
    QIF_FORMAT_AUTO = 0
    QIF_FORMAT_DDMMYY = 2
    QIF_FORMAT_MMDDYY = 1
    QIF_FORMAT_YYMMDD = 3
    QIF_MODE_DOWNLOAD = 1
    QIF_MODE_TRANSFER = 0
    ROOT_ACCOUNT_EXTENSION = u'.mdinternal'
    ROOT_ACCOUNT_FILE = u'root.mdinternal'
    TWO_LETTER_COUNTRY_MAP = "{u'DE': u'DEU', u'BE': u'BEL', u'CH': u'CHE', u'UK': u'GBR', u'GB': u'GBR', u'IT': u'ITA', u'FR': u'FRA', u'CA': u'CAN', u'US': u'USA', u'ES': u'ESP', u'NL': u'NLD'}"
    isMac = True
    
    def __init__(self): ...
    
    @staticmethod
    def getArchiveDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getCertificateDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getCountryName(s: str) -> str: ...
    
    @staticmethod
    def getDataRootDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getDocumentsDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getFeatureModulesDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getPreferencesFile() -> 'java.io.File': ...
    
    @staticmethod
    def getPythonDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getRootDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def getTemporaryDirectory() -> 'java.io.File': ...
    
    @staticmethod
    def initialiseDirectories(p: 'platforms.PlatformHelper') -> None: ...
    
    @staticmethod
    def isNewInstallation() -> bool: ...
    
    @staticmethod
    def setNewInstallation(b: bool) -> None: ...
    
    
    class FileExtension:
        MD_ACCOUNT_BOOK = 'MD_ACCOUNT_BOOK'
        MD_ARCHIVE = 'MD_ARCHIVE'
        MD_OLD_FILE = 'MD_OLD_FILE'
        MD_ROOT_FILE = 'MD_ROOT_FILE'
        MD_XML = 'MD_XML'
        QIF = 'QIF'
        XML = 'XML'
        
        def __init__(self): ...
        
        @staticmethod
        def fromFilename(s: str) -> str: ...
        
        @staticmethod
        def fromString(s: str) -> str: ...
        
        def matchesString(self, s: str) -> bool: ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class EditSecuritySubtypes:
    def __init__(self): ...
    
    @staticmethod
    def buildSubtypeEditor(c: com.moneydance.apps.md.view.gui.MoneydanceGUI, j: 'java.awt.Frame', securitySubtypeManager: 'SecuritySubtypeManager', c2: com.infinitekind.moneydance.model.SecurityType) -> com.moneydance.apps.md.view.gui.editlistdlg.EditStringListDialog: ...
    
    @staticmethod
    def processSubtypeEdits(c: com.infinitekind.moneydance.model.SecurityType, list: List[com.moneydance.apps.md.view.gui.editlistdlg.EditStringListResult], c2: com.infinitekind.moneydance.model.Account) -> List[str]: ...
    
    
class FeatureInvoker:
    def __init__(self, featureModule: 'FeatureModule', s: str, j: 'java.awt.Image', s2: str): ...
    
    def getIcon(self) -> 'java.awt.Image': ...
    
    def getModule(self) -> 'FeatureModule': ...
    
    def getText(self) -> str: ...
    
    def getURI(self) -> str: ...
    
    
class FeatureListener:
    def __init__(self): ...
    
    def featureListModified(self) -> None: ...
    
    
class FeatureModule:
    MONEYBOT_INVOKE_TARGET = u'moneybot'
    
    def __init__(self): ...
    
    def cleanup(self) -> None: ...
    
    def getBuild(self) -> int: ...
    
    def getDescription(self) -> str: ...
    
    def getDisplayName(self) -> str: ...
    
    def getIDStr(self) -> str: ...
    
    def getIconImage(self) -> 'java.awt.Image': ...
    
    def getName(self) -> str: ...
    
    def getSourceFile(self) -> 'java.io.File': ...
    
    def getVendor(self) -> str: ...
    
    def getVendorURL(self) -> str: ...
    
    def handleEvent(self, s: str) -> None: ...
    
    def init(self) -> None: ...
    
    def invoke(self, s: str) -> None: ...
    
    def isBundled(self) -> bool: ...
    
    def isVerified(self) -> bool: ...
    
    def toString(self) -> str: ...
    
    def unload(self) -> None: ...
    
    
    class ActionType:
        ACCOUNT_CONTEXT = 'account_menu'
        INITIALIZER = 'initializer'
        MENU = 'menu'
        METHOD = 'method'
        MONEYBOT = 'moneybot'
        OTHER = 'other'
        TXN_CONTEXT = 'txn_menu'
        
        def __init__(self): ...
        
        @staticmethod
        def fromString(s: str) -> str: ...
        
        def toString(self) -> str: ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class FeatureModuleContext:
    def __init__(self): ...
    
    def getBuild(self) -> int: ...
    
    def getCurrentAccountBook(self) -> com.infinitekind.moneydance.model.AccountBook: ...
    
    def getRootAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getVersion(self) -> str: ...
    
    def registerAccountEditor(self, featureModule: FeatureModule, i: int, c: com.moneydance.apps.md.extensionapi.AccountEditor) -> None: ...
    
    def registerFeature(self, featureModule: FeatureModule, s: str, j: 'java.awt.Image', s2: str) -> None: ...
    
    def registerHomePageView(self, featureModule: FeatureModule, c: com.moneydance.apps.md.view.HomePageView) -> None: ...
    
    def showURL(self, s: str) -> None: ...
    
    
class FullAccountList:
    def __init__(self, c: com.infinitekind.moneydance.model.AccountBook, accountFilter: AccountFilter, b: bool): ...
    
    def getAccountsIDsOfType(self, s: str) -> Set[str]: ...
    
    def getCount(self) -> int: ...
    
    def getFullAccountIDs(self) -> Set[str]: ...
    
    def getFullAccountList(self) -> List[com.infinitekind.moneydance.model.Account]: ...
    
    
class LicenseInfo:
    MDPLUS_LICENSE_PREFIX = u'MDP:'
    
    def __init__(self, main: 'Main'): ...
    
    def getKeyVersion(self) -> 'LicenseKeyVersion': ...
    
    def getLicenseKey(self) -> str: ...
    
    def getStatus(self) -> str: ...
    
    def isRegistered(self) -> bool: ...
    
    def isUpgradeable(self) -> bool: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    def setRegistrationKey(self, s: str) -> bool: ...
    
    def verifyWithServer(self, s: str) -> str: ...
    
    
    class LicenseStatus:
        REFUNDED = 'REFUNDED'
        REGISTERED = 'REGISTERED'
        UNREGISTERED = 'UNREGISTERED'
        UPGRADEABLE = 'UPGRADEABLE'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class LicenseKeyVersion('java.lang.Enum'):
    v2004 = 'v2004'
    v2008 = 'v2008'
    v2010 = 'v2010'
    v2011 = 'v2011'
    v2014 = 'v2014'
    v2015 = 'v2015'
    v2017 = 'v2017'
    v2019 = 'v2019'
    v2021 = 'v2021'
    v2022 = 'v2022'
    
    def __init__(self): ...
    
    def getKeyHash(self) -> List[int]: ...
    
    def getPriorUpgradeableVersion(self) -> 'LicenseKeyVersion': ...
    
    def getVersionID(self) -> int: ...
    
    @staticmethod
    def valueOf(s: str) -> 'LicenseKeyVersion': ...
    
    @staticmethod
    def values() -> List['LicenseKeyVersion']: ...
    
    def verifyKey(self, s: str, b: bool) -> bool: ...
    
    
class LocalStorageCipher:
    def __init__(self, j: 'javax.crypto.SecretKey', s: str): ...
    
    @staticmethod
    def encryptionKeyFromBytesAndPassword(list: List[int], list2: List[int], s: str) -> 'javax.crypto.SecretKey': ...
    
    @staticmethod
    def generateNewMainKey(s: str) -> 'javax.crypto.SecretKey': ...
    
    @staticmethod
    def keyFromPassword(list: List[int], s: str) -> 'javax.crypto.SecretKey': ...
    
    
    class MDCipherLevel:
        GOOD = 'GOOD'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class MDException(Exception):
    HTTPS_NOT_AVAILABLE = 1002
    INTERNAL_ERROR = 1000
    INVALID_MODULE_SIGNATURE = 1001
    INVALID_OFX_DATA = 1003
    SERVER_DID_NOT_ACK = u'server_did_not_ack'
    WRONG_DECRYPTION_PASSWORD = 1004
    
    def __init__(self, i: int): ...
    
    def getCode(self) -> int: ...
    
    def getDescription(self, j: 'java.util.ResourceBundle') -> str: ...
    
    def getMsgKey(self) -> str: ...
    
    def getOriginalError(self) -> 'java.lang.Throwable': ...
    
    
class MDPlus:
    def __init__(self): ...
    
    def getLicenseForBook(self, c: com.infinitekind.moneydance.model.AccountBook, b: bool) -> str: ...
    
    @staticmethod
    def singleton() -> 'MDPlus': ...
    
    
    class MDPlusLicense:
        def __init__(self): ...
        
        def deleteKeyPayload(self, s: str) -> None: ...
        
        def getAuthenticatedManageAccountsURL(self) -> str: ...
        
        def getAuthenticatedToken(self) -> str: ...
        
        def getCreatedDate(self) -> int: ...
        
        def getCustomerEmail(self) -> str: ...
        
        def getKeyID(self) -> str: ...
        
        def getOpenPlaidLinkURL(self) -> str: ...
        
        def getPendingCustomerEmail(self) -> str: ...
        
        def getPlaidRelinkURL(self, s: str) -> str: ...
        
        def getPubkey(self) -> 'java.security.PublicKey': ...
        
        def getRefreshDate(self) -> int: ...
        
        def getSignupStatusWithRefreshing(self) -> str: ...
        
        def getSignupStatusWithoutRefresh(self) -> str: ...
        
        def getStatusLastUpdated(self) -> int: ...
        
        def getSubscriptionStatusURL(self) -> str: ...
        
        def getUserID(self) -> str: ...
        
        def interruptPendingRegistration(self) -> None: ...
        
        def isActivated(self) -> bool: ...
        
        def isSubscriptionActive(self) -> bool: ...
        
        def refreshStatusIfNecessary(self) -> str: ...
        
        def refreshStatusNow(self) -> str: ...
        
        def registerWithEmail(self, s: str, s2: str) -> bool: ...
        
        def signBytes(self, list: List[int]) -> List[int]: ...
        
        
    class SignupStatus:
        ACTIVATED = 'ACTIVATED'
        CONFIRMED = 'CONFIRMED'
        EXPIRED = 'EXPIRED'
        NONE = 'NONE'
        PENDING = 'PENDING'
        SUBSCRIBED = 'SUBSCRIBED'
        UNKNOWN = 'UNKNOWN'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    class Status:
        def __init__(self): ...
        
        def getKeyPayloads(self) -> Dict[str,List[int]]: ...
        
        def getMessage(self) -> str: ...
        
        def getPlaidCountries(self) -> List[str]: ...
        
        def getPlaidProducts(self) -> List[str]: ...
        
        def getStatus(self) -> str: ...
        
        def getUserPayloads(self) -> Dict[str,List[int]]: ...
        
        def isActivated(self) -> bool: ...
        
        def isSubscriptionActive(self) -> bool: ...
        
        def wasSuccessful(self) -> bool: ...
        
        
    
class MDWorker:
    def __init__(self, mDWorkerManager: 'MDWorkerManager'): ...
    
    def doWork(self) -> None: ...
    
    def getProgress(self) -> float: ...
    
    def pleaseStop(self) -> None: ...
    
    def shouldStop(self) -> bool: ...
    
    def shouldStopUpdated(self) -> None: ...
    
    
class MDWorkerListener:
    def __init__(self): ...
    
    def workerFinished(self, mDWorker: MDWorker) -> None: ...
    
    def workerStarted(self, mDWorker: MDWorker) -> None: ...
    
    def workerUpdated(self, mDWorker: MDWorker) -> None: ...
    
    
class MDWorkerManager:
    def __init__(self): ...
    
    def getWorkerIterator(self) -> Iterator: ...
    
    def workerUpdated(self, mDWorker: MDWorker) -> None: ...
    
    
class StatusMonitor:
    def __init__(self): ...
    
    def isCanceled(self) -> bool: ...
    
    def setPercentComplete(self, f: float) -> None: ...
    
    def setStatus(self, s: str) -> None: ...
    
    
class Main(StatusMonitor, FeatureModuleContext, com.moneydance.security.SecretKeyCallback, 'com.moneydance.awt.JLinkListener'):
    BETA_FEATURES = False
    CURRENT_BUILD = 4084
    CURRENT_STATUS = u''
    CURRENT_VERSION = u'2022.3'
    DEBUG = False
    DESCRIPTIVE_NAME = u'Moneydance 2022.3 (4084)'
    EXEC_MODE_APP = 2
    EXEC_MODE_APPLET = 1
    FILE_EXTENSION = u'md'
    MINIMUM_EXTENSION_VERSION_FOR_MD2015 = 1000
    mainObj = 'com.moneydance.apps.md.controller.Main@3114a50a'
    
    def __init__(self): ...
    
    def addAppEventListener(self, appEventListener: AppEventListener) -> None: ...
    
    def addFeatureListener(self, featureListener: FeatureListener) -> None: ...
    
    def addModuleListener(self, moduleListener: 'ModuleListener') -> None: ...
    
    def addViewListener(self, viewListener: 'ViewListener') -> None: ...
    
    def archiveTxns(self, accountBookWrapper: AccountBookWrapper, accountBookWrapper2: AccountBookWrapper, i: int, b: bool, b2: bool, b3: bool) -> bool: ...
    
    def deleteAccountBook(self) -> bool: ...
    
    def exportAllAccountsIntoQIF(self, accountBookWrapper: AccountBookWrapper, j: 'java.io.File', c: com.infinitekind.moneydance.model.CurrencyType, c2: com.infinitekind.moneydance.model.TxnFilter) -> None: ...
    
    def exportAllAccountsIntoTD(self, accountBookWrapper: AccountBookWrapper, j: 'java.io.File', c: com.infinitekind.moneydance.model.TxnFilter) -> None: ...
    
    def exportFile(self, accountBookWrapper: AccountBookWrapper, j: 'java.io.File', i: int, c: com.infinitekind.moneydance.model.TxnFilter) -> bool: ...
    
    def fireAppEvent(self, s: str) -> None: ...
    
    def getBackgroundThread(self) -> BackgroundOpsThread: ...
    
    def getBuild(self) -> int: ...
    
    def getCurrentAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getCurrentAccountBook(self) -> com.infinitekind.moneydance.model.AccountBook: ...
    
    def getCurrentAccounts(self) -> AccountBookWrapper: ...
    
    def getExecutionMode(self) -> int: ...
    
    def getExternalAccountEditors(self) -> List[com.moneydance.apps.md.extensionapi.AccountEditor]: ...
    
    def getExternalFeatureModule(self, s: str, j: 'java.io.File', b: bool) -> FeatureModule: ...
    
    def getExternalViews(self) -> List[com.moneydance.apps.md.view.HomePageView]: ...
    
    def getFeatureInvokers(self) -> Iterator: ...
    
    def getFileForExternalModule(self, s: str) -> 'java.io.File': ...
    
    def getHttpsHelper(self) -> olb.HttpsHelper: ...
    
    def getInternalFeatureModule(self, s: str) -> FeatureModule: ...
    
    def getLicenseInfo(self) -> LicenseInfo: ...
    
    def getLoadedModules(self) -> List[FeatureModule]: ...
    
    def getLogFile(self) -> 'java.io.File': ...
    
    def getModuleForID(self, s: str) -> FeatureModule: ...
    
    def getPassphrase(self, s: str) -> str: ...
    
    def getPlatformHelper(self) -> 'platforms.PlatformHelper': ...
    
    def getPreferences(self) -> 'UserPreferences': ...
    
    def getPythonInterpreter(self) -> 'org.python.util.PythonInterpreter': ...
    
    def getResources(self) -> com.moneydance.apps.md.view.resources.Resources: ...
    
    def getRootAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getSourceInformation(self) -> AppSource: ...
    
    def getSuppressedExtensionIDs(self) -> List[str]: ...
    
    def getUI(self) -> com.moneydance.apps.md.view.MoneydanceUI: ...
    
    def getUnloadableExtensionIDs(self) -> List[str]: ...
    
    def getVersion(self) -> str: ...
    
    def getWorkerManager(self) -> MDWorkerManager: ...
    
    def importQIFIntoAccount(self, c: com.infinitekind.moneydance.model.AccountBook, j: 'java.io.File', i: int, i2: int, c2: com.infinitekind.moneydance.model.CurrencyType, c3: com.infinitekind.moneydance.model.Account, i3: int, b: bool) -> None: ...
    
    def importQIFIntoNewAccount(self, c: com.infinitekind.moneydance.model.AccountBook, j: 'java.io.File', i: int, i2: int, c2: com.infinitekind.moneydance.model.CurrencyType, i3: int, b: bool) -> None: ...
    
    def initializeApp(self) -> None: ...
    
    def initializePythonInterpreter(self, o: 'org.python.util.PythonInterpreter') -> None: ...
    
    def installModule(self, j: 'java.io.File', s: str, b: bool) -> None: ...
    
    def invokeFeatureModuleURI(self, s: str) -> None: ...
    
    def isCanceled(self) -> bool: ...
    
    def isInitialized(self) -> bool: ...
    
    def isLimited(self) -> bool: ...
    
    def isRegistered(self) -> bool: ...
    
    def isUpgradeable(self) -> bool: ...
    
    def linkActivated(self, o: object, j: 'java.awt.event.InputEvent') -> None: ...
    
    def loadExternalFeatureModule(self, s: str, j: 'java.io.File', b: bool) -> FeatureModule: ...
    
    def loadInstalledExternalFeatureModule(self, s: str) -> FeatureModule: ...
    
    def loadInternalFeatureModule(self, s: str) -> FeatureModule: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    def queueFile(self, s: str) -> None: ...
    
    def registerAccountEditor(self, featureModule: FeatureModule, i: int, c: com.moneydance.apps.md.extensionapi.AccountEditor) -> None: ...
    
    def registerFeature(self, featureModule: FeatureModule, s: str, j: 'java.awt.Image', s2: str) -> None: ...
    
    def registerHomePageView(self, featureModule: FeatureModule, c: com.moneydance.apps.md.view.HomePageView) -> None: ...
    
    def removeAppEventListener(self, appEventListener: AppEventListener) -> bool: ...
    
    def removeFeatureListener(self, featureListener: FeatureListener) -> None: ...
    
    def removeModuleListener(self, moduleListener: 'ModuleListener') -> None: ...
    
    def removeViewListener(self, viewListener: 'ViewListener') -> None: ...
    
    def resetPythonInterpreter(self, o: 'org.python.util.PythonInterpreter') -> None: ...
    
    def saveAccountBook(self, accountBookWrapper: AccountBookWrapper) -> bool: ...
    
    def saveCurrentAccount(self) -> bool: ...
    
    def savePreferences(self) -> None: ...
    
    def saveWorkSpace(self) -> None: ...
    
    def sendEventToExtensions(self, s: str) -> None: ...
    
    def setCurrentBook(self, accountBookWrapper: AccountBookWrapper) -> bool: ...
    
    def setInitialFile(self, j: 'java.io.File') -> None: ...
    
    def setPercentComplete(self, f: float) -> None: ...
    
    def setRegistrationKey(self, s: str) -> bool: ...
    
    def setStatus(self, s: str) -> None: ...
    
    def setVerifier(self, c: com.moneydance.security.SecretKeyVerifier) -> None: ...
    
    def showURL(self, s: str) -> None: ...
    
    def showWebsite(self, s: str) -> None: ...
    
    def shutdown(self) -> bool: ...
    
    def startApplication(self) -> None: ...
    
    def uninstallModule(self, featureModule: FeatureModule) -> None: ...
    
    def waitForUI(self) -> bool: ...
    
    
class ModuleListener:
    def __init__(self): ...
    
    def moduleListUpdated(self) -> None: ...
    
    
class ModuleLoader:
    DEFAULT_FEATURE_MODULE_EXTENSION = u'.mxt'
    FEATURE_MODULE_EXTENSIONS = "array(java.lang.String, [u'mxt', u'moneydanceplugin', u'moneydanceext'])"
    
    def __init__(self, main: Main): ...
    
    @staticmethod
    def getFeatureModuleMetaResource(s: str) -> str: ...
    
    @staticmethod
    def getMetadataStream(j: 'java.lang.ClassLoader', s: str) -> 'java.io.InputStream': ...
    
    @staticmethod
    def getSignatureResource(s: str) -> str: ...
    
    @staticmethod
    def getSignatureStream(j: 'java.lang.ClassLoader', s: str) -> 'java.io.InputStream': ...
    
    @staticmethod
    def guessModuleIDFromFile(j: 'java.io.File') -> str: ...
    
    
class ModuleMetaData:
    def __init__(self, c: com.infinitekind.util.StreamTable): ...
    
    def getBuild(self) -> int: ...
    
    def getDescription(self) -> str: ...
    
    def getMaximumSupportedBuild(self) -> int: ...
    
    def getMinimumSupportedBuild(self) -> int: ...
    
    def getModuleDownloadURL(self) -> str: ...
    
    def getModuleID(self) -> str: ...
    
    def getModuleName(self) -> str: ...
    
    def getSize(self) -> str: ...
    
    def getVendor(self) -> str: ...
    
    def getVendorURL(self) -> str: ...
    
    def isMacSandboxFriendly(self) -> bool: ...
    
    def toString(self) -> str: ...
    
    
class ModuleURLHandler('java.net.URLStreamHandler'):
    def __init__(self): ...
    
    
class ModuleUtil:
    def __init__(self): ...
    
    @staticmethod
    def getImage(s: str) -> 'java.awt.Image': ...
    
    
class OutdatedAppException(Exception):
    def __init__(self, s: str): ...
    
    def getExtensionID(self) -> str: ...
    
    
class OutdatedExtensionException(Exception):
    def __init__(self, s: str): ...
    
    def getExtensionID(self) -> str: ...
    
    
class PanelSettings:
    ACCOUNTS = 1
    CALENDAR = 3
    EXCHRATES = 4
    LEFT = 0
    REMINDERS = 2
    RIGHT = 1
    STOCKQUOTES = 5
    panelCodes = "array('i', [1, 2, 3, 4, 5])"
    panelColumns = "array('i', [0, 1, 1, 0, 1])"
    panelRows = "array('i', [1, 1, 2, 2, 3])"
    prefNames = "array(java.lang.String, [u'pnls_acc', u'pnls_rem', u'pnls_cal', u'pnls_exr', u'pnls_stk'])"
    
    def __init__(self, panelSettings: 'PanelSettings'): ...
    
    def getCode(self) -> int: ...
    
    def getColumn(self) -> int: ...
    
    def getPanelName(self) -> str: ...
    
    def getPreferenceName(self) -> str: ...
    
    def getRow(self) -> int: ...
    
    def makeSettings(self) -> str: ...
    
    def setCode(self, i: int) -> None: ...
    
    def setColumn(self, i: int) -> None: ...
    
    def setColumnRow(self, s: str) -> None: ...
    
    def setPanelName(self, s: str) -> None: ...
    
    def setPreferenceName(self, s: str) -> None: ...
    
    def setRow(self, i: int) -> None: ...
    
    def toFullString(self) -> str: ...
    
    def toString(self) -> str: ...
    
    
class PythonExtension(FeatureModule):
    MONEYBOT_INVOKE_TARGET = u'moneybot'
    
    def __init__(self, j: 'java.lang.ClassLoader', c: com.infinitekind.util.StreamTable, o: 'org.python.util.PythonInterpreter'): ...
    
    def getName(self) -> str: ...
    
    def handleEvent(self, s: str) -> None: ...
    
    def init(self) -> None: ...
    
    def installRuntimeExtension(self, main: Main, s: str, c: com.infinitekind.util.StreamTable, j: 'java.lang.ClassLoader', o: object) -> None: ...
    
    def invoke(self, s: str) -> None: ...
    
    def unload(self) -> None: ...
    
    
class SecuritySubtypeManager:
    def __init__(self, c: com.infinitekind.moneydance.model.AccountBook, userPreferences: 'UserPreferences', c2: com.moneydance.apps.md.view.resources.MDResourceProvider): ...
    
    def getSubTypeList(self, c: com.infinitekind.moneydance.model.SecurityType) -> List[str]: ...
    
    def save(self) -> None: ...
    
    def setSubTypeList(self, c: com.infinitekind.moneydance.model.SecurityType, list: List[str]) -> None: ...
    
    
class SnapshotImporter:
    def __init__(self, j: 'java.io.File', c: com.infinitekind.moneydance.model.CurrencyType, c2: com.infinitekind.util.CustomDateFormat, i: int): ...
    
    def detectFormat(self) -> int: ...
    
    def importData(self) -> int: ...
    
    def setColumnsFromHeader(self, s: str) -> bool: ...
    
    
class URLConstants:
    def __init__(self): ...
    
    
class URLUtil:
    MD_ACCOUNT = u'account'
    MD_BUDGETHOME = u'budgethome'
    MD_EXIT = u'exit'
    MD_EXTSN_PREFIX = u'fmodule'
    MD_HOME = u'gohome'
    MD_IMPORTFILE = u'importfile'
    MD_IMPORTPROMPT = u'importprompt'
    MD_NETSYNC = u'netsync'
    MD_REMINDERSHOME = u'remindershome'
    MD_SETPROGRESS = u'setprogress'
    MD_SETSTATUS = u'setstatus'
    MD_SHOWABOUT = u'showabout'
    MD_SHOWBUDGETS = u'showbudgets'
    MD_SHOWCATEGORIES = u'showcategories'
    MD_SHOWCOA = u'showcoa'
    MD_SHOWGRAPH = u'showgraph'
    MD_SHOWGRAPHS = u'showgraphs'
    MD_SHOWPREFS = u'showprefs'
    MD_SHOWREMINDERS = u'editreminders'
    MD_SHOWREPORT = u'showreport'
    MD_SHOWREPORTS = u'showreports'
    MD_SHOWSEARCH = u'showsearch'
    MD_SHOWTXN = u'showtxn'
    MD_SHOWUPCOMINGREMINDERS = u'showupcomingreminders'
    MD_SHOW_OBJECT = u'showobj'
    
    def __init__(self): ...
    
    @staticmethod
    def checkURLIsValid(s: str) -> 'java.net.URL': ...
    
    @staticmethod
    def encode(s: str) -> str: ...
    
    @staticmethod
    def getAccountURL(c: com.infinitekind.moneydance.model.Account) -> str: ...
    
    @staticmethod
    def getBoolean(d: dict, s: str, b: bool) -> bool: ...
    
    @staticmethod
    def getBudgetURL(s: str) -> str: ...
    
    @staticmethod
    def getDate(d: dict, s: str, j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def getInt(d: dict, s: str, i: int) -> int: ...
    
    @staticmethod
    def getMoneydanceURL(s: str) -> str: ...
    
    @staticmethod
    def getMoneydanceURLPrefix() -> str: ...
    
    @staticmethod
    def getURLStartIndex(s: str, s2: str) -> int: ...
    
    @staticmethod
    def parseNextItem(s: str) -> str: ...
    
    
class UserPreferences:
    AINT_TO_PROUD = u'gui.initwin'
    BACKUP_AUTOSAVE_INTERVAL = u'backup.autosave_interval'
    BACKUP_BACKUP_DAYS_INTERVAL = u'backup.backup_days_interval'
    BACKUP_BACKUP_TYPE = u'backup.backup_type'
    BACKUP_DESTROY_NUMBER = u'backup.destroy_number'
    BACKUP_LOCATION = u'backup.location'
    BACKUP_LOCATION_SELECTED = u'backup.location_selected'
    BACKUP_ONLY_AFTER_FIRST_OPEN = u'backup.only_once_daily'
    BACKUP_OPEN_LOCATION = u'backup.last_browsed'
    BACKUP_SAVE_LOCATION = u'backup.last_saved'
    BEEP_ON_TXN_CHANGE = u'beep_on_transaction_change'
    BILLPAY_COUNTRY = u'ofx.bp_country'
    CHECK_PRINTER_CONFIGS = u'print.profiles'
    CHECK_VERSION_AT_START = u'updater.check_version_at_startup'
    CLEAR_CONFIRMED_TXNS = u'net.clear_confirmed_txns'
    CODE_FONT_NAME = u'code_font'
    CONFIRM_TXN_CHANGES = u'confirm_transaction_changes'
    CURRENT_ACCOUNT_BOOK = u'current_accountbook'
    CURRENT_THEME = u'gui.current_theme'
    DATA_DIR = u'gen.data_dir'
    DATE_FORMAT = u'date_format'
    DECIMAL_CHAR = u'decimal_character'
    DEFAULT_CHECK_TYPE = u'print.default_check_type'
    DETAILS_VIEW_MODE = u'details_view_mode'
    DO_AUTOCOMMITS = u'do_autocommits'
    EXTERNAL_ACCT_BOOK_LIST = u'external_files'
    FISCAL_YEAR_START_MMDD = u'gen.fiscal_year_start_mmdd'
    GEN_CASE_SENSITIVE_AUTOCOMPLETE = u'gen.case_sensitive_ac'
    GEN_DONT_BOTHER_REGISTER = u'gen.dont_bother_register'
    GEN_FMODULE_LIST = u'gen.fmodules'
    GEN_HAS_ACCPT_LICENSE = u'gen.has_accpt_license'
    GEN_HAS_REGISTERED = u'gen.has_registered'
    GEN_HAS_SEEN_LIMIT_MSG = u'gen.has_seen_limit_msg'
    GEN_LAST_MOD_FILE_DIR = u'gen.last_ext_file_dir'
    GEN_RECENT_FILES = u'gen.recent_files'
    GEN_SEPARATE_TAX_DATE = u'gen.separate_tax_date'
    GRAPH_DIR = u'gen.graph_dir'
    GUI_ACCT_HEADER_BG = u'gui.acct_header_bg'
    GUI_ACCT_HEADER_FG = u'gui.acct_header_fg'
    GUI_ADDRBOOK_LOC = u'gui.addrbook_location'
    GUI_ADDRBOOK_SIZE = u'gui.addrbook_size'
    GUI_AUTO_INSERT_DEC = u'gui.quickdecimal'
    GUI_BALRPT_CURR = u'gui.bal_report_currency'
    GUI_BALRPT_EDATE = u'gui.bal_report_end_date'
    GUI_BALRPT_SHOWALL = u'gui.bal_report_showall'
    GUI_BASIC_TXN_COL_WIDTHS = u'gui.srch_txn_column_widths'
    GUI_BUDGETLISTWIN_LOC = u'gui.budget_list_location'
    GUI_BUDGETLISTWIN_SIZE = u'gui.budget_list_size'
    GUI_BUDGET_LOC = u'gui.budget_location'
    GUI_BUDGET_SIZE = u'gui.budget_size'
    GUI_CALORMDR_BG = u'gui.cal_overdue_rmdr_bg'
    GUI_CALPASTRMDR_BG = u'gui.cal_overdue_rmdr_bg'
    GUI_CALRMDR_BG = u'gui.cal_rmdr_bg'
    GUI_CAT_WIN_ACTIVE = u'gui.category_window_isopen'
    GUI_CAT_WIN_PREFIX = u'gui.cat_window_'
    GUI_CCTXN_COL_WIDTHS = u'gui.cctxn_column_widths'
    GUI_COA_SHOW_ALL = u'gui.coa_show_all_accounts'
    GUI_COA_WIN_ACTIVE = u'gui.coa_window_isopen'
    GUI_COA_WIN_PREFIX = u'gui.coa_window_'
    GUI_CURRHISTWIN_LOC = u'gui.currency_hist_location'
    GUI_CURRHISTWIN_SIZE = u'gui.currency_hist_size'
    GUI_DASH_BG1 = u'gui.dash_bg1'
    GUI_DASH_BG2 = u'gui.dash_bg2'
    GUI_DASH_FG = u'gui.dash_fg'
    GUI_DASH_ITEM = u'gui.dashboard.item'
    GUI_EXPENSERPT_EDATE = u'gui.expense_report_end_date'
    GUI_EXPENSERPT_SDATE = u'gui.expense_report_start_date'
    GUI_EXPVATED_LOC = u'gui.expvated_location'
    GUI_EXPVATED_SIZE = u'gui.expvated_size'
    GUI_FONT_DIFF = u'gui.font_increment'
    GUI_GRAPHREPSELWIN_LOC = u'gui.graph_rep_sel_location'
    GUI_GRAPHREPSELWIN_SIZE = u'gui.graph_rep_sel_size'
    GUI_GRAPH_3D = u'gui.graph_3d'
    GUI_GRAPH_DETAILEDKEY = u'gui.graph_detailed_key'
    GUI_GRAPH_DIMENSION = u'gui.graph_dimension'
    GUI_GRAPH_EDATE = u'gui.graph_end_date'
    GUI_GRAPH_GROUP = u'gui.graph_group'
    GUI_GRAPH_LOC = u'gui.graph_location'
    GUI_GRAPH_SDATE = u'gui.graph_start_date'
    GUI_GRAPH_SEL_ACCT = u'gui.graph_selected_acct'
    GUI_GRAPH_SIZE = u'gui.graph_size'
    GUI_GRAPH_STYLE = u'gui.graph_style'
    GUI_GRAPH_TOP_ACCTS_SEL = u'gui.graph_top_accts_sel'
    GUI_GRAPH_TOP_INCOME_SEL = u'gui.graph_top_income_num'
    GUI_GRAPH_TYPE = u'gui.graph_type'
    GUI_HDR_BG = u'gui.header_bg'
    GUI_HDR_FG = u'gui.header_fg'
    GUI_HEAVYLOTPAN_LOC = u'gui.heavy_lot_location'
    GUI_HEAVYLOTPAN_SIZE = u'gui.heavy_lot_size'
    GUI_HOMEPGALT_BG = u'gui.home_alt_bg'
    GUI_HOMEPG_BG = u'gui.home_bg'
    GUI_HOMEPG_FG = u'gui.home_fg'
    GUI_HOME_ASSET_BAL = u'gui.home.asset_bal_type'
    GUI_HOME_ASSET_EXP = u'gui.home.asset_expanded'
    GUI_HOME_BANK_BAL = u'gui.home.bank_bal_type'
    GUI_HOME_BANK_EXP = u'gui.home.bank_expanded'
    GUI_HOME_CC_BAL = u'gui.home.cc_bal_type'
    GUI_HOME_CC_EXP = u'gui.home.cc_expanded'
    GUI_HOME_INVERT_RATES = u'gui.home.invert_rates'
    GUI_HOME_INVST_BAL = u'gui.home.invst_bal_type'
    GUI_HOME_INVST_EXP = u'gui.home.invst_expanded'
    GUI_HOME_LIABILITY_BAL = u'gui.home.liability_bal_type'
    GUI_HOME_LIABILITY_EXP = u'gui.home.liability_expanded'
    GUI_HOME_LOAN_BAL = u'gui.home.loan_bal_type'
    GUI_HOME_LOAN_EXP = u'gui.home.loan_expanded'
    GUI_IMPORT_CURR = u'gui.import_curr_id'
    GUI_IMPORT_DEC_IDX = u'gui.import_dec_idx'
    GUI_IMPORT_DT_FMT_IDX = u'gui.import_dt_fmt_idx'
    GUI_INVST_TXN_COL_WIDTHS = u'gui.invst_txn_column_widths'
    GUI_INVST_TXN_REC_COL_WIDTHS = u'gui.reconciler_invst_column_widths'
    GUI_LOANCALC_LOC = u'gui.loancalc_location'
    GUI_LOANCALC_SIZE = u'gui.loancalc_size'
    GUI_LOAN_TXN_COL_WIDTHS = u'gui.loan_txn_column_widths'
    GUI_LOC_PREFIX = u'gui.winloc-'
    GUI_LOOK_AND_FEEL = u'look_and_feel'
    GUI_LOOK_AND_FEEL_CLASS = u'look_and_feel_class'
    GUI_MEMORIZEGRAPHREPWIN_LOC = u'gui.mem_graph_rep_location'
    GUI_MEMORIZEGRAPHREPWIN_SIZE = u'gui.mem_graph_rep_size'
    GUI_NEGATIVE_BAL_FG = u'gui.negative_bal_fg'
    GUI_NEW_TRANSACTION_ON_RECORD = u'gui.new_txn_on_record'
    GUI_OFX_WIN_ACTIVE = u'gui.ofx_window_isopen'
    GUI_OFX_WIN_H = u'gui.ofx_window_h'
    GUI_OFX_WIN_W = u'gui.ofx_window_w'
    GUI_OFX_WIN_X = u'gui.ofx_window_x'
    GUI_OFX_WIN_Y = u'gui.ofx_window_y'
    GUI_ONEGRAPHREPWIN_LOC = u'gui.one_graph_rep_location'
    GUI_ONEGRAPHREPWIN_SIZE = u'gui.one_graph_rep_size'
    GUI_POSITIVE_BAL_FG = u'gui.positive_bal_fg'
    GUI_PRERECONCILE_LOC = u'gui.prereconcile_location'
    GUI_PRERECONCILE_SIZE = u'gui.prereconcile_size'
    GUI_QUICK_GRAPH_TYPE = u'gui.quick_graph_type'
    GUI_RECONCILE_ASOF = u'gui.reconcile_asof'
    GUI_RECONCILE_RECURSE = u'gui.recursive_reconcile'
    GUI_REC_CREDIT_SORT_ASCENDING = u'gui.rec_credit_sort_ascend'
    GUI_REC_CREDIT_SORT_ORDER = u'gui.rec_credit_sort_order'
    GUI_REC_DEBIT_SORT_ASCENDING = u'gui.rec_debit_sort_ascend'
    GUI_REC_DEBIT_SORT_ORDER = u'gui.rec_debit_sort_order'
    GUI_REG_WIN_H = u'gui.reg_win_h'
    GUI_REG_WIN_W = u'gui.reg_win_w'
    GUI_REG_WIN_X = u'gui.reg_win_x'
    GUI_REG_WIN_Y = u'gui.reg_win_y'
    GUI_REMINDERWIN_LOC = u'gui.reminder_win_loc'
    GUI_REMINDERWIN_SIZE = u'gui.reminder_win_size'
    GUI_REPORT_LOC = u'gui.report_location'
    GUI_REPORT_SIZE = u'gui.report_size'
    GUI_REPORT_TYPE = u'gui.report_type'
    GUI_SEC_SUBTYPE_BOND = u'gui.secSubType_bond'
    GUI_SEC_SUBTYPE_CD = u'gui.secSubType_cd'
    GUI_SEC_SUBTYPE_MUTUAL = u'gui.secSubType_mutual'
    GUI_SEC_SUBTYPE_OPTION = u'gui.secSubType_option'
    GUI_SEC_SUBTYPE_OTHER = u'gui.secSubType_other'
    GUI_SEC_SUBTYPE_STOCK = u'gui.secSubType_stock'
    GUI_SEC_TXN_COL_WIDTHS = u'gui.security_txn_column_widths'
    GUI_SEEK_TXN_ON_RECORD = u'gui.seek_txn_on_record'
    GUI_SHOW_IE_IN_POPUP = u'gui.show_all_accts_in_popup'
    GUI_SIZE_PREFIX = u'gui.winsize-'
    GUI_SORT_ASCENDING = u'gui.transaction_sort_ascend'
    GUI_SORT_ORDER = u'gui.transaction_sort_order'
    GUI_SOURCE_LIST_VISIBLE = u'gui.source_list_visible'
    GUI_SOURCE_LIST_WIDTH = u'gui.source_list_width'
    GUI_TICKER_LOC = u'gui.ticker_loc'
    GUI_TWO_LINE_TXNS = u'gui.two_line_transactions'
    GUI_TXNRPT_EDATE = u'gui.txn_report_end_date'
    GUI_TXNRPT_LOC = u'gui.txn_report_location'
    GUI_TXNRPT_SDATE = u'gui.txn_report_start_date'
    GUI_TXNRPT_SEL_ACCT = u'gui.txn_report_account'
    GUI_TXNRPT_SIZE = u'gui.txn_report_size'
    GUI_TXNRPT_SUBT = u'gui.txn_report_subtotal_by'
    GUI_TXNXML_LOC = u'gui.txn_report_location'
    GUI_TXNXML_SIZE = u'gui.txn_report_size'
    GUI_TXN_COL_WIDTHS = u'gui.txn_column_widths'
    GUI_TXN_EDIT_BG = u'gui.txn_edit_bg'
    GUI_TXN_LIST_BG_SEL = u'gui.txn_list_bgsel'
    GUI_TXN_LIST_C1 = u'gui.txn_list_color1'
    GUI_TXN_LIST_C2 = u'gui.txn_list_color2'
    GUI_TXN_LIST_FG_SEL = u'gui.txn_list_fgsel'
    GUI_TXN_LIST_FUT = u'gui.txn_list_color_fut'
    GUI_TXN_LIST_FUT_2 = u'gui.txn_list_color_fut_2'
    GUI_TXN_REC_COL_WIDTHS = u'gui.reconciler_column_widths'
    GUI_UPCOMINGWIN_LOC = u'gui.upcoming_location'
    GUI_UPCOMINGWIN_SIZE = u'gui.upcoming_size'
    GUI_VATTXNS_LOC = u'gui.vattxns_location'
    GUI_VATTXNS_SIZE = u'gui.vattxns_size'
    GUI_VIEW_CFGRD = u'gui.home.configured'
    GUI_VIEW_LEFT = u'gui.home.lefties'
    GUI_VIEW_RIGHT = u'gui.home.righties'
    GUI_VIEW_UNUSED = u'gui.home.unused'
    GUI_WINDOW_IS_MAX = u'gui.is_maximized-'
    GUI_WINDOW_LOC = u'gui.screen_location'
    GUI_WINDOW_SIZE = u'gui.screen_size'
    HIGH_CONTRAST = u'high_contrast'
    HOME_PAGE_MANAGER = u'gui.home_page_manager'
    IMPORT_DIR = u'gen.import_dir'
    IMPORT_DT_FMT_IDX = u'gen.import_dt_fmt_idx'
    LAST_APPROVED_EXT_VERSION = u'confirmedext'
    LAST_USED_BUDGET_PERIOD = u'budget.last_used_period'
    LOCALE_COUNTRY = u'locale.country'
    LOCALE_LANGUAGE = u'locale.language'
    MAIN_FONT_NAME = u'main_font'
    MONO_FONT_NAME = u'mono_font'
    NET_AUTH_PROXY = u'net.auth_proxy'
    NET_AUTO_SYNC = u'net.auto_download'
    NET_DEFAULT_BROWSER = u'net.default_browser'
    NET_PROXY_HOST = u'net.proxy_host'
    NET_PROXY_PASS = u'net.proxy_pass'
    NET_PROXY_PORT = u'net.proxy_port'
    NET_PROXY_USER = u'net.proxy_user'
    NET_USE_PROXY = u'net.use_proxy'
    OFX_APP_ID = u'ofx.app_id'
    OFX_APP_VERSION = u'ofx.app_version'
    OFX_OBSERVE_BILLPAY_WINDOW = u'ofx.observe_bp_window'
    OLB_USE_BANK_DATES = u'olb.prefer_bank_dates'
    PREFER_AMT_SIGN_TO_TXN_TYPE = u'prefer_amt_sign_to_txn_type'
    PREPROCESS_DOWNLOADED_TXNS = u'gen.preprocess_dwnlds'
    PREPROCESS_DOWNLOADED_TXNS_DEFAULT = False
    PRINT_ADDRLOC_X = u'print.addrloc.x'
    PRINT_ADDRLOC_Y = u'print.addrloc.y'
    PRINT_AMOUNTNUMLOC_X = u'print.amountnumloc.x'
    PRINT_AMOUNTNUMLOC_Y = u'print.amountnumloc.y'
    PRINT_AMOUNTTEXTLOC_X = u'print.amounttextloc.x'
    PRINT_AMOUNTTEXTLOC_Y = u'print.amounttextloc.y'
    PRINT_API = u'print.api'
    PRINT_BOTH_VOUCHERS = u'print.both_vouchers'
    PRINT_BOTTOM_MARGIN = u'print.bottom-margin'
    PRINT_CHECKS_PER_PAGE = u'print.checks_per_page'
    PRINT_CHECK_TYPE = u'print.check_type'
    PRINT_CONFIG_NAME = u'print.config_name'
    PRINT_DATELOC_X = u'print.dateloc.x'
    PRINT_DATELOC_Y = u'print.dateloc.y'
    PRINT_FONT_NAME = u'print.font_name'
    PRINT_FONT_SIZE = u'print.font_size'
    PRINT_LAST_SELECTED_CHKTYPE = u'print.last_check_type'
    PRINT_LEFT_MARGIN = u'print.left-margin'
    PRINT_MEMOLOC_X = u'print.memoloc.x'
    PRINT_MEMOLOC_Y = u'print.memoloc.y'
    PRINT_PAYEELOC_X = u'print.payeeloc.x'
    PRINT_PAYEELOC_Y = u'print.payeeloc.y'
    PRINT_RIGHT_MARGIN = u'print.right-margin'
    PRINT_SHOW_ADDRESS = u'print.show_address'
    PRINT_SHOW_MEMO = u'print.show_memo'
    PRINT_STUB_ACCT_X = u'print.stub_acct_x'
    PRINT_STUB_ACCT_Y = u'print.stub_acct_y'
    PRINT_STUB_AMT_X = u'print.stub_amt_x'
    PRINT_STUB_AMT_Y = u'print.stub_amt_y'
    PRINT_STUB_CAT_X = u'print.stub_cat_x'
    PRINT_STUB_CAT_Y = u'print.stub_cat_y'
    PRINT_STUB_DATE_X = u'print.stub_date_x'
    PRINT_STUB_DATE_Y = u'print.stub_date_y'
    PRINT_STUB_MEMO_X = u'print.stub_memo_x'
    PRINT_STUB_MEMO_Y = u'print.stub_memo_y'
    PRINT_STUB_PAYEE_X = u'print.stub_payee_x'
    PRINT_STUB_PAYEE_Y = u'print.stub_payee_y'
    PRINT_STUB_SIZE = u'print.stub_size'
    PRINT_TOP_MARGIN = u'print.top-margin'
    PRINT_VOUCHERACCOUNT_X = u'print.voucher_account.x'
    PRINT_VOUCHERACCOUNT_Y = u'print.voucher_account.y'
    PRINT_VOUCHERAMOUNT1NUM_X = u'print.voucher_amount1_num.x'
    PRINT_VOUCHERAMOUNT1NUM_Y = u'print.voucher_amount1_num.y'
    PRINT_VOUCHERAMOUNT2NUM_X = u'print.voucher_amount2_num.x'
    PRINT_VOUCHERAMOUNT2NUM_Y = u'print.voucher_amount2_num.y'
    PRINT_VOUCHERCATEGORY_X = u'print.voucher_category.x'
    PRINT_VOUCHERCATEGORY_Y = u'print.voucher_category.y'
    PRINT_VOUCHERDATELOC_X = u'print.voucher_date_loc.x'
    PRINT_VOUCHERDATELOC_Y = u'print.voucher_date_loc.y'
    PRINT_VOUCHERMEMO_X = u'print.voucher_memo.x'
    PRINT_VOUCHERMEMO_Y = u'print.voucher_memo.y'
    PRINT_VOUCHERPAYEELOC_X = u'print.voucher_payee_loc.x'
    PRINT_VOUCHERPAYEELOC_Y = u'print.voucher_payee_loc.y'
    PRINT_VOUCHER_P_A_X = u'print.voucher_payee_address_loc.x'
    PRINT_VOUCHER_P_A_Y = u'print.voucher_payee_address_loc.y'
    PYTHON_DEFAULT_FILE = u'gen.python_default_file'
    PYTHON_DIR = u'gen.python_dir'
    REG_ADDRESS1 = u'reg.address1'
    REG_ADDRESS2 = u'reg.address2'
    REG_CITY = u'reg.city'
    REG_CONTACTOK = u'reg.contactok'
    REG_COUNTRY = u'reg.country'
    REG_EMAIL = u'reg.email'
    REG_NAME = u'reg.name'
    REG_PHONE = u'reg.phone'
    REG_STATE = u'reg.state'
    REG_ZIP = u'reg.zip'
    REPORT_DIR = u'gen.report_dir'
    RESTORE_DESKTOP_AT_START = u'restore_desktop_on_startup'
    SAVE_AUTOMATICALLY = u'save_periodically'
    SEEK_RECORDED_TXNS = u'gui.register_follows_txns'
    SHOW_FULL_ACCT_PATH = u'show_full_account_path'
    SIDEBAR_BALANCE_TYPE = u'sidebar_bal_type'
    SPLASH_DELAY = u'splash_delay'
    SPLIT_COL_WIDTHS = u'gui.split_column_widths'
    STARTUP_ACTION = u'startup_action'
    SUPPRESS_NOTIFICATIONS_UP_TO_BUILD = u'updater.suppress_until_after'
    TIME_FORMAT = u'time_format'
    TXN_MATCH_NUM_DAY_THRESHOLD = u'net.downloaded_txn_date_window'
    USE_VAT = u'gen.use_vat'
    VERSIONS_TO_TRACK = u'updater.version_to_track'
    
    def __init__(self, j: 'java.io.File'): ...
    
    def addListener(self, preferencesListener: PreferencesListener) -> None: ...
    
    def firePreferencesUpdated(self) -> None: ...
    
    def getAvailableLocales(self) -> List['java.util.Locale']: ...
    
    def getBoolSetting(self, s: str, b: bool) -> bool: ...
    
    def getCheckBoolSetting(self, i: int, s: str, b: bool) -> bool: ...
    
    def getCheckIntSetting(self, i: int, s: str, i2: int) -> int: ...
    
    def getCheckProfileCount(self) -> int: ...
    
    def getCheckSetting(self, i: int, s: str, s2: str) -> str: ...
    
    def getDecimalChar(self) -> int: ...
    
    def getDoubleSetting(self, s: str, f: float) -> float: ...
    
    def getExportCharset(self) -> 'java.nio.charset.Charset': ...
    
    @staticmethod
    def getInstance() -> 'UserPreferences': ...
    
    def getIntSetting(self, s: str, i: int) -> int: ...
    
    def getLocale(self) -> 'java.util.Locale': ...
    
    def getLongDateFormatter(self) -> com.infinitekind.util.CustomDateFormat: ...
    
    def getLongSetting(self, s: str, i: int) -> int: ...
    
    def getResources(self) -> com.moneydance.apps.md.view.resources.Resources: ...
    
    def getSetting(self, s: str) -> str: ...
    
    def getShortDateFormat(self) -> str: ...
    
    def getShortDateFormatter(self) -> com.infinitekind.util.CustomDateFormat: ...
    
    def getSideBarBalanceType(self) -> BalanceType: ...
    
    def getSizeSetting(self, s: str) -> 'java.awt.Dimension': ...
    
    def getTableSetting(self, s: str, c: com.infinitekind.util.StreamTable) -> com.infinitekind.util.StreamTable: ...
    
    def getTimeFormat(self) -> str: ...
    
    def getTimeFormatter(self) -> 'java.text.DateFormat': ...
    
    def getVectorSetting(self, s: str, c: com.infinitekind.util.StreamVector) -> com.infinitekind.util.StreamVector: ...
    
    def getXYSetting(self, s: str, i: int, i2: int) -> 'java.awt.Point': ...
    
    def removeListener(self, preferencesListener: PreferencesListener) -> None: ...
    
    def setCheckSetting(self, i: int, s: str, i2: int) -> None: ...
    
    def setLocale(self, j: 'java.util.Locale') -> None: ...
    
    def setSetting(self, s: str, i: int) -> None: ...
    
    def setShortDateFormat(self, s: str) -> str: ...
    
    def setSideBarBalanceType(self, balanceType: BalanceType) -> None: ...
    
    def setSizeSetting(self, s: str, j: 'java.awt.Dimension') -> None: ...
    
    def setTimeFormat(self, s: str) -> None: ...
    
    def setXYSetting(self, s: str, j: 'java.awt.Point') -> None: ...
    
    
class Util:
    def __init__(self): ...
    
    @staticmethod
    def calculateDaysBetween(i: int, i2: int) -> int: ...
    
    @staticmethod
    def calculateDaysInMonth(i: int) -> int: ...
    
    @staticmethod
    def calculateDaysInYear(i: int) -> int: ...
    
    @staticmethod
    def convertCalToInt(j: 'java.util.Calendar') -> int: ...
    
    @staticmethod
    def convertDateToInt(j: 'java.util.Date') -> int: ...
    
    @staticmethod
    def convertIntDateToLong(i: int) -> 'java.util.Date': ...
    
    @staticmethod
    def convertLongDateToInt(i: int) -> int: ...
    
    @staticmethod
    def copyFile(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def dateIsAfterCurrentMonth(j: 'java.util.Date') -> bool: ...
    
    @staticmethod
    def decrementDate(i: int) -> int: ...
    
    @staticmethod
    def decrementMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def decrementYear(i: int) -> int: ...
    
    @staticmethod
    def firstDayInFiscalYear(i: int) -> int: ...
    
    @staticmethod
    def firstDayInMonth(i: int) -> int: ...
    
    @staticmethod
    def firstDayInQuarter(i: int) -> int: ...
    
    @staticmethod
    def firstDayInWeek(i: int) -> int: ...
    
    @staticmethod
    def firstDayInYear(i: int) -> int: ...
    
    @staticmethod
    def firstMinuteInDay(i: int) -> int: ...
    
    @staticmethod
    def getAdjustedRate(i: int, i2: int) -> float: ...
    
    @staticmethod
    def getDate(i: int, i2: int, i3: int) -> int: ...
    
    @staticmethod
    def getStrippedDate() -> int: ...
    
    @staticmethod
    def getStrippedDateInt() -> int: ...
    
    @staticmethod
    def getStrippedDateObj() -> 'java.util.Date': ...
    
    @staticmethod
    def incrementDate(i: int) -> int: ...
    
    @staticmethod
    def incrementMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def incrementYear(i: int) -> int: ...
    
    @staticmethod
    def isSameLocale(j: 'java.util.Locale', j2: 'java.util.Locale') -> bool: ...
    
    @staticmethod
    def lastDayInMonth(i: int) -> int: ...
    
    @staticmethod
    def lastDayInQuarter(i: int) -> int: ...
    
    @staticmethod
    def lastDayInWeek(i: int) -> int: ...
    
    @staticmethod
    def lastDayInYear(i: int) -> int: ...
    
    @staticmethod
    def lastMinuteInDay(i: int) -> int: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    @staticmethod
    def minmax(i: int, i2: int, i3: int) -> int: ...
    
    @staticmethod
    def monthsInPeriod(i: int, i2: int) -> float: ...
    
    @staticmethod
    def renameAtomicallyWithNIO(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def safeRate(f: float) -> float: ...
    
    @staticmethod
    def setCalendarDate(j: 'java.util.Calendar', i: int) -> None: ...
    
    @staticmethod
    def setToBeginningOfMonth(j: 'java.util.Calendar') -> None: ...
    
    @staticmethod
    def setToEndOfMonth(j: 'java.util.Calendar') -> None: ...
    
    @staticmethod
    def sortVector(l: list, s: str) -> None: ...
    
    @staticmethod
    def stripTimeFromCal(j: 'java.util.Calendar') -> None: ...
    
    @staticmethod
    def stripTimeFromDate(i: int) -> int: ...
    
    @staticmethod
    def yearsInPeriod(i: int, i2: int) -> float: ...
    
    
    class Comparator:
        def __init__(self): ...
        
        
    
class ViewListener:
    def __init__(self): ...
    
    def viewListModified(self) -> None: ...
    
    
