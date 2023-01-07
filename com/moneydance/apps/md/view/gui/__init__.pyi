from typing import Callable, Dict, Iterable, List, Set, TypeVar
import bot
import com.infinitekind.moneydance.model
import com.infinitekind.moneydance.online
import com.infinitekind.tiksync
import com.infinitekind.util
import com.moneydance.apps.md.controller
import com.moneydance.apps.md.controller.fileimport
import com.moneydance.apps.md.controller.olb
import com.moneydance.apps.md.controller.sync
import com.moneydance.apps.md.view
import com.moneydance.apps.md.view.resources
import com.moneydance.security
import com.moneydance.util

T = TypeVar("T")


class SecondaryWindow(com.moneydance.apps.md.controller.PreferencesListener):
    def __init__(self): ...
    
    def getUsesDataFile(self) -> bool: ...
    
    def getWindow(self) -> 'java.awt.Window': ...
    
    def getWindowName(self) -> str: ...
    
    def goAway(self) -> bool: ...
    
    def goingAway(self) -> bool: ...
    
    
class SecondaryDialog(SecondaryWindow, 'javax.swing.JDialog'):
    pass
    
class AboutWindow(SecondaryDialog):
    pass
    
class AbstractTxnRenderer('java.awt.Component', 'javax.swing.ListCellRenderer'):
    pass
    
class AccountBookSaveDialog('javax.swing.JDialog', 'java.awt.event.ActionListener', 'java.beans.PropertyChangeListener'):
    pass
    
class AccountChoice('javax.swing.JComboBox', 'java.awt.event.ItemListener'):
    pass
    
class DisposablePanel('javax.swing.JPanel'):
    pass
    
class AccountDetailPanel(DisposablePanel, com.moneydance.apps.md.controller.PreferencesListener):
    pass
    
class AccountDetailWindow:
    def __init__(self): ...
    
    
class AccountInfoListener:
    def __init__(self): ...
    
    def accountInfoUpdated(self) -> None: ...
    
    
class AccountInfoPanel('javax.swing.JPanel'):
    pass
    
class OKButtonListener:
    def __init__(self): ...
    
    def buttonPressed(self, i: int) -> None: ...
    
    
class AccountInfoWindow(SecondaryDialog, OKButtonListener):
    pass
    
class AccountKeySelectionManager(str):
    def __init__(self): ...
    
    def selectionForKey(self, i: int, j: 'javax.swing.ComboBoxModel') -> int: ...
    
    def setUseBaseAccountName(self, b: bool) -> None: ...
    
    
class AccountListModel('javax.swing.AbstractListModel', 'javax.swing.ComboBoxModel', com.infinitekind.moneydance.model.AccountListener, 'java.awt.ItemSelectable', Callable):
    pass
    
class InterfacePanel:
    def __init__(self): ...
    
    def getSearchField(self) -> 'javax.swing.JTextField': ...
    
    def getSelectedAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getVisiblePanel(self) -> DisposablePanel: ...
    
    def goingAway(self) -> bool: ...
    
    def goneAway(self) -> None: ...
    
    def selectAccount(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def showEmbeddedBudget(self, s: str) -> None: ...
    
    def showEmbeddedReminders(self) -> None: ...
    
    def showEmbeddedReport(self, c: com.infinitekind.moneydance.model.ReportSpec) -> None: ...
    
    
class AccountPanel(InterfacePanel, 'javax.swing.JPanel', com.infinitekind.moneydance.model.AccountListener, 'java.awt.event.ActionListener', com.moneydance.apps.md.controller.PreferencesListener, Callable):
    pass
    
class RegTxnListModel('javax.swing.ListModel', Iterable):
    pass
    
class TxnListModel(RegTxnListModel, 'javax.swing.AbstractListModel', com.infinitekind.moneydance.model.TransactionListener, Iterable):
    pass
    
class AccountRegTxnListModel(TxnListModel, com.infinitekind.moneydance.model.AccountListener):
    pass
    
class AccountSelectionListener:
    def __init__(self): ...
    
    def accountSelected(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def createAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def deleteAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def editAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def graphAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def reportOnAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    
class AccountTreeCellRenderer('javax.swing.tree.DefaultTreeCellRenderer', 'javax.swing.ListCellRenderer', 'javax.swing.table.TableCellRenderer'):
    pass
    
class AccountTreeModel('javax.swing.tree.TreeModel', 'com.moneydance.awt.treetable.TreeTableModel', com.infinitekind.moneydance.model.AccountListener, com.moneydance.apps.md.controller.PreferencesListener):
    pass
    
class AddressBookImagePanel('com.moneydance.awt.ImagePanel', 'java.awt.event.ActionListener', 'java.awt.event.MouseListener'):
    pass
    
class AddressSelector('javax.swing.JPanel', 'java.awt.event.MouseListener', 'java.awt.event.ActionListener'):
    pass
    
class AlertController:
    def __init__(self): ...
    
    def addAlert(self, s: str, s2: str, j: 'javax.swing.Action') -> None: ...
    
    def addAlertListener(self, s: str) -> None: ...
    
    def removeAlert(self, s: str) -> None: ...
    
    def removeAlertListener(self, s: str) -> None: ...
    
    
    class AlertInfo:
        def __init__(self, s: str, s2: str, s3: str, s4: str, j: 'javax.swing.Action'): ...
        
        def getAlertDescription(self) -> str: ...
        
        def getAlertHandler(self) -> 'javax.swing.Action': ...
        
        def getAlertID(self) -> str: ...
        
        def getAlertTitle(self) -> str: ...
        
        def getAlertType(self) -> str: ...
        
        
    class AlertListener:
        def __init__(self): ...
        
        def alertsChanged(self, alertController: 'AlertController', list: List[str], list2: List[str], list3: List[str]) -> None: ...
        
        
    class AlertType:
        information = 'information'
        mdplus_relink_needed = 'mdplus_relink_needed'
        other = 'other'
        problem = 'problem'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class ArchiveWindow(SecondaryDialog, OKButtonListener):
    pass
    
class AssetAccountInfoPanel(AccountInfoPanel):
    pass
    
class AttachmentHolder:
    def __init__(self): ...
    
    def attachmentPressed(self) -> None: ...
    
    def deleteAttachment(self, c: com.infinitekind.moneydance.model.AbstractTxn, s: str) -> None: ...
    
    
class AttachmentsPanel('javax.swing.JPanel'):
    pass
    
class AutoCompletable:
    def __init__(self): ...
    
    def findAutoCompletions(self, j: 'javax.swing.text.JTextComponent', s: str) -> List[object]: ...
    
    def getTextForObject(self, j: 'javax.swing.text.JTextComponent', o: object) -> str: ...
    
    
class AutoCompletion('javax.swing.event.DocumentListener'):
    def __init__(self, autoCompletable: AutoCompletable, j: 'javax.swing.text.JTextComponent'): ...
    
    def changedUpdate(self, j: 'javax.swing.event.DocumentEvent') -> None: ...
    
    def completionWasSuccessful(self) -> bool: ...
    
    def getMatch(self) -> object: ...
    
    def insertUpdate(self, j: 'javax.swing.event.DocumentEvent') -> None: ...
    
    def removeUpdate(self, j: 'javax.swing.event.DocumentEvent') -> None: ...
    
    def setTokenDelimiter(self, i: int) -> None: ...
    
    
class BackgroundImagePanel('javax.swing.JPanel'):
    pass
    
class BankAccountInfoPanel(AccountInfoPanel, 'java.awt.event.ItemListener'):
    pass
    
class BankInvestPanel(AccountDetailPanel):
    pass
    
class BasicReminderInfoWindow(SecondaryDialog, OKButtonListener):
    pass
    
class BasicReminderNotificationWindow(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class BasicTxnRenderer(AbstractTxnRenderer):
    pass
    
class BegForRatingPanel('javax.swing.JPanel'):
    pass
    
class BigDetailedButton('javax.swing.JPanel'):
    pass
    
class CCAccountInfoPanel(AccountInfoPanel, 'java.awt.event.ItemListener'):
    pass
    
class CCTxnRenderer(AbstractTxnRenderer):
    pass
    
class COATreePanel('javax.swing.JPanel', 'javax.swing.event.ChangeListener', 'java.awt.event.ActionListener'):
    pass
    
class SecondaryFrame(SecondaryWindow, 'javax.swing.JFrame', 'java.awt.event.KeyListener'):
    pass
    
class COAWindow(SecondaryFrame, 'java.awt.event.ActionListener'):
    pass
    
class Calculator('javax.swing.JComponent'):
    pass
    
class CalendarMouseListener:
    def __init__(self, moneydanceGUI: 'MoneydanceGUI', monthView: 'MonthView', c: com.infinitekind.moneydance.model.AccountBook): ...
    
    
class CheckNumbersEditor('javax.swing.JPanel'):
    pass
    
class ChooseSplitType('javax.swing.JDialog', 'java.awt.event.ActionListener'):
    pass
    
class CircleDrawer('org.jfree.ui.Drawable'):
    def __init__(self, j: 'java.awt.Paint', j2: 'java.awt.Stroke', j3: 'java.awt.Paint'): ...
    
    def draw(self, j: 'java.awt.Graphics2D', j2: 'java.awt.geom.Rectangle2D') -> None: ...
    
    
class ConfirmDeleteDialog(OKButtonListener, 'javax.swing.JDialog'):
    pass
    
class ConsoleWindow(SecondaryFrame):
    pass
    
class CreateAccountWizard(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class CurrHistoryWindow(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class CurrInfoPanel('javax.swing.JPanel'):
    pass
    
class CurrencyGraphLabeler('com.moneydance.awt.graph.ValueLabeler'):
    def __init__(self, moneydanceGUI: 'MoneydanceGUI', c: com.infinitekind.moneydance.model.CurrencyType): ...
    
    def getLabelForValue(self, f: float, i: int) -> str: ...
    
    def preferencesUpdated(self) -> None: ...
    
    
class CurrencyModel('javax.swing.AbstractListModel', 'javax.swing.ComboBoxModel', com.infinitekind.moneydance.model.CurrencyListener):
    pass
    
class CustomFilterButton('javax.swing.JToggleButton'):
    pass
    
class DateGraphLabeler('com.moneydance.awt.graph.ValueLabeler'):
    def __init__(self, moneydanceGUI: 'MoneydanceGUI'): ...
    
    def getLabelForValue(self, f: float, i: int) -> str: ...
    
    def preferencesUpdated(self) -> None: ...
    
    
class DateRangeChooser(com.moneydance.util.BasePropertyChangeReporter, 'java.awt.event.ItemListener', 'java.beans.PropertyChangeListener'):
    pass
    
class DebugWindow(SecondaryDialog):
    pass
    
class DefaultAcctSearch(com.infinitekind.moneydance.model.AcctFilter):
    ACTIVE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$2@3cc82d81'
    ACTIVE_CATEGORY_CHOICE_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$9@be7fc86'
    ALL_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$7@6a996a69'
    CATEGORY_CHOICE_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$8@442a0860'
    CATEGORY_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$6@39f38141'
    EDITABLE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$5@d444935'
    FORMAT_FULL_PATH = 0
    FORMAT_INDENTED = 1
    INACTIVE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$3@2cafb0d6'
    NON_CATEGORY_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$1@38d2c42b'
    VIEWABLE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$4@1d8ea3f9'
    
    def __init__(self): ...
    
    def clearDontShowAccounts(self) -> None: ...
    
    def format(self, c: com.infinitekind.moneydance.model.Account) -> str: ...
    
    def getContainerAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def setContainerAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def setDontShowInactiveAccounts(self, b: bool) -> None: ...
    
    def setFormatMethod(self, i: int) -> None: ...
    
    def setShowAccount(self, c: com.infinitekind.moneydance.model.Account, b: bool) -> None: ...
    
    def setShowAssetAccounts(self, b: bool) -> None: ...
    
    def setShowBankAccounts(self, b: bool) -> None: ...
    
    def setShowCreditCardAccounts(self, b: bool) -> None: ...
    
    def setShowExpenseAccounts(self, b: bool) -> None: ...
    
    def setShowIncomeAccounts(self, b: bool) -> None: ...
    
    def setShowInvestAccounts(self, b: bool) -> None: ...
    
    def setShowLiabilityAccounts(self, b: bool) -> None: ...
    
    def setShowLoanAccounts(self, b: bool) -> None: ...
    
    def setShowOnlyDescendantsOf(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def setShowOnlyOnlineBankingCandidates(self, b: bool) -> None: ...
    
    def setShowOnlyOnlineBillPayCandidates(self, b: bool) -> None: ...
    
    def setShowOtherAccounts(self, b: bool) -> None: ...
    
    def setShowRootAccounts(self, b: bool) -> None: ...
    
    def setShowSecurityAccounts(self, b: bool) -> None: ...
    
    def showAllAccountTypes(self) -> None: ...
    
    
class DefaultOnlineUIProxy(com.infinitekind.moneydance.online.OnlineBankingUI):
    DEFAULT_ERROR_WINDOW_HEIGHT = 400
    DEFAULT_ERROR_WINDOW_WIDTH = 700
    
    def __init__(self, moneydanceGUI: 'MoneydanceGUI', c: com.infinitekind.moneydance.model.AccountBook, accountPanel: AccountPanel): ...
    
    def authenticateUser(self, c: com.infinitekind.moneydance.model.OnlineService, s: str, c2: com.infinitekind.moneydance.model.OnlineAccountProxy) -> com.infinitekind.moneydance.online.OFXAuthInfo: ...
    
    def getClientUID(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.online.OFXAuthInfo) -> str: ...
    
    def getResourceString(self, s: str) -> str: ...
    
    def getShortDateFormat(self) -> 'java.text.DateFormat': ...
    
    def matchSecurity(self, c: com.infinitekind.moneydance.model.OnlineService, s: str, s2: str, s3: str) -> com.infinitekind.moneydance.model.CurrencyType: ...
    
    def receivedStatement(self, c: com.infinitekind.moneydance.model.OnlineAccountProxy) -> None: ...
    
    def recordUndoableChange(self, list: List[com.infinitekind.moneydance.model.MoneydanceSyncableItem], list2: List[com.infinitekind.moneydance.model.MoneydanceSyncableItem]) -> None: ...
    
    def selectBankAccount(self, c: com.infinitekind.moneydance.model.OnlineService, s: str) -> com.infinitekind.moneydance.model.OnlineAccountProxy: ...
    
    def selectCreditCardAccount(self, c: com.infinitekind.moneydance.model.OnlineService, s: str) -> com.infinitekind.moneydance.model.OnlineAccountProxy: ...
    
    def selectInvestmentAccount(self, c: com.infinitekind.moneydance.model.OnlineService, s: str) -> com.infinitekind.moneydance.model.OnlineAccountProxy: ...
    
    def setPlaidItemStatus(self, c: 'com.moneydance.apps.md.controller.olb.plaid.PlaidConnection', c2: com.infinitekind.moneydance.model.OnlineAccountProxy, s: str, b: bool) -> None: ...
    
    def setStatus(self, s: str, f: float) -> None: ...
    
    def showOFXError(self, c: com.infinitekind.moneydance.online.ErrorMessage) -> None: ...
    
    
class DeleteSecurityWindow(SecondaryDialog, OKButtonListener):
    pass
    
class DocumentsRootSelectionDialog:
    def __init__(self, j: 'java.awt.Frame', c: com.moneydance.apps.md.view.resources.Resources): ...
    
    def getWorkingDirectory(self) -> 'java.io.File': ...
    
    def show(self) -> None: ...
    
    
class DropTargetDelegate:
    def __init__(self): ...
    
    def dragEntered(self) -> None: ...
    
    def dragExited(self) -> None: ...
    
    def dragOver(self, j: 'java.awt.Point') -> None: ...
    
    def droppedFiles(self, list: List['java.io.File']) -> None: ...
    
    def isAcceptableFile(self, j: 'java.io.File') -> bool: ...
    
    
class DropboxFileWarning:
    def __init__(self): ...
    
    @staticmethod
    def checkFileBeforeOpening(moneydanceGUI: 'MoneydanceGUI', c: com.moneydance.apps.md.controller.AccountBookWrapper) -> com.moneydance.apps.md.controller.AccountBookWrapper: ...
    
    
class EditCurrencyWindow(SecondaryDialog):
    pass
    
class EditInvestTxnListener:
    def __init__(self): ...
    
    def doneEditing(self, investTransactionEditor: 'InvestTransactionEditor', c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    
class EditRemindersWindow(SecondaryDialog, 'java.awt.event.ActionListener', 'print.MDPrintable'):
    pass
    
class EditSecuritiesWindow(SecondaryDialog):
    pass
    
class EditTransactionListener:
    def __init__(self): ...
    
    def cancelEdits(self) -> None: ...
    
    def txnDeleted(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def txnRecorded(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    
class EncryptInfoWin(SecondaryDialog, OKButtonListener, 'java.awt.event.ItemListener'):
    pass
    
class ExchangeRateEditor('javax.swing.JPanel', 'java.awt.event.ItemListener', 'java.awt.event.KeyListener'):
    pass
    
class ExpenseIncomeAccountInfoPanel(AccountInfoPanel, 'javax.swing.event.ChangeListener'):
    pass
    
class ExportWindow(SecondaryDialog, OKButtonListener, 'java.awt.event.ItemListener'):
    pass
    
class FXWebView(Callable):
    def __init__(self): ...
    
    def loadURL(self, s: str) -> None: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    def run(self) -> None: ...
    
    def setDeleteEnvironment(self, b: bool) -> None: ...
    
    
class FieldCalculator(SecondaryDialog, 'javax.swing.event.DocumentListener'):
    pass
    
class FileFixer:
    def __init__(self): ...
    
    def repairWrapper(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> com.moneydance.apps.md.controller.AccountBookWrapper: ...
    
    def restoreFromBackup(self, moneydanceGUI: 'MoneydanceGUI', c: com.moneydance.apps.md.controller.AccountBookWrapper) -> com.moneydance.apps.md.controller.AccountBookWrapper: ...
    
    
class FindTxnWindow(SecondaryDialog, OKButtonListener):
    pass
    
class FlatButtonUI('javax.swing.plaf.basic.BasicButtonUI'):
    def __init__(self, s: str): ...
    
    def getBackgroundColor(self) -> 'java.awt.Paint': ...
    
    def getForegroundColor(self) -> 'java.awt.Color': ...
    
    def getPreferredSize(self, j: 'javax.swing.JComponent') -> 'java.awt.Dimension': ...
    
    def getSelectedBackgroundColor(self) -> 'java.awt.Paint': ...
    
    def getSelectedForegroundColor(self) -> 'java.awt.Color': ...
    
    def getShadowPaint(self) -> 'java.awt.Paint': ...
    
    def installDefaults(self, j: 'javax.swing.AbstractButton') -> None: ...
    
    def installUI(self, j: 'javax.swing.JComponent') -> None: ...
    
    def paint(self, j: 'java.awt.Graphics', j2: 'javax.swing.JComponent') -> None: ...
    
    def setBackgroundColor(self, j: 'java.awt.Paint') -> None: ...
    
    def setDisabledTextColor(self, j: 'java.awt.Color') -> None: ...
    
    def setForegroundColor(self, j: 'java.awt.Color') -> None: ...
    
    def setSelectedBackgroundColor(self, j: 'java.awt.Paint') -> None: ...
    
    def setSelectedForegroundColor(self, j: 'java.awt.Color') -> None: ...
    
    def setShadowPaint(self, j: 'java.awt.Paint') -> None: ...
    
    def uninstallDefaults(self, j: 'javax.swing.AbstractButton') -> None: ...
    
    def update(self, j: 'java.awt.Graphics', j2: 'javax.swing.JComponent') -> None: ...
    
    
    class FlatButtonType:
        BOTH = 'BOTH'
        LEFT = 'LEFT'
        MIDDLE = 'MIDDLE'
        RIGHT = 'RIGHT'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class GenericDialog(OKButtonListener, 'javax.swing.JDialog'):
    pass
    
class GenericDropTargetListener('java.awt.dnd.DropTargetListener'):
    INVALID_FILE = ''
    
    def __init__(self, t: 'T'): ...
    
    def dragEnter(self, j: 'java.awt.dnd.DropTargetDragEvent') -> None: ...
    
    def dragExit(self, j: 'java.awt.dnd.DropTargetEvent') -> None: ...
    
    def dragOver(self, j: 'java.awt.dnd.DropTargetDragEvent') -> None: ...
    
    def drop(self, j: 'java.awt.dnd.DropTargetDropEvent') -> None: ...
    
    def dropActionChanged(self, j: 'java.awt.dnd.DropTargetDragEvent') -> None: ...
    
    def getDropTarget(self) -> 'java.awt.dnd.DropTarget': ...
    
    def getTransferHandler(self) -> 'javax.swing.TransferHandler': ...
    
    
class GradientPanel('javax.swing.JPanel'):
    pass
    
class GraphReportGenerator:
    GRFNAME_ACCBALANCE = u'com.moneydance.apps.md.view.gui.graphtool.AccountBalanceGraph'
    GRFNAME_ASSETALLOCATE = u'com.moneydance.apps.md.view.gui.graphtool.AssetAllocationGraph'
    GRFNAME_CURRENCY = u'com.moneydance.apps.md.view.gui.graphtool.CurrencyGraph'
    GRFNAME_EXPENSES = u'com.moneydance.apps.md.view.gui.graphtool.ExpensesGraph'
    GRFNAME_INCOME = u'com.moneydance.apps.md.view.gui.graphtool.IncomeGraph'
    GRFNAME_INCOME_EXPENSE = u'com.moneydance.apps.md.view.gui.graphtool.IncomeExpenseGraph'
    GRFNAME_MEMORIZED = u'com.moneydance.apps.md.view.gui.graphtool.MemorizedGraph'
    GRFNAME_NETWORTH = u'com.moneydance.apps.md.view.gui.graphtool.NetWorthGraph'
    PARAM_ACCOUNT = u'account'
    PARAM_ACCTS = u'accounts'
    PARAM_ALL_ACCOUNTS = u'all_accounts'
    PARAM_ALL_CATEGORIES = u'all_categories'
    PARAM_AMOUNT = u'amount'
    PARAM_AS_OF = u'as_of'
    PARAM_BALANCE_TYPE = u'balance'
    PARAM_BUDGET_KEY = u'budget_key'
    PARAM_BY_INV_ACCT = u'inv_acct'
    PARAM_BY_SECURITY = u'security'
    PARAM_CATEGORIES = u'categories'
    PARAM_CHECKNUM = u'cknum'
    PARAM_CLEARED = u'cleared'
    PARAM_COL_WIDTHS = u'colWidths'
    PARAM_COMBINE_TYPE = u'combine'
    PARAM_CUMULATIVE = u'cumulative'
    PARAM_CURRENCY = u'currency'
    PARAM_CURRENCY_FROM = u'fm_curr_id'
    PARAM_CURRENCY_TO = u'to_curr_id'
    PARAM_DATE = u'date'
    PARAM_DESC = u'desc'
    PARAM_DESC_MEMO_SAME_LINE = u'desc_memo_same_line'
    PARAM_FILTER_LEGACY_TAGS = u'tags'
    PARAM_FILTER_TAGLOGIC = u'taglogic'
    PARAM_FILTER_TAGS = u'tags2'
    PARAM_FULL_ACCT_PATH = u'fullpath'
    PARAM_GROUP_BY = u'group_by'
    PARAM_INCLUDE_SECURITIES = u'include_securities'
    PARAM_INCLUDE_SUBACCOUNTS = u'include_subaccounts'
    PARAM_INCLUDE_ZERO_BAL_ACCTS = u'inc_zero_balances'
    PARAM_INC_LIABILITIES = u'include_liabilities'
    PARAM_MEMO = u'memo'
    PARAM_ORIENTATION = u'landscape'
    PARAM_RELATIVE_TO = u'relative_to'
    PARAM_SELECTED_ACCOUNTS = u'selected_accounts'
    PARAM_SHOW_3D = u'show_3d'
    PARAM_SHOW_EXTRAINFO = u'show_extra'
    PARAM_SHOW_LEGEND = u'show_legend'
    PARAM_SHOW_MEMOS = u'show_memos'
    PARAM_SHOW_SPLITS = u'show_splits'
    PARAM_SHOW_TOP = u'show_top'
    PARAM_SHOW_TRANSFERS = u'show_xfers'
    PARAM_SHOW_UNREALIZED = u'show_unrealized'
    PARAM_SHOW_ZEROES = u'show_zeroes'
    PARAM_SOURCE_ACCOUNTS = u'source_accts'
    PARAM_STACKED = u'stacked'
    PARAM_SUBTOTAL_CATEGORIES = u'subtotal_categories'
    PARAM_TAX_DATE = u'useTaxDate'
    PARAM_TAX_RELATED = u'tax_related'
    PARAM_TWO_LINES = u'twolines'
    PARAM_USE_TAX_DATE = u'use_tax_date'
    REPNAME_ACCBALANCE = u'com.moneydance.apps.md.view.gui.reporttool.AccountBalanceReport'
    REPNAME_ASSETALLOCATE = u'com.moneydance.apps.md.view.gui.reporttool.AssetAllocationReport'
    REPNAME_BUDGET = u'com.moneydance.apps.md.view.gui.reporttool.BudgetReport'
    REPNAME_CAPGAINS = u'com.moneydance.apps.md.view.gui.reporttool.CapitalGainsReport'
    REPNAME_CASHFLOW = u'com.moneydance.apps.md.view.gui.reporttool.RealCashFlowReport'
    REPNAME_COSTBASIS = u'com.moneydance.apps.md.view.gui.reporttool.CostBasisReport'
    REPNAME_DETAILEDCASHFLOW = u'com.moneydance.apps.md.view.gui.reporttool.RealDetailedCashFlowReport'
    REPNAME_DETAILEDINCEXP = u'com.moneydance.apps.md.view.gui.reporttool.DetailedCashFlowReport'
    REPNAME_DETAILEDXFER = u'com.moneydance.apps.md.view.gui.reporttool.DetailedTransferReport'
    REPNAME_INCEXP = u'com.moneydance.apps.md.view.gui.reporttool.CashFlowReport'
    REPNAME_INVESTPERF = u'com.moneydance.apps.md.view.gui.reporttool.InvestmentPerformanceReport'
    REPNAME_INVSEARCH = u'com.moneydance.apps.md.view.gui.reporttool.InvestTxnReport'
    REPNAME_MEMORIZED = u'com.moneydance.apps.md.view.gui.reporttool.MemorizedReport'
    REPNAME_MISSCHECKS = u'com.moneydance.apps.md.view.gui.reporttool.MissingChecksReport'
    REPNAME_NETWORTH = u'com.moneydance.apps.md.view.gui.reporttool.NetWorthReport'
    REPNAME_PORTFOLIO = u'com.moneydance.apps.md.view.gui.reporttool.PortfolioReport'
    REPNAME_RECONCILIATION = u'com.moneydance.apps.md.view.gui.reporttool.ReconciliationReport'
    REPNAME_SEARCH = u'com.moneydance.apps.md.view.gui.reporttool.SearchReport'
    REPNAME_TAGTOTAL = u'com.moneydance.apps.md.view.gui.reporttool.TagTotalReport'
    REPNAME_TXN = u'com.moneydance.apps.md.view.gui.reporttool.TxnReport'
    REPNAME_VAT = u'com.moneydance.apps.md.view.gui.reporttool.VATReport'
    REPNAME_XFER = u'com.moneydance.apps.md.view.gui.reporttool.TransferReport'
    
    def __init__(self): ...
    
    @staticmethod
    def findOrMakeReportInfo(c: com.infinitekind.moneydance.model.AccountBook, s: str, s2: str, b: bool) -> com.infinitekind.moneydance.model.ReportSpec: ...
    
    def generate(self) -> object: ...
    
    def getClassName(self) -> str: ...
    
    def getConfigPanel(self) -> 'javax.swing.JPanel': ...
    
    @staticmethod
    def getGenerator(c: com.infinitekind.moneydance.model.ReportSpec, moneydanceGUI: 'MoneydanceGUI') -> 'GraphReportGenerator': ...
    
    def getInfo(self) -> com.infinitekind.moneydance.model.ReportSpec: ...
    
    def getName(self) -> str: ...
    
    def goneAway(self) -> None: ...
    
    def isGraph(self) -> bool: ...
    
    @staticmethod
    def reportInfoFromURI(c: com.infinitekind.moneydance.model.AccountBook, s: str) -> com.infinitekind.moneydance.model.ReportSpec: ...
    
    def setGUI(self, moneydanceGUI: 'MoneydanceGUI') -> None: ...
    
    def setInfo(self, c: com.infinitekind.moneydance.model.ReportSpec) -> None: ...
    
    def setParameters(self, c: com.infinitekind.tiksync.SyncRecord) -> None: ...
    
    def setSuppressMessageDialogs(self, b: bool) -> None: ...
    
    @staticmethod
    def showReport(c: com.infinitekind.moneydance.model.ReportSpec, moneydanceGUI: 'MoneydanceGUI') -> None: ...
    
    def toString(self) -> str: ...
    
    
class GraphReportWindow(SecondaryDialog, 'java.awt.event.ActionListener', com.infinitekind.moneydance.model.AccountListener):
    pass
    
class HeavyLotIDPanel(SecondaryDialog, OKButtonListener, 'javax.swing.event.ListSelectionListener'):
    pass
    
class HomePageBorder('javax.swing.border.Border'):
    def __init__(self): ...
    
    def getBorderInsets(self, j: 'java.awt.Component') -> 'java.awt.Insets': ...
    
    def getFillColor(self) -> 'java.awt.Color': ...
    
    def getLineColor(self) -> 'java.awt.Color': ...
    
    def getSectionBackground(self) -> 'java.awt.Color': ...
    
    def isBorderOpaque(self) -> bool: ...
    
    def paintBorder(self, j: 'java.awt.Component', j2: 'java.awt.Graphics', i: int, i2: int, i3: int, i4: int) -> None: ...
    
    def setBorderInsets(self, j: 'java.awt.Insets') -> None: ...
    
    def setFillColor(self, j: 'java.awt.Color') -> None: ...
    
    def setLineColor(self, j: 'java.awt.Color') -> None: ...
    
    def setSectionBackground(self, j: 'java.awt.Color') -> None: ...
    
    def updateUI(self) -> None: ...
    
    
class HomeViewSettings('javax.swing.JPanel', 'java.awt.event.ActionListener'):
    pass
    
class ImportCurrHistoryWindow(SecondaryDialog, OKButtonListener):
    pass
    
class ImportFileTransferHandler('javax.swing.TransferHandler'):
    COPY = 1
    COPY_OR_MOVE = 3
    LINK = 1073741824
    MOVE = 2
    NONE = 0
    
    def __init__(self, moneydanceGUI: 'MoneydanceGUI'): ...
    
    def getSourceActions(self, j: 'javax.swing.JComponent') -> int: ...
    
    
class ImportOFCWindow(SecondaryDialog, OKButtonListener, 'java.awt.event.ActionListener'):
    pass
    
class ImportOFXWindow(SecondaryDialog, OKButtonListener, 'java.awt.event.ActionListener'):
    pass
    
class ImportTask:
    def __init__(self, moneydanceGUI: 'MoneydanceGUI', c: com.moneydance.apps.md.controller.fileimport.FileImporter, j: 'java.io.InputStream'): ...
    
    def start(self) -> None: ...
    
    
class IntegerGraphLabeler('com.moneydance.awt.graph.ValueLabeler'):
    def __init__(self): ...
    
    def getLabelForValue(self, f: float, i: int) -> str: ...
    
    
class IntervalChooser('javax.swing.JComboBox'):
    pass
    
class InvestAccountDetailPanel(AccountDetailPanel, 'java.awt.event.ActionListener', com.infinitekind.moneydance.model.AccountListener):
    pass
    
class InvestTxnEditInterface:
    def __init__(self): ...
    
    def beginEditing(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def commitEdits(self) -> None: ...
    
    def getEdits(self) -> com.moneydance.util.StreamTable: ...
    
    def getOnlineMode(self) -> bool: ...
    
    def getPanel(self) -> 'javax.swing.JComponent': ...
    
    def goingAway(self) -> bool: ...
    
    def goneAway(self) -> None: ...
    
    def inputCheck(self) -> bool: ...
    
    def setBackground(self, j: 'java.awt.Color') -> None: ...
    
    def setEdits(self, c: com.moneydance.util.StreamTable) -> None: ...
    
    def setOnlineMode(self, b: bool) -> None: ...
    
    def setSecurity(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    
class InvestBankTxnEditor(InvestTxnEditInterface, 'javax.swing.JPanel'):
    pass
    
class InvestTxnEditor(InvestTxnEditInterface, 'javax.swing.JPanel', com.moneydance.apps.md.controller.PreferencesListener):
    pass
    
class InvestBuySellEditor(InvestTxnEditor, 'java.awt.event.ItemListener', 'javax.swing.event.DocumentListener'):
    pass
    
class InvestDividendEditor(InvestTxnEditor, 'java.awt.event.ItemListener', 'java.awt.event.FocusListener', 'javax.swing.event.DocumentListener'):
    pass
    
class InvestDividendXfrEditor(InvestTxnEditor, 'java.awt.event.ItemListener'):
    pass
    
class InvestMiscTxnEditor(InvestTxnEditor, 'java.awt.event.ItemListener'):
    pass
    
class InvestRegister(AccountDetailPanel):
    pass
    
class InvestShortCoverEditor(InvestTxnEditor, 'java.awt.event.ItemListener'):
    pass
    
class InvestTransactionEditor('javax.swing.JPanel', 'java.awt.event.ActionListener'):
    pass
    
class InvestTxnRenderer(AbstractTxnRenderer):
    pass
    
class InvestTxnUtil:
    def __init__(self): ...
    
    @staticmethod
    def getTxnEditor(moneydanceGUI: 'MoneydanceGUI', c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.InvestTxnType, investTxnEditInterface: InvestTxnEditInterface) -> InvestTxnEditInterface: ...
    
    
class InvestTxnWindow(SecondaryDialog):
    pass
    
class InvestXfrEditor(InvestTxnEditor, 'java.awt.event.ItemListener', 'javax.swing.event.DocumentListener'):
    pass
    
class InvestmentAccountInfoPanel(AccountInfoPanel, 'java.awt.event.ItemListener'):
    pass
    
class InvstRecTxnRenderer(AbstractTxnRenderer):
    pass
    
class JSmartPanel('javax.swing.JPanel', 'java.awt.event.ActionListener'):
    pass
    
class LastPrintedCheckWindow(OKButtonListener, 'javax.swing.JDialog'):
    pass
    
class LiabilityAccountInfoPanel(AccountInfoPanel):
    pass
    
class LicenseAgreementWindow('javax.swing.JDialog', 'java.awt.event.ActionListener'):
    pass
    
class LicenseKeyWindow(SecondaryDialog, OKButtonListener):
    pass
    
class LicenseWindow(SecondaryDialog, OKButtonListener):
    pass
    
class LightLotIDPanel(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class LoanAccountDetailPanel(AccountDetailPanel, com.infinitekind.moneydance.model.AccountListener, 'java.awt.event.ActionListener'):
    pass
    
class LoanAccountInfoPanel(AccountInfoPanel, 'javax.swing.event.ChangeListener', 'java.awt.event.ItemListener', 'java.awt.event.FocusListener', 'java.awt.event.ActionListener'):
    pass
    
class LoanCalculator('javax.swing.JPanel', 'java.awt.event.ActionListener', 'java.awt.event.FocusListener'):
    pass
    
class LoanReminderTxnEditPanel(AutoCompletable, 'javax.swing.JPanel', 'java.awt.event.FocusListener', 'java.awt.event.ItemListener', 'java.awt.event.KeyListener', Callable):
    pass
    
class LoanToolsWin(SecondaryFrame):
    pass
    
class LoanTxnReminderInfoWindow(SecondaryDialog, OKButtonListener):
    pass
    
class LoanTxnReminderNotificationWindow(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class LoanTxnRenderer(AbstractTxnRenderer):
    pass
    
class LotChooser('javax.swing.JPanel', 'java.awt.event.FocusListener'):
    pass
    
class MDAccountProxy(com.infinitekind.moneydance.model.OnlineAccountProxy):
    def __init__(self, c: com.infinitekind.moneydance.model.Account): ...
    
    def getAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getAccountInfo(self) -> com.infinitekind.moneydance.model.OnlineAccountInfo: ...
    
    def getAccountKey(self) -> str: ...
    
    def getAccountMsgType(self) -> int: ...
    
    def getCurrency(self) -> com.infinitekind.moneydance.model.CurrencyType: ...
    
    def getDownloadStartDate(self, s: str) -> 'java.util.Date': ...
    
    def getDownloadedTxns(self) -> com.infinitekind.moneydance.model.OnlineTxnList: ...
    
    def getOFXAccountKey(self) -> str: ...
    
    def getOFXAccountNumber(self) -> str: ...
    
    def getOFXAccountType(self) -> str: ...
    
    def getOFXBranchID(self) -> str: ...
    
    def getOFXBrokerID(self) -> str: ...
    
    def getOFXRoutingNumber(self) -> str: ...
    
    def getPayees(self) -> com.infinitekind.moneydance.model.OnlinePayeeList: ...
    
    def getPayments(self) -> com.infinitekind.moneydance.model.OnlinePaymentList: ...
    
    def isCreditCard(self) -> bool: ...
    
    def isInvestment(self) -> bool: ...
    
    def setOFXLastTxnUpdate(self, i: int, s: str) -> None: ...
    
    def setOnlineAvailBalance(self, i: int, i2: int) -> None: ...
    
    def setOnlineLedgerBalance(self, i: int, i2: int) -> None: ...
    
    def toString(self) -> str: ...
    
    
class MDAction('javax.swing.AbstractAction'):
    pass
    
class MDColors:
    TRANSPARENT = 'java.awt.Color[r=0,g=0,b=0]'
    accountIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.accountIconTint at 0x3b>'
    budgetAcceptableColor = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.budgetAcceptableColor at 0x3c>'
    budgetAlertColor = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.budgetAlertColor at 0x3d>'
    budgetGraphWarning = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.budgetGraphWarning at 0x3e>'
    budgetHealthyColor = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.budgetHealthyColor at 0x3f>'
    budgetIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.budgetIconTint at 0x40>'
    calEventBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.calEventBG at 0x41>'
    calPastEventBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.calPastEventBG at 0x42>'
    dashboardFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.dashboardFG at 0x43>'
    defaultBackground = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.defaultBackground at 0x44>'
    defaultTextForeground = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.defaultTextForeground at 0x45>'
    dimmedRegisterOverlay = 'java.awt.Color[r=255,g=255,b=255]'
    errorMessageForeground = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.errorMessageForeground at 0x46>'
    errorPanelBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.errorPanelBG at 0x47>'
    errorPanelFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.errorPanelFG at 0x48>'
    expenseIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.expenseIconTint at 0x49>'
    filterBarBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.filterBarBG at 0x4a>'
    filterBarBorderPaint = '<reflected field public java.awt.Paint com.moneydance.apps.md.view.gui.MDColors.filterBarBorderPaint at 0x4b>'
    filterBarBtnBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.filterBarBtnBG at 0x4c>'
    filterBarFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.filterBarFG at 0x4d>'
    filterBarSelBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.filterBarSelBG at 0x4e>'
    filterBarSelFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.filterBarSelFG at 0x4f>'
    filterBarShadow = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.filterBarShadow at 0x50>'
    filterBarShadowPaint = '<reflected field public java.awt.Paint com.moneydance.apps.md.view.gui.MDColors.filterBarShadowPaint at 0x51>'
    futureTxn2BG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.futureTxn2BG at 0x52>'
    futureTxnBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.futureTxnBG at 0x53>'
    futureTxnIndicator = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.futureTxnIndicator at 0x54>'
    graphBG1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphBG1 at 0x55>'
    graphBG2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphBG2 at 0x56>'
    graphBGGradient = '<reflected field public java.awt.GradientPaint com.moneydance.apps.md.view.gui.MDColors.graphBGGradient at 0x57>'
    graphData1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData1 at 0x58>'
    graphData10 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData10 at 0x59>'
    graphData11 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData11 at 0x5a>'
    graphData12 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData12 at 0x5b>'
    graphData13 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData13 at 0x5c>'
    graphData14 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData14 at 0x5d>'
    graphData15 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData15 at 0x5e>'
    graphData16 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData16 at 0x5f>'
    graphData17 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData17 at 0x60>'
    graphData18 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData18 at 0x61>'
    graphData19 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData19 at 0x62>'
    graphData2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData2 at 0x63>'
    graphData20 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData20 at 0x64>'
    graphData21 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData21 at 0x65>'
    graphData22 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData22 at 0x66>'
    graphData23 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData23 at 0x67>'
    graphData3 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData3 at 0x68>'
    graphData4 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData4 at 0x69>'
    graphData5 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData5 at 0x6a>'
    graphData6 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData6 at 0x6b>'
    graphData7 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData7 at 0x6c>'
    graphData8 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData8 at 0x6d>'
    graphData9 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphData9 at 0x6e>'
    graphIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.graphIconTint at 0x6f>'
    headerBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.headerBG at 0x70>'
    headerBG1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.headerBG1 at 0x71>'
    headerBG2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.headerBG2 at 0x72>'
    headerBGGradient = '<reflected field public java.awt.GradientPaint com.moneydance.apps.md.view.gui.MDColors.headerBGGradient at 0x73>'
    headerBorder = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.headerBorder at 0x74>'
    headerFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.headerFG at 0x75>'
    homeIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.homeIconTint at 0x76>'
    homePageAltBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.homePageAltBG at 0x77>'
    homePageBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.homePageBG at 0x78>'
    homePageFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.homePageFG at 0x79>'
    homepageSectionBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.homepageSectionBG at 0x7a>'
    hudBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.hudBG at 0x7b>'
    hudBG1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.hudBG1 at 0x7c>'
    hudBG2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.hudBG2 at 0x7d>'
    hudBorderColor = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.hudBorderColor at 0x7e>'
    hudFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.hudFG at 0x7f>'
    incomeIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.incomeIconTint at 0x80>'
    listBackground = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.listBackground at 0x81>'
    listSelectionBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.listSelectionBG at 0x82>'
    mainDivider = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.mainDivider at 0x83>'
    mainPanelBorderColor = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.mainPanelBorderColor at 0x84>'
    negativeBalFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.negativeBalFG at 0x85>'
    popoverBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.popoverBG at 0x86>'
    popoverBorder = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.popoverBorder at 0x87>'
    popoverTriangleBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.popoverTriangleBG at 0x88>'
    positiveBalFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.positiveBalFG at 0x89>'
    registerBG1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerBG1 at 0x8a>'
    registerBG2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerBG2 at 0x8b>'
    registerGrid = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerGrid at 0x8c>'
    registerSelectedBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerSelectedBG at 0x8d>'
    registerSelectedFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerSelectedFG at 0x8e>'
    registerTextFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerTextFG at 0x8f>'
    registerUnconfirmedIconFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerUnconfirmedIconFG at 0x90>'
    registerUnfocusedSelectedBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.registerUnfocusedSelectedBG at 0x91>'
    reminderHomeInnerLine = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.reminderHomeInnerLine at 0x92>'
    remindersIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.remindersIconTint at 0x93>'
    reportBlueFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.reportBlueFG at 0x94>'
    reportIconTint = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.reportIconTint at 0x95>'
    reportRedFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.reportRedFG at 0x96>'
    scrollThumb = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.scrollThumb at 0x97>'
    secondaryTextFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.secondaryTextFG at 0x98>'
    selectedRowGradient1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.selectedRowGradient1 at 0x99>'
    selectedRowGradient2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.selectedRowGradient2 at 0x9a>'
    selectedRowUFGradient1 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.selectedRowUFGradient1 at 0x9b>'
    selectedRowUFGradient2 = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.selectedRowUFGradient2 at 0x9c>'
    sidebarBackground = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarBackground at 0x9d>'
    sidebarHeader = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarHeader at 0x9e>'
    sidebarNegativeBalanceFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarNegativeBalanceFG at 0x9f>'
    sidebarPositiveBalanceFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarPositiveBalanceFG at 0xa0>'
    sidebarSecondaryTextFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarSecondaryTextFG at 0xa1>'
    sidebarSelectedBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarSelectedBG at 0xa2>'
    sidebarSelectedFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarSelectedFG at 0xa3>'
    sidebarUFSelectedBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.sidebarUFSelectedBG at 0xa4>'
    tableHeaderBG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.tableHeaderBG at 0xa5>'
    tertiaryTextFG = '<reflected field public java.awt.Color com.moneydance.apps.md.view.gui.MDColors.tertiaryTextFG at 0xa6>'
    
    def __init__(self): ...
    
    def colorsWereUpdated(self) -> None: ...
    
    def decorateFrame(self, j: 'javax.swing.JFrame') -> None: ...
    
    def decorateTopLevelPanel(self, j: 'javax.swing.JPanel') -> None: ...
    
    @staticmethod
    def getDefaultColorMap() -> Dict[str,'java.awt.Color']: ...
    
    @staticmethod
    def getPrintableColors() -> 'MDColors': ...
    
    @staticmethod
    def getSingleton() -> 'MDColors': ...
    
    def isDarkTheme(self) -> bool: ...
    
    def loadDefaultColors(self) -> None: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    
class MDFieldPanel('javax.swing.JPanel'):
    pass
    
class MDFileDialog('java.awt.FileDialog'):
    pass
    
class MDFonts:
    calendarTitle = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.calendarTitle at 0xa7>'
    code = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.code at 0xa8>'
    codeDefault = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.codeDefault at 0xa9>'
    defaultMetrics = '<reflected field public java.awt.FontMetrics com.moneydance.apps.md.view.gui.MDFonts.defaultMetrics at 0xaa>'
    defaultSystemFont = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.defaultSystemFont at 0xab>'
    defaultSystemMetrics = '<reflected field public java.awt.font.LineMetrics com.moneydance.apps.md.view.gui.MDFonts.defaultSystemMetrics at 0xac>'
    defaultText = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.defaultText at 0xad>'
    defaultTextDefault = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.defaultTextDefault at 0xae>'
    detailTitle = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.detailTitle at 0xaf>'
    detailTitleMetrics = '<reflected field public java.awt.FontMetrics com.moneydance.apps.md.view.gui.MDFonts.detailTitleMetrics at 0xb0>'
    header = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.header at 0xb1>'
    headerMetrics = '<reflected field public java.awt.FontMetrics com.moneydance.apps.md.view.gui.MDFonts.headerMetrics at 0xb2>'
    mini = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.mini at 0xb3>'
    mono = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.mono at 0xb4>'
    monoDefault = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.monoDefault at 0xb5>'
    monoMetrics = '<reflected field public java.awt.FontMetrics com.moneydance.apps.md.view.gui.MDFonts.monoMetrics at 0xb6>'
    print = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.print at 0xb7>'
    printDefault = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.printDefault at 0xb8>'
    register = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.register at 0xb9>'
    registerMetrics = '<reflected field public java.awt.FontMetrics com.moneydance.apps.md.view.gui.MDFonts.registerMetrics at 0xba>'
    reportHeader = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.reportHeader at 0xbb>'
    reportTitle = '<reflected field public java.awt.Font com.moneydance.apps.md.view.gui.MDFonts.reportTitle at 0xbc>'
    reportTitleMetrics = '<reflected field public java.awt.FontMetrics com.moneydance.apps.md.view.gui.MDFonts.reportTitleMetrics at 0xbd>'
    
    def __init__(self): ...
    
    @staticmethod
    def getSingleton() -> 'MDFonts': ...
    
    def updateFonts(self, b: bool) -> None: ...
    
    def updateMetricsIfNecessary(self, j: 'java.awt.Graphics') -> None: ...
    
    
class MDHeaderRenderer('javax.swing.table.DefaultTableCellRenderer'):
    pass
    
class MDImages:
    ACCT_ASSET_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_assets.png'
    ACCT_BANK_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_bank.png'
    ACCT_BANK_OL_ICON = u'/com/moneydance/apps/md/view/gui/images/md_tree_account_ol_icon.gif'
    ACCT_CC_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_cc.png'
    ACCT_DEFAULT_ICON = u'/com/moneydance/apps/md/view/gui/images/md_tree_uneditable_account_icon.gif'
    ACCT_DEFAULT_ICON_GRAY = u'/com/moneydance/apps/md/view/gui/images/md_tree_uneditable_account_icon_gray.gif'
    ACCT_EXPENSE_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_expense.png'
    ACCT_INCOME_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_income.png'
    ACCT_INVEST_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_invest.png'
    ACCT_LIABILITY_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_liability.png'
    ACCT_LOAN_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_loan.png'
    ACCT_RECONCILING_ICON = u'/com/moneydance/apps/md/view/gui/images/md_txn_reconciling_icon.gif'
    ACCT_STAT_NEW = u'/com/moneydance/apps/md/view/gui/glyphs/acct_status_unconfirmed.png'
    ACCT_STOCK_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_invest.png'
    ACTIONS = u'/com/moneydance/apps/md/view/gui/icons/actions.png'
    ACTIONS_SMALL = u'/com/moneydance/apps/md/view/gui/icons/actions_sm.png'
    ALERT_ICON = u'/com/moneydance/apps/md/view/gui/icons/alert16.png'
    APP_ICON_128 = u'/com/moneydance/apps/md/view/gui/glyphs/appicon_128.png'
    APP_ICON_512 = u'/com/moneydance/apps/md/view/gui/glyphs/appicon_512.png'
    APP_ICON_64 = u'/com/moneydance/apps/md/view/gui/glyphs/appicon_64.png'
    BACKGROUND_HEADER = u'/com/moneydance/apps/md/view/gui/images/bg_tiled.png'
    BLANK_ICON = u'/com/moneydance/apps/md/view/gui/images/blank_64.png'
    BLUE_DOT = u'/com/moneydance/apps/md/view/gui/icons/bluedot.png'
    BOTTOM_STATUS_BG = u'/com/moneydance/apps/md/view/gui/icons/bottom_status_bg.png'
    BOTTOM_STATUS_BG_MAC = u'/com/moneydance/apps/md/view/gui/icons/bottom_status_bg_grey.png'
    BOTTOM_TOOLBAR_BG = u'/com/moneydance/apps/md/view/gui/icons/bottom_toolbar_bg.png'
    BUDGET_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_budget.png'
    CALCULATOR_ICON = u'/com/moneydance/apps/md/view/gui/icons/calculator_icon.png'
    CALENDAR_NEXT_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/big_arrow_right.png'
    CALENDAR_PREV_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/big_arrow_left.png'
    CLOSE_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_close.png'
    CLOSE_ICON_HIGHLIGHT_SMALL = u'/com/moneydance/apps/md/view/gui/icons/close_toolbar_hl_14.png'
    CLOSE_ICON_SMALL = u'/com/moneydance/apps/md/view/gui/icons/close_toolbar_14.png'
    CONTEXT_MENU_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/context_menu_icon.png'
    DARK_STONE_BACKGROUND = u'/com/moneydance/apps/md/view/gui/images/stone_background.png'
    DELETE_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_delete.png'
    DELETE_ICON_PRESSED = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_delete.png'
    DIALOG = u'/com/moneydance/apps/md/view/gui/glyphs/appicon_64.png'
    DOWN_TRIANGLE = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_triangle_down.png'
    DROPBOX_ICON = u'/com/moneydance/apps/md/view/gui/images/dropbox_64.png'
    FILTER_BAR_BG = u'/com/moneydance/apps/md/view/gui/images/FilterBarBG.png'
    FOLDER_ICON = u'/com/moneydance/apps/md/view/gui/images/folder_64.png'
    GENERIC_FILE_ICON = u'/com/moneydance/apps/md/view/gui/icons/generic_file_icon.png'
    GREEN_DOT = u'/com/moneydance/apps/md/view/gui/icons/greendot.png'
    GRIP_HORIZONTAL = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_grip_horizontal.png'
    GRIP_VERTICAL = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_grip_vertical.png'
    HOME_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_summary.png'
    LCD_BACKGROUND = u'/com/moneydance/apps/md/view/gui/images/lcd_background.png'
    LEFT_TRIANGLE = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_triangle_left.png'
    LIGHT_STONE_BACKGROUND = u'/com/moneydance/apps/md/view/gui/images/light_stone_background.png'
    LINK_ARROW = u'/com/moneydance/apps/md/view/gui/icons/link_arrow.png'
    MINUS = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_minus.png'
    NOISE_OVERLAY = u'/com/moneydance/apps/md/view/gui/images/noise_overlay.png'
    NO_DOT = u'/com/moneydance/apps/md/view/gui/icons/nodot.png'
    OUTER_SHADOW = u'/com/moneydance/apps/md/view/gui/images/outershadow.png'
    PLUS = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_plus.png'
    POPOVER_CLOSE_ICON = u'/com/moneydance/awt/images/close.png'
    POPOVER_NEXT_ICON = u'/com/moneydance/awt/images/right_arrow.png'
    POPOVER_PREVIOUS_ICON = u'/com/moneydance/awt/images/left_arrow.png'
    POPOVER_TITLE_BG = u'/com/moneydance/apps/md/view/gui/images/popover_title_bg.png'
    PYTHON_BUTTON = u'/com/moneydance/apps/md/view/gui/glyphs/browser_python.png'
    RECESSED_AREA_BACKGROUND = u'/com/moneydance/apps/md/view/gui/images/recessed_bg.png'
    RED_DOT = u'/com/moneydance/apps/md/view/gui/icons/reddot.png'
    REFRESH = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_refresh.png'
    REMINDERS_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_reminders.png'
    RIGHT_TRIANGLE = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_triangle_right.png'
    SB_GRAPH = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_graphs.png'
    SB_REPORT = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_reports.png'
    SEARCH_SMALL = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_search.png'
    SELECTOR = u'/com/moneydance/apps/md/view/gui/glyphs/selector.png'
    SELECTOR_SMALL = u'/com/moneydance/apps/md/view/gui/glyphs/selector_sm.png'
    SMALL_MINUS = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_small_minus.png'
    SMALL_PLUS = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_small_plus.png'
    SPLIT_REGISER_ICON_BRIGHT = u'/com/moneydance/apps/md/view/gui/icons/reg_split_bright.png'
    SPLIT_REGISER_ICON_DARK = u'/com/moneydance/apps/md/view/gui/icons/reg_split.png'
    TAG_SELECTED = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_selected.png'
    TAG_UNSELECTED = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_unselected.png'
    TICK_MARK = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_tick.png'
    TREE_COLLAPSED_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_tree_collapsed.png'
    TREE_EXPANDED_ICON = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_tree_expanded.png'
    TXN_STAT_ADDRESS = u'/com/moneydance/apps/md/view/gui/glyphs/txn_status_hasaddress.png'
    TXN_STAT_ATTACHMENT = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_attachment.png'
    TXN_STAT_CLEARED = u'/com/moneydance/apps/md/view/gui/glyphs/txn_status_cleared.png'
    TXN_STAT_NEW = u'/com/moneydance/apps/md/view/gui/glyphs/txn_status_unconfirmed.png'
    TXN_STAT_ONLINE = u'/com/moneydance/apps/md/view/gui/glyphs/txn_status_downloaded.png'
    TXN_STAT_RECONCILING = u'/com/moneydance/apps/md/view/gui/glyphs/txn_status_reconciling.png'
    TXN_STAT_SPLIT = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_split.png'
    TXN_STAT_UNCLEARED = u'/com/moneydance/apps/md/view/gui/glyphs/txn_status_uncleared.png'
    UNSPLIT_REGISER_ICON_BRIGHT = u'/com/moneydance/apps/md/view/gui/icons/reg_combined_bright.png'
    UNSPLIT_REGISER_ICON_DARK = u'/com/moneydance/apps/md/view/gui/icons/reg_combined.png'
    UP_TRIANGLE = u'/com/moneydance/apps/md/view/gui/glyphs/glyph_triangle_up.png'
    VIEW_SOURCE = u'/com/moneydance/apps/md/view/gui/glyphs/browser_source_html.png'
    VISIBILITY_ICON = u'/com/moneydance/apps/md/view/gui/icons/visibility_toggle.png'
    WHITE_DOT = u'/com/moneydance/apps/md/view/gui/icons/whitedot.png'
    YELLOW_DOT = u'/com/moneydance/apps/md/view/gui/icons/yellowdot.png'
    
    def __init__(self): ...
    
    @staticmethod
    def get2xImagePath(s: str) -> str: ...
    
    def getIcon(self, s: str) -> 'javax.swing.Icon': ...
    
    def getIconForAccount(self, c: com.infinitekind.moneydance.model.Account) -> 'javax.swing.Icon': ...
    
    def getIconForAccountType(self, s: str) -> 'javax.swing.Icon': ...
    
    @staticmethod
    def getIconPathForAccountType(s: str) -> str: ...
    
    def getIconTintForAccountType(self, s: str) -> 'java.awt.Color': ...
    
    def getIconWithColor(self, s: str, j: 'java.awt.Color') -> 'javax.swing.Icon': ...
    
    @staticmethod
    def getImage(s: str) -> 'java.awt.Image': ...
    
    @staticmethod
    def getMDIcon(s: str) -> 'javax.swing.Icon': ...
    
    @staticmethod
    def getMDIconWithColor(s: str, j: 'java.awt.Color') -> 'javax.swing.Icon': ...
    
    def getPreviewForFile(self, j: 'java.io.File', j2: 'java.awt.Dimension') -> 'java.awt.Image': ...
    
    @staticmethod
    def getSingletonImages() -> 'MDImages': ...
    
    def getStatusImage(self, s: str) -> 'java.awt.Image': ...
    
    @staticmethod
    def scaledMultiresImage(list: List[int], i: int, i2: int) -> 'java.awt.Image': ...
    
    @staticmethod
    def toBufferedImage(j: 'java.awt.Image') -> 'java.awt.image.BufferedImage': ...
    
    
class MDLabel('javax.swing.JComponent'):
    pass
    
class MDPlusController:
    def __init__(self): ...
    
    def addOneOffTask(self, s: str, b: bool) -> None: ...
    
    def addStatusListener(self, s: str) -> None: ...
    
    def addTask(self, s: str, b: bool, b2: bool, i: int, i2: int, b3: bool, i3: int, b4: bool) -> None: ...
    
    def getItemLinkStatus(self, s: str) -> str: ...
    
    def getSignupStatus(self) -> str: ...
    
    def refreshAccountsList(self, callable: Callable) -> None: ...
    
    def removeStatusListener(self, s: str) -> None: ...
    
    def removeTask(self, s: str) -> None: ...
    
    def setItemLinkStatus(self, s: str, s2: str) -> bool: ...
    
    
    class ItemLinkStatus:
        needsLinking = 'needsLinking'
        ok = 'ok'
        unknown = 'unknown'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    class StatusListener:
        def __init__(self): ...
        
        def licenseStatusUpdated(self, s: str, s2: str) -> None: ...
        
        
    class TaskRunner:
        def __init__(self): ...
        
        def runTask(self, s: str, s2: str) -> None: ...
        
        
    
class MDPlusController$StatusListener:
    def __init__(self): ...
    
    def licenseStatusUpdated(self, s: str, s2: str) -> None: ...
    
    
class MDPlusSettingsWindow(SecondaryFrame, MDPlusController$StatusListener):
    pass
    
class MDSounds:
    CASH_REGISTER = u'cash_register.wav'
    
    def __init__(self): ...
    
    def playSound(self, s: str) -> bool: ...
    
    
class MDStrings:
    BUDGETS = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.BUDGETS at 0xbe>'
    CATEGORIES = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.CATEGORIES at 0xbf>'
    EXPENSE_CAT = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.EXPENSE_CAT at 0xc0>'
    GRAPHS = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.GRAPHS at 0xc1>'
    INCOME_CAT = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.INCOME_CAT at 0xc2>'
    LLIDP = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.LLIDP at 0xc3>'
    LT_cap_gains = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.LT_cap_gains at 0xc4>'
    MT_cap_gains = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.MT_cap_gains at 0xc5>'
    REPGRAPHS = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.REPGRAPHS at 0xc6>'
    REPORTS = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.REPORTS at 0xc7>'
    ST_cap_gains = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ST_cap_gains at 0xc8>'
    TRANSFERS_IN = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.TRANSFERS_IN at 0xc9>'
    TRANSFERS_OUT = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.TRANSFERS_OUT at 0xca>'
    _continue = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings._continue at 0xcb>'
    _default = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings._default at 0xcc>'
    _import = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings._import at 0xcd>'
    _new = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings._new at 0xce>'
    a_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.a_s at 0xcf>'
    a_s_every = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.a_s_every at 0xd0>'
    a_s_question = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.a_s_question at 0xd1>'
    about_html = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.about_html at 0xd2>'
    about_moneydance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.about_moneydance at 0xd3>'
    about_trans = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.about_trans at 0xd4>'
    accept_all_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accept_all_txns at 0xd5>'
    accept_oltxn_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accept_oltxn_label at 0xd6>'
    accept_oltxns_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accept_oltxns_label at 0xd7>'
    accept_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accept_txn at 0xd8>'
    account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account at 0xd9>'
    account_book_already_exists = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_book_already_exists at 0xda>'
    account_book_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_book_name at 0xdb>'
    account_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_description at 0xdc>'
    account_details = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_details at 0xdd>'
    account_info_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_info_title at 0xde>'
    account_is_inactive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_is_inactive at 0xdf>'
    account_map_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_map_desc at 0xe0>'
    account_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_name at 0xe1>'
    account_number = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_number at 0xe2>'
    account_sets = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_sets at 0xe3>'
    account_specific_settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_specific_settings at 0xe4>'
    account_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_type at 0xe5>'
    account_type_Investment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_type_Investment at 0xe6>'
    account_type_bank = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_type_bank at 0xe7>'
    account_type_expense = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_type_expense at 0xe8>'
    account_type_income = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_type_income at 0xe9>'
    account_url = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.account_url at 0xea>'
    accountfilter_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accountfilter_all at 0xeb>'
    accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accounts at 0xec>'
    accountselect_accountnotfound = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.accountselect_accountnotfound at 0xed>'
    acct_book_delete_confirmation = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_book_delete_confirmation at 0xee>'
    acct_book_delete_failed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_book_delete_failed at 0xef>'
    acct_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_list at 0xf0>'
    acct_num_with_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_num_with_payee at 0xf1>'
    acct_type0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type0 at 0xf2>'
    acct_type0S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type0S at 0xf3>'
    acct_type0s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type0s at 0xf4>'
    acct_type1000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type1000 at 0xf5>'
    acct_type10000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type10000 at 0xf6>'
    acct_type10000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type10000S at 0xf7>'
    acct_type10000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type10000s at 0xf8>'
    acct_type1000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type1000S at 0xf9>'
    acct_type1000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type1000s at 0xfa>'
    acct_type2000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type2000 at 0xfb>'
    acct_type2000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type2000S at 0xfc>'
    acct_type2000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type2000s at 0xfd>'
    acct_type3000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type3000 at 0xfe>'
    acct_type3000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type3000S at 0xff>'
    acct_type3000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type3000s at 0x100>'
    acct_type4000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4000 at 0x101>'
    acct_type4000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4000S at 0x102>'
    acct_type4000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4000s at 0x103>'
    acct_type4300 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4300 at 0x104>'
    acct_type4300S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4300S at 0x105>'
    acct_type4300s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4300s at 0x106>'
    acct_type4600 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4600 at 0x107>'
    acct_type4600S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4600S at 0x108>'
    acct_type4600s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type4600s at 0x109>'
    acct_type5000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type5000 at 0x10a>'
    acct_type5000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type5000S at 0x10b>'
    acct_type5000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type5000s at 0x10c>'
    acct_type6000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type6000 at 0x10d>'
    acct_type6000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type6000S at 0x10e>'
    acct_type6000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type6000s at 0x10f>'
    acct_type7000 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type7000 at 0x110>'
    acct_type7000S = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type7000S at 0x111>'
    acct_type7000s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_type7000s at 0x112>'
    acct_types_to_include = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_types_to_include at 0x113>'
    acct_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.acct_value at 0x114>'
    action_menu = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.action_menu at 0x115>'
    add = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add at 0x116>'
    add___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add___ at 0x117>'
    add_attachment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_attachment at 0x118>'
    add_ext_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_ext_desc at 0x119>'
    add_from_file___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_from_file___ at 0x11a>'
    add_module = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_module at 0x11b>'
    add_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_payee at 0x11c>'
    add_payee_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_payee_header at 0x11d>'
    add_payee_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_payee_title at 0x11e>'
    add_payment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_payment at 0x11f>'
    add_sidebar_dlg_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_sidebar_dlg_title at 0x120>'
    add_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.add_to at 0x121>'
    additional_olb_info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.additional_olb_info at 0x122>'
    addr_sel_tooltip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.addr_sel_tooltip at 0x123>'
    address = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.address at 0x124>'
    address1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.address1 at 0x125>'
    address2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.address2 at 0x126>'
    adjust_local_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.adjust_local_amount at 0x127>'
    adjust_other_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.adjust_other_amount at 0x128>'
    adjust_vat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.adjust_vat at 0x129>'
    advanced_search = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.advanced_search at 0x12a>'
    aes128_crypto_option = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.aes128_crypto_option at 0x12b>'
    agree = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.agree at 0x12c>'
    allOutOfDate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.allOutOfDate at 0x12d>'
    all_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_accounts at 0x12e>'
    all_accts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_accts at 0x12f>'
    all_categories = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_categories at 0x130>'
    all_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_checks at 0x131>'
    all_dates = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_dates at 0x132>'
    all_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_expenses at 0x133>'
    all_fields = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_fields at 0x134>'
    all_securities = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.all_securities at 0x135>'
    allocated_too_many_shares = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.allocated_too_many_shares at 0x136>'
    already_changed_pin = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.already_changed_pin at 0x137>'
    alternatives = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.alternatives at 0x138>'
    amex = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.amex at 0x139>'
    amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.amount at 0x13a>'
    amt_borrowed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.amt_borrowed at 0x13b>'
    any_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.any_acct at 0x13c>'
    any_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.any_category at 0x13d>'
    apply = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apply at 0x13e>'
    apply_dates = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apply_dates at 0x13f>'
    apply_vat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apply_vat at 0x140>'
    apr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apr at 0x141>'
    apr_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apr_rate at 0x142>'
    apr_then = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apr_then at 0x143>'
    apr_until = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.apr_until at 0x144>'
    april = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.april at 0x145>'
    archive___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archive___ at 0x146>'
    archive_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archive_error at 0x147>'
    archive_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archive_file at 0x148>'
    archive_only_clrd = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archive_only_clrd at 0x149>'
    archive_only_remove_cleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archive_only_remove_cleared at 0x14a>'
    archive_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archive_txns at 0x14b>'
    archiving_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.archiving_data at 0x14c>'
    as_downloaded_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.as_downloaded_txn at 0x14d>'
    as_downloaded_txn_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.as_downloaded_txn_description at 0x14e>'
    as_of = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.as_of at 0x14f>'
    ask_delete_cleared_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ask_delete_cleared_txn at 0x150>'
    ask_save_cleared_other = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ask_save_cleared_other at 0x151>'
    ask_save_cleared_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ask_save_cleared_txn at 0x152>'
    ask_save_cleared_xfer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ask_save_cleared_xfer at 0x153>'
    attachment_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.attachment_error at 0x154>'
    attachments = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.attachments at 0x155>'
    august = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.august at 0x156>'
    authenticated_proxy = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.authenticated_proxy at 0x157>'
    autoRollUp_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.autoRollUp_text at 0x158>'
    auto_matchmerge_downloaded_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.auto_matchmerge_downloaded_txns at 0x159>'
    auto_merge_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.auto_merge_txns at 0x15a>'
    autosave_option_auto = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.autosave_option_auto at 0x15b>'
    autosave_option_onexit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.autosave_option_onexit at 0x15c>'
    autosync_pref = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.autosync_pref at 0x15d>'
    avail_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.avail_items at 0x15e>'
    available_extensions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.available_extensions at 0x15f>'
    avg_cost = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.avg_cost at 0x160>'
    back = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.back at 0x161>'
    backing_up = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.backing_up at 0x162>'
    backup_loc_in_root_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.backup_loc_in_root_err at 0x163>'
    backup_loc_not_folder_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.backup_loc_not_folder_err at 0x164>'
    backup_loc_not_writable_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.backup_loc_not_writable_err at 0x165>'
    bad_addr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_addr at 0x166>'
    bad_anwp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_anwp at 0x167>'
    bad_country = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_country at 0x168>'
    bad_field_0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_field_0 at 0x169>'
    bad_field_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_field_1 at 0x16a>'
    bad_field_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_field_2 at 0x16b>'
    bad_field_3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_field_3 at 0x16c>'
    bad_field_4 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_field_4 at 0x16d>'
    bad_format_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_format_file at 0x16e>'
    bad_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_memo at 0x16f>'
    bad_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_name at 0x170>'
    bad_password = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_password at 0x171>'
    bad_payeeID = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_payeeID at 0x172>'
    bad_phone = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_phone at 0x173>'
    bad_state = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_state at 0x174>'
    bad_zip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bad_zip at 0x175>'
    balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.balance at 0x176>'
    balance_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.balance_type at 0x177>'
    bank_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bank_account at 0x178>'
    bank_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bank_name at 0x179>'
    base_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.base_currency at 0x17a>'
    batch_change = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_change at 0x17b>'
    batch_change_txns_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_change_txns_msg at 0x17c>'
    batch_date_increment_days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_date_increment_days at 0x17d>'
    batch_date_increment_months = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_date_increment_months at 0x17e>'
    batch_date_increment_years = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_date_increment_years at 0x17f>'
    batch_date_set = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_date_set at 0x180>'
    batch_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.batch_msg at 0x181>'
    bdgt_acct_item_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_acct_item_desc at 0x182>'
    bdgt_active = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_active at 0x183>'
    bdgt_actual = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_actual at 0x184>'
    bdgt_actual_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_actual_s at 0x185>'
    bdgt_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_all at 0x186>'
    bdgt_amt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_amt at 0x187>'
    bdgt_amt_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_amt_s at 0x188>'
    bdgt_calc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_calc at 0x189>'
    bdgt_calc_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_calc_desc at 0x18a>'
    bdgt_calc_nodates = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_calc_nodates at 0x18b>'
    bdgt_class = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_class at 0x18c>'
    bdgt_class_d = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_class_d at 0x18d>'
    bdgt_class_i = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_class_i at 0x18e>'
    bdgt_class_m = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_class_m at 0x18f>'
    bdgt_class_r = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_class_r at 0x190>'
    bdgt_conflict_0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_conflict_0 at 0x191>'
    bdgt_conflict_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_conflict_1 at 0x192>'
    bdgt_diff = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_diff at 0x193>'
    bdgt_diff_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_diff_s at 0x194>'
    bdgt_effective_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_effective_date at 0x195>'
    bdgt_from = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_from at 0x196>'
    bdgt_int_m = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_int_m at 0x197>'
    bdgt_int_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_int_q at 0x198>'
    bdgt_int_w = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_int_w at 0x199>'
    bdgt_int_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_int_y at 0x19a>'
    bdgt_item_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_item_desc at 0x19b>'
    bdgt_item_desc_wsubcats = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_item_desc_wsubcats at 0x19c>'
    bdgt_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_name at 0x19d>'
    bdgt_per_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_per_acct at 0x19e>'
    bdgt_prorated_amt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_prorated_amt at 0x19f>'
    bdgt_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_title at 0x1a0>'
    bdgt_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgt_to at 0x1a1>'
    bdgti_annually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_annually at 0x1a2>'
    bdgti_bimonthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_bimonthly at 0x1a3>'
    bdgti_biweekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_biweekly at 0x1a4>'
    bdgti_daily = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_daily at 0x1a5>'
    bdgti_interval = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_interval at 0x1a6>'
    bdgti_monthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_monthly at 0x1a7>'
    bdgti_norepeat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_norepeat at 0x1a8>'
    bdgti_once_annually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_annually at 0x1a9>'
    bdgti_once_bimonthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_bimonthly at 0x1aa>'
    bdgti_once_biweekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_biweekly at 0x1ab>'
    bdgti_once_monthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_monthly at 0x1ac>'
    bdgti_once_semiannually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_semiannually at 0x1ad>'
    bdgti_once_semimonthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_semimonthly at 0x1ae>'
    bdgti_once_trimonthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_trimonthly at 0x1af>'
    bdgti_once_triweekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_triweekly at 0x1b0>'
    bdgti_once_weekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_once_weekly at 0x1b1>'
    bdgti_semiannually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_semiannually at 0x1b2>'
    bdgti_semimonthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_semimonthly at 0x1b3>'
    bdgti_trimonthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_trimonthly at 0x1b4>'
    bdgti_triweekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_triweekly at 0x1b5>'
    bdgti_weekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bdgti_weekly at 0x1b6>'
    beep_on_txn_change = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.beep_on_txn_change at 0x1b7>'
    beg_for_review = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.beg_for_review at 0x1b8>'
    between_dates_x_and_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.between_dates_x_and_y at 0x1b9>'
    biller_ref_info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.biller_ref_info at 0x1ba>'
    bluLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bluLabel at 0x1bb>'
    bondSubType_corp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bondSubType_corp at 0x1bc>'
    bondSubType_junk = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bondSubType_junk at 0x1bd>'
    bondSubType_muni = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bondSubType_muni at 0x1be>'
    bondSubType_revenue = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bondSubType_revenue at 0x1bf>'
    bond_broker = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bond_broker at 0x1c0>'
    bond_coupon = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bond_coupon at 0x1c1>'
    bond_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bond_type at 0x1c2>'
    bp_acct_bankbranch = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_bankbranch at 0x1c3>'
    bp_acct_bankcity = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_bankcity at 0x1c4>'
    bp_acct_bankname = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_bankname at 0x1c5>'
    bp_acct_bankpostal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_bankpostal at 0x1c6>'
    bp_acct_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_id at 0x1c7>'
    bp_acct_key = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_key at 0x1c8>'
    bp_acct_pttacctid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_pttacctid at 0x1c9>'
    bp_acct_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_acct_type at 0x1ca>'
    bp_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_amount at 0x1cb>'
    bp_bankid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_bankid at 0x1cc>'
    bp_branch_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_branch_id at 0x1cd>'
    bp_cust_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_cust_acct at 0x1ce>'
    bp_dt_due = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_dt_due at 0x1cf>'
    bp_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_memo at 0x1d0>'
    bp_payee_addr1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_addr1 at 0x1d1>'
    bp_payee_addr2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_addr2 at 0x1d2>'
    bp_payee_addr3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_addr3 at 0x1d3>'
    bp_payee_city = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_city at 0x1d4>'
    bp_payee_country = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_country at 0x1d5>'
    bp_payee_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_name at 0x1d6>'
    bp_payee_phone = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_phone at 0x1d7>'
    bp_payee_postal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_postal at 0x1d8>'
    bp_payee_state = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bp_payee_state at 0x1d9>'
    bpto_bank_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bpto_bank_acct at 0x1da>'
    bpto_newpayee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bpto_newpayee at 0x1db>'
    bpto_predefpayee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bpto_predefpayee at 0x1dc>'
    browse_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.browse_files at 0x1dd>'
    budget = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget at 0x1de>'
    budgetAmountTip_format = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budgetAmountTip_format at 0x1df>'
    budget_already_exists = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_already_exists at 0x1e0>'
    budget_class = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_class at 0x1e1>'
    budget_copy_and_rollover_prev_period = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_copy_and_rollover_prev_period at 0x1e2>'
    budget_copy_prev_period = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_copy_prev_period at 0x1e3>'
    budget_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_item at 0x1e4>'
    budget_list_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_list_win_title at 0x1e5>'
    budget_tip_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_tip_title at 0x1e6>'
    budget_use_prev_actual = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budget_use_prev_actual at 0x1e7>'
    budgets = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budgets at 0x1e8>'
    budgets___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.budgets___ at 0x1e9>'
    build = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.build at 0x1ea>'
    buy_now = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.buy_now at 0x1eb>'
    buy_upgrade = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.buy_upgrade at 0x1ec>'
    by_inv_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.by_inv_acct at 0x1ed>'
    by_sec = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.by_sec at 0x1ee>'
    bytes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.bytes at 0x1ef>'
    cal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cal at 0x1f0>'
    calc_budget = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.calc_budget at 0x1f1>'
    calc_expl_html = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.calc_expl_html at 0x1f2>'
    calculate_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.calculate_pmt at 0x1f3>'
    calibrate_printer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.calibrate_printer at 0x1f4>'
    calibrate_printer_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.calibrate_printer_title at 0x1f5>'
    call = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.call at 0x1f6>'
    cancel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cancel at 0x1f7>'
    cancel_payment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cancel_payment at 0x1f8>'
    cancel_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cancel_txn at 0x1f9>'
    canceled = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.canceled at 0x1fa>'
    cannot_open_book_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cannot_open_book_file at 0x1fb>'
    cannot_remove_currency1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cannot_remove_currency1 at 0x1fc>'
    cannot_remove_currency2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cannot_remove_currency2 at 0x1fd>'
    cant_delete_nonempty_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cant_delete_nonempty_acct at 0x1fe>'
    cant_delete_root_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cant_delete_root_acct at 0x1ff>'
    cant_edit_splits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cant_edit_splits at 0x200>'
    casestv_ac = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.casestv_ac at 0x201>'
    cash = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cash at 0x202>'
    cashflow_dest = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cashflow_dest at 0x203>'
    cashflow_source = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cashflow_source at 0x204>'
    categories = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.categories at 0x205>'
    category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.category at 0x206>'
    category_info_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.category_info_title at 0x207>'
    category_is_inactive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.category_is_inactive at 0x208>'
    category_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.category_list at 0x209>'
    category_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.category_name at 0x20a>'
    catsHelp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.catsHelp at 0x20b>'
    catsHelpSelected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.catsHelpSelected at 0x20c>'
    catsLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.catsLabel at 0x20d>'
    cc_exp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cc_exp at 0x20e>'
    cc_start_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cc_start_bal at 0x20f>'
    ccard_number = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ccard_number at 0x210>'
    cdSubType_broker = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_broker at 0x211>'
    cdSubType_bumpup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_bumpup at 0x212>'
    cdSubType_callable = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_callable at 0x213>'
    cdSubType_fixed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_fixed at 0x214>'
    cdSubType_liquid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_liquid at 0x215>'
    cdSubType_variable = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_variable at 0x216>'
    cdSubType_zerocoupon = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cdSubType_zerocoupon at 0x217>'
    cd_apr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cd_apr at 0x218>'
    cd_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cd_name at 0x219>'
    cd_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cd_price at 0x21a>'
    certificate_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.certificate_error at 0x21b>'
    changelog_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.changelog_title at 0x21c>'
    check_for_updates = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_for_updates at 0x21d>'
    check_for_updates_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_for_updates_q at 0x21e>'
    check_num_nextnum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_nextnum at 0x21f>'
    check_num_printnum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_printnum at 0x220>'
    check_num_settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_settings at 0x221>'
    check_num_settings_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_settings_label at 0x222>'
    check_num_settings_show_nextnum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_settings_show_nextnum at 0x223>'
    check_num_settings_show_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_settings_show_print at 0x224>'
    check_num_settings_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_settings_title at 0x225>'
    check_num_tags = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_num_tags at 0x226>'
    check_on_startup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_on_startup at 0x227>'
    check_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_type at 0x228>'
    check_version_at_startup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_version_at_startup at 0x229>'
    check_versions_ext = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.check_versions_ext at 0x22a>'
    checknums_recents = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checknums_recents at 0x22b>'
    checknums_recents_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checknums_recents_all at 0x22c>'
    checknums_recents_from_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checknums_recents_from_account at 0x22d>'
    checknums_recents_max = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checknums_recents_max at 0x22e>'
    checknums_recents_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checknums_recents_none at 0x22f>'
    checks_on_1st_page = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checks_on_1st_page at 0x230>'
    checks_per_page = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checks_per_page at 0x231>'
    checks_through_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checks_through_date at 0x232>'
    checks_with_stubs = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.checks_with_stubs at 0x233>'
    chg_curr_msg1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chg_curr_msg1 at 0x234>'
    chg_pin_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chg_pin_win_title at 0x235>'
    chknum_atm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_atm at 0x236>'
    chknum_buy = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_buy at 0x237>'
    chknum_buyx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_buyx at 0x238>'
    chknum_ckcard = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_ckcard at 0x239>'
    chknum_dep = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_dep at 0x23a>'
    chknum_nextchecknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_nextchecknum at 0x23b>'
    chknum_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_print at 0x23c>'
    chknum_sell = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_sell at 0x23d>'
    chknum_sellx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_sellx at 0x23e>'
    chknum_split = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_split at 0x23f>'
    chknum_transfer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.chknum_transfer at 0x240>'
    choose_acct_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_acct_file_title at 0x241>'
    choose_archive_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_archive_file_title at 0x242>'
    choose_documents_dir = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_documents_dir at 0x243>'
    choose_exp_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_exp_file_title at 0x244>'
    choose_ext_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_ext_file at 0x245>'
    choose_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_file at 0x246>'
    choose_folder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_folder at 0x247>'
    choose_graph_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_graph_file_title at 0x248>'
    choose_import_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_import_file at 0x249>'
    choose_location = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_location at 0x24a>'
    choose_moneydance_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_moneydance_file at 0x24b>'
    choose_ofx_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_ofx_file_title at 0x24c>'
    choose_ol_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_ol_account at 0x24d>'
    choose_png_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_png_file at 0x24e>'
    choose_qem_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_qem_file at 0x24f>'
    choose_qif_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_qif_file_title at 0x250>'
    choose_report_file_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_report_file_title at 0x251>'
    choose_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.choose_security at 0x252>'
    city = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.city at 0x253>'
    clear = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.clear at 0x254>'
    clear_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.clear_all at 0x255>'
    clear_all_auth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.clear_all_auth at 0x256>'
    clear_menu = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.clear_menu at 0x257>'
    cleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cleared at 0x258>'
    cleared_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cleared_balance at 0x259>'
    click2update = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.click2update at 0x25a>'
    click_to_select_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.click_to_select_account at 0x25b>'
    close = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.close at 0x25c>'
    close_edit_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.close_edit_script at 0x25d>'
    closing_and_syncing_changes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.closing_and_syncing_changes at 0x25e>'
    coa = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.coa at 0x25f>'
    colorSelect_hueTip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.colorSelect_hueTip at 0x260>'
    colorSelect_lumTip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.colorSelect_lumTip at 0x261>'
    colorSelect_satTip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.colorSelect_satTip at 0x262>'
    color_accountIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_accountIconTint at 0x263>'
    color_budgetAcceptableColor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_budgetAcceptableColor at 0x264>'
    color_budgetAlertColor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_budgetAlertColor at 0x265>'
    color_budgetGraphWarning = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_budgetGraphWarning at 0x266>'
    color_budgetHealthyColor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_budgetHealthyColor at 0x267>'
    color_budgetIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_budgetIconTint at 0x268>'
    color_calEventBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_calEventBG at 0x269>'
    color_calPastEventBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_calPastEventBG at 0x26a>'
    color_dashboardFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_dashboardFG at 0x26b>'
    color_defaultBackground = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_defaultBackground at 0x26c>'
    color_defaultTextForeground = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_defaultTextForeground at 0x26d>'
    color_errorMessageForeground = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_errorMessageForeground at 0x26e>'
    color_expenseIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_expenseIconTint at 0x26f>'
    color_filterBarBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_filterBarBG at 0x270>'
    color_filterBarBtnBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_filterBarBtnBG at 0x271>'
    color_filterBarFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_filterBarFG at 0x272>'
    color_filterBarSelBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_filterBarSelBG at 0x273>'
    color_filterBarSelFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_filterBarSelFG at 0x274>'
    color_filterBarShadow = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_filterBarShadow at 0x275>'
    color_futureTxn2BG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_futureTxn2BG at 0x276>'
    color_futureTxnBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_futureTxnBG at 0x277>'
    color_futureTxnIndicator = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_futureTxnIndicator at 0x278>'
    color_graphBG1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphBG1 at 0x279>'
    color_graphBG2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphBG2 at 0x27a>'
    color_graphData1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData1 at 0x27b>'
    color_graphData10 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData10 at 0x27c>'
    color_graphData11 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData11 at 0x27d>'
    color_graphData12 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData12 at 0x27e>'
    color_graphData13 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData13 at 0x27f>'
    color_graphData14 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData14 at 0x280>'
    color_graphData15 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData15 at 0x281>'
    color_graphData16 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData16 at 0x282>'
    color_graphData17 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData17 at 0x283>'
    color_graphData18 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData18 at 0x284>'
    color_graphData19 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData19 at 0x285>'
    color_graphData2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData2 at 0x286>'
    color_graphData20 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData20 at 0x287>'
    color_graphData21 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData21 at 0x288>'
    color_graphData22 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData22 at 0x289>'
    color_graphData23 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData23 at 0x28a>'
    color_graphData3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData3 at 0x28b>'
    color_graphData4 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData4 at 0x28c>'
    color_graphData5 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData5 at 0x28d>'
    color_graphData6 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData6 at 0x28e>'
    color_graphData7 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData7 at 0x28f>'
    color_graphData8 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData8 at 0x290>'
    color_graphData9 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphData9 at 0x291>'
    color_graphIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_graphIconTint at 0x292>'
    color_headerBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_headerBG at 0x293>'
    color_headerBG1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_headerBG1 at 0x294>'
    color_headerBG2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_headerBG2 at 0x295>'
    color_headerBorder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_headerBorder at 0x296>'
    color_headerFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_headerFG at 0x297>'
    color_homeIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_homeIconTint at 0x298>'
    color_homePageAltBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_homePageAltBG at 0x299>'
    color_homePageBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_homePageBG at 0x29a>'
    color_homePageFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_homePageFG at 0x29b>'
    color_homepageSectionBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_homepageSectionBG at 0x29c>'
    color_hudBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_hudBG at 0x29d>'
    color_hudBG1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_hudBG1 at 0x29e>'
    color_hudBG2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_hudBG2 at 0x29f>'
    color_hudBorderColor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_hudBorderColor at 0x2a0>'
    color_hudFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_hudFG at 0x2a1>'
    color_incomeIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_incomeIconTint at 0x2a2>'
    color_listBackground = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_listBackground at 0x2a3>'
    color_listSelectioBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_listSelectioBG at 0x2a4>'
    color_mainDivider = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_mainDivider at 0x2a5>'
    color_mainPanelBorderColor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_mainPanelBorderColor at 0x2a6>'
    color_negativeBalFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_negativeBalFG at 0x2a7>'
    color_popoverBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_popoverBG at 0x2a8>'
    color_popoverBorder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_popoverBorder at 0x2a9>'
    color_popoverTriangleBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_popoverTriangleBG at 0x2aa>'
    color_positiveBalFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_positiveBalFG at 0x2ab>'
    color_registerBG1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerBG1 at 0x2ac>'
    color_registerBG2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerBG2 at 0x2ad>'
    color_registerGrid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerGrid at 0x2ae>'
    color_registerSelectedBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerSelectedBG at 0x2af>'
    color_registerSelectedFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerSelectedFG at 0x2b0>'
    color_registerTextFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerTextFG at 0x2b1>'
    color_registerUnconfirmedIconFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerUnconfirmedIconFG at 0x2b2>'
    color_registerUnfocusedSelectedBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_registerUnfocusedSelectedBG at 0x2b3>'
    color_reminderHomeInnerLine = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_reminderHomeInnerLine at 0x2b4>'
    color_reminderIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_reminderIconTint at 0x2b5>'
    color_reportBlueFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_reportBlueFG at 0x2b6>'
    color_reportIconTint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_reportIconTint at 0x2b7>'
    color_reportRedFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_reportRedFG at 0x2b8>'
    color_scrollThumb = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_scrollThumb at 0x2b9>'
    color_secondaryTextFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_secondaryTextFG at 0x2ba>'
    color_selectedRowGradient1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_selectedRowGradient1 at 0x2bb>'
    color_selectedRowGradient2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_selectedRowGradient2 at 0x2bc>'
    color_sidebarBackground = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarBackground at 0x2bd>'
    color_sidebarHeader = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarHeader at 0x2be>'
    color_sidebarNegativeBalanceFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarNegativeBalanceFG at 0x2bf>'
    color_sidebarPositiveBalanceFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarPositiveBalanceFG at 0x2c0>'
    color_sidebarSecondaryTextFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarSecondaryTextFG at 0x2c1>'
    color_sidebarSelectedBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarSelectedBG at 0x2c2>'
    color_sidebarSelectedFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarSelectedFG at 0x2c3>'
    color_sidebarUFSelectedBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_sidebarUFSelectedBG at 0x2c4>'
    color_tableHeaderBG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_tableHeaderBG at 0x2c5>'
    color_tertiaryTextFG = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_tertiaryTextFG at 0x2c6>'
    color_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.color_text at 0x2c7>'
    colorselect_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.colorselect_label at 0x2c8>'
    combine_criteria = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.combine_criteria at 0x2c9>'
    comm_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.comm_error at 0x2ca>'
    compounding = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.compounding at 0x2cb>'
    confirm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm at 0x2cc>'
    confirm_clear_snapshots = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_clear_snapshots at 0x2cd>'
    confirm_del_acct_book_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_acct_book_q at 0x2ce>'
    confirm_del_acct_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_acct_q at 0x2cf>'
    confirm_del_currencies = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_currencies at 0x2d0>'
    confirm_del_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_currency at 0x2d1>'
    confirm_del_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_payee at 0x2d2>'
    confirm_del_payment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_payment at 0x2d3>'
    confirm_del_securities = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_securities at 0x2d4>'
    confirm_del_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_security at 0x2d5>'
    confirm_del_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_del_tag at 0x2d6>'
    confirm_delete_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_delete_acct at 0x2d7>'
    confirm_delete_addrbkentry = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_delete_addrbkentry at 0x2d8>'
    confirm_delete_reminder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_delete_reminder at 0x2d9>'
    confirm_delete_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_delete_txn at 0x2da>'
    confirm_no_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_no_match at 0x2db>'
    confirm_pos_rec_cc_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_pos_rec_cc_bal at 0x2dc>'
    confirm_txn_changes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_txn_changes at 0x2dd>'
    confirm_yes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirm_yes at 0x2de>'
    confirmed_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.confirmed_balance at 0x2df>'
    conn_state_authorising = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.conn_state_authorising at 0x2e0>'
    conn_state_connected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.conn_state_connected at 0x2e1>'
    conn_state_connecting = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.conn_state_connecting at 0x2e2>'
    conn_state_disconnected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.conn_state_disconnected at 0x2e3>'
    console_window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.console_window at 0x2e4>'
    console_window_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.console_window_title at 0x2e5>'
    copied = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.copied at 0x2e6>'
    copy_mdplus_settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.copy_mdplus_settings at 0x2e7>'
    copy_of = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.copy_of at 0x2e8>'
    copy_to_clipboard = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.copy_to_clipboard at 0x2e9>'
    copyright = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.copyright at 0x2ea>'
    corp_bond = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.corp_bond at 0x2eb>'
    cost_basis = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cost_basis at 0x2ec>'
    cost_basis_invalid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cost_basis_invalid at 0x2ed>'
    cost_per_share = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cost_per_share at 0x2ee>'
    country = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.country at 0x2ef>'
    create = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create at 0x2f0>'
    create_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_acct at 0x2f1>'
    create_cat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_cat at 0x2f2>'
    create_extension = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_extension at 0x2f3>'
    create_init_tfr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_init_tfr at 0x2f4>'
    create_loan_rem = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_loan_rem at 0x2f5>'
    create_new_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_new_file at 0x2f6>'
    create_new_file_expl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_new_file_expl at 0x2f7>'
    create_reminder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_reminder at 0x2f8>'
    create_sec = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_sec at 0x2f9>'
    create_txn_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_txn_tag at 0x2fa>'
    create_txn_tag_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_txn_tag_msg at 0x2fb>'
    create_watch_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.create_watch_list at 0x2fc>'
    credit_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.credit_amount at 0x2fd>'
    credit_limit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.credit_limit at 0x2fe>'
    credit_remaining = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.credit_remaining at 0x2ff>'
    crypto_level = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.crypto_level at 0x300>'
    cumulative = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cumulative at 0x301>'
    curr_del = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_del at 0x302>'
    curr_hist_download = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_hist_download at 0x303>'
    curr_hist_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_hist_title at 0x304>'
    curr_new = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_new at 0x305>'
    curr_splits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_splits at 0x306>'
    curr_type_curr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_type_curr at 0x307>'
    curr_type_sec = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.curr_type_sec at 0x308>'
    currencies = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currencies at 0x309>'
    currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency at 0x30a>'
    currency_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_id at 0x30b>'
    currency_id_exists_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_id_exists_msg at 0x30c>'
    currency_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_name at 0x30d>'
    currency_num_decimal_points = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_num_decimal_points at 0x30e>'
    currency_prefix = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_prefix at 0x30f>'
    currency_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_rate at 0x310>'
    currency_suffix = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_suffix at 0x311>'
    currency_ticker = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_ticker at 0x312>'
    currency_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.currency_type at 0x313>'
    current_period = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.current_period at 0x314>'
    custom = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.custom at 0x315>'
    custom_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.custom_date at 0x316>'
    customer_id_num = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.customer_id_num at 0x317>'
    customize_theme = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.customize_theme at 0x318>'
    cutoff_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.cutoff_date at 0x319>'
    date_due = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.date_due at 0x31a>'
    date_fmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.date_fmt at 0x31b>'
    date_format = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.date_format at 0x31c>'
    day = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.day at 0x31d>'
    day_headers = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.day_headers at 0x31e>'
    days_to_sync = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.days_to_sync at 0x31f>'
    db_blank = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.db_blank at 0x320>'
    db_budget_status = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.db_budget_status at 0x321>'
    db_networth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.db_networth at 0x322>'
    debit_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.debit_amount at 0x323>'
    debt_payment_clearedbal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.debt_payment_clearedbal at 0x324>'
    debt_payment_currentbal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.debt_payment_currentbal at 0x325>'
    debt_payment_fixed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.debt_payment_fixed at 0x326>'
    debt_payment_pctclearedbal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.debt_payment_pctclearedbal at 0x327>'
    debt_payment_pctcurrentbal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.debt_payment_pctcurrentbal at 0x328>'
    december = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.december at 0x329>'
    decimal_char = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.decimal_char at 0x32a>'
    decimal_point = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.decimal_point at 0x32b>'
    decimal_point_comma = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.decimal_point_comma at 0x32c>'
    decimal_point_dot = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.decimal_point_dot at 0x32d>'
    decrease = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.decrease at 0x32e>'
    default_account_book_names = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.default_account_book_names at 0x32f>'
    default_archive_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.default_archive_file at 0x330>'
    default_browser = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.default_browser at 0x331>'
    default_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.default_category at 0x332>'
    default_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.default_currency at 0x333>'
    default_new_budget_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.default_new_budget_name at 0x334>'
    deflt_chknum_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.deflt_chknum_list at 0x335>'
    del_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.del_msg at 0x336>'
    del_reminder_ques = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.del_reminder_ques at 0x337>'
    del_sec_txt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.del_sec_txt at 0x338>'
    del_sec_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.del_sec_win at 0x339>'
    del_sel_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.del_sel_txns at 0x33a>'
    del_splits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.del_splits at 0x33b>'
    delete = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete at 0x33c>'
    delete___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete___ at 0x33d>'
    delete_acct___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_acct___ at 0x33e>'
    delete_attachment_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_attachment_message at 0x33f>'
    delete_attachment_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_attachment_title at 0x340>'
    delete_book___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_book___ at 0x341>'
    delete_budget_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_budget_q at 0x342>'
    delete_mem_report_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_mem_report_q at 0x343>'
    delete_split = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_split at 0x344>'
    delete_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_txn at 0x345>'
    delete_txns_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.delete_txns_q at 0x346>'
    des_crypto_option = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.des_crypto_option at 0x347>'
    desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.desc at 0x348>'
    desc_memo_same_line = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.desc_memo_same_line at 0x349>'
    destination_of_funds = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.destination_of_funds at 0x34a>'
    did_save_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.did_save_data at 0x34b>'
    diff_bet_expenses_income = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.diff_bet_expenses_income at 0x34c>'
    disagree = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.disagree at 0x34d>'
    discounted_update_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.discounted_update_msg at 0x34e>'
    div_inc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.div_inc at 0x34f>'
    dividend = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dividend at 0x350>'
    dling_fi_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dling_fi_list at 0x351>'
    dling_from = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dling_from at 0x352>'
    dling_module = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dling_module at 0x353>'
    dling_versions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dling_versions at 0x354>'
    done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.done at 0x355>'
    dont_adjust_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dont_adjust_rate at 0x356>'
    dont_bother = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dont_bother at 0x357>'
    dont_download = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dont_download at 0x358>'
    dont_repeat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dont_repeat at 0x359>'
    down = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.down at 0x35a>'
    download = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download at 0x35b>'
    download___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download___ at 0x35c>'
    download_all_available = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_all_available at 0x35d>'
    download_ext_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_ext_error at 0x35e>'
    download_from_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_from_x at 0x35f>'
    download_history_length_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_history_length_msg at 0x360>'
    download_history_length_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_history_length_title at 0x361>'
    download_sync_reset_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_sync_reset_msg at 0x362>'
    download_txns_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.download_txns_for_acct at 0x363>'
    downloaded_n_txns_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.downloaded_n_txns_for_acct at 0x364>'
    downloaded_one_txn_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.downloaded_one_txn_for_acct at 0x365>'
    downloaded_zero_txns_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.downloaded_zero_txns_for_acct at 0x366>'
    downloading_acct_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.downloading_acct_x at 0x367>'
    downloading_all_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.downloading_all_done at 0x368>'
    downloading_extension_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.downloading_extension_list at 0x369>'
    dropbox = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox at 0x36a>'
    dropbox_auth_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_auth_err at 0x36b>'
    dropbox_auth_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_auth_msg at 0x36c>'
    dropbox_auth_wait_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_auth_wait_msg at 0x36d>'
    dropbox_authorize = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_authorize at 0x36e>'
    dropbox_connect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_connect at 0x36f>'
    dropbox_disconnect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_disconnect at 0x370>'
    dropbox_login = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_login at 0x371>'
    dropbox_syncing = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropbox_syncing at 0x372>'
    dropboxapi_sync_instructions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropboxapi_sync_instructions at 0x373>'
    dropboxfolder_sync_instructions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.dropboxfolder_sync_instructions at 0x374>'
    duplicate_chknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.duplicate_chknum at 0x375>'
    duplicate_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.duplicate_txn at 0x376>'
    edit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit at 0x377>'
    edit___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit___ at 0x378>'
    edit_acct___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_acct___ at 0x379>'
    edit_budget_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_budget_win_title at 0x37a>'
    edit_copy = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_copy at 0x37b>'
    edit_currencies___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_currencies___ at 0x37c>'
    edit_currency_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_currency_win_title at 0x37d>'
    edit_custom_filter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_custom_filter at 0x37e>'
    edit_cut = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_cut at 0x37f>'
    edit_history = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_history at 0x380>'
    edit_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_list at 0x381>'
    edit_lots = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_lots at 0x382>'
    edit_paste = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_paste at 0x383>'
    edit_payee_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_payee_title at 0x384>'
    edit_payment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_payment at 0x385>'
    edit_payment_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_payment_title at 0x386>'
    edit_reminders_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_reminders_win_title at 0x387>'
    edit_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_script at 0x388>'
    edit_securities___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_securities___ at 0x389>'
    edit_securities_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_securities_win_title at 0x38a>'
    edit_select_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_select_all at 0x38b>'
    edit_them_overwrite_warning = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_them_overwrite_warning at 0x38c>'
    edit_theme = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_theme at 0x38d>'
    edit_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_txn at 0x38e>'
    edit_txn_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_txn_tag at 0x38f>'
    edit_txn_tag_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_txn_tag_msg at 0x390>'
    edit_txn_tag_prompt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_txn_tag_prompt at 0x391>'
    edit_txn_tags = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edit_txn_tags at 0x392>'
    edited_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edited_txn at 0x393>'
    edited_txn_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.edited_txn_description at 0x394>'
    editlist_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.editlist_error at 0x395>'
    editlist_inuse_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.editlist_inuse_msg at 0x396>'
    editlist_prompt_fmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.editlist_prompt_fmt at 0x397>'
    editlist_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.editlist_title at 0x398>'
    email = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.email at 0x399>'
    email_address = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.email_address at 0x39a>'
    empty_currency_id_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.empty_currency_id_msg at 0x39b>'
    encrypt_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.encrypt_desc at 0x39c>'
    encrypt_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.encrypt_file at 0x39d>'
    encrypt_not_available = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.encrypt_not_available at 0x39e>'
    encryption___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.encryption___ at 0x39f>'
    encryption_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.encryption_error at 0x3a0>'
    enter_bp_acct_num = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_bp_acct_num at 0x3a1>'
    enter_budget_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_budget_name at 0x3a2>'
    enter_graph_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_graph_name at 0x3a3>'
    enter_license_key = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_license_key at 0x3a4>'
    enter_passwd = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_passwd at 0x3a5>'
    enter_passwd_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_passwd_desc at 0x3a6>'
    enter_rpt_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.enter_rpt_name at 0x3a7>'
    err_bad_mod_sig = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.err_bad_mod_sig at 0x3a8>'
    err_internal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.err_internal at 0x3a9>'
    err_save_graph = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.err_save_graph at 0x3aa>'
    err_save_report = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.err_save_report at 0x3ab>'
    err_unknown = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.err_unknown at 0x3ac>'
    error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error at 0x3ad>'
    error_backing_up_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_backing_up_file at 0x3ae>'
    error_checking_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_checking_version at 0x3af>'
    error_creating_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_creating_file at 0x3b0>'
    error_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_desc at 0x3b1>'
    error_during_download = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_during_download at 0x3b2>'
    error_getting_ext_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_getting_ext_list at 0x3b3>'
    error_loading_ext_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_loading_ext_file at 0x3b4>'
    error_loading_module = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_loading_module at 0x3b5>'
    error_loading_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_loading_msg at 0x3b6>'
    error_loading_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_loading_title at 0x3b7>'
    error_module_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_module_name at 0x3b8>'
    error_opening_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_opening_file at 0x3b9>'
    error_saving_currency_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_saving_currency_data at 0x3ba>'
    error_saving_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_saving_file at 0x3bb>'
    error_saving_theme = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_saving_theme at 0x3bc>'
    error_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.error_title at 0x3bd>'
    escrow = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.escrow at 0x3be>'
    escrow_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.escrow_acct at 0x3bf>'
    escrow_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.escrow_pmt at 0x3c0>'
    ex_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ex_month at 0x3c1>'
    exact_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exact_match at 0x3c2>'
    except_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.except_type at 0x3c3>'
    exchange_as = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_as at 0x3c4>'
    exchange_ase = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ase at 0x3c5>'
    exchange_ax = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ax at 0x3c6>'
    exchange_ba = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ba at 0x3c7>'
    exchange_bc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_bc at 0x3c8>'
    exchange_be = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_be at 0x3c9>'
    exchange_bi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_bi at 0x3ca>'
    exchange_bm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_bm at 0x3cb>'
    exchange_bo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_bo at 0x3cc>'
    exchange_cbt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_cbt at 0x3cd>'
    exchange_cme = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_cme at 0x3ce>'
    exchange_co = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_co at 0x3cf>'
    exchange_de = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_de at 0x3d0>'
    exchange_du = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_du at 0x3d1>'
    exchange_f = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_f at 0x3d2>'
    exchange_ha = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ha at 0x3d3>'
    exchange_hk = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_hk at 0x3d4>'
    exchange_hm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_hm at 0x3d5>'
    exchange_jk = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_jk at 0x3d6>'
    exchange_kq = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_kq at 0x3d7>'
    exchange_ks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ks at 0x3d8>'
    exchange_l = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_l at 0x3d9>'
    exchange_ma = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ma at 0x3da>'
    exchange_mc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_mc at 0x3db>'
    exchange_mf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_mf at 0x3dc>'
    exchange_mi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_mi at 0x3dd>'
    exchange_mu = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_mu at 0x3de>'
    exchange_mx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_mx at 0x3df>'
    exchange_nasdaq = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_nasdaq at 0x3e0>'
    exchange_ns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ns at 0x3e1>'
    exchange_nyb = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_nyb at 0x3e2>'
    exchange_nym = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_nym at 0x3e3>'
    exchange_nyse = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_nyse at 0x3e4>'
    exchange_nyx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_nyx at 0x3e5>'
    exchange_nz = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_nz at 0x3e6>'
    exchange_ol = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ol at 0x3e7>'
    exchange_otc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_otc at 0x3e8>'
    exchange_pa = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_pa at 0x3e9>'
    exchange_pk = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_pk at 0x3ea>'
    exchange_sa = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_sa at 0x3eb>'
    exchange_sg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_sg at 0x3ec>'
    exchange_si = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_si at 0x3ed>'
    exchange_ss = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ss at 0x3ee>'
    exchange_st = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_st at 0x3ef>'
    exchange_sw = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_sw at 0x3f0>'
    exchange_sz = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_sz at 0x3f1>'
    exchange_ta = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_ta at 0x3f2>'
    exchange_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_to at 0x3f3>'
    exchange_tw = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_tw at 0x3f4>'
    exchange_two = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_two at 0x3f5>'
    exchange_v = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_v at 0x3f6>'
    exchange_vi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exchange_vi at 0x3f7>'
    excluded_extension_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.excluded_extension_message at 0x3f8>'
    existing_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.existing_account at 0x3f9>'
    exp_vat_editor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exp_vat_editor at 0x3fa>'
    expense_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.expense_account at 0x3fb>'
    expenses_graph = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.expenses_graph at 0x3fc>'
    export_all_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.export_all_accounts at 0x3fd>'
    export_completed_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.export_completed_message at 0x3fe>'
    export_data___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.export_data___ at 0x3ff>'
    export_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.export_done at 0x400>'
    export_format = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.export_format at 0x401>'
    export_qif_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.export_qif_header at 0x402>'
    exporting_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.exporting_file at 0x403>'
    ext_bad_sig_warning = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_bad_sig_warning at 0x404>'
    ext_download = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_download at 0x405>'
    ext_download_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_download_desc at 0x406>'
    ext_downloading = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_downloading at 0x407>'
    ext_file_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_file_desc at 0x408>'
    ext_from_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_from_file at 0x409>'
    ext_info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_info at 0x40a>'
    ext_install = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_install at 0x40b>'
    ext_installed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_installed at 0x40c>'
    ext_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_name at 0x40d>'
    ext_selectdl_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_selectdl_desc at 0x40e>'
    ext_selectfile_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_selectfile_desc at 0x40f>'
    ext_src = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_src at 0x410>'
    ext_uninstall = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_uninstall at 0x411>'
    ext_upgrade = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ext_upgrade at 0x412>'
    external_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.external_files at 0x413>'
    face_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.face_value at 0x414>'
    fc_location = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fc_location at 0x415>'
    february = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.february at 0x416>'
    fewer_fields = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fewer_fields at 0x417>'
    fi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fi at 0x418>'
    fi_acct_assoc_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fi_acct_assoc_error at 0x419>'
    fi_refresh_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fi_refresh_err at 0x41a>'
    field_delimiter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.field_delimiter at 0x41b>'
    field_exp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.field_exp at 0x41c>'
    fifo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fifo at 0x41d>'
    file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.file at 0x41e>'
    file_encoding = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.file_encoding at 0x41f>'
    file_exists_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.file_exists_q at 0x420>'
    file_not_found = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.file_not_found at 0x421>'
    file_read_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.file_read_error at 0x422>'
    file_was_downloaded = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.file_was_downloaded at 0x423>'
    filter_by_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.filter_by_tag at 0x424>'
    filter_has_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.filter_has_tag at 0x425>'
    filter_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.filter_label at 0x426>'
    findAnd_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.findAnd_text at 0x427>'
    findCategoriesSelect_mnemonic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.findCategoriesSelect_mnemonic at 0x428>'
    findExact_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.findExact_text at 0x429>'
    findOr_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.findOr_text at 0x42a>'
    find___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.find___ at 0x42b>'
    find_again = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.find_again at 0x42c>'
    find_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.find_txn at 0x42d>'
    finding_syncable_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.finding_syncable_files at 0x42e>'
    finish = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.finish at 0x42f>'
    first_chk_num = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.first_chk_num at 0x430>'
    fiscal_year_start = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fiscal_year_start at 0x431>'
    fiscal_year_to_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fiscal_year_to_date at 0x432>'
    folder_sync_instructions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.folder_sync_instructions at 0x433>'
    font = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.font at 0x434>'
    font_size = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.font_size at 0x435>'
    foreign_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.foreign_amount at 0x436>'
    foreign_amt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.foreign_amt at 0x437>'
    format_commadel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_commadel at 0x438>'
    format_commadel_with_bom = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_commadel_with_bom at 0x439>'
    format_html = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_html at 0x43a>'
    format_md2008 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_md2008 at 0x43b>'
    format_md2010 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_md2010 at 0x43c>'
    format_qif = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_qif at 0x43d>'
    format_raw_json = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_raw_json at 0x43e>'
    format_tabdel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_tabdel at 0x43f>'
    format_xml = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.format_xml at 0x440>'
    forward = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.forward at 0x441>'
    found_syncable_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.found_syncable_files at 0x442>'
    free_update_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.free_update_msg at 0x443>'
    fri_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fri_s at 0x444>'
    from_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.from_acct at 0x445>'
    from_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.from_currency at 0x446>'
    from_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.from_file at 0x447>'
    from_ofx_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.from_ofx_file at 0x448>'
    from_qif_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.from_qif_file at 0x449>'
    from_txn_primacct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.from_txn_primacct at 0x44a>'
    fund_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.fund_name at 0x44b>'
    gen_graph = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.gen_graph at 0x44c>'
    gen_graph_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.gen_graph_error at 0x44d>'
    gen_graph_report = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.gen_graph_report at 0x44e>'
    gen_report = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.gen_report at 0x44f>'
    gen_report_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.gen_report_error at 0x450>'
    general_error_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.general_error_msg at 0x451>'
    generating = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.generating at 0x452>'
    generic_confirm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.generic_confirm at 0x453>'
    generic_error_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.generic_error_message at 0x454>'
    get_info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.get_info at 0x455>'
    getting_started_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.getting_started_win_title at 0x456>'
    got_zero_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.got_zero_rate at 0x457>'
    gov_bond = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.gov_bond at 0x458>'
    graph = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph at 0x459>'
    graph___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph___ at 0x45a>'
    graph_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_account at 0x45b>'
    graph_account_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_account_balance at 0x45c>'
    graph_asset_alloc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_asset_alloc at 0x45d>'
    graph_avg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_avg at 0x45e>'
    graph_bar = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_bar at 0x45f>'
    graph_begindate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_begindate at 0x460>'
    graph_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_currency at 0x461>'
    graph_detailed_key = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_detailed_key at 0x462>'
    graph_dimension_3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_dimension_3 at 0x463>'
    graph_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_done at 0x464>'
    graph_dot__expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_dot__expenses at 0x465>'
    graph_dot__incomes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_dot__incomes at 0x466>'
    graph_enddate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_enddate at 0x467>'
    graph_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_expenses at 0x468>'
    graph_explast30days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_explast30days at 0x469>'
    graph_explast365days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_explast365days at 0x46a>'
    graph_explastmonth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_explastmonth at 0x46b>'
    graph_expnext30days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_expnext30days at 0x46c>'
    graph_expnextmonth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_expnextmonth at 0x46d>'
    graph_expthismonth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_expthismonth at 0x46e>'
    graph_expthisyear = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_expthisyear at 0x46f>'
    graph_groupby = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby at 0x470>'
    graph_groupby_day = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_day at 0x471>'
    graph_groupby_fquarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_fquarter at 0x472>'
    graph_groupby_fyear = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_fyear at 0x473>'
    graph_groupby_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_month at 0x474>'
    graph_groupby_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_none at 0x475>'
    graph_groupby_quarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_quarter at 0x476>'
    graph_groupby_week = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_week at 0x477>'
    graph_groupby_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_groupby_year at 0x478>'
    graph_inclast30days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_inclast30days at 0x479>'
    graph_inclast365days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_inclast365days at 0x47a>'
    graph_inclastmonth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_inclastmonth at 0x47b>'
    graph_income = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_income at 0x47c>'
    graph_income_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_income_expenses at 0x47d>'
    graph_incthismonth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_incthismonth at 0x47e>'
    graph_incthisyear = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_incthisyear at 0x47f>'
    graph_line = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_line at 0x480>'
    graph_max = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_max at 0x481>'
    graph_med = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_med at 0x482>'
    graph_memorize = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_memorize at 0x483>'
    graph_memorize_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_memorize_title at 0x484>'
    graph_min = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_min at 0x485>'
    graph_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_name at 0x486>'
    graph_net_worth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_net_worth at 0x487>'
    graph_pie = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_pie at 0x488>'
    graph_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_print at 0x489>'
    graph_relative_to_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_relative_to_currency at 0x48a>'
    graph_save = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_save at 0x48b>'
    graph_security_performance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_security_performance at 0x48c>'
    graph_sel_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_sel_expenses at 0x48d>'
    graph_sel_incomes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_sel_incomes at 0x48e>'
    graph_show_noncleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_show_noncleared at 0x48f>'
    graph_top_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_top_expenses at 0x490>'
    graph_top_expenses___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_top_expenses___ at 0x491>'
    graph_top_incomes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_top_incomes at 0x492>'
    graph_top_incomes___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_top_incomes___ at 0x493>'
    graph_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_type at 0x494>'
    graph_update = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_update at 0x495>'
    graph_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graph_win_title at 0x496>'
    graphs = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graphs at 0x497>'
    graphs_and_reports = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.graphs_and_reports at 0x498>'
    grnLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.grnLabel at 0x499>'
    have_most_recent_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.have_most_recent_version at 0x49a>'
    heavy_lot_panel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.heavy_lot_panel at 0x49b>'
    help = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help at 0x49c>'
    help_contents = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help_contents at 0x49d>'
    help_dir = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help_dir at 0x49e>'
    help_reg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help_reg at 0x49f>'
    help_support_site = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help_support_site at 0x4a0>'
    help_userguide = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help_userguide at 0x4a1>'
    help_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.help_win_title at 0x4a2>'
    hidden_panels = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.hidden_panels at 0x4a3>'
    hideBudgetItemPrompt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.hideBudgetItemPrompt at 0x4a4>'
    hide_on_hp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.hide_on_hp at 0x4a5>'
    hide_source_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.hide_source_list at 0x4a6>'
    high_contrast_setting = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.high_contrast_setting at 0x4a7>'
    hint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.hint at 0x4a8>'
    home = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home at 0x4a9>'
    home_asset_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_asset_balances at 0x4aa>'
    home_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_balances at 0x4ab>'
    home_bank_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_bank_balances at 0x4ac>'
    home_calendar = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_calendar at 0x4ad>'
    home_cc_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_cc_balances at 0x4ae>'
    home_exchangerates = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_exchangerates at 0x4af>'
    home_invst_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_invst_balances at 0x4b0>'
    home_liability_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_liability_balances at 0x4b1>'
    home_loan_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_loan_balances at 0x4b2>'
    home_stocksprices = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_stocksprices at 0x4b3>'
    home_versions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_versions at 0x4b4>'
    home_view_config_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.home_view_config_desc at 0x4b5>'
    https_not_available = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.https_not_available at 0x4b6>'
    hueLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.hueLabel at 0x4b7>'
    icloud = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.icloud at 0x4b8>'
    iclouddrive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.iclouddrive at 0x4b9>'
    iclouddrive_sync_instructions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.iclouddrive_sync_instructions at 0x4ba>'
    ignore = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ignore at 0x4bb>'
    ignore_this_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ignore_this_version at 0x4bc>'
    import_accts_only = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_accts_only at 0x4bd>'
    import_backup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_backup at 0x4be>'
    import_csv_error_columns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_csv_error_columns at 0x4bf>'
    import_csv_error_nodata = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_csv_error_nodata at 0x4c0>'
    import_csv_ready_fmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_csv_ready_fmt at 0x4c1>'
    import_data___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_data___ at 0x4c2>'
    import_download_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_download_desc at 0x4c3>'
    import_error_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_error_msg at 0x4c4>'
    import_from_download = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_download at 0x4c5>'
    import_from_program = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_program at 0x4c6>'
    import_from_qem = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_qem at 0x4c7>'
    import_from_qem_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_qem_desc at 0x4c8>'
    import_from_qem_expl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_qem_expl at 0x4c9>'
    import_from_qem_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_qem_title at 0x4ca>'
    import_from_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_from_txns at 0x4cb>'
    import_hist_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_hist_desc at 0x4cc>'
    import_hist_from_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_hist_from_file at 0x4cd>'
    import_hist_from_txns_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_hist_from_txns_desc at 0x4ce>'
    import_into_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_into_acct at 0x4cf>'
    import_multiple_settings_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_multiple_settings_desc at 0x4d0>'
    import_no_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_no_file at 0x4d1>'
    import_ofc_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_ofc_header at 0x4d2>'
    import_ofx_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_ofx_header at 0x4d3>'
    import_partial_fmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_partial_fmt at 0x4d4>'
    import_price_hist = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_price_hist at 0x4d5>'
    import_price_hist_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_price_hist_error at 0x4d6>'
    import_qif_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_qif_header at 0x4d7>'
    import_single_acct_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_single_acct_desc at 0x4d8>'
    import_status_merging = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_status_merging at 0x4d9>'
    import_status_prescanning = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_status_prescanning at 0x4da>'
    import_status_reading = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_status_reading at 0x4db>'
    import_success_fmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.import_success_fmt at 0x4dc>'
    imported_ofx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.imported_ofx at 0x4dd>'
    importing_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.importing_data at 0x4de>'
    in_window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.in_window at 0x4df>'
    inbox = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.inbox at 0x4e0>'
    inc_exp_include_xfer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.inc_exp_include_xfer at 0x4e1>'
    inc_liabilities = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.inc_liabilities at 0x4e2>'
    inc_sec_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.inc_sec_bal at 0x4e3>'
    inc_subaccts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.inc_subaccts at 0x4e4>'
    incl_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.incl_items at 0x4e5>'
    include_reconciling = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.include_reconciling at 0x4e6>'
    incomeAsMax_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.incomeAsMax_text at 0x4e7>'
    income_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.income_acct at 0x4e8>'
    incoming = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.incoming at 0x4e9>'
    increase = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.increase at 0x4ea>'
    index = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.index at 0x4eb>'
    info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.info at 0x4ec>'
    information = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.information at 0x4ed>'
    init_srng___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.init_srng___ at 0x4ee>'
    initial_liability = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.initial_liability at 0x4ef>'
    initial_sync_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.initial_sync_msg at 0x4f0>'
    initial_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.initial_value at 0x4f1>'
    input_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.input_error at 0x4f2>'
    insert_dec = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.insert_dec at 0x4f3>'
    install = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.install at 0x4f4>'
    install_extension = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.install_extension at 0x4f5>'
    install_extension_from_script_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.install_extension_from_script_q at 0x4f6>'
    installed_extensions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.installed_extensions at 0x4f7>'
    int_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.int_acct at 0x4f8>'
    int_inc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.int_inc at 0x4f9>'
    int_rem = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.int_rem at 0x4fa>'
    interest = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.interest at 0x4fb>'
    internal_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.internal_files at 0x4fc>'
    invalid_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invalid_checknum at 0x4fd>'
    invalid_key = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invalid_key at 0x4fe>'
    invalid_ofx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invalid_ofx at 0x4ff>'
    invalid_olb_signon_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invalid_olb_signon_msg at 0x500>'
    invst_cash_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_cash_balance at 0x501>'
    invst_port_val = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_port_val at 0x502>'
    invst_txntype_0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_0 at 0x503>'
    invst_txntype_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_1 at 0x504>'
    invst_txntype_10 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_10 at 0x505>'
    invst_txntype_11 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_11 at 0x506>'
    invst_txntype_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_2 at 0x507>'
    invst_txntype_3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_3 at 0x508>'
    invst_txntype_4 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_4 at 0x509>'
    invst_txntype_5 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_5 at 0x50a>'
    invst_txntype_6 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_6 at 0x50b>'
    invst_txntype_7 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_7 at 0x50c>'
    invst_txntype_8 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_8 at 0x50d>'
    invst_txntype_9 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_9 at 0x50e>'
    invst_txntype_unreal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntype_unreal at 0x50f>'
    invst_txntypel_0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_0 at 0x510>'
    invst_txntypel_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_1 at 0x511>'
    invst_txntypel_10 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_10 at 0x512>'
    invst_txntypel_11 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_11 at 0x513>'
    invst_txntypel_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_2 at 0x514>'
    invst_txntypel_3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_3 at 0x515>'
    invst_txntypel_4 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_4 at 0x516>'
    invst_txntypel_5 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_5 at 0x517>'
    invst_txntypel_6 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_6 at 0x518>'
    invst_txntypel_7 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_7 at 0x519>'
    invst_txntypel_8 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_8 at 0x51a>'
    invst_txntypel_9 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_txntypel_9 at 0x51b>'
    invst_unsprtd_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.invst_unsprtd_txn at 0x51c>'
    is_child_of = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.is_child_of at 0x51d>'
    is_reg_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.is_reg_desc at 0x51e>'
    item_exists_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.item_exists_q at 0x51f>'
    january = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.january at 0x520>'
    java_laf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.java_laf at 0x521>'
    java_loc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.java_loc at 0x522>'
    java_vendor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.java_vendor at 0x523>'
    java_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.java_version at 0x524>'
    july = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.july at 0x525>'
    june = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.june at 0x526>'
    keep_reminders_in_archive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.keep_reminders_in_archive at 0x527>'
    key_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.key_desc at 0x528>'
    key_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.key_title at 0x529>'
    labelColon = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.labelColon at 0x52a>'
    last_12_months = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_12_months at 0x52b>'
    last_1_day = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_1_day at 0x52c>'
    last_30_days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_30_days at 0x52d>'
    last_365_days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_365_days at 0x52e>'
    last_fiscal_quarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_fiscal_quarter at 0x52f>'
    last_fiscal_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_fiscal_year at 0x530>'
    last_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_month at 0x531>'
    last_quarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_quarter at 0x532>'
    last_week = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_week at 0x533>'
    last_x_days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_x_days at 0x534>'
    last_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.last_year at 0x535>'
    latest_build = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.latest_build at 0x536>'
    latest_licensed_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.latest_licensed_msg at 0x537>'
    latest_update = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.latest_update at 0x538>'
    least_gain = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.least_gain at 0x539>'
    left_panels = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.left_panels at 0x53a>'
    license = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.license at 0x53b>'
    license_agree = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.license_agree at 0x53c>'
    license_key = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.license_key at 0x53d>'
    limits_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.limits_text at 0x53e>'
    list_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.list_name at 0x53f>'
    loading___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loading___ at 0x540>'
    loading_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loading_file at 0x541>'
    loan_amt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_amt at 0x542>'
    loan_principal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_principal at 0x543>'
    loan_pts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_pts at 0x544>'
    loan_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_rate at 0x545>'
    loan_reminder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_reminder at 0x546>'
    loan_term_yrs = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_term_yrs at 0x547>'
    loan_tfr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.loan_tfr at 0x548>'
    locale = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.locale at 0x549>'
    log_mdplus_settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.log_mdplus_settings at 0x54a>'
    login = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.login at 0x54b>'
    look_and_feel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.look_and_feel at 0x54c>'
    lot_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.lot_match at 0x54d>'
    lumLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.lumLabel at 0x54e>'
    make_duplicate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.make_duplicate at 0x54f>'
    manage_extensions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.manage_extensions at 0x550>'
    manually_open_url_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.manually_open_url_message at 0x551>'
    march = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.march at 0x552>'
    mark_confirmed_txns_cleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mark_confirmed_txns_cleared at 0x553>'
    mark_txns_as_confirmed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mark_txns_as_confirmed at 0x554>'
    mark_txns_cleared_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mark_txns_cleared_q at 0x555>'
    mark_txns_reconciling_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mark_txns_reconciling_q at 0x556>'
    mark_txns_uncleared_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mark_txns_uncleared_q at 0x557>'
    match_local_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_local_account at 0x558>'
    match_local_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_local_category at 0x559>'
    match_lots = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_lots at 0x55a>'
    match_lots2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_lots2 at 0x55b>'
    match_online_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_online_accounts at 0x55c>'
    match_online_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_online_name at 0x55d>'
    match_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_txns at 0x55e>'
    match_type_correction = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_correction at 0x55f>'
    match_type_delete = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_delete at 0x560>'
    match_type_duplicate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_duplicate at 0x561>'
    match_type_merge = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_merge at 0x562>'
    match_type_orig = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_orig at 0x563>'
    match_type_revert = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_revert at 0x564>'
    match_type_similar = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.match_type_similar at 0x565>'
    maturity_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.maturity_date at 0x566>'
    may = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.may at 0x567>'
    md_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.md_files at 0x568>'
    mdplus = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus at 0x569>'
    mdplus_authentication_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_authentication_error at 0x56a>'
    mdplus_confirmation_expired = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_confirmation_expired at 0x56b>'
    mdplus_confirmation_pending = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_confirmation_pending at 0x56c>'
    mdplus_disconnect_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_disconnect_x at 0x56d>'
    mdplus_doing_initial_download_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_doing_initial_download_msg at 0x56e>'
    mdplus_error_refreshing = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_error_refreshing at 0x56f>'
    mdplus_expires_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_expires_x at 0x570>'
    mdplus_fully_connected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_fully_connected at 0x571>'
    mdplus_item_is_relinking_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_is_relinking_desc at 0x572>'
    mdplus_item_needs_relink = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_needs_relink at 0x573>'
    mdplus_item_needs_relink_prompt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_needs_relink_prompt at 0x574>'
    mdplus_item_relink_needed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_relink_needed at 0x575>'
    mdplus_item_status_connected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_status_connected at 0x576>'
    mdplus_item_status_expiration_imminent = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_status_expiration_imminent at 0x577>'
    mdplus_item_status_expired = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_status_expired at 0x578>'
    mdplus_item_status_unknown = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_item_status_unknown at 0x579>'
    mdplus_manage_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_manage_account at 0x57a>'
    mdplus_pending_subscription = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_pending_subscription at 0x57b>'
    mdplus_relink_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_relink_error at 0x57c>'
    mdplus_service = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_service at 0x57d>'
    mdplus_service_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_service_desc at 0x57e>'
    mdplus_setup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_setup at 0x57f>'
    mdplus_setup_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_setup_accounts at 0x580>'
    mdplus_signup_connect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_connect at 0x581>'
    mdplus_signup_connect_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_connect_accounts at 0x582>'
    mdplus_signup_extra_activated = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_activated at 0x583>'
    mdplus_signup_extra_confirmed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_confirmed at 0x584>'
    mdplus_signup_extra_expired = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_expired at 0x585>'
    mdplus_signup_extra_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_none at 0x586>'
    mdplus_signup_extra_pending = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_pending at 0x587>'
    mdplus_signup_extra_subscribed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_subscribed at 0x588>'
    mdplus_signup_extra_unknown = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_extra_unknown at 0x589>'
    mdplus_signup_go_to_browser = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_go_to_browser at 0x58a>'
    mdplus_signup_link_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_link_accounts at 0x58b>'
    mdplus_signup_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_message at 0x58c>'
    mdplus_signup_message2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_message2 at 0x58d>'
    mdplus_signup_preparing = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_preparing at 0x58e>'
    mdplus_signup_reconnect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_reconnect at 0x58f>'
    mdplus_signup_subscribe = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_signup_subscribe at 0x590>'
    mdplus_status_checking = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_status_checking at 0x591>'
    mdplus_subscription_confirmed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_subscription_confirmed at 0x592>'
    mdplus_table_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_table_desc at 0x593>'
    mdplus_unable_to_add_connection = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_unable_to_add_connection at 0x594>'
    mdplus_unable_to_disconnect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_unable_to_disconnect at 0x595>'
    mdplus_unable_to_register_key = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_unable_to_register_key at 0x596>'
    mdplus_update_link = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mdplus_update_link at 0x597>'
    memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.memo at 0x598>'
    memorize_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.memorize_txn at 0x599>'
    memorized = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.memorized at 0x59a>'
    memorized_graphs = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.memorized_graphs at 0x59b>'
    memorized_reports = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.memorized_reports at 0x59c>'
    merge_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.merge_txn at 0x59d>'
    migrate_file_continue = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.migrate_file_continue at 0x59e>'
    migrate_file_continue_external = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.migrate_file_continue_external at 0x59f>'
    migrate_file_internal_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.migrate_file_internal_desc at 0x5a0>'
    minimize_window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.minimize_window at 0x5a1>'
    misc_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.misc_error at 0x5a2>'
    misc_exp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.misc_exp at 0x5a3>'
    misc_inc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.misc_inc at 0x5a4>'
    missing_field = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.missing_field at 0x5a5>'
    missing_r_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.missing_r_desc at 0x5a6>'
    missing_r_desc_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.missing_r_desc_title at 0x5a7>'
    mixed_interval_budget = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mixed_interval_budget at 0x5a8>'
    mon_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mon_s at 0x5a9>'
    moneybot = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.moneybot at 0x5aa>'
    month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.month at 0x5ab>'
    month_to_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.month_to_date at 0x5ac>'
    monthly_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.monthly_pmt at 0x5ad>'
    more = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.more at 0x5ae>'
    more___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.more___ at 0x5af>'
    more_fields = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.more_fields at 0x5b0>'
    motif_laf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.motif_laf at 0x5b1>'
    moveDown = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.moveDown at 0x5b2>'
    moveUp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.moveUp at 0x5b3>'
    move_file_from_dropbox = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_file_from_dropbox at 0x5b4>'
    move_file_from_dropbox_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_file_from_dropbox_msg at 0x5b5>'
    move_internal_storage_failed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_internal_storage_failed at 0x5b6>'
    move_internal_storage_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_internal_storage_message at 0x5b7>'
    move_internal_storage_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_internal_storage_title at 0x5b8>'
    move_left_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_left_item at 0x5b9>'
    move_right_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_right_item at 0x5ba>'
    move_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.move_txn at 0x5bb>'
    msg_from = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.msg_from at 0x5bc>'
    msg_subj = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.msg_subj at 0x5bd>'
    msg_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.msg_to at 0x5be>'
    multiple_selections = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.multiple_selections at 0x5bf>'
    multiple_selections_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.multiple_selections_description at 0x5c0>'
    multiple_txns_selected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.multiple_txns_selected at 0x5c1>'
    mun_bond = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mun_bond at 0x5c2>'
    mutualSubType_US = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mutualSubType_US at 0x5c3>'
    mutualSubType_balanced = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mutualSubType_balanced at 0x5c4>'
    mutualSubType_bond = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mutualSubType_bond at 0x5c5>'
    mutualSubType_etf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mutualSubType_etf at 0x5c6>'
    mutualSubType_intl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mutualSubType_intl at 0x5c7>'
    mutualSubType_money = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.mutualSubType_money at 0x5c8>'
    n_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.n_total at 0x5c9>'
    n_unconfirmed_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.n_unconfirmed_txns at 0x5ca>'
    name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.name at 0x5cb>'
    nasdaq = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nasdaq at 0x5cc>'
    net_worth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.net_worth at 0x5cd>'
    netsync = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.netsync at 0x5ce>'
    netsync_at_startup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.netsync_at_startup at 0x5cf>'
    netsync_wait = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.netsync_wait at 0x5d0>'
    network_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.network_error at 0x5d1>'
    new___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new___ at 0x5d2>'
    new_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_account at 0x5d3>'
    new_account_book = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_account_book at 0x5d4>'
    new_account_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_account_name at 0x5d5>'
    new_account_url_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_account_url_text at 0x5d6>'
    new_account_url_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_account_url_title at 0x5d7>'
    new_acct___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_acct___ at 0x5d8>'
    new_basic_reminder_on_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_basic_reminder_on_date at 0x5d9>'
    new_bond_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_bond_win at 0x5da>'
    new_budget = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_budget at 0x5db>'
    new_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_category at 0x5dc>'
    new_category_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_category_name at 0x5dd>'
    new_cd_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_cd_win at 0x5de>'
    new_check_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_check_tag at 0x5df>'
    new_currency_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_currency_win_title at 0x5e0>'
    new_fi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_fi at 0x5e1>'
    new_file_contents0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_contents0 at 0x5e2>'
    new_file_contents1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_contents1 at 0x5e3>'
    new_file_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_currency at 0x5e4>'
    new_file_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_desc at 0x5e5>'
    new_file_desc0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_desc0 at 0x5e6>'
    new_file_desc1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_desc1 at 0x5e7>'
    new_file_from_import = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_from_import at 0x5e8>'
    new_file_from_import_expl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_from_import_expl at 0x5e9>'
    new_file_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_header at 0x5ea>'
    new_file_inv_acct_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_inv_acct_name at 0x5eb>'
    new_file_inv_acct_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_inv_acct_type at 0x5ec>'
    new_file_inv_curr_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_inv_curr_type at 0x5ed>'
    new_file_location = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_location at 0x5ee>'
    new_file_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_type at 0x5ef>'
    new_file_type0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_type0 at 0x5f0>'
    new_file_type1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_type1 at 0x5f1>'
    new_file_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_file_win_title at 0x5f2>'
    new_invest_txn_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_invest_txn_win at 0x5f3>'
    new_manual_fi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_manual_fi at 0x5f4>'
    new_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_msg at 0x5f5>'
    new_mutual_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_mutual_win at 0x5f6>'
    new_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_payee at 0x5f7>'
    new_payee_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_payee_title at 0x5f8>'
    new_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_script at 0x5f9>'
    new_script_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_script_title at 0x5fa>'
    new_sec_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_sec_win at 0x5fb>'
    new_split = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_split at 0x5fc>'
    new_stock_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_stock_win at 0x5fd>'
    new_transaction = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_transaction at 0x5fe>'
    new_transaction_on_record = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_transaction_on_record at 0x5ff>'
    new_txn_reminder_on_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_txn_reminder_on_date at 0x600>'
    new_updater_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_updater_msg at 0x601>'
    new_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_version at 0x602>'
    new_watch_list_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.new_watch_list_win at 0x603>'
    newextavail = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.newextavail at 0x604>'
    next = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.next at 0x605>'
    next_check_num = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.next_check_num at 0x606>'
    no = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no at 0x607>'
    noBudget = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.noBudget at 0x608>'
    noCategory = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.noCategory at 0x609>'
    noEndDate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.noEndDate at 0x60a>'
    no_bdgt_selected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_bdgt_selected at 0x60b>'
    no_checks_to_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_checks_to_print at 0x60c>'
    no_dldr_for_currtype = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_dldr_for_currtype at 0x60d>'
    no_emails = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_emails at 0x60e>'
    no_fields_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_fields_err at 0x60f>'
    no_file_opened_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_file_opened_error at 0x610>'
    no_files_selected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_files_selected at 0x611>'
    no_folder_selected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_folder_selected at 0x612>'
    no_info_about_features = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_info_about_features at 0x613>'
    no_new_online_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_new_online_txns at 0x614>'
    no_online_banking_test = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_online_banking_test at 0x615>'
    no_sec_selected_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_sec_selected_err at 0x616>'
    no_security_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_security_q at 0x617>'
    no_sells = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_sells at 0x618>'
    no_shares_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_shares_date at 0x619>'
    no_syncable_files_found = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_syncable_files_found at 0x61a>'
    no_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_txns at 0x61b>'
    no_txns_selected = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.no_txns_selected at 0x61c>'
    none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.none at 0x61d>'
    none_of_the_above = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.none_of_the_above at 0x61e>'
    notes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.notes at 0x61f>'
    nothing_to_download_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nothing_to_download_msg at 0x620>'
    nothing_to_graph = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nothing_to_graph at 0x621>'
    nothing_to_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nothing_to_print at 0x622>'
    nothing_to_report = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nothing_to_report at 0x623>'
    november = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.november at 0x624>'
    null_pointer_exception = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.null_pointer_exception at 0x625>'
    num_payments = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.num_payments at 0x626>'
    num_pmts_rem = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.num_pmts_rem at 0x627>'
    num_txns_left_in_demo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.num_txns_left_in_demo at 0x628>'
    num_years = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.num_years at 0x629>'
    numeric_font = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.numeric_font at 0x62a>'
    nxt_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nxt_pmt at 0x62b>'
    nyse = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.nyse at 0x62c>'
    observe_bp_window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.observe_bp_window at 0x62d>'
    october = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.october at 0x62e>'
    of_string = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.of_string at 0x62f>'
    of_the_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.of_the_month at 0x630>'
    ofc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofc at 0x631>'
    ofx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx at 0x632>'
    ofx_acct_type_cc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_acct_type_cc at 0x633>'
    ofx_acct_type_checking = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_acct_type_checking at 0x634>'
    ofx_acct_type_lineofcredit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_acct_type_lineofcredit at 0x635>'
    ofx_acct_type_loc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_acct_type_loc at 0x636>'
    ofx_acct_type_moneymkt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_acct_type_moneymkt at 0x637>'
    ofx_acct_type_savings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_acct_type_savings at 0x638>'
    ofx_app_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_app_id at 0x639>'
    ofx_app_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_app_version at 0x63a>'
    ofx_bad_pin1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bad_pin1 at 0x63b>'
    ofx_bad_pin2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bad_pin2 at 0x63c>'
    ofx_bad_pin3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bad_pin3 at 0x63d>'
    ofx_bank_fid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bank_fid at 0x63e>'
    ofx_bank_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bank_id at 0x63f>'
    ofx_bank_org = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bank_org at 0x640>'
    ofx_bank_url = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_bank_url at 0x641>'
    ofx_billpayment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_billpayment at 0x642>'
    ofx_broker_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_broker_id at 0x643>'
    ofx_changing_pin = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_changing_pin at 0x644>'
    ofx_chg_pin_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_chg_pin_desc at 0x645>'
    ofx_getting_fi_prof = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_getting_fi_prof at 0x646>'
    ofx_manual_setup_html = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_manual_setup_html at 0x647>'
    ofx_newpass = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_newpass at 0x648>'
    ofx_newpass2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_newpass2 at 0x649>'
    ofx_olbanking = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_olbanking at 0x64a>'
    ofx_oldpass = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_oldpass at 0x64b>'
    ofx_pin_mismatch = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_pin_mismatch at 0x64c>'
    ofx_realm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_realm at 0x64d>'
    ofx_service = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_service at 0x64e>'
    ofx_service_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_service_desc at 0x64f>'
    ofx_signup_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_signup_done at 0x650>'
    ofx_signup_needs_pin_chg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_signup_needs_pin_chg at 0x651>'
    ofx_userid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_userid at 0x652>'
    ofx_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ofx_win_title at 0x653>'
    ok = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ok at 0x654>'
    ol_avail_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ol_avail_bal at 0x655>'
    ol_ledger_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.ol_ledger_bal at 0x656>'
    olb_accept_suggestion = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_accept_suggestion at 0x657>'
    olb_accept_suggestions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_accept_suggestions at 0x658>'
    olb_acct_not_found = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_acct_not_found at 0x659>'
    olb_acct_type_mismatch = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_acct_type_mismatch at 0x65a>'
    olb_best_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_best_match at 0x65b>'
    olb_by_addr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_by_addr at 0x65c>'
    olb_by_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_by_id at 0x65d>'
    olb_change_pin = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_change_pin at 0x65e>'
    olb_chg_conn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_chg_conn at 0x65f>'
    olb_conn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_conn at 0x660>'
    olb_correction_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_correction_to at 0x661>'
    olb_del_connection = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_del_connection at 0x662>'
    olb_delete_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_delete_txn at 0x663>'
    olb_disconnect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_disconnect at 0x664>'
    olb_disconnect_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_disconnect_q at 0x665>'
    olb_enroll_msg1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_enroll_msg1 at 0x666>'
    olb_enroll_web = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_enroll_web at 0x667>'
    olb_exact_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_exact_match at 0x668>'
    olb_fi_addr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_addr at 0x669>'
    olb_fi_citystate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_citystate at 0x66a>'
    olb_fi_ctry = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_ctry at 0x66b>'
    olb_fi_cust_svc_phone = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_cust_svc_phone at 0x66c>'
    olb_fi_dateup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_dateup at 0x66d>'
    olb_fi_lookup_instruct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_lookup_instruct at 0x66e>'
    olb_fi_lookup_instruct2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_lookup_instruct2 at 0x66f>'
    olb_fi_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_name at 0x670>'
    olb_fi_tech_svc_phone = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_tech_svc_phone at 0x671>'
    olb_fi_url = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_url at 0x672>'
    olb_fi_zip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fi_zip at 0x673>'
    olb_fitable_accesstype = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fitable_accesstype at 0x674>'
    olb_fitable_finame = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fitable_finame at 0x675>'
    olb_fitable_fitype = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_fitable_fitype at 0x676>'
    olb_lookup_fi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_lookup_fi at 0x677>'
    olb_match_correction = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_match_correction at 0x678>'
    olb_match_deletion = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_match_deletion at 0x679>'
    olb_match_option = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_match_option at 0x67a>'
    olb_matched_option = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_matched_option at 0x67b>'
    olb_msg_set_not_supported = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_msg_set_not_supported at 0x67c>'
    olb_new_conn_expl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_new_conn_expl at 0x67d>'
    olb_new_connection = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_new_connection at 0x67e>'
    olb_new_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_new_txn at 0x67f>'
    olb_no_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_no_match at 0x680>'
    olb_payment_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_payment_description at 0x681>'
    olb_possible_match = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_possible_match at 0x682>'
    olb_refresh_connection = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_refresh_connection at 0x683>'
    olb_refresh_fi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_refresh_fi at 0x684>'
    olb_reject_suggestion = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_reject_suggestion at 0x685>'
    olb_reject_suggestions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_reject_suggestions at 0x686>'
    olb_reset_sync = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_reset_sync at 0x687>'
    olb_service = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_service at 0x688>'
    olb_setup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_setup at 0x689>'
    olb_signup_wizard = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_signup_wizard at 0x68a>'
    olb_similar_option = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_similar_option at 0x68b>'
    olb_similar_prev_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_similar_prev_txn at 0x68c>'
    olb_wiz_retrieve_fi = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_wiz_retrieve_fi at 0x68d>'
    olb_wiz_youchose1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_wiz_youchose1 at 0x68e>'
    olb_wiz_youchose2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olb_wiz_youchose2 at 0x68f>'
    olbp_conn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_conn at 0x690>'
    olbp_date_too_early = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_date_too_early at 0x691>'
    olbp_disconnect_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_disconnect_q at 0x692>'
    olbp_msg_set_not_supported = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_msg_set_not_supported at 0x693>'
    olbp_service = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_service at 0x694>'
    olbp_setup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_setup at 0x695>'
    olbp_signup_wizard = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olbp_signup_wizard at 0x696>'
    olemail_msg_set_not_supported = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.olemail_msg_set_not_supported at 0x697>'
    one = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.one at 0x698>'
    one_line_mode = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.one_line_mode at 0x699>'
    one_unconfirmed_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.one_unconfirmed_txn at 0x69a>'
    onlbp_instr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.onlbp_instr at 0x69b>'
    online_acct_bp_not_configured = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_acct_bp_not_configured at 0x69c>'
    online_acct_not_configured = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_acct_not_configured at 0x69d>'
    online_all_txns_processed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_all_txns_processed at 0x69e>'
    online_amt_sign_overrides_txntype = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_amt_sign_overrides_txntype at 0x69f>'
    online_auth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_auth at 0x6a0>'
    online_auth_anonymous = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_auth_anonymous at 0x6a1>'
    online_auth_fixed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_auth_fixed at 0x6a2>'
    online_auth_hwtoken = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_auth_hwtoken at 0x6a3>'
    online_auth_onetime = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_auth_onetime at 0x6a4>'
    online_auth_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_auth_type at 0x6a5>'
    online_billpay = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_billpay at 0x6a6>'
    online_bills_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_bills_title at 0x6a7>'
    online_confirm_sel_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_confirm_sel_txns at 0x6a8>'
    online_connect_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_connect_to at 0x6a9>'
    online_connections = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_connections at 0x6aa>'
    online_downloading_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_downloading_txns at 0x6ab>'
    online_error_code = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_error_code at 0x6ac>'
    online_error_expl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_error_expl at 0x6ad>'
    online_error_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_error_msg at 0x6ae>'
    online_error_start = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_error_start at 0x6af>'
    online_error_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_error_title at 0x6b0>'
    online_menu = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_menu at 0x6b1>'
    online_payees_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_payees_title at 0x6b2>'
    online_removing_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_removing_payee at 0x6b3>'
    online_retrieve_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_retrieve_txns at 0x6b4>'
    online_submitting_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_submitting_payee at 0x6b5>'
    online_submitting_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_submitting_pmt at 0x6b6>'
    online_transfer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_transfer at 0x6b7>'
    online_txn_corrxn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_txn_corrxn at 0x6b8>'
    online_txn_delete = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_txn_delete at 0x6b9>'
    online_txn_match_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_txn_match_desc at 0x6ba>'
    online_txn_new_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_txn_new_desc at 0x6bb>'
    online_update = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_update at 0x6bc>'
    online_update_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_update_all at 0x6bd>'
    online_update_txns_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_update_txns_title at 0x6be>'
    online_updating_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.online_updating_payee at 0x6bf>'
    open = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open at 0x6c0>'
    open___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open___ at 0x6c1>'
    open_archive_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_archive_description at 0x6c2>'
    open_archive_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_archive_title at 0x6c3>'
    open_existing_book = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_existing_book at 0x6c4>'
    open_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_file at 0x6c5>'
    open_file_expl = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_file_expl at 0x6c6>'
    open_most_recent = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_most_recent at 0x6c7>'
    open_new_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_new_win at 0x6c8>'
    open_other = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_other at 0x6c9>'
    open_recent = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_recent at 0x6ca>'
    open_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_script at 0x6cb>'
    open_script_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_script_title at 0x6cc>'
    open_sync_new_local = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_sync_new_local at 0x6cd>'
    open_sync_text_dropbox = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_sync_text_dropbox at 0x6ce>'
    open_sync_text_folder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_sync_text_folder at 0x6cf>'
    open_synced_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_synced_file at 0x6d0>'
    open_this_window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_this_window at 0x6d1>'
    open_website = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_website at 0x6d2>'
    open_x_in_external_browser = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.open_x_in_external_browser at 0x6d3>'
    optionSubType_incentive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.optionSubType_incentive at 0x6d4>'
    optionSubType_nonqual = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.optionSubType_nonqual at 0x6d5>'
    option_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.option_price at 0x6d6>'
    orig_oltxn_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.orig_oltxn_label at 0x6d7>'
    original_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.original_memo at 0x6d8>'
    original_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.original_payee at 0x6d9>'
    otc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.otc at 0x6da>'
    other = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.other at 0x6db>'
    otherSubType_gold = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.otherSubType_gold at 0x6dc>'
    otherSubType_oil = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.otherSubType_oil at 0x6dd>'
    otherSubType_realestate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.otherSubType_realestate at 0x6de>'
    outOfDate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.outOfDate at 0x6df>'
    outOfDateTip_format = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.outOfDateTip_format at 0x6e0>'
    outbox = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.outbox at 0x6e1>'
    outgoing = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.outgoing at 0x6e2>'
    outgoing_olp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.outgoing_olp at 0x6e3>'
    over_mnemonic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.over_mnemonic at 0x6e4>'
    over_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.over_text at 0x6e5>'
    overdue = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.overdue at 0x6e6>'
    overdue_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.overdue_items at 0x6e7>'
    overwrite_theme_conf_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.overwrite_theme_conf_text at 0x6e8>'
    overwrite_theme_conf_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.overwrite_theme_conf_title at 0x6e9>'
    p_b_destroy_msg1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_b_destroy_msg1 at 0x6ea>'
    p_b_destroy_msg2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_b_destroy_msg2 at 0x6eb>'
    p_b_destroy_u = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_b_destroy_u at 0x6ec>'
    p_bkup_daily = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_bkup_daily at 0x6ed>'
    p_bkup_es = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_bkup_es at 0x6ee>'
    p_bkup_esp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_bkup_esp at 0x6ef>'
    p_bkup_first_open = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_bkup_first_open at 0x6f0>'
    p_bkup_no = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_bkup_no at 0x6f1>'
    p_bkup_s_l = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_bkup_s_l at 0x6f2>'
    p_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.p_total at 0x6f3>'
    page = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.page at 0x6f4>'
    paid_update_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.paid_update_msg at 0x6f5>'
    parent_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.parent_acct at 0x6f6>'
    parent_cat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.parent_cat at 0x6f7>'
    parse_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.parse_error at 0x6f8>'
    password = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.password at 0x6f9>'
    password_confirm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.password_confirm at 0x6fa>'
    password_pin = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.password_pin at 0x6fb>'
    payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.payee at 0x6fc>'
    payee_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.payee_id at 0x6fd>'
    payees = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.payees at 0x6fe>'
    payment_plan = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.payment_plan at 0x6ff>'
    pending_txns_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pending_txns_msg at 0x700>'
    period = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.period at 0x701>'
    periodically_autosave = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.periodically_autosave at 0x702>'
    phone = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.phone at 0x703>'
    phone_number = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.phone_number at 0x704>'
    plaid_setup_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.plaid_setup_msg at 0x705>'
    please_confirm = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.please_confirm at 0x706>'
    please_wait = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.please_wait at 0x707>'
    pls_enter_passwd = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pls_enter_passwd at 0x708>'
    pmt_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_amount at 0x709>'
    pmt_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_balance at 0x70a>'
    pmt_calc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_calc at 0x70b>'
    pmt_interest = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_interest at 0x70c>'
    pmt_num = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_num at 0x70d>'
    pmt_or_dep_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_or_dep_q at 0x70e>'
    pmt_principal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_principal at 0x70f>'
    pmt_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_total at 0x710>'
    pmt_total_int = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_total_int at 0x711>'
    pmt_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_win at 0x712>'
    pmt_xtra_princ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmt_xtra_princ at 0x713>'
    pmts_per_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pmts_per_year at 0x714>'
    png_files = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.png_files at 0x715>'
    pnts_vs_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pnts_vs_rate at 0x716>'
    pnts_vs_rate_advice0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pnts_vs_rate_advice0 at 0x717>'
    pnts_vs_rate_advice1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pnts_vs_rate_advice1 at 0x718>'
    pnts_vs_rate_advice2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pnts_vs_rate_advice2 at 0x719>'
    pnts_vs_rate_advice3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pnts_vs_rate_advice3 at 0x71a>'
    pnts_vs_rate_advice4 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pnts_vs_rate_advice4 at 0x71b>'
    portion_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.portion_text at 0x71c>'
    potential_duplicate_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.potential_duplicate_txns at 0x71d>'
    potential_duplicate_txns_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.potential_duplicate_txns_description at 0x71e>'
    pref_acct_bg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_acct_bg_col at 0x71f>'
    pref_acct_fg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_acct_fg_col at 0x720>'
    pref_appearance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_appearance at 0x721>'
    pref_autocommit_reminders = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_autocommit_reminders at 0x722>'
    pref_backup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_backup at 0x723>'
    pref_cal_overdue_rmdr_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_cal_overdue_rmdr_col at 0x724>'
    pref_cal_past_rmdr_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_cal_past_rmdr_col at 0x725>'
    pref_cal_rmdr_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_cal_rmdr_col at 0x726>'
    pref_checkPrint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_checkPrint at 0x727>'
    pref_col_chooser = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_col_chooser at 0x728>'
    pref_colors = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_colors at 0x729>'
    pref_general = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_general at 0x72a>'
    pref_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_header at 0x72b>'
    pref_homepage = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_homepage at 0x72c>'
    pref_hp_altbg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_hp_altbg_col at 0x72d>'
    pref_hp_bg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_hp_bg_col at 0x72e>'
    pref_network = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_network at 0x72f>'
    pref_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_print at 0x730>'
    pref_txn_edit_bg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_txn_edit_bg_col at 0x731>'
    pref_txn_list1_bg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_txn_list1_bg_col at 0x732>'
    pref_txn_list2_bg_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_txn_list2_bg_col at 0x733>'
    pref_txn_list2_fut_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_txn_list2_fut_col at 0x734>'
    pref_txn_list_fut_col = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.pref_txn_list_fut_col at 0x735>'
    preferences___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.preferences___ at 0x736>'
    preview_releases = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.preview_releases at 0x737>'
    preview_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.preview_text at 0x738>'
    previous = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.previous at 0x739>'
    primary_currency_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.primary_currency_type at 0x73a>'
    principal_rem = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.principal_rem at 0x73b>'
    print_all_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_all_checks at 0x73c>'
    print_api = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_api at 0x73d>'
    print_cal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_cal at 0x73e>'
    print_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_checks at 0x73f>'
    print_checks___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_checks___ at 0x740>'
    print_font = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_font at 0x741>'
    print_font_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_font_desc at 0x742>'
    print_graph_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_graph_title at 0x743>'
    print_page_setup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_page_setup at 0x744>'
    print_test_check = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_test_check at 0x745>'
    print_transactions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.print_transactions at 0x746>'
    printadj_accountX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_accountX at 0x747>'
    printadj_accountY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_accountY at 0x748>'
    printadj_address_X = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_address_X at 0x749>'
    printadj_address_Y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_address_Y at 0x74a>'
    printadj_amount1numX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amount1numX at 0x74b>'
    printadj_amount1numY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amount1numY at 0x74c>'
    printadj_amount2numX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amount2numX at 0x74d>'
    printadj_amount2numY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amount2numY at 0x74e>'
    printadj_amtnumlocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amtnumlocX at 0x74f>'
    printadj_amtnumlocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amtnumlocY at 0x750>'
    printadj_amttextlocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amttextlocX at 0x751>'
    printadj_amttextlocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_amttextlocY at 0x752>'
    printadj_botmarg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_botmarg at 0x753>'
    printadj_categoryX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_categoryX at 0x754>'
    printadj_categoryY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_categoryY at 0x755>'
    printadj_datelocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_datelocX at 0x756>'
    printadj_datelocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_datelocY at 0x757>'
    printadj_leftmarg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_leftmarg at 0x758>'
    printadj_memoX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_memoX at 0x759>'
    printadj_memoY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_memoY at 0x75a>'
    printadj_memolocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_memolocX at 0x75b>'
    printadj_memolocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_memolocY at 0x75c>'
    printadj_num_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_num_checks at 0x75d>'
    printadj_payeelocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_payeelocX at 0x75e>'
    printadj_payeelocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_payeelocY at 0x75f>'
    printadj_rightmarg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_rightmarg at 0x760>'
    printadj_showaddress = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_showaddress at 0x761>'
    printadj_showbothvouchers = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_showbothvouchers at 0x762>'
    printadj_showmemo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_showmemo at 0x763>'
    printadj_stub_acct_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_acct_x at 0x764>'
    printadj_stub_acct_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_acct_y at 0x765>'
    printadj_stub_amt_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_amt_x at 0x766>'
    printadj_stub_amt_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_amt_y at 0x767>'
    printadj_stub_cat_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_cat_x at 0x768>'
    printadj_stub_cat_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_cat_y at 0x769>'
    printadj_stub_date_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_date_x at 0x76a>'
    printadj_stub_date_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_date_y at 0x76b>'
    printadj_stub_memo_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_memo_x at 0x76c>'
    printadj_stub_memo_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_memo_y at 0x76d>'
    printadj_stub_payee_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_payee_x at 0x76e>'
    printadj_stub_payee_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_payee_y at 0x76f>'
    printadj_stub_size = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_stub_size at 0x770>'
    printadj_topmarg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_topmarg at 0x771>'
    printadj_v_datelocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_v_datelocX at 0x772>'
    printadj_v_datelocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_v_datelocY at 0x773>'
    printadj_v_p_a_X = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_v_p_a_X at 0x774>'
    printadj_v_p_a_Y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_v_p_a_Y at 0x775>'
    printadj_v_payeelocX = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_v_payeelocX at 0x776>'
    printadj_v_payeelocY = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printadj_v_payeelocY at 0x777>'
    printchk_first_err_error1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_error1 at 0x778>'
    printchk_first_err_error2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_error2 at 0x779>'
    printchk_first_err_error3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_error3 at 0x77a>'
    printchk_first_err_num = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_num at 0x77b>'
    printchk_first_err_text1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_text1 at 0x77c>'
    printchk_first_err_text2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_text2 at 0x77d>'
    printchk_first_err_text3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_first_err_text3 at 0x77e>'
    printchk_print_hdr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_print_hdr at 0x77f>'
    printchk_select_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_select_checks at 0x780>'
    printchk_verify = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printchk_verify at 0x781>'
    printreg_print_hdr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.printreg_print_hdr at 0x782>'
    processed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.processed at 0x783>'
    processing_downloaded_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.processing_downloaded_txns at 0x784>'
    product_info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.product_info at 0x785>'
    proxy_host = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.proxy_host at 0x786>'
    proxy_port = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.proxy_port at 0x787>'
    put = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.put at 0x788>'
    python_snippet = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.python_snippet at 0x789>'
    qem_import_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qem_import_title at 0x78a>'
    qem_reading_from = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qem_reading_from at 0x78b>'
    qif = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif at 0x78c>'
    qif_datefmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif_datefmt at 0x78d>'
    qif_datefmt_auto = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif_datefmt_auto at 0x78e>'
    qif_err_nofilename = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif_err_nofilename at 0x78f>'
    qif_export_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif_export_error at 0x790>'
    qif_file_source = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif_file_source at 0x791>'
    qif_import_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.qif_import_error at 0x792>'
    quarter_to_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.quarter_to_date at 0x793>'
    question = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.question at 0x794>'
    quit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.quit at 0x795>'
    r_add_basic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_add_basic at 0x796>'
    r_add_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_add_txn at 0x797>'
    r_annually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_annually at 0x798>'
    r_auto_commit_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_auto_commit_1 at 0x799>'
    r_auto_commit_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_auto_commit_2 at 0x79a>'
    r_b_ack = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_ack at 0x79b>'
    r_b_defer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_defer at 0x79c>'
    r_b_description1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_description1 at 0x79d>'
    r_b_description2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_description2 at 0x79e>'
    r_b_msg1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_msg1 at 0x79f>'
    r_b_msg2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_msg2 at 0x7a0>'
    r_b_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_b_title at 0x7a1>'
    r_daily = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_daily at 0x7a2>'
    r_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_desc at 0x7a3>'
    r_e_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_e_1 at 0x7a4>'
    r_e_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_e_2 at 0x7a5>'
    r_e_y = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_e_y at 0x7a6>'
    r_edit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_edit at 0x7a7>'
    r_f = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_f at 0x7a8>'
    r_gen_editwin = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_gen_editwin at 0x7a9>'
    r_l = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_l at 0x7aa>'
    r_m = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m at 0x7ab>'
    r_m_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_1 at 0x7ac>'
    r_m_10 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_10 at 0x7ad>'
    r_m_11 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_11 at 0x7ae>'
    r_m_12 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_12 at 0x7af>'
    r_m_13 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_13 at 0x7b0>'
    r_m_14 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_14 at 0x7b1>'
    r_m_15 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_15 at 0x7b2>'
    r_m_16 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_16 at 0x7b3>'
    r_m_17 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_17 at 0x7b4>'
    r_m_18 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_18 at 0x7b5>'
    r_m_19 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_19 at 0x7b6>'
    r_m_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_2 at 0x7b7>'
    r_m_20 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_20 at 0x7b8>'
    r_m_21 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_21 at 0x7b9>'
    r_m_22 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_22 at 0x7ba>'
    r_m_23 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_23 at 0x7bb>'
    r_m_24 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_24 at 0x7bc>'
    r_m_25 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_25 at 0x7bd>'
    r_m_26 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_26 at 0x7be>'
    r_m_27 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_27 at 0x7bf>'
    r_m_28 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_28 at 0x7c0>'
    r_m_29 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_29 at 0x7c1>'
    r_m_3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_3 at 0x7c2>'
    r_m_30 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_30 at 0x7c3>'
    r_m_31 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_31 at 0x7c4>'
    r_m_4 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_4 at 0x7c5>'
    r_m_5 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_5 at 0x7c6>'
    r_m_6 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_6 at 0x7c7>'
    r_m_7 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_7 at 0x7c8>'
    r_m_8 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_8 at 0x7c9>'
    r_m_9 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_9 at 0x7ca>'
    r_m_every = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_every at 0x7cb>'
    r_m_every_fourth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_every_fourth at 0x7cc>'
    r_m_every_other = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_every_other at 0x7cd>'
    r_m_every_sixth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_every_sixth at 0x7ce>'
    r_m_every_third = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_every_third at 0x7cf>'
    r_m_last = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_m_last at 0x7d0>'
    r_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_memo at 0x7d1>'
    r_monthly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_monthly at 0x7d2>'
    r_new_b = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_new_b at 0x7d3>'
    r_new_t = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_new_t at 0x7d4>'
    r_no_overdue = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_no_overdue at 0x7d5>'
    r_no_upcoming = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_no_upcoming at 0x7d6>'
    r_not_win = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_not_win at 0x7d7>'
    r_remove = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_remove at 0x7d8>'
    r_rpt_yearly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_rpt_yearly at 0x7d9>'
    r_t_ack = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_t_ack at 0x7da>'
    r_t_defer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_t_defer at 0x7db>'
    r_t_ign = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_t_ign at 0x7dc>'
    r_txn_editwin = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_txn_editwin at 0x7dd>'
    r_txn_err1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_txn_err1 at 0x7de>'
    r_txn_err2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_txn_err2 at 0x7df>'
    r_txn_err3 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_txn_err3 at 0x7e0>'
    r_txn_primacct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_txn_primacct at 0x7e1>'
    r_txn_secacct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_txn_secacct at 0x7e2>'
    r_w = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w at 0x7e3>'
    r_w_every = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_every at 0x7e4>'
    r_w_fifth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_fifth at 0x7e5>'
    r_w_first = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_first at 0x7e6>'
    r_w_fourth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_fourth at 0x7e7>'
    r_w_last = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_last at 0x7e8>'
    r_w_second = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_second at 0x7e9>'
    r_w_third = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_w_third at 0x7ea>'
    r_weekly = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.r_weekly at 0x7eb>'
    rating_no = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rating_no at 0x7ec>'
    rating_no_never = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rating_no_never at 0x7ed>'
    rating_no_not_now = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rating_no_not_now at 0x7ee>'
    rating_no_not_this_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rating_no_not_this_version at 0x7ef>'
    rating_yes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rating_yes at 0x7f0>'
    rec_as_of_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_as_of_desc at 0x7f1>'
    rec_begin_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_begin_balance at 0x7f2>'
    rec_cancel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_cancel at 0x7f3>'
    rec_credits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_credits at 0x7f4>'
    rec_curr_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_curr_bal at 0x7f5>'
    rec_debits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_debits at 0x7f6>'
    rec_delete_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_delete_txn at 0x7f7>'
    rec_delete_txn_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_delete_txn_q at 0x7f8>'
    rec_diff = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_diff at 0x7f9>'
    rec_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_done at 0x7fa>'
    rec_edit_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_edit_txn at 0x7fb>'
    rec_end_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_end_bal at 0x7fc>'
    rec_end_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_end_balance at 0x7fd>'
    rec_new_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_new_txn at 0x7fe>'
    rec_start_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_start_bal at 0x7ff>'
    rec_target_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_target_bal at 0x800>'
    rec_txn_functions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rec_txn_functions at 0x801>'
    received_n_new_txns_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.received_n_new_txns_for_acct at 0x802>'
    received_one_new_txn_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.received_one_new_txn_for_acct at 0x803>'
    received_sync_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.received_sync_data at 0x804>'
    received_zero_new_txns_for_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.received_zero_new_txns_for_acct at 0x805>'
    receiving_sync_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.receiving_sync_data at 0x806>'
    reconcile = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reconcile at 0x807>'
    reconcile_header = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reconcile_header at 0x808>'
    reconcile_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reconcile_win_title at 0x809>'
    reconciling = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reconciling at 0x80a>'
    record_next_occurrence = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.record_next_occurrence at 0x80b>'
    record_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.record_txn at 0x80c>'
    redLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redLabel at 0x80d>'
    redo_add_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_add_item at 0x80e>'
    redo_add_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_add_items at 0x80f>'
    redo_add_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_add_txn at 0x810>'
    redo_add_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_add_txns at 0x811>'
    redo_del_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_del_item at 0x812>'
    redo_del_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_del_items at 0x813>'
    redo_del_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_del_txn at 0x814>'
    redo_del_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_del_txns at 0x815>'
    redo_mod_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_mod_item at 0x816>'
    redo_mod_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_mod_items at 0x817>'
    redo_mod_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_mod_txn at 0x818>'
    redo_mod_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.redo_mod_txns at 0x819>'
    refresh = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.refresh at 0x81a>'
    reg_later = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_later at 0x81b>'
    reg_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_message at 0x81c>'
    reg_message2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_message2 at 0x81d>'
    reg_never = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_never at 0x81e>'
    reg_no_response = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_no_response at 0x81f>'
    reg_notice = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_notice at 0x820>'
    reg_notice2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_notice2 at 0x821>'
    reg_now = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_now at 0x822>'
    reg_window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reg_window at 0x823>'
    reinvest = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reinvest at 0x824>'
    reinvested = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reinvested at 0x825>'
    remember_this_choice = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.remember_this_choice at 0x826>'
    reminders___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reminders___ at 0x827>'
    remove = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.remove at 0x828>'
    remove___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.remove___ at 0x829>'
    remove_archived_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.remove_archived_txns at 0x82a>'
    remove_from_sidebar = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.remove_from_sidebar at 0x82b>'
    remove_sidebar_dlg_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.remove_sidebar_dlg_title at 0x82c>'
    rename___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rename___ at 0x82d>'
    repair = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.repair at 0x82e>'
    repeat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.repeat at 0x82f>'
    repeat_manually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.repeat_manually at 0x830>'
    repeat_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.repeat_none at 0x831>'
    repeat_until_end_of_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.repeat_until_end_of_year at 0x832>'
    repeat_until_eoy = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.repeat_until_eoy at 0x833>'
    report = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report at 0x834>'
    report___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report___ at 0x835>'
    report_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_account at 0x836>'
    report_asofdate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_asofdate at 0x837>'
    report_balances = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_balances at 0x838>'
    report_begindate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_begindate at 0x839>'
    report_blank_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_blank_category at 0x83a>'
    report_blank_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_blank_checknum at 0x83b>'
    report_blank_fee_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_blank_fee_category at 0x83c>'
    report_blank_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_blank_payee at 0x83d>'
    report_blank_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_blank_security at 0x83e>'
    report_budget = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_budget at 0x83f>'
    report_budget_show_zeroes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_budget_show_zeroes at 0x840>'
    report_capital_gains = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_capital_gains at 0x841>'
    report_cash_flow = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_cash_flow at 0x842>'
    report_cat_transfers = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_cat_transfers at 0x843>'
    report_cost_basis = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_cost_basis at 0x844>'
    report_detailed_cash_flow = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_detailed_cash_flow at 0x845>'
    report_detailed_income_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_detailed_income_expenses at 0x846>'
    report_detailed_transfers = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_detailed_transfers at 0x847>'
    report_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_done at 0x848>'
    report_enddate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_enddate at 0x849>'
    report_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_expenses at 0x84a>'
    report_generated = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_generated at 0x84b>'
    report_ie_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_ie_total at 0x84c>'
    report_include_allcats = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_include_allcats at 0x84d>'
    report_include_categories = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_include_categories at 0x84e>'
    report_income = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_income at 0x84f>'
    report_income_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_income_expenses at 0x850>'
    report_incomes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_incomes at 0x851>'
    report_invest_perf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_invest_perf at 0x852>'
    report_invest_portfolio = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_invest_portfolio at 0x853>'
    report_invest_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_invest_txn at 0x854>'
    report_landscape = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_landscape at 0x855>'
    report_memorize = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_memorize at 0x856>'
    report_memorize_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_memorize_title at 0x857>'
    report_missingchecks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_missingchecks at 0x858>'
    report_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_name at 0x859>'
    report_noncat_transfers = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_noncat_transfers at 0x85a>'
    report_other_suffix = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_other_suffix at 0x85b>'
    report_page_footer = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_page_footer at 0x85c>'
    report_print = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_print at 0x85d>'
    report_reconciliation = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_reconciliation at 0x85e>'
    report_save = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_save at 0x85f>'
    report_search = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_search at 0x860>'
    report_show_all_acct_types = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_show_all_acct_types at 0x861>'
    report_show_all_accts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_show_all_accts at 0x862>'
    report_subtotal_cats = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotal_cats at 0x863>'
    report_subtotal_for = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotal_for at 0x864>'
    report_subtotalby_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_account at 0x865>'
    report_subtotalby_action = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_action at 0x866>'
    report_subtotalby_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_category at 0x867>'
    report_subtotalby_chknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_chknum at 0x868>'
    report_subtotalby_day = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_day at 0x869>'
    report_subtotalby_fee_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_fee_category at 0x86a>'
    report_subtotalby_fquarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_fquarter at 0x86b>'
    report_subtotalby_fyear = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_fyear at 0x86c>'
    report_subtotalby_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_month at 0x86d>'
    report_subtotalby_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_none at 0x86e>'
    report_subtotalby_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_payee at 0x86f>'
    report_subtotalby_quarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_quarter at 0x870>'
    report_subtotalby_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_security at 0x871>'
    report_subtotalby_week = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_week at 0x872>'
    report_subtotalby_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotalby_year at 0x873>'
    report_subtotallabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_subtotallabel at 0x874>'
    report_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_total at 0x875>'
    report_total_suffix = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_total_suffix at 0x876>'
    report_transactions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_transactions at 0x877>'
    report_transfers = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_transfers at 0x878>'
    report_txn_search = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_txn_search at 0x879>'
    report_txn_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_txn_tag at 0x87a>'
    report_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_type at 0x87b>'
    report_update = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_update at 0x87c>'
    report_vat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_vat at 0x87d>'
    report_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_win_title at 0x87e>'
    report_xfer_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.report_xfer_total at 0x87f>'
    reports = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reports at 0x880>'
    req_field = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.req_field at 0x881>'
    reset = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reset at 0x882>'
    reset_sync_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reset_sync_date at 0x883>'
    reset_to_default = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.reset_to_default at 0x884>'
    resource_error = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.resource_error at 0x885>'
    restore_button = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.restore_button at 0x886>'
    restore_keep_sync_settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.restore_keep_sync_settings at 0x887>'
    restore_keep_sync_settings_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.restore_keep_sync_settings_desc at 0x888>'
    restore_message = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.restore_message at 0x889>'
    restore_settings_on_startup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.restore_settings_on_startup at 0x88a>'
    right_panels = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.right_panels at 0x88b>'
    rpt_mischcks_0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rpt_mischcks_0 at 0x88c>'
    rpt_mischcks_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rpt_mischcks_1 at 0x88d>'
    rpt_mischcks_2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.rpt_mischcks_2 at 0x88e>'
    run_python_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.run_python_title at 0x88f>'
    run_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.run_script at 0x890>'
    run_snippet = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.run_snippet at 0x891>'
    satLabel = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.satLabel at 0x892>'
    sat_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sat_s at 0x893>'
    save = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save at 0x894>'
    save_as___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_as___ at 0x895>'
    save_backup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_backup at 0x896>'
    save_changes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_changes at 0x897>'
    save_changes_question = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_changes_question at 0x898>'
    save_done = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_done at 0x899>'
    save_eq = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_eq at 0x89a>'
    save_graph_err = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_graph_err at 0x89b>'
    save_txn_changes_q = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_txn_changes_q at 0x89c>'
    save_txn_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.save_txn_title at 0x89d>'
    saving_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.saving_file at 0x89e>'
    scanning_data = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.scanning_data at 0x89f>'
    scenario_a = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.scenario_a at 0x8a0>'
    scenario_b = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.scenario_b at 0x8a1>'
    sch_f_d = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sch_f_d at 0x8a2>'
    sch_l_d = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sch_l_d at 0x8a3>'
    scheduled_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.scheduled_items at 0x8a4>'
    screen_bottom = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.screen_bottom at 0x8a5>'
    screen_left = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.screen_left at 0x8a6>'
    screen_right = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.screen_right at 0x8a7>'
    screen_top = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.screen_top at 0x8a8>'
    script_tool = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.script_tool at 0x8a9>'
    search_this_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.search_this_acct at 0x8aa>'
    sec = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec at 0x8ab>'
    sec_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_account at 0x8ac>'
    sec_already_created = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_already_created at 0x8ad>'
    sec_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_amount at 0x8ae>'
    sec_bankregister_view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_bankregister_view at 0x8af>'
    sec_bond = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_bond at 0x8b0>'
    sec_broker = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_broker at 0x8b1>'
    sec_buy = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_buy at 0x8b2>'
    sec_buy_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_buy_txn at 0x8b3>'
    sec_buywhenshort_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_buywhenshort_msg at 0x8b4>'
    sec_cd = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_cd at 0x8b5>'
    sec_comments = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_comments at 0x8b6>'
    sec_commission = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_commission at 0x8b7>'
    sec_cost_basis = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_cost_basis at 0x8b8>'
    sec_cover_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_cover_txn at 0x8b9>'
    sec_current_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_current_price at 0x8ba>'
    sec_dayhigh = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_dayhigh at 0x8bb>'
    sec_daylow = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_daylow at 0x8bc>'
    sec_del = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_del at 0x8bd>'
    sec_del_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_del_security at 0x8be>'
    sec_divdnd_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_divdnd_txn at 0x8bf>'
    sec_divreinvest_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_divreinvest_txn at 0x8c0>'
    sec_edit_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_edit_security at 0x8c1>'
    sec_exchange = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_exchange at 0x8c2>'
    sec_gain_loss_pcnt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_gain_loss_pcnt at 0x8c3>'
    sec_hist = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_hist at 0x8c4>'
    sec_last_trade = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_last_trade at 0x8c5>'
    sec_misc_inc_exp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_misc_inc_exp at 0x8c6>'
    sec_miscexp_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_miscexp_txn at 0x8c7>'
    sec_miscinc_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_miscinc_txn at 0x8c8>'
    sec_mutual = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_mutual at 0x8c9>'
    sec_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_name at 0x8ca>'
    sec_new_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_new_price at 0x8cb>'
    sec_new_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_new_security at 0x8cc>'
    sec_news = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_news at 0x8cd>'
    sec_nothing_to_split = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_nothing_to_split at 0x8ce>'
    sec_num_shares = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_num_shares at 0x8cf>'
    sec_option = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_option at 0x8d0>'
    sec_other = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_other at 0x8d1>'
    sec_overcover_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_overcover_msg at 0x8d2>'
    sec_oversell_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_oversell_msg at 0x8d3>'
    sec_perf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_perf at 0x8d4>'
    sec_phone = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_phone at 0x8d5>'
    sec_portfolio_for = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_portfolio_for at 0x8d6>'
    sec_portfolio_view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_portfolio_view at 0x8d7>'
    sec_positivecover_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_positivecover_msg at 0x8d8>'
    sec_positiveshort_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_positiveshort_msg at 0x8d9>'
    sec_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_price at 0x8da>'
    sec_price_share = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_price_share at 0x8db>'
    sec_register_view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_register_view at 0x8dc>'
    sec_secdetail_view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_secdetail_view at 0x8dd>'
    sec_sell = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_sell at 0x8de>'
    sec_sell_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_sell_txn at 0x8df>'
    sec_shares = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_shares at 0x8e0>'
    sec_shares_in = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_shares_in at 0x8e1>'
    sec_short_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_short_txn at 0x8e2>'
    sec_split = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split at 0x8e3>'
    sec_split_for = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split_for at 0x8e4>'
    sec_split_in = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split_in at 0x8e5>'
    sec_split_new_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split_new_price at 0x8e6>'
    sec_split_new_shares = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split_new_shares at 0x8e7>'
    sec_split_old_shares = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split_old_shares at 0x8e8>'
    sec_split_out = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_split_out at 0x8e9>'
    sec_stk_divdnd_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_stk_divdnd_txn at 0x8ea>'
    sec_stock = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_stock at 0x8eb>'
    sec_subtype = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_subtype at 0x8ec>'
    sec_tickersym = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_tickersym at 0x8ed>'
    sec_transfer_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_transfer_txn at 0x8ee>'
    sec_txn_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_txn_type at 0x8ef>'
    sec_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_type at 0x8f0>'
    sec_unknown_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_unknown_txn at 0x8f1>'
    sec_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_value at 0x8f2>'
    sec_vol = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_vol at 0x8f3>'
    sec_xfr_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfr_acct at 0x8f4>'
    sec_xfr_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfr_rate at 0x8f5>'
    sec_xfrbuy_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfrbuy_txn at 0x8f6>'
    sec_xfrdivdnd_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfrdivdnd_txn at 0x8f7>'
    sec_xfrin_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfrin_txn at 0x8f8>'
    sec_xfrout_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfrout_txn at 0x8f9>'
    sec_xfrsell_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sec_xfrsell_txn at 0x8fa>'
    secondary_currency_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.secondary_currency_type at 0x8fb>'
    securities = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.securities at 0x8fc>'
    security_id = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.security_id at 0x8fd>'
    security_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.security_price at 0x8fe>'
    security_price_history = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.security_price_history at 0x8ff>'
    seek_to_recorded_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.seek_to_recorded_txns at 0x900>'
    sel_accts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sel_accts at 0x901>'
    sel_categories = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sel_categories at 0x902>'
    selby_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selby_acct at 0x903>'
    selby_acct_both = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selby_acct_both at 0x904>'
    selby_acct_cat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selby_acct_cat at 0x905>'
    selby_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selby_type at 0x906>'
    selby_type_both = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selby_type_both at 0x907>'
    selby_type_cat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selby_type_cat at 0x908>'
    select = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select at 0x909>'
    select_acct_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_acct_title at 0x90a>'
    select_acct_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_acct_type at 0x90b>'
    select_acct_wnum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_acct_wnum at 0x90c>'
    select_backup_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_backup_file at 0x90d>'
    select_browser_executable = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_browser_executable at 0x90e>'
    select_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_checks at 0x90f>'
    select_currency_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_currency_type at 0x910>'
    select_or_add_security = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_or_add_security at 0x911>'
    select_or_create_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_or_create_script at 0x912>'
    select_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_payee at 0x913>'
    select_qem_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.select_qem_file at 0x914>'
    selected_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selected_checks at 0x915>'
    selection = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selection at 0x916>'
    selection_details_view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selection_details_view at 0x917>'
    selection_details_view_inwindow = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selection_details_view_inwindow at 0x918>'
    selection_details_view_separate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selection_details_view_separate at 0x919>'
    selector_add = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_add at 0x91a>'
    selector_addall = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_addall at 0x91b>'
    selector_addexcept = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_addexcept at 0x91c>'
    selector_advanced = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_advanced at 0x91d>'
    selector_basic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_basic at 0x91e>'
    selector_remove = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_remove at 0x91f>'
    selector_removeall = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_removeall at 0x920>'
    selector_removeexcept = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_removeexcept at 0x921>'
    selector_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.selector_title at 0x922>'
    sell_invalid = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sell_invalid at 0x923>'
    sell_long_term = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sell_long_term at 0x924>'
    sell_short = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sell_short at 0x925>'
    sell_short_term = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sell_short_term at 0x926>'
    send_online_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.send_online_pmt at 0x927>'
    send_payment = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.send_payment at 0x928>'
    send_pmt_menu = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.send_pmt_menu at 0x929>'
    send_pmt_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.send_pmt_to at 0x92a>'
    seprt_tax_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.seprt_tax_date at 0x92b>'
    september = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.september at 0x92c>'
    set_as_default = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.set_as_default at 0x92d>'
    set_base_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.set_base_currency at 0x92e>'
    set_cleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.set_cleared at 0x92f>'
    set_reconciling = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.set_reconciling at 0x930>'
    set_uncleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.set_uncleared at 0x931>'
    settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.settings at 0x932>'
    settingsTitle_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.settingsTitle_text at 0x933>'
    setup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.setup at 0x934>'
    shared_file_warning_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shared_file_warning_title at 0x935>'
    shares_allocated = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shares_allocated at 0x936>'
    shares_available = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shares_available at 0x937>'
    shares_available_fmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shares_available_fmt at 0x938>'
    shares_remaining = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shares_remaining at 0x939>'
    shares_sold = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shares_sold at 0x93a>'
    shortcuts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shortcuts at 0x93b>'
    show = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show at 0x93c>'
    showFullCat_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.showFullCat_text at 0x93d>'
    show_3d = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_3d at 0x93e>'
    show_all_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_all_accounts at 0x93f>'
    show_archive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_archive at 0x940>'
    show_average_doublecat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_average_doublecat at 0x941>'
    show_docs_folder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_docs_folder at 0x942>'
    show_file_location = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_file_location at 0x943>'
    show_full_account_path = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_full_account_path at 0x944>'
    show_hint = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_hint at 0x945>'
    show_ie_in_popup = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_ie_in_popup at 0x946>'
    show_in_finder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_in_finder at 0x947>'
    show_legend = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_legend at 0x948>'
    show_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_memo at 0x949>'
    show_moneybot_console = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_moneybot_console at 0x94a>'
    show_on_hp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_on_hp at 0x94b>'
    show_on_open_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_on_open_label at 0x94c>'
    show_onlbs = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_onlbs at 0x94d>'
    show_online_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_online_txns at 0x94e>'
    show_onlmail = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_onlmail at 0x94f>'
    show_onlpayees = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_onlpayees at 0x950>'
    show_other_side = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_other_side at 0x951>'
    show_python_console = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_python_console at 0x952>'
    show_source_code = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_source_code at 0x953>'
    show_source_list = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_source_list at 0x954>'
    show_splits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_splits at 0x955>'
    show_two_lines = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_two_lines at 0x956>'
    show_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_txn at 0x957>'
    show_unrealized = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_unrealized at 0x958>'
    show_upcoming_one_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_upcoming_one_month at 0x959>'
    show_upcoming_this_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_upcoming_this_month at 0x95a>'
    show_upcoming_two_weeks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_upcoming_two_weeks at 0x95b>'
    show_welcome_screen = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_welcome_screen at 0x95c>'
    show_xml = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_xml at 0x95d>'
    show_zero_bal_accts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.show_zero_bal_accts at 0x95e>'
    shutting_down = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.shutting_down at 0x95f>'
    sidebar_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sidebar_balance at 0x960>'
    similar_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.similar_txns at 0x961>'
    similar_txns_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.similar_txns_description at 0x962>'
    since_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.since_date at 0x963>'
    since_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.since_x at 0x964>'
    skip_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.skip_txn at 0x965>'
    sort_ascending = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sort_ascending at 0x966>'
    sort_by = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sort_by at 0x967>'
    sortby_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_account at 0x968>'
    sortby_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_amount at 0x969>'
    sortby_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_checknum at 0x96a>'
    sortby_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_date at 0x96b>'
    sortby_date_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_date_amount at 0x96c>'
    sortby_date_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_date_checknum at 0x96d>'
    sortby_date_entered = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_date_entered at 0x96e>'
    sortby_date_status = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_date_status at 0x96f>'
    sortby_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_description at 0x970>'
    sortby_status = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_status at 0x971>'
    sortby_status_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sortby_status_checknum at 0x972>'
    source_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.source_accounts at 0x973>'
    source_of_funds = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.source_of_funds at 0x974>'
    specify_manually = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.specify_manually at 0x975>'
    specify_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.specify_pmt at 0x976>'
    split = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split at 0x977>'
    split_acct_conflict = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split_acct_conflict at 0x978>'
    split_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split_label at 0x979>'
    split_label1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split_label1 at 0x97a>'
    split_label2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split_label2 at 0x97b>'
    split_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split_txn at 0x97c>'
    split_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.split_win_title at 0x97d>'
    srch = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch at 0x97e>'
    srch_by_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_acct at 0x97f>'
    srch_by_amt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_amt at 0x980>'
    srch_by_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_checknum at 0x981>'
    srch_by_cleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_cleared at 0x982>'
    srch_by_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_date at 0x983>'
    srch_by_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_desc at 0x984>'
    srch_by_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_memo at 0x985>'
    srch_by_tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_by_tag at 0x986>'
    srch_op_intersect = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_op_intersect at 0x987>'
    srch_op_union = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_op_union at 0x988>'
    srch_range0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_range0 at 0x989>'
    srch_range1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_range1 at 0x98a>'
    srch_range2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_range2 at 0x98b>'
    srch_use_tax_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.srch_use_tax_date at 0x98c>'
    stable_releases = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stable_releases at 0x98d>'
    stacked = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stacked at 0x98e>'
    standard = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.standard at 0x98f>'
    start_bal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.start_bal at 0x990>'
    starting_on_date_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.starting_on_date_x at 0x991>'
    state = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.state at 0x992>'
    status = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.status at 0x993>'
    stockSubType_growth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stockSubType_growth at 0x994>'
    stockSubType_largecap = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stockSubType_largecap at 0x995>'
    stockSubType_midcap = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stockSubType_midcap at 0x996>'
    stockSubType_smallcap = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stockSubType_smallcap at 0x997>'
    stockSubType_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stockSubType_value at 0x998>'
    stop_script = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.stop_script at 0x999>'
    store_passwords = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.store_passwords at 0x99a>'
    strike_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.strike_price at 0x99b>'
    submit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.submit at 0x99c>'
    subtype_inuse_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.subtype_inuse_tip at 0x99d>'
    summary = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.summary at 0x99e>'
    summary_page = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.summary_page at 0x99f>'
    sun_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sun_s at 0x9a0>'
    sync_add_device = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_add_device at 0x9a1>'
    sync_change_pass = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_change_pass at 0x9a2>'
    sync_change_pass_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_change_pass_msg at 0x9a3>'
    sync_enc_pass = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_enc_pass at 0x9a4>'
    sync_enter_pass_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_enter_pass_msg at 0x9a5>'
    sync_enter_pass_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_enter_pass_title at 0x9a6>'
    sync_error_secondary_with_no_sync_method = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_error_secondary_with_no_sync_method at 0x9a7>'
    sync_here_is_your_passwd = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_here_is_your_passwd at 0x9a8>'
    sync_method = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method at 0x9a9>'
    sync_method_dropbox_api = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method_dropbox_api at 0x9aa>'
    sync_method_dropbox_folder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method_dropbox_folder at 0x9ab>'
    sync_method_iclouddrive = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method_iclouddrive at 0x9ac>'
    sync_method_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method_none at 0x9ad>'
    sync_method_select_shared_folder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method_select_shared_folder at 0x9ae>'
    sync_method_shared_folder = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_method_shared_folder at 0x9af>'
    sync_pass_label = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_pass_label at 0x9b0>'
    sync_pass_show = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_pass_show at 0x9b1>'
    sync_password_entry_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_password_entry_msg at 0x9b2>'
    sync_remove_device = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_remove_device at 0x9b3>'
    sync_start = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_start at 0x9b4>'
    sync_stop = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_stop at 0x9b5>'
    sync_tax_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_tax_date at 0x9b6>'
    sync_window_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.sync_window_title at 0x9b7>'
    synced_as_of_x = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.synced_as_of_x at 0x9b8>'
    syncing___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.syncing___ at 0x9b9>'
    table_column_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_account at 0x9ba>'
    table_column_account_action = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_account_action at 0x9bb>'
    table_column_action = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_action at 0x9bc>'
    table_column_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_amount at 0x9bd>'
    table_column_annual_return = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_annual_return at 0x9be>'
    table_column_balance = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_balance at 0x9bf>'
    table_column_balance_due = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_balance_due at 0x9c0>'
    table_column_buys = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_buys at 0x9c1>'
    table_column_cashbal = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_cashbal at 0x9c2>'
    table_column_category = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_category at 0x9c3>'
    table_column_cc_charge = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_cc_charge at 0x9c4>'
    table_column_cc_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_cc_pmt at 0x9c5>'
    table_column_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_checknum at 0x9c6>'
    table_column_clearedchar = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_clearedchar at 0x9c7>'
    table_column_cost_basis = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_cost_basis at 0x9c8>'
    table_column_credit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_credit at 0x9c9>'
    table_column_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_date at 0x9ca>'
    table_column_debit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_debit at 0x9cb>'
    table_column_decrease = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_decrease at 0x9cc>'
    table_column_description = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_description at 0x9cd>'
    table_column_fee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_fee at 0x9ce>'
    table_column_feecat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_feecat at 0x9cf>'
    table_column_feerate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_feerate at 0x9d0>'
    table_column_gains = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_gains at 0x9d1>'
    table_column_gross = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_gross at 0x9d2>'
    table_column_increase = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_increase at 0x9d3>'
    table_column_interval = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_interval at 0x9d4>'
    table_column_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_memo at 0x9d5>'
    table_column_net = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_net at 0x9d6>'
    table_column_price = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_price at 0x9d7>'
    table_column_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_rate at 0x9d8>'
    table_column_return_period = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_return_period at 0x9d9>'
    table_column_return_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_return_rate at 0x9da>'
    table_column_roi_1yr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_roi_1yr at 0x9db>'
    table_column_roi_3yr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_roi_3yr at 0x9dc>'
    table_column_roi_5yr = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_roi_5yr at 0x9dd>'
    table_column_roi_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_roi_all at 0x9de>'
    table_column_running_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_running_total at 0x9df>'
    table_column_sale_curr_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_sale_curr_value at 0x9e0>'
    table_column_sales = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_sales at 0x9e1>'
    table_column_shares = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_shares at 0x9e2>'
    table_column_source = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_source at 0x9e3>'
    table_column_source_dest = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_source_dest at 0x9e4>'
    table_column_splitratio = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_splitratio at 0x9e5>'
    table_column_tags = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_tags at 0x9e6>'
    table_column_target = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_target at 0x9e7>'
    table_column_taxdate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_taxdate at 0x9e8>'
    table_column_ticker = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_ticker at 0x9e9>'
    table_column_vat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_column_vat at 0x9ea>'
    table_payment_number = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.table_payment_number at 0x9eb>'
    tag = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tag at 0x9ec>'
    tag_in_use_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tag_in_use_msg at 0x9ed>'
    tag_inuse_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tag_inuse_tip at 0x9ee>'
    target_accounts = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.target_accounts at 0x9ef>'
    tax_related = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tax_related at 0x9f0>'
    text_snippet = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.text_snippet at 0x9f1>'
    tfr_from_loan = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tfr_from_loan at 0x9f2>'
    theme_change_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_change_msg at 0x9f3>'
    theme_name = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name at 0x9f4>'
    theme_name_classic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_classic at 0x9f5>'
    theme_name_custom = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_custom at 0x9f6>'
    theme_name_darcula = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_darcula at 0x9f7>'
    theme_name_dark = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_dark at 0x9f8>'
    theme_name_default = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_default at 0x9f9>'
    theme_name_high_contrast = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_high_contrast at 0x9fa>'
    theme_name_light = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_light at 0x9fb>'
    theme_name_mac_dark_mode = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_mac_dark_mode at 0x9fc>'
    theme_name_solarized_dark = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_solarized_dark at 0x9fd>'
    theme_name_solarized_light = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.theme_name_solarized_light at 0x9fe>'
    this_fiscal_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.this_fiscal_year at 0x9ff>'
    this_month = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.this_month at 0xa00>'
    this_quarter = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.this_quarter at 0xa01>'
    this_week = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.this_week at 0xa02>'
    this_year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.this_year at 0xa03>'
    three = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.three at 0xa04>'
    thu_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.thu_s at 0xa05>'
    time_format = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.time_format at 0xa06>'
    title_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.title_text at 0xa07>'
    tkr_location = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tkr_location at 0xa08>'
    tkr_nowhere = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tkr_nowhere at 0xa09>'
    to_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.to_acct at 0xa0a>'
    to_be_printed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.to_be_printed at 0xa0b>'
    to_currency = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.to_currency at 0xa0c>'
    to_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.to_file at 0xa0d>'
    to_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.to_payee at 0xa0e>'
    today = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.today at 0xa0f>'
    too_many_accts_wtype = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.too_many_accts_wtype at 0xa10>'
    tools = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tools at 0xa11>'
    tools_address_book = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tools_address_book at 0xa12>'
    tools_calc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tools_calc at 0xa13>'
    tools_exp_vat_editor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tools_exp_vat_editor at 0xa14>'
    tools_loan_calc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tools_loan_calc at 0xa15>'
    tools_normal_calc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tools_normal_calc at 0xa16>'
    tot_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tot_pmt at 0xa17>'
    total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.total at 0xa18>'
    total_expenses = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.total_expenses at 0xa19>'
    total_from = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.total_from at 0xa1a>'
    total_income = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.total_income at 0xa1b>'
    total_to = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.total_to at 0xa1c>'
    transfers_in = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.transfers_in at 0xa1d>'
    transfers_out = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.transfers_out at 0xa1e>'
    translate_currencies___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.translate_currencies___ at 0xa1f>'
    translate_currency_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.translate_currency_win_title at 0xa20>'
    try_again = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.try_again at 0xa21>'
    tue_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.tue_s at 0xa22>'
    two = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.two at 0xa23>'
    two_line_mode = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.two_line_mode at 0xa24>'
    txn_account = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_account at 0xa25>'
    txn_amount = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_amount at 0xa26>'
    txn_checknum = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_checknum at 0xa27>'
    txn_credit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_credit at 0xa28>'
    txn_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_date at 0xa29>'
    txn_date_match_window_0 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_date_match_window_0 at 0xa2a>'
    txn_date_match_window_1 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_date_match_window_1 at 0xa2b>'
    txn_debit = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_debit at 0xa2c>'
    txn_details = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_details at 0xa2d>'
    txn_filter_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_all at 0xa2e>'
    txn_filter_cleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_cleared at 0xa2f>'
    txn_filter_combined = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_combined at 0xa30>'
    txn_filter_confirmed = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_confirmed at 0xa31>'
    txn_filter_divided = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_divided at 0xa32>'
    txn_filter_last30days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_last30days at 0xa33>'
    txn_filter_last60days = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_last60days at 0xa34>'
    txn_filter_new = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_new at 0xa35>'
    txn_filter_none = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_none at 0xa36>'
    txn_filter_thismonth = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_thismonth at 0xa37>'
    txn_filter_thisyear = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_thisyear at 0xa38>'
    txn_filter_uncleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_filter_uncleared at 0xa39>'
    txn_limit_info_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_limit_info_msg at 0xa3a>'
    txn_limit_msg2 = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_limit_msg2 at 0xa3b>'
    txn_memo = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_memo at 0xa3c>'
    txn_numsplits = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_numsplits at 0xa3d>'
    txn_originally = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_originally at 0xa3e>'
    txn_payee = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_payee at 0xa3f>'
    txn_rate = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_rate at 0xa40>'
    txn_split_error_a = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_split_error_a at 0xa41>'
    txn_status = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_status at 0xa42>'
    txn_tax_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.txn_tax_date at 0xa43>'
    type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.type at 0xa44>'
    unable_to_read_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unable_to_read_file at 0xa45>'
    unable_to_set_laf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unable_to_set_laf at 0xa46>'
    unable_to_update_extension_info = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unable_to_update_extension_info at 0xa47>'
    unable_to_update_passphrase = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unable_to_update_passphrase at 0xa48>'
    unclear_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unclear_all at 0xa49>'
    uncleared = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.uncleared at 0xa4a>'
    unconfirmed_total = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unconfirmed_total at 0xa4b>'
    unconfirmed_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unconfirmed_txns at 0xa4c>'
    under_mnemonic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.under_mnemonic at 0xa4d>'
    under_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.under_text at 0xa4e>'
    undo_add_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_add_item at 0xa4f>'
    undo_add_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_add_items at 0xa50>'
    undo_add_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_add_txn at 0xa51>'
    undo_add_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_add_txns at 0xa52>'
    undo_del_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_del_item at 0xa53>'
    undo_del_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_del_items at 0xa54>'
    undo_del_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_del_txn at 0xa55>'
    undo_del_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_del_txns at 0xa56>'
    undo_mod_item = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_mod_item at 0xa57>'
    undo_mod_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_mod_items at 0xa58>'
    undo_mod_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_mod_txn at 0xa59>'
    undo_mod_txns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.undo_mod_txns at 0xa5a>'
    unknown = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unknown at 0xa5b>'
    unknown_file_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unknown_file_type at 0xa5c>'
    unknown_txn_correction = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unknown_txn_correction at 0xa5d>'
    unknown_txn_type = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unknown_txn_type at 0xa5e>'
    unmerge_txn = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unmerge_txn at 0xa5f>'
    unmerge_txn_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unmerge_txn_desc at 0xa60>'
    unmerge_txns_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unmerge_txns_desc at 0xa61>'
    unregistered = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unregistered at 0xa62>'
    unsigned_ext_uninstall = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unsigned_ext_uninstall at 0xa63>'
    unsigned_ext_warning_short = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.unsigned_ext_warning_short at 0xa64>'
    untitled = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.untitled at 0xa65>'
    up = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.up at 0xa66>'
    up_to_date_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.up_to_date_msg at 0xa67>'
    upcoming = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.upcoming at 0xa68>'
    upcoming_items = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.upcoming_items at 0xa69>'
    upcoming_pmt = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.upcoming_pmt at 0xa6a>'
    update = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update at 0xa6b>'
    update_all = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_all at 0xa6c>'
    update_available_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_available_msg at 0xa6d>'
    update_dont_check = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_dont_check at 0xa6e>'
    update_ext_msg = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_ext_msg at 0xa6f>'
    update_from = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_from at 0xa70>'
    update_graph_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_graph_tip at 0xa71>'
    update_report_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.update_report_tip at 0xa72>'
    updateable_extensions = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.updateable_extensions at 0xa73>'
    updater = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.updater at 0xa74>'
    upgrade_win_title = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.upgrade_win_title at 0xa75>'
    upgrading_data___ = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.upgrading_data___ at 0xa76>'
    url = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.url at 0xa77>'
    use_bank_clearance_dates = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.use_bank_clearance_dates at 0xa78>'
    use_default_settings = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.use_default_settings at 0xa79>'
    use_proxy = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.use_proxy at 0xa7a>'
    use_tax_related = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.use_tax_related at 0xa7b>'
    use_vat = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.use_vat at 0xa7c>'
    username = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.username at 0xa7d>'
    vat_acct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vat_acct at 0xa7e>'
    vat_config_exp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vat_config_exp at 0xa7f>'
    vat_pct = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vat_pct at 0xa80>'
    vat_txns_editor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vat_txns_editor at 0xa81>'
    vat_txns_exp = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vat_txns_exp at 0xa82>'
    vendor = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vendor at 0xa83>'
    vendor_url = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.vendor_url at 0xa84>'
    version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.version at 0xa85>'
    view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.view at 0xa86>'
    voucher_checks = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.voucher_checks at 0xa87>'
    waiting_for_authorization = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.waiting_for_authorization at 0xa88>'
    warning = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.warning at 0xa89>'
    warning_mnemonic = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.warning_mnemonic at 0xa8a>'
    warning_text = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.warning_text at 0xa8b>'
    web_browser = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.web_browser at 0xa8c>'
    web_view = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.web_view at 0xa8d>'
    wed_s = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.wed_s at 0xa8e>'
    week = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.week at 0xa8f>'
    welcome_create_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_create_file at 0xa90>'
    welcome_create_file_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_create_file_desc at 0xa91>'
    welcome_get_help = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_get_help at 0xa92>'
    welcome_get_help_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_get_help_desc at 0xa93>'
    welcome_import_file = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_import_file at 0xa94>'
    welcome_import_file_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_import_file_desc at 0xa95>'
    welcome_import_qem = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_import_qem at 0xa96>'
    welcome_import_qem_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_import_qem_desc at 0xa97>'
    welcome_subscribe = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_subscribe at 0xa98>'
    welcome_subscribe_desc = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_subscribe_desc at 0xa99>'
    welcome_to_xxx = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_to_xxx at 0xa9a>'
    welcome_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.welcome_version at 0xa9b>'
    will_process = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.will_process at 0xa9c>'
    window = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.window at 0xa9d>'
    window_menu = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.window_menu at 0xa9e>'
    windows_laf = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.windows_laf at 0xa9f>'
    wrong_encryption_password_or_data_version = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.wrong_encryption_password_or_data_version at 0xaa0>'
    xtnsns = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.xtnsns at 0xaa1>'
    year = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.year at 0xaa2>'
    year_to_date = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.year_to_date at 0xaa3>'
    yes = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.yes at 0xaa4>'
    yes_emails = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.yes_emails at 0xaa5>'
    zero_bal_asof_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.zero_bal_asof_tip at 0xaa6>'
    zero_bal_preview_clear_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.zero_bal_preview_clear_tip at 0xaa7>'
    zero_bal_preview_tip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.zero_bal_preview_tip at 0xaa8>'
    zero_bond = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.zero_bond at 0xaa9>'
    zero_value = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.zero_value at 0xaaa>'
    zip = '<reflected field public java.lang.String com.moneydance.apps.md.view.gui.MDStrings.zip at 0xaab>'
    
    def __init__(self): ...
    
    def getKeys(self) -> Set[str]: ...
    
    @staticmethod
    def getSingleton() -> 'MDStrings': ...
    
    def getString(self, s: str, s2: str) -> str: ...
    
    def loadFromInfo(self, c: com.infinitekind.util.StreamTable) -> None: ...
    
    def loadFromStream(self, j: 'java.io.InputStream') -> None: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    @staticmethod
    def mainPrintCodeForStrings(list: List[str]) -> None: ...
    
    
class MDURLUtil:
    def __init__(self): ...
    
    @staticmethod
    def getBoolean(d: dict, s: str, b: bool) -> bool: ...
    
    @staticmethod
    def getDate(d: dict, s: str, i: int) -> int: ...
    
    @staticmethod
    def getInt(d: dict, s: str, i: int) -> int: ...
    
    @staticmethod
    def makeLink(j: 'javax.swing.JLabel', j2: 'javax.swing.Action') -> 'javax.swing.JLabel': ...
    
    @staticmethod
    def parseParams(s: str) -> com.infinitekind.tiksync.SyncRecord: ...
    
    @staticmethod
    def putDate(d: dict, s: str, i: int) -> None: ...
    
    
class MDUndoManager('javax.swing.undo.UndoManager', com.infinitekind.moneydance.model.UndoManagerInterface):
    def __init__(self, moneydanceGUI: 'MoneydanceGUI'): ...
    
    def addEdit(self, j: 'javax.swing.undo.UndoableEdit') -> bool: ...
    
    def addItem(self, c: com.infinitekind.moneydance.model.MoneydanceSyncableItem) -> com.infinitekind.moneydance.model.MoneydanceSyncableItem: ...
    
    def addItems(self, list: List[com.infinitekind.moneydance.model.MoneydanceSyncableItem]) -> List[com.infinitekind.moneydance.model.MoneydanceSyncableItem]: ...
    
    def deleteItem(self, c: com.infinitekind.moneydance.model.MoneydanceSyncableItem) -> None: ...
    
    def deleteItems(self, list: List[com.infinitekind.moneydance.model.MoneydanceSyncableItem]) -> None: ...
    
    def modifyItem(self, c: com.infinitekind.moneydance.model.MoneydanceSyncableItem, c2: com.infinitekind.moneydance.model.MoneydanceSyncableItem) -> None: ...
    
    def modifyItems(self, list: List[com.infinitekind.moneydance.model.MoneydanceSyncableItem], list2: List[com.infinitekind.moneydance.model.MoneydanceSyncableItem]) -> None: ...
    
    
class MDWindowListener:
    def __init__(self): ...
    
    def windowAdded(self, secondaryWindow: SecondaryWindow) -> None: ...
    
    def windowRemoved(self, secondaryWindow: SecondaryWindow) -> None: ...
    
    
class MainFrame(SecondaryFrame, com.infinitekind.moneydance.model.MDFileListener):
    pass
    
class MainMenu('java.awt.event.ActionListener', com.moneydance.apps.md.controller.PreferencesListener, com.moneydance.apps.md.controller.ModuleListener):
    acctDeleteAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.acctDeleteAction at 0xaac>'
    acctEditAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.acctEditAction at 0xaad>'
    acctNewAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.acctNewAction at 0xaae>'
    clearRecentFilesAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.clearRecentFilesAction at 0xaaf>'
    confirmSelectedTxnsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.confirmSelectedTxnsAction at 0xab0>'
    debugResetMenu = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.debugResetMenu at 0xab1>'
    downloadAllAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.downloadAllAction at 0xab2>'
    downloadTxnsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.downloadTxnsAction at 0xab3>'
    editAdvancedFindAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.editAdvancedFindAction at 0xab4>'
    editCopyAction = '<reflected field public javax.swing.Action com.moneydance.apps.md.view.gui.MainMenu.editCopyAction at 0xab5>'
    editCutAction = '<reflected field public javax.swing.Action com.moneydance.apps.md.view.gui.MainMenu.editCutAction at 0xab6>'
    editFindAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.editFindAction at 0xab7>'
    editPasteAction = '<reflected field public javax.swing.Action com.moneydance.apps.md.view.gui.MainMenu.editPasteAction at 0xab8>'
    editSelectAllAction = '<reflected field public javax.swing.Action com.moneydance.apps.md.view.gui.MainMenu.editSelectAllAction at 0xab9>'
    fileArchiveAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileArchiveAction at 0xaba>'
    fileEncryptionAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileEncryptionAction at 0xabb>'
    fileExportAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileExportAction at 0xabc>'
    fileImportBackupAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileImportBackupAction at 0xabd>'
    fileImportMDAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileImportMDAction at 0xabe>'
    fileNewAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileNewAction at 0xabf>'
    fileOpenOtherAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileOpenOtherAction at 0xac0>'
    filePreferencesAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.filePreferencesAction at 0xac1>'
    fileQuitAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileQuitAction at 0xac2>'
    fileSaveAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileSaveAction at 0xac3>'
    fileSaveBackupAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileSaveBackupAction at 0xac4>'
    fileSyncingAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.fileSyncingAction at 0xac5>'
    forgetPasswdsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.forgetPasswdsAction at 0xac6>'
    helpAboutAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpAboutAction at 0xac7>'
    helpCheckForUpdatesAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpCheckForUpdatesAction at 0xac8>'
    helpConsoleAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpConsoleAction at 0xac9>'
    helpLicenseAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpLicenseAction at 0xaca>'
    helpRegisterAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpRegisterAction at 0xacb>'
    helpShowArchiveAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpShowArchiveAction at 0xacc>'
    helpShowDocsFolderAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpShowDocsFolderAction at 0xacd>'
    helpSupportAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.helpSupportAction at 0xace>'
    manageExtsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.manageExtsAction at 0xacf>'
    minimizeWindowAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.minimizeWindowAction at 0xad0>'
    moneybotAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.moneybotAction at 0xad1>'
    moneybotKeystrokeAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.moneybotKeystrokeAction at 0xad2>'
    newTxnAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.newTxnAction at 0xad3>'
    onlineMDPlusAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.onlineMDPlusAction at 0xad4>'
    openWebsiteAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.openWebsiteAction at 0xad5>'
    printChecksAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.printChecksAction at 0xad6>'
    printSetupAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.printSetupAction at 0xad7>'
    printTxnsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.printTxnsAction at 0xad8>'
    reconcileAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.reconcileAction at 0xad9>'
    redoAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.redoAction at 0xada>'
    sendOnlineBPAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.sendOnlineBPAction at 0xadb>'
    setupOnlineAccountMapAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.setupOnlineAccountMapAction at 0xadc>'
    setupOnlineAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.setupOnlineAction at 0xadd>'
    setupOnlineBPAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.setupOnlineBPAction at 0xade>'
    showOnlineBPAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.showOnlineBPAction at 0xadf>'
    showWelcomeScreenAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.showWelcomeScreenAction at 0xae0>'
    toggleSourceListAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toggleSourceListAction at 0xae1>'
    toolsAddressBookAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsAddressBookAction at 0xae2>'
    toolsBudgetAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsBudgetAction at 0xae3>'
    toolsCOAAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsCOAAction at 0xae4>'
    toolsCategoriesAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsCategoriesAction at 0xae5>'
    toolsCurrencyAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsCurrencyAction at 0xae6>'
    toolsExpensesVATEditorAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsExpensesVATEditorAction at 0xae7>'
    toolsLoanCalcAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsLoanCalcAction at 0xae8>'
    toolsNormalCalcAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsNormalCalcAction at 0xae9>'
    toolsRemindersAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsRemindersAction at 0xaea>'
    toolsReportsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsReportsAction at 0xaeb>'
    toolsSecuritiesAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsSecuritiesAction at 0xaec>'
    toolsTranslateCurrencyAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsTranslateCurrencyAction at 0xaed>'
    toolsVATTxnsAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.toolsVATTxnsAction at 0xaee>'
    undoAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.undoAction at 0xaef>'
    viewDBBudget = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.viewDBBudget at 0xaf0>'
    viewDBNetWorth = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.viewDBNetWorth at 0xaf1>'
    viewDBNothing = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.viewDBNothing at 0xaf2>'
    viewHomeAction = '<reflected field public com.moneydance.apps.md.view.gui.MDAction com.moneydance.apps.md.view.gui.MainMenu.viewHomeAction at 0xaf3>'
    viewSourceListItem = '<reflected field public javax.swing.JMenuItem com.moneydance.apps.md.view.gui.MainMenu.viewSourceListItem at 0xaf4>'
    
    def __init__(self, moneydanceGUI: 'MoneydanceGUI', secondaryFrame: SecondaryFrame): ...
    
    def actionPerformed(self, j: 'java.awt.event.ActionEvent') -> None: ...
    
    def createAccount(self) -> None: ...
    
    def deleteAccount(self) -> None: ...
    
    def editAccount(self) -> None: ...
    
    def goneAway(self) -> None: ...
    
    def moduleListUpdated(self) -> None: ...
    
    def preferencesUpdated(self) -> None: ...
    
    def updateOpenFilesMenu(self) -> None: ...
    
    def updateWindows(self) -> None: ...
    
    def windowAdded(self, secondaryWindow: SecondaryWindow) -> None: ...
    
    def windowRemoved(self, secondaryWindow: SecondaryWindow) -> None: ...
    
    
class MigrateFileWindow(SecondaryDialog):
    pass
    
class ModuleInfoWindow(SecondaryDialog, OKButtonListener):
    pass
    
class MoneydanceGUI(com.moneydance.apps.md.view.MoneydanceUI, com.moneydance.apps.md.controller.PreferencesListener, Callable, com.moneydance.security.SecretKeyCallback):
    ACCELERATOR_MASK = 4
    ACCELERATOR_MASK_STR = u'\u2318'
    drawMacNative = True
    isLinux = False
    isMac = True
    isWindows = False
    javaVersion = 0
    
    def __init__(self, c: com.moneydance.apps.md.controller.Main): ...
    
    def addWindowListener(self, mDWindowListener: MDWindowListener) -> None: ...
    
    def adjustWindow(self, j: 'java.awt.Window', j2: 'java.awt.Component', j3: 'java.awt.Dimension', s: str, j4: 'java.awt.Dimension') -> None: ...
    
    def applyButtonBarProperties(self, j: 'javax.swing.AbstractButton') -> None: ...
    
    def applyFilterBarProperties(self, j: 'javax.swing.AbstractButton') -> None: ...
    
    def applyToolbarButtonProperties(self, j: 'javax.swing.AbstractButton') -> None: ...
    
    def archiveFile(self, j: 'java.awt.Frame') -> None: ...
    
    def askForAccountBookNameToSave(self) -> 'java.io.File': ...
    
    def askForAccountFileToLoad(self, j: 'java.awt.Frame') -> 'java.io.File': ...
    
    def askForAccountFileToSave(self) -> 'java.io.File': ...
    
    def askForInput(self, s: str, s2: str, s3: str, b: bool) -> str: ...
    
    def askQuestion(self, s: str) -> bool: ...
    
    def autocommitReminders(self) -> None: ...
    
    def beep(self) -> None: ...
    
    def calculateFontScale(self, j: 'java.awt.Graphics2D') -> float: ...
    
    def closeBotInterface(self) -> None: ...
    
    def createAccount(self, c: com.infinitekind.moneydance.model.Account, j: 'java.awt.Component') -> None: ...
    
    def dataFileOpened(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> bool: ...
    
    def deleteAccount(self, c: com.infinitekind.moneydance.model.Account, j: 'java.awt.Frame') -> bool: ...
    
    def deleteAccountAndAllReferences(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def displayReferenceObject(self, o: object) -> None: ...
    
    def doImport(self, c: com.moneydance.apps.md.controller.fileimport.FileImporter, j: 'java.io.InputStream') -> bool: ...
    
    def doNetSync(self) -> None: ...
    
    def editAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def editCurrencies(self, j: 'java.awt.Frame') -> None: ...
    
    def editCurrency(self, c: com.infinitekind.moneydance.model.CurrencyType) -> None: ...
    
    def editPreferences(self) -> None: ...
    
    def editSecurities(self, j: 'java.awt.Frame') -> None: ...
    
    def exit(self) -> None: ...
    
    def exportFile(self, j: 'java.awt.Frame') -> None: ...
    
    def getAlertController(self) -> AlertController: ...
    
    def getBotInterface(self) -> bot.PythonInterface: ...
    
    def getColors(self) -> MDColors: ...
    
    def getCurrentAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getCurrentAccounts(self) -> com.moneydance.apps.md.controller.AccountBookWrapper: ...
    
    def getCurrentBook(self) -> com.infinitekind.moneydance.model.AccountBook: ...
    
    def getCurrentTheme(self) -> 'theme.ThemeInfo': ...
    
    def getFileChooser(self, j: 'java.awt.Frame', s: str, i: int, j2: 'java.io.FilenameFilter', list: List[str]) -> 'java.awt.FileDialog': ...
    
    def getFileImporter(self, j: 'java.io.File') -> com.moneydance.apps.md.controller.fileimport.FileImporter: ...
    
    def getFileToSave(self, j: 'java.awt.Frame', s: str, s2: str, b: bool) -> 'java.io.File': ...
    
    @staticmethod
    def getFileWithMDExtension(j: 'java.io.File') -> 'java.io.File': ...
    
    def getFirstMainFrame(self) -> MainFrame: ...
    
    def getFonts(self) -> MDFonts: ...
    
    def getHTMLForTxn(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> str: ...
    
    def getIcon(self, s: str) -> 'javax.swing.Icon': ...
    
    def getImage(self, s: str) -> 'java.awt.Image': ...
    
    def getImages(self) -> MDImages: ...
    
    def getMainFrameCount(self) -> int: ...
    
    def getMostActiveAccountPanel(self) -> AccountPanel: ...
    
    def getOnlineManager(self) -> 'OnlineManager': ...
    
    def getPassphrase(self, s: str) -> str: ...
    
    def getPlusController(self) -> MDPlusController: ...
    
    def getPopUpProgressMonitor(self, s: str) -> com.moneydance.apps.md.controller.StatusMonitor: ...
    
    def getPreferences(self) -> com.moneydance.apps.md.controller.UserPreferences: ...
    
    def getResources(self) -> com.moneydance.apps.md.view.resources.Resources: ...
    
    def getSecondaryWindows(self) -> List[SecondaryWindow]: ...
    
    def getSecretKeyCallback(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> com.moneydance.security.SecretKeyCallback: ...
    
    def getSounds(self) -> MDSounds: ...
    
    def getStr(self, s: str) -> str: ...
    
    def getStrings(self) -> MDStrings: ...
    
    def getSuspendRefreshes(self) -> bool: ...
    
    def getSyncManager(self) -> com.moneydance.apps.md.controller.sync.SyncManager: ...
    
    def getTopLevelFrame(self) -> 'javax.swing.JFrame': ...
    
    def getUndoManager(self) -> MDUndoManager: ...
    
    def go(self) -> None: ...
    
    def importFile(self, s: str) -> None: ...
    
    def importFiles(self, list: List['java.io.File']) -> None: ...
    
    def initializePythonInterpreter(self, o: 'org.python.util.PythonInterpreter') -> None: ...
    
    def makeButtonBarButton(self, j: 'javax.swing.AbstractAction') -> 'javax.swing.JButton': ...
    
    def makeToolbarButton(self, mDAction: MDAction) -> 'javax.swing.JButton': ...
    
    def moveTransaction(self, c: com.infinitekind.moneydance.model.AbstractTxn, j: 'java.awt.Component') -> None: ...
    
    def newFile(self, j: 'java.awt.Frame') -> None: ...
    
    def openAccountBook(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> bool: ...
    
    def openBackup(self, j: 'java.awt.Frame') -> bool: ...
    
    def openExternalFile(self, j: 'java.awt.Frame') -> bool: ...
    
    def openFile(self, j: 'java.io.File') -> bool: ...
    
    def payBillsOnline(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def preferencesUpdated(self) -> None: ...
    
    def prepareToOpenData(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> com.moneydance.apps.md.controller.AccountBookWrapper: ...
    
    def registerSecondaryWindow(self, secondaryWindow: SecondaryWindow) -> None: ...
    
    def removeWindowListener(self, mDWindowListener: MDWindowListener) -> None: ...
    
    def reportError(self, j: 'java.lang.Throwable') -> None: ...
    
    def resetPythonInterpreter(self, o: 'org.python.util.PythonInterpreter') -> None: ...
    
    def run(self) -> None: ...
    
    def saveCurrentAccount(self) -> bool: ...
    
    def saveToBackup(self, secondaryFrame: SecondaryFrame) -> None: ...
    
    def secondaryWindowFinished(self, secondaryWindow: SecondaryWindow) -> None: ...
    
    def selectAccount(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def selectAccountNewWindow(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def setDefaultCursor(self, j: 'java.awt.Frame') -> None: ...
    
    def setStatus(self, s: str, f: float) -> None: ...
    
    def setSuspendRefresh(self, b: bool) -> None: ...
    
    def setVerifier(self, c: com.moneydance.security.SecretKeyVerifier) -> None: ...
    
    def setWaitCursor(self, j: 'java.awt.Frame') -> None: ...
    
    def setupOnlineBanking(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def setupOnlineBillpay(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def setupScreenshots(self) -> None: ...
    
    def showAbout(self) -> None: ...
    
    def showAccount(self, c: com.infinitekind.moneydance.model.Account) -> AccountDetailPanel: ...
    
    def showAccountWebsite(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def showAddressBook(self, j: 'java.awt.Frame') -> None: ...
    
    def showBudget(self, s: str) -> None: ...
    
    def showBudgetTool(self) -> None: ...
    
    def showCOA(self) -> None: ...
    
    def showCalculator(self, j: 'java.awt.Frame') -> None: ...
    
    def showCategories(self) -> None: ...
    
    def showDebugOFXWindow(self) -> None: ...
    
    def showDownloadedTxns(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def showErrorMessage(self, s: str) -> None: ...
    
    def showHelp(self) -> None: ...
    
    def showImportUI(self, s: str, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def showInfoMessage(self, s: str) -> None: ...
    
    def showInternetURL(self, s: str) -> None: ...
    
    def showLoanTools(self) -> None: ...
    
    def showMainView(self) -> None: ...
    
    def showMoneydancePlus(self, secondaryFrame: SecondaryFrame, b: bool) -> None: ...
    
    def showObject(self, c: com.infinitekind.moneydance.model.MoneydanceSyncableItem) -> None: ...
    
    def showOnlineBills(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def showOnlineMail(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def showOnlinePayees(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def showOtherSideOfTxn(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def showPreferences(self) -> None: ...
    
    def showPrintChecksWindow(self, j: 'java.awt.Frame', c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def showPythonConsole(self) -> None: ...
    
    def showRawItemDetails(self, c: com.infinitekind.moneydance.model.MoneydanceSyncableItem, j: 'java.awt.Component') -> None: ...
    
    def showReminders(self) -> None: ...
    
    def showReport(self, c: com.infinitekind.moneydance.model.ReportSpec) -> None: ...
    
    def showReports(self) -> None: ...
    
    def showRestoreFromBackupOptions(self, c: com.infinitekind.moneydance.model.AccountBook) -> 'java.io.File': ...
    
    def showSearch(self) -> None: ...
    
    def showSupport(self) -> None: ...
    
    def showTxn(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def showTxnFromURI(self, s: str) -> None: ...
    
    def showTxnInNewWindow(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def showTxnSearch(self) -> None: ...
    
    def showTxnXML(self, c: com.infinitekind.moneydance.model.AbstractTxn, j: 'java.awt.Component') -> None: ...
    
    def showUpcomingReminders(self) -> None: ...
    
    def showVATConfig(self, j: 'java.awt.Frame') -> None: ...
    
    def showVATTxns(self, j: 'java.awt.Frame') -> None: ...
    
    def shutdownApp(self, b: bool) -> bool: ...
    
    def shutdownCompleted(self) -> None: ...
    
    def storeWindowSettings(self, j: 'java.awt.Window', s: str) -> None: ...
    
    def strings(self) -> MDStrings: ...
    
    def translateCurrencies(self, j: 'java.awt.Frame') -> None: ...
    
    def unshowHelp(self) -> None: ...
    
    def updateOnline(self, accountDetailPanel: AccountDetailPanel) -> None: ...
    
    def updateOpenFilesMenus(self) -> None: ...
    
    def updateUndoMenus(self) -> None: ...
    
    
    class FileExtensionFilter:
        def __init__(self): ...
        
        def accept(self, j: 'java.io.File') -> bool: ...
        
        def getDescription(self) -> str: ...
        
        
    
class MoneydanceLAF:
    debugBorder = 'javax.swing.border.LineBorder@296e958b'
    emptyBorder = 'javax.swing.border.EmptyBorder@5de68c32'
    filterBarButtonUIBoth = 'com.moneydance.apps.md.view.gui.FlatButtonUI@770cc11f'
    filterBarButtonUILeft = 'com.moneydance.apps.md.view.gui.FlatButtonUI@72810597'
    filterBarButtonUIMiddle = 'com.moneydance.apps.md.view.gui.FlatButtonUI@2f9e1481'
    filterBarButtonUIRight = 'com.moneydance.apps.md.view.gui.FlatButtonUI@46f08a5c'
    homePageBorder = 'com.moneydance.apps.md.view.gui.HomePageBorder@57e5afa4'
    homePageInsetBorder = 'com.moneydance.apps.md.view.gui.HomePageBorder@2db2a572'
    lineBorder = 'com.moneydance.awt.FlexLineBorder@72578659'
    ovalBorder = 'com.moneydance.apps.md.view.gui.OvalBorder@30b75025'
    zeroBorder = 'javax.swing.border.EmptyBorder@4ad55118'
    
    def __init__(self): ...
    
    @staticmethod
    def applyButtonBarProperties(j: 'javax.swing.AbstractButton') -> None: ...
    
    @staticmethod
    def applyDebugBorder(j: 'javax.swing.JComponent') -> 'javax.swing.JComponent': ...
    
    @staticmethod
    def applyFilterBarProperties(j: 'javax.swing.AbstractButton') -> None: ...
    
    @staticmethod
    def applyRegisterUI(j: 'javax.swing.JComponent') -> None: ...
    
    @staticmethod
    def applyToolbarButtonProperties(j: 'javax.swing.AbstractButton') -> None: ...
    
    @staticmethod
    def containsComboBox(j: 'javax.swing.JComponent') -> bool: ...
    
    @staticmethod
    def fixForMac(j: 'javax.swing.JButton') -> 'javax.swing.JButton': ...
    
    @staticmethod
    def fixForMacRecursive(j: 'javax.swing.JComponent') -> None: ...
    
    @staticmethod
    def getPopupDisplayPoint(j: 'java.awt.Dimension', j2: 'java.awt.Component') -> 'java.awt.Point': ...
    
    @staticmethod
    def installUIRecursive(j: 'javax.swing.JComponent') -> None: ...
    
    @staticmethod
    def makeBackgroundsClear(j: 'javax.swing.JComponent') -> 'javax.swing.JComponent': ...
    
    @staticmethod
    def makeButtonBarButton(j: 'javax.swing.AbstractAction') -> 'javax.swing.JButton': ...
    
    @staticmethod
    def makeCloseButton(mDImages: MDImages) -> 'javax.swing.JButton': ...
    
    @staticmethod
    def makePlainButton(j: 'javax.swing.Action') -> 'javax.swing.JButton': ...
    
    @staticmethod
    def makeToolbarButton(mDAction: MDAction) -> 'javax.swing.JButton': ...
    
    @staticmethod
    def makeWelcomeButton(mDAction: MDAction) -> 'javax.swing.JButton': ...
    
    @staticmethod
    def paintPlaceholder(j: 'java.awt.Graphics', s: str, j2: 'javax.swing.JTextField') -> None: ...
    
    @staticmethod
    def updateLAFItems(moneydanceGUI: MoneydanceGUI) -> None: ...
    
    
class MonthView('javax.swing.JPanel', com.infinitekind.moneydance.model.ReminderListener):
    pass
    
class NewCheckNumWindow(SecondaryDialog, OKButtonListener, 'java.awt.event.ActionListener'):
    pass
    
class NewFileWizard:
    def __init__(self, j: 'java.awt.Frame', moneydanceGUI: MoneydanceGUI): ...
    
    def doIt(self) -> None: ...
    
    
    class SyncFolderType:
        DROPBOX_API = 'Dropbox Connection'
        DROPBOX_FOLDER = 'Dropbox Folder'
        FOLDER = 'Shared Folder'
        ICLOUD_FOLDER = 'iCloud Drive'
        NONE = 'None'
        
        def __init__(self): ...
        
        def syncMethodID(self) -> str: ...
        
        def toString(self) -> str: ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class NewStockSplitWin(SecondaryDialog, OKButtonListener):
    pass
    
class OFXAuthPanel('javax.swing.JPanel'):
    pass
    
class OFXChangePINWindow(SecondaryDialog, OKButtonListener):
    pass
    
class OFXConnectionInfoPanel('javax.swing.JPanel'):
    pass
    
class OFXFIInfoWindow(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class OFXTransferPanel('javax.swing.JPanel'):
    pass
    
class OKButtonPanel('javax.swing.JPanel'):
    pass
    
class OKButtonWindow(SecondaryDialog, OKButtonListener):
    pass
    
class OLBAuthWin(SecondaryDialog, OKButtonListener):
    pass
    
class OnlineAccountMapPanel('javax.swing.JPanel'):
    pass
    
class OnlineManager:
    AUTHENTICATION_CACHE_PREFIX = u''
    
    def __init__(self, moneydanceGUI: MoneydanceGUI): ...
    
    def canDownloadAccount(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def changePIN(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.online.OFXAuthInfo, s: str) -> bool: ...
    
    def clearAuthenticationCache(self) -> None: ...
    
    def completelyDestroyOldDownloadedTxns(self, c: com.infinitekind.moneydance.model.AccountBook) -> None: ...
    
    @staticmethod
    def defaultMessageSetForAccount(c: com.infinitekind.moneydance.model.Account) -> int: ...
    
    def downloadAllTxns(self, accountPanel: AccountPanel, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def downloadTransactions(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def editPayment(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.OnlinePayment) -> com.infinitekind.moneydance.model.OnlinePayment: ...
    
    def getConnection(self, c: com.infinitekind.moneydance.model.OnlineService) -> com.moneydance.apps.md.controller.olb.OLBConnection: ...
    
    def getTxnMerger(self, c: com.infinitekind.moneydance.model.Account) -> com.infinitekind.moneydance.online.OnlineTxnMerger: ...
    
    def getUIProxy(self, accountPanel: AccountPanel) -> DefaultOnlineUIProxy: ...
    
    def mergeOldDownloadedTxns(self, c: com.infinitekind.moneydance.model.AccountBook) -> None: ...
    
    def payBillsOnline(self, c: com.infinitekind.moneydance.model.Account, j: 'java.awt.Frame') -> None: ...
    
    def processDownloadedTxns(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def refreshBills(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def refreshMail(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def removePayee(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.OnlinePayee) -> bool: ...
    
    def removePayment(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.OnlinePayment) -> None: ...
    
    def showBillsOnline(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def showOnlineMail(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def showPayeesOnline(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def submitNewMail(self, c: com.infinitekind.moneydance.model.OnlineService, c2: com.infinitekind.moneydance.model.Account, c3: com.infinitekind.moneydance.model.OnlineMail) -> bool: ...
    
    def submitNewPayee(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.OnlinePayee) -> bool: ...
    
    def submitNewPayment(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.OnlinePayment, c3: com.infinitekind.moneydance.model.OnlinePayee) -> com.infinitekind.moneydance.model.OnlinePayment: ...
    
    def syncPayments(self, c: com.infinitekind.moneydance.model.OnlineService, mDAccountProxy: MDAccountProxy) -> bool: ...
    
    def updateAvailableAccounts(self, c: com.infinitekind.moneydance.model.OnlineService) -> bool: ...
    
    def updatePayee(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.OnlinePayee) -> bool: ...
    
    def updateServiceInfo(self, c: com.infinitekind.moneydance.model.OnlineService) -> None: ...
    
    
class OnlineTxnListModel('javax.swing.AbstractListModel', com.infinitekind.moneydance.model.OnlineTxnListener):
    pass
    
class OnlineUpdateTxnsWindow(SecondaryDialog, 'java.awt.event.ActionListener', 'javax.swing.event.ListSelectionListener'):
    pass
    
class OpenArchiveWindow(SecondaryDialog):
    pass
    
class OpenFileAction(MDAction):
    pass
    
class OvalBorder('javax.swing.border.Border'):
    def __init__(self): ...
    
    def getBackgroundColor(self) -> 'java.awt.Color': ...
    
    def getBorderInsets(self, j: 'java.awt.Component') -> 'java.awt.Insets': ...
    
    def getOvalColor(self) -> 'java.awt.Color': ...
    
    def isBorderOpaque(self) -> bool: ...
    
    def paintBorder(self, j: 'java.awt.Component', j2: 'java.awt.Graphics', i: int, i2: int, i3: int, i4: int) -> None: ...
    
    def setOvalColor(self, j: 'java.awt.Color', j2: 'java.awt.Color') -> None: ...
    
    
class PassphraseCallbackProxy(com.moneydance.security.SecretKeyCallback):
    def __init__(self): ...
    
    def getPassphrase(self, s: str) -> str: ...
    
    def setVerifier(self, c: com.moneydance.security.SecretKeyVerifier) -> None: ...
    
    
class PasswordDialog(SecondaryDialog, OKButtonListener, 'java.awt.event.ActionListener'):
    pass
    
class PercentGraphLabeler('com.moneydance.awt.graph.ValueLabeler'):
    def __init__(self, moneydanceGUI: MoneydanceGUI): ...
    
    def getLabelForValue(self, f: float, i: int) -> str: ...
    
    def preferencesUpdated(self) -> None: ...
    
    
class PlainButton('javax.swing.JButton'):
    pass
    
class PointsVsRate('javax.swing.JPanel', 'java.awt.event.ActionListener', 'java.awt.event.FocusListener'):
    pass
    
class PopUpStatusMonitor(com.moneydance.apps.md.controller.StatusMonitor):
    def __init__(self, j: 'java.awt.Component', s: str): ...
    
    def isCanceled(self) -> bool: ...
    
    def setPercentComplete(self, f: float) -> None: ...
    
    def setStatus(self, s: str) -> None: ...
    
    
class Popover:
    def __init__(self, moneydanceGUI: MoneydanceGUI, j: 'java.awt.Window', j2: 'javax.swing.JComponent'): ...
    
    def getPopupComponent(self) -> str: ...
    
    def goAway(self) -> bool: ...
    
    def goingAway(self) -> bool: ...
    
    def goneAway(self) -> None: ...
    
    def isDontShowAnchor(self) -> bool: ...
    
    def isNowVisible(self) -> None: ...
    
    def isVisible(self) -> bool: ...
    
    def setAllowFocusing(self, b: bool) -> None: ...
    
    def setAllowMoving(self, b: bool) -> None: ...
    
    def setAnchorPosition(self, s: str) -> None: ...
    
    def setContentPane(self, j: 'javax.swing.JComponent') -> None: ...
    
    def setDontShowAnchor(self, b: bool) -> None: ...
    
    def setSticky(self, b: bool) -> None: ...
    
    def showFromComponent(self, j: 'javax.swing.JComponent') -> None: ...
    
    def showFromRect(self, j: 'java.awt.Rectangle') -> None: ...
    
    
    class PopoverAnchorPosition:
        ANY = 'ANY'
        EAST = 'EAST'
        NORTH = 'NORTH'
        SOUTH = 'SOUTH'
        WEST = 'WEST'
        
        def __init__(self): ...
        
        def getSwingConstant(self) -> int: ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    class PopupDialog:
        pass
        
    class Type:
        DIALOG = 'DIALOG'
        POPUP = 'POPUP'
        WINDOW = 'WINDOW'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class PopoverBorder('javax.swing.border.Border'):
    def __init__(self, moneydanceGUI: MoneydanceGUI): ...
    
    def getBorderInsets(self, j: 'java.awt.Component') -> 'java.awt.Insets': ...
    
    def isBorderOpaque(self) -> bool: ...
    
    def paintBorder(self, j: 'java.awt.Component', j2: 'java.awt.Graphics', i: int, i2: int, i3: int, i4: int) -> None: ...
    
    def setAnchorPosition(self, i: int) -> None: ...
    
    
class PopupWindow('javax.swing.JDialog'):
    pass
    
class PortfolioPanel(AccountDetailPanel, com.infinitekind.moneydance.model.TransactionListener, com.infinitekind.moneydance.model.AccountListener, com.infinitekind.moneydance.model.CurrencyListener, 'com.moneydance.awt.JLinkListener'):
    pass
    
class PreReconcilerWindow(SecondaryDialog, OKButtonListener, 'java.awt.event.ActionListener'):
    pass
    
class PreferencesWindow(SecondaryDialog, OKButtonListener, 'java.awt.event.ActionListener', 'javax.swing.event.ChangeListener', 'java.awt.event.ItemListener', 'checks.CheckListener'):
    pass
    
class PrintChecksWindow(SecondaryDialog, 'java.awt.event.ActionListener', 'java.awt.event.ItemListener'):
    pass
    
class ProcessIndicator:
    def __init__(self, moneydanceGUI: MoneydanceGUI): ...
    
    def invokeTask(self, callable: Callable, s: str) -> None: ...
    
    
class QIFImportSettingsWindow(SecondaryDialog, OKButtonListener):
    pass
    
class QuestionDialog(SecondaryDialog, OKButtonListener):
    pass
    
class RateEditor('javax.swing.JPanel', 'java.awt.event.ItemListener'):
    pass
    
class RateGraphLabeler('com.moneydance.awt.graph.ValueLabeler'):
    def __init__(self, moneydanceGUI: MoneydanceGUI): ...
    
    def getLabelForValue(self, f: float, i: int) -> str: ...
    
    def preferencesUpdated(self) -> None: ...
    
    
class RatingInfo:
    def __init__(self, c: com.moneydance.apps.md.controller.Main): ...
    
    def rate(self) -> None: ...
    
    def ratingInfoWasUpdated(self) -> None: ...
    
    def reload(self) -> None: ...
    
    def shouldPrompt(self) -> bool: ...
    
    def stopRemindingMe(self) -> None: ...
    
    def stopRemindingMeForThisVersion(self) -> None: ...
    
    def stopRemindingMeUntilDate(self, i: int) -> None: ...
    
    
    class StopBothering:
        EVER = 'EVER'
        FOR_NOW = 'FOR_NOW'
        THIS_BUILD = 'THIS_BUILD'
        
        def __init__(self): ...
        
        def code(self) -> int: ...
        
        @staticmethod
        def fromCode(i: int) -> str: ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class RecTxnRenderer(AbstractTxnRenderer):
    pass
    
class ReconcilerWindow(SecondaryFrame, AccountInfoListener, 'java.awt.event.ActionListener', com.infinitekind.moneydance.model.TransactionListener, Callable):
    pass
    
class RegTxnRenderer(AbstractTxnRenderer):
    pass
    
class RegisterPrinter('print.MDPrintable'):
    def __init__(self, moneydanceGUI: MoneydanceGUI, j: 'javax.swing.JList', j2: 'javax.swing.JComponent', s: str): ...
    
    def doPrintJob(self) -> None: ...
    
    def getSettingsKey(self) -> str: ...
    
    def getTitle(self) -> str: ...
    
    def isLandscape(self) -> bool: ...
    
    def printPage(self, j: 'java.awt.Graphics2D', i: int, f: float, f2: float, i2: int) -> bool: ...
    
    def usesWholePage(self) -> bool: ...
    
    
class RegisterWindow(SecondaryDialog, OKButtonListener):
    pass
    
class RegistrationNotificationWindow(SecondaryDialog):
    pass
    
class ReminderListModel('javax.swing.AbstractListModel', com.infinitekind.moneydance.model.ReminderListener):
    pass
    
class ReminderTxnEditPanel('javax.swing.JPanel'):
    pass
    
class TitledDetailPanel(DisposablePanel, 'java.awt.event.ActionListener'):
    pass
    
class RemindersDetailPanel(TitledDetailPanel, 'print.MDPrintable'):
    pass
    
class RestoreBackupWindow(SecondaryDialog):
    pass
    
class RootAccountDetailPanel(AccountDetailPanel, com.moneydance.apps.md.controller.ViewListener, com.moneydance.apps.md.controller.AppEventListener, com.moneydance.apps.md.controller.ModuleListener):
    pass
    
class RootAccountInfoPanel(AccountInfoPanel):
    pass
    
class ScheduleInfoPanel('javax.swing.JPanel', 'java.awt.event.ActionListener'):
    pass
    
class SearchField('javax.swing.JPanel', 'java.awt.event.ActionListener', 'javax.swing.event.DocumentListener'):
    pass
    
class SearchFieldBorder('javax.swing.border.AbstractBorder'):
    def __init__(self): ...
    
    def getOuterColor(self) -> 'java.awt.Color': ...
    
    def isBorderOpaque(self) -> bool: ...
    
    def isCancelIconPressed(self) -> bool: ...
    
    def isCancelVisible(self) -> bool: ...
    
    def isOverCancel(self, j: 'java.awt.Point', j2: 'java.awt.Component') -> bool: ...
    
    def isOverSearch(self, j: 'java.awt.Point', j2: 'java.awt.Component') -> bool: ...
    
    def isSearchIconPressed(self) -> bool: ...
    
    def paintBorder(self, j: 'java.awt.Component', j2: 'java.awt.Graphics', i: int, i2: int, i3: int, i4: int) -> None: ...
    
    def setCancelIconPressed(self, b: bool) -> None: ...
    
    def setCancelVisible(self, b: bool) -> None: ...
    
    def setOuterColor(self, j: 'java.awt.Color') -> None: ...
    
    def setSearchIconPressed(self, b: bool) -> None: ...
    
    
class SearchListener:
    def __init__(self): ...
    
    def searchUpdated(self, c: com.infinitekind.moneydance.model.TxnSearch) -> None: ...
    
    
class SearchRegTxnListModel(TxnListModel):
    pass
    
class SecurityAccountInfoPanel(AccountInfoPanel, 'java.awt.event.ActionListener'):
    pass
    
class SecurityDetailPanel(AccountDetailPanel, com.infinitekind.moneydance.model.TransactionListener, com.infinitekind.moneydance.model.CurrencyListener, 'java.awt.event.ActionListener', com.infinitekind.moneydance.model.AccountListener, Callable):
    pass
    
class SecurityRenderer('javax.swing.JComponent', 'javax.swing.ListCellRenderer'):
    pass
    
class SecurityTxnRenderer(AbstractTxnRenderer):
    pass
    
class SelectChecksWindow(SecondaryDialog, OKButtonListener):
    pass
    
class ShowUpcomingRemindersWindow(SecondaryDialog, com.infinitekind.moneydance.model.ReminderListener, 'com.moneydance.awt.JLinkListener'):
    pass
    
class TotalListener:
    def __init__(self): ...
    
    def totalUpdated(self) -> None: ...
    
    
class SplitEditor(SecondaryDialog, TotalListener, 'java.awt.event.ActionListener', Callable):
    pass
    
class SplitPanel('javax.swing.JPanel', 'java.awt.event.KeyListener'):
    pass
    
class TxnEditorInterface:
    def __init__(self): ...
    
    def getTransactionAmount(self) -> int: ...
    
    def goingAway(self) -> bool: ...
    
    def setCheckNumber(self, s: str) -> None: ...
    
    def setDate(self, i: int) -> None: ...
    
    def setMemo(self, s: str) -> None: ...
    
    def setPayee(self, s: str) -> None: ...
    
    def setTaxDate(self, i: int) -> None: ...
    
    def setValue(self, i: int) -> None: ...
    
    def transactionModified(self) -> bool: ...
    
    
class SplitTxnEditor(AutoCompletable, TxnEditorInterface, 'javax.swing.JPanel', 'java.awt.event.KeyListener', 'java.awt.event.FocusListener', Callable):
    pass
    
class StatusButton('javax.swing.JComponent', 'java.awt.event.MouseListener', 'java.awt.event.KeyListener', 'java.awt.event.FocusListener', 'java.awt.event.ActionListener'):
    pass
    
class StatusPanel('javax.swing.JPanel'):
    pass
    
class StretchableImage:
    def __init__(self, j: 'java.awt.Image', j2: 'java.awt.Insets'): ...
    
    def setInsets(self, j: 'java.awt.Insets') -> None: ...
    
    
class SubAcctSearch(com.infinitekind.moneydance.model.AcctFilter):
    ACTIVE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$2@3cc82d81'
    ACTIVE_CATEGORY_CHOICE_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$9@be7fc86'
    ALL_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$7@6a996a69'
    CATEGORY_CHOICE_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$8@442a0860'
    CATEGORY_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$6@39f38141'
    EDITABLE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$5@d444935'
    INACTIVE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$3@2cafb0d6'
    NON_CATEGORY_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$1@38d2c42b'
    VIEWABLE_ACCOUNTS_FILTER = 'com.infinitekind.moneydance.model.AcctFilter$4@1d8ea3f9'
    
    def __init__(self, c: com.infinitekind.moneydance.model.Account): ...
    
    def format(self, c: com.infinitekind.moneydance.model.Account) -> str: ...
    
    def getAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Account) -> bool: ...
    
    def setAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    
class TagLogic('java.lang.Enum'):
    AND = 'AND'
    EXACT = 'EXACT'
    OR = 'OR'
    
    def __init__(self): ...
    
    @staticmethod
    def fromString(s: str) -> 'TagLogic': ...
    
    def getConfigKey(self) -> str: ...
    
    @staticmethod
    def valueOf(s: str) -> 'TagLogic': ...
    
    @staticmethod
    def values() -> List['TagLogic']: ...
    
    
class TaskIndicator(SecondaryDialog, Callable):
    pass
    
class ToolbarLabel('javax.swing.JLabel'):
    pass
    
class TransactionPopup(PopupWindow, AttachmentHolder):
    pass
    
class TransactionSortListener:
    def __init__(self): ...
    
    def setSortKey(self, c: com.infinitekind.moneydance.model.TxnSortOrder, b: bool) -> None: ...
    
    
class TransferWindow(SecondaryDialog, OKButtonListener):
    pass
    
class TranslateCurrencyWindow(SecondaryDialog, 'java.awt.event.ItemListener', com.infinitekind.moneydance.model.CurrencyListener):
    pass
    
class TxnAccountSearch(com.infinitekind.moneydance.model.TxnSearch):
    def __init__(self, c: com.infinitekind.moneydance.model.Account): ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Txn) -> bool: ...
    
    def matchesAll(self) -> bool: ...
    
    
class TxnAmountSearch(com.infinitekind.moneydance.model.TxnSearch):
    def __init__(self, f: float): ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Txn) -> bool: ...
    
    def matchesAll(self) -> bool: ...
    
    
class TxnClearedSearch(com.infinitekind.moneydance.model.TxnSearch):
    def __init__(self, b: bool, b2: bool, b3: bool): ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Txn) -> bool: ...
    
    def matchesAll(self) -> bool: ...
    
    
class TxnDateSearch(com.infinitekind.moneydance.model.TxnSearch):
    def __init__(self, i: int): ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Txn) -> bool: ...
    
    def matchesAll(self) -> bool: ...
    
    
class TxnDetailsView:
    def __init__(self, moneydanceGUI: MoneydanceGUI, t: 'txnreg.TxnRegister'): ...
    
    def dismiss(self) -> bool: ...
    
    def isShowing(self) -> bool: ...
    
    def selectionWasUpdated(self, list: List[com.infinitekind.moneydance.model.AbstractTxn]) -> 'txnreg.TxnInfoPanel': ...
    
    def setInfoPanels(self, list: List['txnreg.TxnInfoPanel']) -> None: ...
    
    def showDetails(self, j: 'javax.swing.JComponent', j2: 'java.awt.Rectangle', t: 'txnreg.TxnInfoPanel') -> None: ...
    
    def showDetailsInPanel(self, j: 'javax.swing.JPanel', t: 'txnreg.TxnInfoPanel') -> None: ...
    
    
class TxnEditor(AutoCompletable, TxnEditorInterface, 'javax.swing.JPanel', 'java.awt.event.ActionListener', 'java.awt.event.KeyListener', 'java.awt.event.FocusListener'):
    pass
    
class TxnEditorWrapper('javax.swing.JPanel'):
    pass
    
class TxnModifier:
    def __init__(self): ...
    
    def modifyTxn(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    
class TxnReminderInfoWindow(SecondaryDialog, OKButtonListener):
    pass
    
class TxnReminderNotificationWindow(SecondaryDialog, 'java.awt.event.ActionListener'):
    pass
    
class TxnSearchConfigPanel(MDFieldPanel, 'javax.swing.event.DocumentListener', 'java.beans.PropertyChangeListener'):
    pass
    
class TxnSearchWindow(SecondaryFrame, 'java.awt.event.ActionListener'):
    pass
    
class TxnSearcher(Callable):
    def __init__(self, accountRegTxnListModel: AccountRegTxnListModel): ...
    
    def run(self) -> None: ...
    
    def setSearch(self, c: com.infinitekind.moneydance.model.TxnSearch) -> None: ...
    
    
class TxnTagsSearch(com.infinitekind.moneydance.model.TxnSearch):
    def __init__(self, list: List[str], tagLogic: TagLogic): ...
    
    def matches(self, c: com.infinitekind.moneydance.model.Txn) -> bool: ...
    
    def matchesAll(self) -> bool: ...
    
    
class TxnWrapper:
    attachment = '<reflected field public java.lang.Object com.moneydance.apps.md.view.gui.TxnWrapper.attachment at 0xaf5>'
    balance = '<reflected field public long com.moneydance.apps.md.view.gui.TxnWrapper.balance at 0xaf6>'
    decorator = '<reflected field public com.moneydance.apps.md.view.gui.txnreg.TxnDecorator com.moneydance.apps.md.view.gui.TxnWrapper.decorator at 0xaf7>'
    isFocused = '<reflected field public boolean com.moneydance.apps.md.view.gui.TxnWrapper.isFocused at 0xaf8>'
    isSelected = '<reflected field public boolean com.moneydance.apps.md.view.gui.TxnWrapper.isSelected at 0xaf9>'
    row = '<reflected field public int com.moneydance.apps.md.view.gui.TxnWrapper.row at 0xafa>'
    txn = '<reflected field public com.infinitekind.moneydance.model.AbstractTxn com.moneydance.apps.md.view.gui.TxnWrapper.txn at 0xafb>'
    
    def __init__(self): ...
    
    def hasAttachments(self) -> bool: ...
    
    
class WelcomeWindow('javax.swing.JFrame'):
    pass
    
class Wizard(SecondaryDialog):
    pass
    
class WizardPane:
    def __init__(self): ...
    
    def activated(self, wizard: Wizard) -> None: ...
    
    def getPanel(self) -> 'javax.swing.JComponent': ...
    
    def goneAway(self) -> None: ...
    
    def isLastPane(self) -> bool: ...
    
    def storeValues(self) -> 'WizardPane': ...
    
    
