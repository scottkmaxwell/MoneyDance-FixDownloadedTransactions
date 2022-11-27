# !/usr/bin/env python
# coding=utf-8
# Python script to be run in Moneydance to perform amazing feats of
# financial scripting

try:
    from com.infinitekind.moneydance.model import *
except ImportError:
    from moneydance import *
    from com.infinitekind.moneydance.model import *

try:
    # noinspection PyUnresolvedReferences
    from typing import Dict, Generator, Iterator, List, Optional, Set, Union
except ImportError:
    pass

CSV_FILE_NAME = '/Users/smaxwell/Documents/MoneyDance.csv'


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


prefix_to_strip = ('SQ *', 'TST* ', 'PY *', 'SP * ')


def strip_prefixes(s):
    # type: (str) -> str
    if '*' in s:
        for prefix in prefix_to_strip:
            if s.startswith(prefix):
                return s[len(prefix):]
    return s


def first_word(s):
    # type: (str) -> str
    return s.partition(" ")[0].partition("*")[0].partition(".")[0].upper()


def remove_extra_spaces(s):
    return " ".join(part.strip() for part in s.split(" ") if part.strip())


def find_account(account):
    # type: (str) -> Optional[Account]
    if not account:
        return None
    return moneydance_data.getRootAccount().getAccountByName(account)


class Transaction(object):
    def __init__(self, txn):
        # type: (ParentTxn) -> None
        self._txn = txn
        self._description = remove_extra_spaces(strip_prefixes(txn.getDescription()))
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
        return self._txn.getSplit(0).getAccount() if self._txn.getSplitCount() == 1 else None

    @category.setter
    def category(self, value):
        # type: (Union[str, Account]) -> None
        if isinstance(value, str):
            value = find_account(value)
        self._txn.getSplit(0).setAccount(value)

    @property
    def dateint(self):
        # type: () -> int
        return self._txn.getDateInt()

    @property
    def description(self):
        # type: () -> str
        return self._description

    @description.setter
    def description(self, value):
        # type: (str) -> None
        if self._description != value:
            self._description = value
            self._txn.setDescription(value)

    @property
    def first_word(self):
        # type: () -> str
        return first_word(self._description)

    @property
    def dollars(self):
        # type: () -> str
        if self._dollars is None:
            # noinspection PyTypeChecker
            self._dollars = self._txn.getAccount().getCurrencyType(

            ).formatFancy(
                self._txn.getValue(), '.')
        return self._dollars

    @property
    def is_new(self):
        # type: () -> bool
        return self._txn.isNew()

    @is_new.setter
    def is_new(self, value):
        # type: (bool) -> None
        self._txn.setIsNew(value)

    @property
    def memo(self):
        # type: () -> str
        if self._memo is None:
            orig = self._txn.getTags().get(u'ol.orig-txn', "")
            if orig:
                for line in (line.strip() for line in orig.splitlines()):
                    if line.startswith('"memo"'):
                        self._memo = remove_extra_spaces(line.partition(" = ")[2])
                        break
            if not self._memo:
                self._memo = ""
        return self._memo

    def sync(self):
        # type: () -> None
        self._txn.getParentTxn().syncItem()


class Fixer(object):
    def __init__(self, replacement, exact_match="", starts_with="",
                 memo_contains="", amount=0.0, amount_below=0.0, amount_above=0.0, category="", skip_confirm=False):
        # type: (str, str, str, str, float, float, float, str, bool) -> None
        self.replacement = replacement
        if not exact_match and not starts_with:
            starts_with = replacement
        self.exact_match = remove_extra_spaces(strip_prefixes(exact_match.upper()))
        self.starts_with = strip_prefixes(starts_with.upper())
        self.memo_contains = memo_contains.upper()
        self.amount = float(amount) if amount else 0.0
        self.amount_below = float(amount_below) if amount_below else 0.0
        self.amount_above = float(amount_above) if amount_above else 0.0
        self.category = find_account(category) if category else None
        self.confirm = not skip_confirm

    def check_replacement(self, txn):
        # type: (Transaction) -> bool
        if self.starts_with:
            matched = False
            if self.exact_match and txn.description.upper() == self.exact_match:
                matched = True
            elif txn.description.upper().startswith(self.starts_with):
                matched = True
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

    def fix(self, txn):
        # type: (Transaction) -> bool
        if not self.check_replacement(txn):
            return False
        txn.description = self.replacement
        if self.confirm:
            txn.is_new = False
        if self.category:
            txn.category = self.category
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
        if fixer.exact_match:
            self.exact_matches.setdefault(fixer.exact_match, []).append(fixer)
        if fixer.starts_with:
            self.starts_with.setdefault(fixer.first_word, []).append(fixer)

    def fix(self, txn):
        # type: (Transaction) -> bool
        for possible in self.exact_matches.get(txn.description.upper(), []):
            if possible.fix(txn):
                return True
        for possible in self.starts_with.get(txn.first_word, []):
            if possible.fix(txn):
                return True
        return False

    def find_replacement(self, txn):
        # type: (Transaction) -> str
        for possible in self.exact_matches.get(txn.description.upper(), []):
            if possible.check_replacement(txn):
                return possible.replacement
        for possible in self.starts_with.get(txn.first_word, []):
            if possible.check_replacement(txn):
                return possible.replacement
        return ""


class FixerCollection(object):
    _fixer_groups_by_account_type = {}  # type: Dict[str, FixerGroup]
    _fixer_groups_by_account_name = {}  # type: Dict[str, FixerGroup]
    _global_fixers = FixerGroup()
    _loaded = set()  # type: Set[str]

    @classmethod
    def load(cls, path):
        if path not in cls._loaded:
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
            group = cls._fixer_groups_by_account_name.setdefault(account_name,
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
                      amount=amount, amount_above=amount_above, amount_below=amount_below, category=category, skip_confirm=skip_confirm),
                account_type, account_name)

    @classmethod
    def fix(cls, txn):
        # type: (Transaction) -> bool
        group = cls._fixer_groups_by_account_name.get(txn.account)
        if group and group.fix(txn):
            return True
        account_type = str(txn.account.getAccountType())
        group = cls._fixer_groups_by_account_type.get(account_type)
        if group and group.fix(txn):
            return True
        if cls._global_fixers.fix(txn):
            return True
        return False

    @classmethod
    def find_replacement(cls, txn):
        # type: (Transaction) -> str
        group = cls._fixer_groups_by_account_name.get(
            str(txn.account))  # type: FixerGroup
        if group:
            replacement = group.find_replacement(txn)
            if replacement:
                return replacement
        account_type = str(txn.account.getAccountType())
        group = cls._fixer_groups_by_account_type.get(account_type)
        if group:
            replacement = group.find_replacement(txn)
            if replacement:
                return replacement
        replacement = cls._global_fixers.find_replacement(txn)
        if replacement:
            return replacement
        return ""


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
        self.descriptions.setdefault(description, DescriptionCounter(description)).add(output)

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
        self.first_words.setdefault(fw, DescriptionFirstWordCounter(fw)).add(description, output)

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
            print 'Type:', account_type
            for account in sorted(
                    self.account_names_by_type.get(account_type, [])):
                print '- Account:', account

    def show_sample_transactions(self):  # type: () -> None
        # Costco Anywhere Visa
        # Citi Double Cash World MasterCard
        all_parented_transactions = list(
            self.get_unreconciled_for(AccountType.CREDIT_CARD))
        all_parented_transactions.sort(key=lambda x: -x.dateint)
        counter = 0
        fixed = 0
        limit = 20000
        unmodified = DescriptionContainer()
        for txn in all_parented_transactions:
            if counter < limit:
                found = FixerCollection.find_replacement(txn)
                # desc = txn.description
                desc = found or txn.description
                output = "%u: %s (%s, " \
                      "%s, %s, %s)" % \
                      (txn.dateint, desc,
                       txn.dollars,
                       txn.account,
                       txn.category,
                       txn.memo,
                       )
                if found:
                    fixed += 1
                    # print output
                else:
                    unmodified.add(desc, output)
            counter += 1
        if unmodified:
            print "\n--- Not fixed ---"
            for entry in unmodified.sorted():
                print "{}({}):".format(entry.first_word, entry.count)
                for desc in entry.sorted():
                    print "- {} ({})".format(desc.description, desc.count)
                    for o in sorted(desc.outputs):
                        print "  -", o
        print "Fixed {} of {} ({}%)".format(fixed, counter, (fixed*100/counter))

    def get_unreconciled_for(self, account_type, *account):
        # type: (str, *str) -> Generator[Transaction, None, None]
        accounts_to_match = set(account)
        for txn in moneydance.getCurrentAccountBook().getTransactionSet(

        ).iterator():
            if txn != txn.getParentTxn():
                continue
            # if not txn.getDescription().isupper():
            #     continue
            if not txn.isNew():
                continue
            # if str(txn.getClearedStatus()) != ClearedStatus.UNRECONCILED:
            #     continue
            account_name = str(txn.getAccount())
            if accounts_to_match and account_name not in accounts_to_match:
                continue
            if account_type and account_name not in \
                    self.account_names_by_type.get(
                        account_type, set()):
                continue
            yield Transaction(txn)

    # invoke(eventstring) is called when we receive a callback for the
    # feature that
    # we registered in the initialize method
    def __str__(self):
        return "FixDownloadedTransactions"


# setting the "moneydance_extension" variable tells Moneydance to register
# that object
# as an extension
# moneydance_extension = FixDownloadedTransactionsExtension.get_instance()

# FixerCollection.add("Lincoln Life Insurance for Seongsuk",
#           exact_match="ACH DEBIT *LINCOLN NATLIFE PREMP",
#           memo_contains="SEONGSUK")
# FixerCollection.add("Lincoln Life Insurance for Scott",
#           exact_match="ACH DEBIT *LINCOLN NATLIFE PREMP",
#           memo_contains="SCOTT")


class ShellFixer(Fixer):
    def __init__(self):  # type: () -> None
        super(ShellFixer, self).__init__("Shell Oil", starts_with='SHELL ', category='Automotive:Fuel')

    def check_replacement(self, txn):  # type: (Transaction) -> bool
        if super(ShellFixer, self).check_replacement(txn):
            parts = txn.description.split()
            if len(parts) < 2:
                return False
            if parts[1].upper() == 'OIL':
                return True
            return parts[1].isdigit()

FixerCollection.add(ShellFixer())

def immediate_mode():
    o = FixDownloadedTransactionsExtension.get_instance()
    FixerCollection.load(CSV_FILE_NAME)
    # o.show_accounts()
    o.show_sample_transactions()


immediate_mode()
