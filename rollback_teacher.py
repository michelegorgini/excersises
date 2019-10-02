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
            new_insert_dict = {'table_db': 'accounts',                          # dict for new account
                               'parameters': [self.name, self._balance],
                               'final_update': True}
            result = self.database.insert_row(new_insert_dict)
            if result == 'ok':
                print("Account created for {}.\n".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()

        update_balance = {'table_db': 'accounts',                      # dict for update balance in accounts table
                          'fields': ['balance', ],
                          'where_fields': ['name', ],
                          'parameters': [new_balance, self.name],
                          'final_update': False}
        self.database.update_row(update_balance)

        new_history = {'table_db': 'history',                          # dict for insert ner row in history table
                       'parameters': [deposit_time, self.name, amount],
                       'final_update': True}
        result = self.database.insert_row(new_history)
        if result == 'ok':                                             # I used this test to update sel._balance inside
            self._balance = new_balance                                # the class Account

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
        self.count_sql_in_queue = 0

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
        #print(query)
        return self.db.execute(query, parameters).fetchall()

    # def insert_row(self, table, parameters, final=True):
    def insert_row(self, new_insert):
        param_insert = []
        insert = "INSERT INTO " + new_insert['table_db'] + ' VALUES ('
        for i in range(len(new_insert['parameters'])):        # I check how many parameters we have
            if new_insert['parameters'][i] is not None:
                insert = insert + '?,'
                param_insert.append(new_insert['parameters'][i])
        insert = insert.rstrip(',')
        insert = insert + ')'
        self.count_sql_in_queue += 1                          # I create the dict for commit_on method
        self.queue['sql_code' + str(self.count_sql_in_queue)] = insert
        self.queue['parameters'+ str(self.count_sql_in_queue)] = param_insert
        # print(insert)
        # print("*insert* "*20)
        # print(self.queue)
        if new_insert['final_update']:
            result = self.commit_on()
            return result
        else:
            return

    def update_row(self, new_update):
        # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        param_update = []
        update = "UPDATE " + new_update['table_db'] + ' SET '
        for i in range(len(new_update['fields'])):                             # I fiX the SET fields
            if new_update['fields'][i] is not None:
                update = update + new_update['fields'][i] + ' = ? , '
        update = update.rstrip(' , ')
        update = update + ' WHERE ('
        for j in range(len(new_update['where_fields'])):                       # I fix the WHERE clause fields
            if new_update['where_fields'][j] is not None:
                update = update + new_update['where_fields'][j] + ' = ?)' + ' AND ('
        update = update.rstrip(' AND (')
        for i in range(len(new_update['parameters'])):                         # I check how many parameters we have
            if new_update['parameters'][i] is not None:
                param_update.append(new_update['parameters'][i])
        self.count_sql_in_queue += 1                            # I count how many sql_code we have inside self.queue
        self.queue['sql_code' + str(self.count_sql_in_queue)] = update      # I create the dict for commit_on method
        self.queue['parameters' + str(self.count_sql_in_queue)] = param_update
        if new_update['final_update']:
            result = self.commit_on()
            return result
        else:
            return

    def commit_on(self):
        if self.count_sql_in_queue == 1:         # case where we have only one sql_statements
            self.db.execute(self.queue['sql_code1'], self.queue['parameters1'])
            self.db.commit()
            self.queue.clear()             # I delete self.queue
            self.count_sql_in_queue = 0    # I put zero self.count_sql_in_queue. How many sql_statements in self.queue
            return "ok"
        else:                              # case where we have two sql_statements
            try:
                self.db.execute(self.queue['sql_code1'], self.queue['parameters1'])
                self.db.execute(self.queue['sql_code2'], self.queue['parameters2'])
            except sqlite3.Error:
                db.rollback()
            else:
                self.db.commit()
                return "ok"
            finally:
                self.queue.clear()           # I delete self.queue
                self.count_sql_in_queue = 0  # I put zero self.count_sql_in_queue.How many sql_statements in self.queue


if __name__ == '__main__':
    sql_database = Database()
    john = Account(sql_database, "John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)


    # terry = Account("TerryJ")
    # graham = Account("Graham", 9000)
    # eric = Account("Eric", 7000)
    # michael = Account("Michael")
    # terryG = Account("TerryG")

    db.close()