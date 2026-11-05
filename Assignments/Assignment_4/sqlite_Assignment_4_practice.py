import sqlite3
conn = sqlite3.connect("sensor_data.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS sensor_data.db")


#ask for one of four options





#Database needs columns for id, timestamp, sensor type, sensor reading value


class DatabaseManager:
    cur.execute("""CREATE TABLE sensor_data.db
    (   id INT NOT NULL,
        timestamp INT NOT NULL,
        sensor_type VARCHAR(30) NOT NULL,
        sensor_reading_value INT NOT NULL,
        PRIMARY KEY (id));

    """)
    

