# !/usr/bin/env python
# coding=utf-8
# Python script to be run in Moneydance to perform amazing feats of
# financial scripting
import os.path

try:
    from com.infinitekind.moneydance.model import *
except ImportError:
    from moneydance import *
    from com.infinitekind.moneydance.model import *

try:
    # noinspection PyUnresolvedReferences
    from typing import Dict, Generator, Iterator, List, Optional, Set, Tuple, Union
except ImportError:
    pass

CSV_FILE_NAME = 'Downloads/MoneyDance.csv'


# ClearedStatus = AbstractTxn.ClearedStatus
class ClearedStatus(object):
    CLEARED = 'CLEARED'
    RECONCILING = 'RECONCILING'
    UNRECONCILED = 'UNRECONCILED'


# AccountType = Account.AccountType
class AccountType(object):
    ASSET = 'ASSET'
    BANK = 'BANK'
    CREDIT_CARD = 'CREDIT_CARD'
    EXPENSE = 'EXPENSE'
    INCOME = 'INCOME'
    INVESTMENT = 'INVESTMENT'
    LIABILITY = 'LIABILITY'
    LOAN = 'LOAN'
    ROOT = 'ROOT'
    SECURITY = 'SECURITY'


# BalanceType = Account.BalanceType
class BalanceType(object):
    CLEARED = 'CLEARED'
    CONFIRMED = 'CONFIRMED'
    CURRENT = 'CURRENT'
    NORMAL = 'NORMAL'
    UNCONFIRMED = 'UNCONFIRMED'


prefix_to_strip = ('SQ *', 'TST* ', 'PY *', 'SP * ', 'EV* ', 'CKE*')


def strip_prefixes(s):
    # type: (str) -> str
    if '*' in s:
        for prefix in prefix_to_strip:
            if s.startswith(prefix):
                return s[len(prefix):]
    return s


def first_word(s):
    # type: (str) -> str
    s = s.upper()
    for separator in (" ", "*", ".", "-", "/"):
        s = s.partition(separator)[0]
    return s


def remove_extra_spaces(s):
    return " ".join(part.strip() for part in s.split(" ") if part.strip())


def find_account(account):
    # type: (str) -> Optional[Account]
    if not account:
        return None
    return moneydance.getCurrentAccountBook().getRootAccount().getAccountByName(account)


class Transaction(object):
    """
                if txn != txn.getParentTxn():
                continue
            if not txn.isNew():
                continue
            account_name = str(txn.getAccount())

    """

    _category = None
    _original_category = None
    _description = None
    _original_description = None
    _is_new = None
    _original_is_new = None

    def __init__(self, txn):
        # type: (ParentTxn) -> None
        self._txn = txn
        self._dollars = None
        self._memo = None

    @property
    def account(self):
        # type: () -> Account
        return self._txn.getAccount()

    @property
    def amount(self):
        # type: () -> float
        return float(self._txn.getValue()) / 100.0

    @property
    def category(self):
        # type: () -> Account
        if self._original_category is None:
            self._original_category = self._txn.getSplit(0).getAccount() if self._txn.getSplitCount() == 1 else None
            self._category = self._original_category
        return self._category

    @category.setter
    def category(self, value):
        # type: (Union[str, Account]) -> None
        if isinstance(value, str):
            value = find_account(value)
        if str(self.category) != str(value):
            self._category = value

    @property
    def dateint(self):
        # type: () -> int
        return self._txn.getDateInt()

    @property
    def description(self):
        # type: () -> str
        if self._original_description is None:
            self._original_description = remove_extra_spaces(
                strip_prefixes(self._txn.getDescription()))
            self._description = self._original_description
        return self._description

    @description.setter
    def description(self, value):
        # type: (str) -> None
        if self.description != value:
            self._description = value

    @property
    def online_description(self):
        return strip_prefixes(self._txn.getOriginalOnlineTxn().getName())

    @property
    def first_word(self):
        # type: () -> str
        return first_word(self.online_description)

    @property
    def dollars(self):
        # type: () -> str
        if self._dollars is None:
            # noinspection PyTypeChecker
            currency_type = self.account.getCurrencyType()
            # noinspection PyTypeChecker
            self._dollars = currency_type.formatFancy(self._txn.getValue(), '.')
        return self._dollars

    @property
    def is_new(self):
        # type: () -> bool
        if self._original_is_new is None:
            self._original_is_new = self._txn.isNew()
            self._is_new = self._original_is_new
        return self._is_new

    @is_new.setter
    def is_new(self, value):
        # type: (bool) -> None
        if self.is_new != value:
            self._is_new = value

    @property
    def memo(self):
        # type: () -> str
        if self._memo is None:
            self._memo = self._txn.getMemo()
        return self._memo

    def sync(self):
        # type: () -> None
        needs_sync = False
        if self._description != self._original_description:
            self._txn.setDescription(self._description)
            needs_sync = True
        if self._is_new != self._original_is_new:
            self._txn.setIsNew(self._is_new)
            needs_sync = True
        if self._original_category != self._category:
            self._txn.getSplit(0).setAccount(self._category)
            needs_sync = True
        if needs_sync:
            self._txn.getParentTxn().syncItem()

    def __str__(self):
        # type: () -> str
        return self.summary()

    @property
    def is_modified(self):
        # type: () -> bool
        return (
            self.description != self._original_description
            or self.is_new != self._original_is_new
            or self.category != self._original_category
        )

    def changes(self):
        # type: () -> List[str]
        changes = []  # type: List[str]
        if self.description != self._original_description:
            changes.append("description: {} -> {}".format(self._original_description, self.description))
        if self.category != self._original_category:
            changes.append("category: {} -> {}".format(self._original_category, self.category))
        if self.is_new != self._original_is_new:
            changes.append("confirmed: {}".format("True" if self._original_is_new else "False"))
        return changes

    def summary(self, original=False):
        # type: (bool) -> str
        is_new = self.is_new
        desc = self.description
        cat = self.category
        if original:
            is_new = self._original_is_new
            desc = self._original_description
            cat = self._original_category
        return '%s%u: %s - %s (%s, %s) online: "%s" memo: "%s"' % \
            (
                "*" if is_new else "", self.dateint, desc, self.dollars,
                self.account, cat, self.online_description, self.memo
            )


class Fixer(object):
    def __init__(self, replacement, exact_match="", starts_with="",
                 memo_contains="", amount=0.0, amount_below=0.0,
                 amount_above=0.0, category="", skip_confirm=False):
        # type: (str, str, str, str, float, float, float, str, bool) -> None
        self.replacement = replacement
        if not exact_match and not starts_with:
            starts_with = replacement
        self.exact_match = remove_extra_spaces(
            strip_prefixes(exact_match.upper()))
        self.starts_with = strip_prefixes(starts_with.upper())
        self.memo_contains = memo_contains.upper()
        self.amount = float(amount) if amount else 0.0
        self.amount_below = float(amount_below) if amount_below else 0.0
        self.amount_above = float(amount_above) if amount_above else 0.0
        self.category = find_account(category) if category else None
        self.confirm = not skip_confirm

    def check_replacement(self, txn, check_starts_with=True):
        # type: (Transaction, bool) -> bool
        if check_starts_with and self.starts_with:
            matched = txn.online_description.upper().startswith(self.starts_with) or (self.exact_match and txn.online_description.upper() == self.exact_match)
            if not matched:
                return False
        if self.memo_contains and self.memo_contains not in txn.memo.upper():
            return False
        if self.amount and txn.amount != self.amount:
            return False
        if self.amount_above and txn.amount < self.amount_above:
            return False
        if self.amount_below and txn.amount > self.amount_below:
            return False
        return True

    def fix(self, txn, save_changes=False, check_starts_with=True):
        # type: (Transaction, bool, bool) -> bool
        if not self.check_replacement(txn, check_starts_with):
            return False
        txn.description = self.replacement
        if self.confirm:
            txn.is_new = False
        if self.category:
            txn.category = self.category
        if save_changes:
            txn.sync()
        return True

    @property
    def first_word(self):
        # type: () -> str
        return first_word(self.starts_with)


class FixerGroup(object):
    def __init__(self):
        # type: () -> None
        self.exact_matches = {}  # type: Dict[str, List[Fixer]]
        self.starts_with = {}  # type: Dict[str, List[Fixer]]

    def add(self, fixer):
        # type: (Fixer) -> None
        if fixer.starts_with:
            self.starts_with.setdefault(fixer.first_word, []).append(fixer)
        elif fixer.exact_match:
            self.exact_matches.setdefault(fixer.exact_match, []).append(fixer)
            if fixer.exact_match == fixer.replacement.upper():
                # Don't add it twice
                return
        self.exact_matches.setdefault(fixer.replacement.upper(), []).append(fixer)

    def fix(self, txn, save_changes=False):
        # type: (Transaction, bool) -> bool
        for possible in self.exact_matches.get(txn.online_description.upper(), []):
            if possible.fix(txn, save_changes=save_changes, check_starts_with=False):
                return True
        for possible in self.starts_with.get(txn.first_word, []):
            if possible.fix(txn, save_changes=save_changes):
                return True
        return False


class FixerCollection(object):
    _fixer_groups_by_account_type = {}  # type: Dict[str, FixerGroup]
    _fixer_groups_by_account_name = {}  # type: Dict[str, FixerGroup]
    _global_fixers = FixerGroup()
    _loaded = set()  # type: Set[str]

    @classmethod
    def load(cls, path):
        if path not in cls._loaded:
            path = os.path.join(os.getcwd(), path)
            if not os.path.exists(path):
                print("No data file found at {}".format(os.path.realpath(path)))
                return
            print("Loading {}".format(os.path.realpath(path)))
            with open(path, 'r') as f:
                lines = [line.strip().replace('\xe2\x80\x99', "'") for line in
                         f]
            field_names = lines[0].split(',')
            for line in lines[1:]:
                kwargs = dict(zip(field_names, line.split(',')))
                # print(kwargs)
                cls.create_fixer(**kwargs)

            cls._loaded.add(path)

    @classmethod
    def add(cls, fixer, account_type="", account_name=""):
        # type: (Fixer, str, str) -> None
        if account_name:
            group = cls._fixer_groups_by_account_name.setdefault(account_name.upper(),
                                                                 FixerGroup())
        elif account_type:
            group = cls._fixer_groups_by_account_type.setdefault(account_type,
                                                                 FixerGroup())
        else:
            group = cls._global_fixers
        group.add(fixer)

    @classmethod
    def create_fixer(cls, replacement, exact_match="", starts_with="",
                     memo_contains="", amount=0.0, amount_above=0.0,
                     amount_below=0.0, category="", skip_confirm=False,
                     account_type="", account_name=""):
        # type: (str, str, str, str, float, float, float, str, bool, str, str) -> None
        cls.add(Fixer(replacement, exact_match=exact_match,
                      starts_with=starts_with, memo_contains=memo_contains,
                      amount=amount, amount_above=amount_above,
                      amount_below=amount_below, category=category,
                      skip_confirm=skip_confirm),
                account_type, account_name)

    @classmethod
    def fix(cls, txn, save_changes=False):
        # type: (Transaction, bool) -> bool
        group = cls._fixer_groups_by_account_name.get(str(txn.account).upper())
        if group and group.fix(txn, save_changes):
            return True
        account_type = str(txn.account.getAccountType())
        group = cls._fixer_groups_by_account_type.get(account_type)
        if group and group.fix(txn, save_changes):
            return True
        if cls._global_fixers.fix(txn, save_changes):
            return True
        return False


class DescriptionCounter(object):
    def __init__(self, description):
        # type: (str) -> None
        self.count = 0
        self.description = description
        self.outputs = set()

    def add(self, s):
        # type: (str) -> None
        self.count += 1
        self.outputs.add(s)

    def __cmp__(self, other):
        if self.count < other.count:
            return -1
        if self.count > other.count:
            return 1
        if self.description < other.description:
            return -1
        if self.description > other.description:
            return 1
        return 0


class DescriptionFirstWordCounter(object):
    def __init__(self, fw):
        # type: (str) -> None
        self.count = 0
        self.first_word = fw
        self.descriptions = {}  # type: Dict[str, DescriptionCounter]

    def add(self, description, output):
        # type: (str, str) -> None
        self.count += 1
        self.descriptions.setdefault(description,
                                     DescriptionCounter(description)).add(
            output)

    def __cmp__(self, other):
        if self.count < other.count:
            return -1
        if self.count > other.count:
            return 1
        if self.first_word < other.first_word:
            return -1
        if self.first_word > other.first_word:
            return 1
        return 0

    def sorted(self):
        return sorted(self.descriptions.values())


class DescriptionContainer(object):
    def __init__(self):
        # type: () -> None
        self.first_words = {}  # type: Dict[str, DescriptionFirstWordCounter]

    def add(self, description, output):
        # type: (str, str) -> None
        fw = first_word(description)
        if fw == "THE":
            fw = first_word(description[4:])
        self.first_words.setdefault(fw, DescriptionFirstWordCounter(fw)).add(
            description, output)

    def sorted(self):
        # type: () -> List[DescriptionFirstWordCounter]
        return sorted(self.first_words.values())


class FixDownloadedTransactionsExtension(object):
    myContext = None
    myExtensionObject = None
    name = "Fix Downloaded Transactions"
    _accounts_by_type = {}  # type: Dict[str, List[Account]]
    _account_names_by_type = {}  # type: Dict[str, Set[str]]
    _fixer_groups_by_account_type = {}  # type: Dict[str, FixerGroup]
    _fixer_groups_by_account_name = {}  # type: Dict[str, FixerGroup]
    _global_fixers = FixerGroup()
    _instance = None

    # The initialize method is called when the extension is loaded and
    # provides the extension's context.  The context implements the methods
    # defined in the FeatureModuleContext:
    # http://infinitekind.com/dev/apidoc/com/moneydance/apps/md/controller
    # /FeatureModuleContext.html

    @classmethod
    def get_instance(cls):  # type: () -> FixDownloadedTransactionsExtension
        if cls._instance is None:
            cls._instance = FixDownloadedTransactionsExtension()
        return cls._instance

    @property
    def account_names_by_type(self):  # type: () -> Dict[str, Set[str]]
        if not self._account_names_by_type:
            self._init_data()
        return self._account_names_by_type

    @property
    def accounts_by_type(self):  # type: () -> Dict[str, List[Account]]
        if not self._accounts_by_type:
            self._init_data()
        return self._accounts_by_type

    def _init_data(self):  # type: () -> None
        self._account_names_by_type = {}
        for account in AccountIterator(moneydance.getCurrentAccountBook()):
            if account.getAccountOrParentIsInactive():
                continue
            account_type = str(account.getAccountType())
            if account_type in (
                    AccountType.EXPENSE, AccountType.INCOME, AccountType.ROOT):
                continue
            self._accounts_by_type.setdefault(str(account.getAccountType()),
                                              []).append(account)
            self._account_names_by_type.setdefault(
                str(account.getAccountType()),
                set()).add(str(account))

    def initialize(self, extension_context, extension_object):
        self.myContext = extension_context
        self.myExtensionObject = extension_object
        self._init_data()
        FixerCollection.load(CSV_FILE_NAME)

        # here we register ourselves with a menu item to invoke a feature
        # (ignore the button and icon mentions in the docs)
        self.myContext.registerFeature(extension_object,
                                       "fixDownloadedTransactions", None,
                                       "Fix Downloaded Transactions")

    # invoke(eventstring) is called when we receive a callback for the
    # feature that we registered in the initialize method
    def invoke(self, eventString=""):
        self.myContext.setStatus(
            "Python extension received command: %s" % eventString)

    def show_accounts(self):  # type: () -> None
        for account_type in sorted(self.account_names_by_type):
            print('Type: {}'.format(account_type))
            for account in sorted(
                    self.account_names_by_type.get(account_type, [])):
                print('- Account: {}'.format(account))

    def _process_transactions(
            self,
            account_types,
            commit_changes=False,
            limit=1000000):
        # type: (Tuple[str, ...], bool, int) -> None
        all_parented_transactions = list(
            self.get_unreconciled_for_account_types(*account_types))
        all_parented_transactions.sort(key=lambda x: -x.dateint)
        counter = 0
        fix_count = 0
        no_change_required = 0
        unmodified = DescriptionContainer()
        for txn in all_parented_transactions:
            if counter < limit:
                fixed = FixerCollection.fix(txn, save_changes=commit_changes)
                if fixed:
                    if txn.is_modified:
                        print(txn)
                        for change in txn.changes():
                            print("- {}".format(change))
                        fix_count += 1
                    else:
                        no_change_required += 1
                else:
                    unmodified.add(txn.online_description, str(txn))
            counter += 1
        if unmodified:
            print("\n--- Not fixed ---")
            for entry in unmodified.sorted():
                print("{}:".format(entry.first_word))
                for desc in entry.sorted():
                    print("- {} ({})".format(desc.description, desc.count))
                    for o in sorted(desc.outputs):
                        print("  - {}".format(o))
        print("Fixed {} of {} ({}%)".format(fix_count, counter,
                                            (fix_count * 100 / counter)))
        if no_change_required:
            print("{} were unconfirmed but no change required".format(no_change_required))

    def test_fix_transactions(self, *account_types):
        # type: (*str) -> None
        self._process_transactions(account_types, commit_changes=False)

    def fix_transactions(self, *account_types):
        # type: (*str) -> None
        self._process_transactions(account_types, commit_changes=True)

    @property
    def transactions(self):
        # type: () -> Generator[Transaction, None, None]
        i = moneydance.getCurrentAccountBook().getTransactionSet().iterator()
        for txn in i:
            if txn != txn.getParentTxn():
                continue
            yield Transaction(txn)

    def get_unreconciled_for_account_types(self, *account_types):
        # type: (*str) -> Generator[Transaction, None, None]
        for txn in self.transactions:
            if not txn.is_new:
                continue
            account_name = str(txn.account)
            for account_type in account_types:
                if account_name in self.account_names_by_type.get(account_type, set()):
                    yield txn
                    break

    def get_unreconciled_for_account_names(self, *accounts):
        # type: (*str) -> Generator[Transaction, None, None]
        accounts_to_match = set(accounts)
        for txn in self.transactions:
            if not txn.is_new:
                continue
            if str(txn.account) not in accounts_to_match:
                continue
            yield txn

    # invoke(eventstring) is called when we receive a callback for the
    # feature that we registered in the initialize method
    def __str__(self):
        return "FixDownloadedTransactions"


# setting the "moneydance_extension" variable tells Moneydance to register
# that object as an extension
# moneydance_extension = FixDownloadedTransactionsExtension.get_instance()


def immediate_mode():
    o = FixDownloadedTransactionsExtension.get_instance()
    FixerCollection.load(CSV_FILE_NAME)
    # o.show_accounts()
    # o.test_fix_transactions(AccountType.BANK)
    # o.test_fix_transactions(AccountType.CREDIT_CARD)
    # o.test_fix_transactions(AccountType.BANK, AccountType.CREDIT_CARD)
    o.fix_transactions(AccountType.BANK, AccountType.CREDIT_CARD)


immediate_mode()
