import psycopg2 as psg
import streamlit as st

def Query_DB(date):
    conn = psg.connect(database='indian_tbill_data', user=st.secrets['db_username'], password=st.secrets['db_password'])
    cur = conn.cursor()
    cur.execute("""SELECT yield 
                      FROM tbill_data 
                      WHERE tbill_data.date BETWEEN %s AND now() 
                      ORDER BY date""", (date,))

    yields = []
    for res in cur.fetchall():
        yields.append(float(res[0]))

    conn.close()

    return yields