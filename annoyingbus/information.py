from tabulate import tabulate
import sqlite3

class Information(object):

    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE journey 
            (Company text, Origin text, Destination text, Date text, 
            Departure text, Arrival text, Duration text, Price real)
            """)
        self.row_info = {} 
    
    def update_row(self):
        self.cursor.execute("""
            INSERT INTO journey (Company, Origin, Destination, Date,
            Departure, Arrival, Duration, Price)
            VALUES (:Company, :Origin, :Destination, :Date,
            :Departure, :Arrival, :Duration, :Price)
            """, self.row_info)

    def show_all(self):
        curs = self.conn.execute("SELECT * FROM journey")
        headers = [description[0] for description in curs.description]
        self.cursor.execute("""
            SELECT * FROM journey ORDER BY datetime(Date), datetime(Departure)
            """)
        print(tabulate(self.cursor.fetchall(), headers=headers))
    
    def close(self):
        self.conn.commit()
        self.conn.close()

