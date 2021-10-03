# !/usr/bin/env python
# coding=utf-8
# Python script to be run in Moneydance to perform amazing feats of financial scripting

try:
    from com.infinitekind.moneydance.model import *
except ImportError:
    from moneydance import *

# get the default environment variables, set by Moneydance
print "The Moneydance app controller: %s (%s)" % (moneydance, type(moneydance).__name__)
print "The current data set: %s (%s)" % (moneydance_data, type(moneydance_data).__name__)
print "The UI: %s (%s)" % (moneydance_ui, type(moneydance_ui).__name__)
print "Bot interface: %s" % moneybot


def getAccountsByType(account_type):
    # type: (str) -> list
    return [account for account in AccountIterator(moneydance_data) if account.getAccountType() == account_type and not account.getAccountOrParentIsInactive() and not account.getHideOnHomePage()]


account_types = set([str(account.getAccountType()) for account in AccountIterator(moneydance_data)])
print 'Types:', sorted(account_types)

bank_accounts = getAccountsByType(Account.AccountType.CREDIT_CARD)
for account in bank_accounts:
    print account, account.APR

if moneydance_data:
    txnSet = moneydance_data.getTransactionSet()

    counter = 0
    for txn in txnSet.iterableTxns():
        if counter < 10:
            print "transaction: date %u: description: %s for amount %s" % \
                  (txn.getDateInt(), txn.getDescription(),
                   txn.getAccount().getCurrencyType().formatFancy(
                       txn.getValue(), '.'))
        counter += 1


class ExampleExtension:
    myContext = None
    myExtensionObject = None
    name = "Fix Downloaded Transactions"

    # The initialize method is called when the extension is loaded and
    # provides the
    # extension's context.  The context implements the methods defined in
    # the FeatureModuleContext:
    # http://infinitekind.com/dev/apidoc/com/moneydance/apps/md/controller
    # /FeatureModuleContext.html
    def initialize(self, extension_context, extension_object):
        self.myContext = extension_context
        self.myExtensionObject = extension_object

        # here we register ourselves with a menu item to invoke a feature
        # (ignore the button and icon mentions in the docs)
        self.myContext.registerFeature(extension_object,
                                       "fixDownloadedTransactions", None,
                                       "Fix Downloaded Transactions")

    # invoke(eventstring) is called when we receive a callback for the
    # feature that
    # we registered in the initialize method
    def invoke(self, eventString=""):
        self.myContext.setStatus(
            "Python extension received command: %s" % (eventString))

    # invoke(eventstring) is called when we receive a callback for the
    # feature that
    # we registered in the initialize method
    def __str__(self):
        return "FixDownloadedTransactions"


# setting the "moneydance_extension" variable tells Moneydance to register that object
# as an extension
# moneydance_extension = ExampleExtension()

