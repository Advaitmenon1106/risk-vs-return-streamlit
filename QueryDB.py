import psycopg2 as psg

def Query_DB(date):
    conn = psg.connect(database='indian_tbill_data', user='postgres', password='supes@123')
    cur = conn.cursor()
    cur.execute("""SELECT yield 
                      FROM tbill_data 
                      WHERE tbill_data.date BETWEEN %s AND now();""", (date,))

    yields = []
    for res in cur.fetchall():
        yields.append(float(res[0]))

    conn.close()

    return yields