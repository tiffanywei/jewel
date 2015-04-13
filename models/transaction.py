class Transaction(object):
  """
  Given a primary user and a transaction type compute the debtor and creditor
  of the transaction.
  """
  class Type:
    BORROWED = 'borrowed'
    LENT = 'lent'

  def __init__(self, transaction_type, primary_user, secondary_user):
    self._transaction_type = transaction_type
    self._primary_user = primary_user
    self._secondary_user = secondary_user

  def get_debtor(self):
    return self._primary_user if self.transaction_type == Transaction.Type.BORROWED else self._secondary_user

  def get_creditor(self):
    return self._primary_user if self.transaction_type == Transaction.Type.LENT else self._secondary_user
