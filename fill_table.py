import os
import psycopg2


conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=""
        )


cur = conn.cursor()

cur.execute('DROP TABLE expenses;')


cur.execute('CREATE TABLE expenses (id serial PRIMARY KEY,'
                                'type varchar (150) NOT NULL,'
                                'value integer NOT NULL,'
                                'category varchar (150) NOT NULL,'
                                'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                )

# alter_query = "ALTER TABLE expenses ALTER COLUMN id TYPE SERIAL, ALTER COLUMN id SET NOT NULL, ADD PRIMARY KEY (id);"
# cur.execute(alter_query)


cur.execute('INSERT INTO expenses (type, value, category)'
            'VALUES (%s, %s, %s)',
            ('out',
            1,
            'car')
            )
            
conn.commit()

cur.close()
conn.close()