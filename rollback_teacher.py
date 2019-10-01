import sqlite3
import datetime
import pytz



db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    @staticmethod
    def _current_time():
        #return 1
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, database, name: str, opening_balance: int = 0):
        self.database = database
        self.name = name
        self._balance = opening_balance
        row = self.database.select_one('accounts', ['name', 'balance'], ['name'], [self.name])

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}\n".format(self.name), end='')
        else:
            # ***** New Code
            new_insert_dict = {'table_db': {'table': 'accounts'},
                                #'where_fields': {'where_field1': None, 'where_field2': None},
                                'parameters': {'name': 'self.name', 'balance': 'self._balance'},
                                'final_update': {'final': True}}

            # print("%"*20)
            # print(type(new_insert_dict))
            print(new_insert_dict)
            # print("%"*20)
            self.database.insert_row(new_insert_dict)
            # ***** New Code

            # self.database.commit_single(new_account[0], new_account[1])
            print("Account created for {}.\n".format(self.name), end='')
        self.show_balance()


    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        # statments = (('accounts', ['balance',], ['name'], [new_balance, self.name], False))
        update_balance = self.database.update_row(('accounts', ['balance',], ['name'], [new_balance, self.name], False))
        # print("?"*20)
        # print(update_balance)
        # print("?"*20)
        # remember "balance' must to be multiple fields
        new_history = self.database.insert_row_history('history', [deposit_time, self.name, amount])
        # print("!"*20)
        # print(new_history)
        # print("!"*20)
        result = self.database.commit(update_balance[0], update_balance[1], new_history[0], new_history[1])
        if result:
            self._balance = new_balance

    def deposit(self, amount: int) -> float:
        print("{} wants to deposit {:.2f} euros".format(self.name, amount / 100))
        if amount > 0.0:
            self._save_update(amount)
            print("{} GOT the deposit of {:.2f} euros".format(self.name, amount / 100))
            print("="*100)
        self.show_balance()
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        print("{} wants to withdraw {:.2f} euros".format(self.name, amount / 100))
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{} GOT the withdraw of {:.2f} euros".format(self.name, amount / 100))
            print("="*100)
            self.show_balance()
            return amount / 100
        else:
            print("You withdraw {} and your balance is {}. You cannot do it".format(amount/100, self._balance/100))
            print("="*100)
            self.show_balance()
            return 0.0


    def show_balance(self):
        print("Balance on account {} is {:.2f}\n".format(self.name, self._balance / 100))


class Database:

    def __init__(self):
        self.db = sqlite3.connect("accounts.sqlite")
        self.queue = {}

    def select_one (self, table, fields, where_fields, parameters):
        # cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        query = "SELECT "
        for field in fields:
            query = query + field + ','
        query = query.rstrip(',')
        query = query + ' FROM ' + table
        query = query + ' WHERE '
        for field in where_fields:
            query = query + '(' + field + ' = ' + '?' + ')' + ' AND '
        query = query.rstrip(' WHERE ')
        query = query.rstrip(' AND ')
        #print(query)
        return self.db.execute(query, parameters).fetchone()

    def select_all (self, table, where_fields, parameters):
        # cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        query = "SELECT * FROM " + table
        query = query + ' WHERE '
        for field in where_fields:
            query = query + '(' + field + ' = ' + '?' + ')' + ' AND '
        query = query.rstrip(' AND ')
        print(query)
        return self.db.execute(query, parameters).fetchall()

    #def insert_row(self, table, parameters, final=True):  # I make the insert SQL statement
    # ***** New Code
    def insert_row(self, kwargs):
        insert = "INSERT INTO " + kwargs['table_db']['table'] + ' VALUES ('
        for par in kwargs['parameters']:
            if par:
                insert = insert + '?,'
        insert = insert.rstrip(',')
        insert = insert + ')'
        print(insert)
        self.queue['sql_code'] = insert
        self.queue['name'] = kwargs['parameters']['name']
        self.queue['balance'] = kwargs['parameters']['balance']
        self.queue['final'] = kwargs['final_update']['final']
        print(self.queue)
        if self.queue['final']:
            self.db.commit(self.queue)
        else:
            return
    # ***** New Code


    def insert_row_history (self, table, parameters, final=True):  # I make the insert SQL statement
        insert = "INSERT INTO " + table + ' VALUES (?, ?, ?)'
        return insert, parameters

    def update_row(self, table, field, where_fields, parameters, final=True):   # I make the update SQL statement
        # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        update = "UPDATE " + table + ' SET ' + field + ' = ? WHERE '
        for cond in where_fields:
            update = update + '(' + cond + ' = ' + '?' + ')' + ' AND '
        update = update.rstrip(' AND ')
        #add statement to the list as a tuple of an operation and parameters

        #if final, commit by using the commit function

        #else do nothing

        return update, parameters

    def commit(self, kwargs):
        # commit the entire queue
        print(type(kwargs))
        print(kwargs)
        pass

        try:
            db.execute(operation1, parameters1)
            db.execute(operation2, parameters2)
        except sqlite3.Error:
            db.rollback()
            print("Commit blocked")
        else:
            db.commit()
            print("Commit executed with success")
            return "ok"

if __name__ == '__main__':
    sql_database = Database()
    john = Account(sql_database, "John")
    # john.deposit(1010)
    # john.deposit(10)
    # john.deposit(10)
    # john.withdraw(30)
    # john.withdraw(0)


    # terry = Account("TerryJ")
    # graham = Account("Graham", 9000)
    # eric = Account("Eric", 7000)
    # michael = Account("Michael")
    # terryG = Account("TerryG")

    db.close()
