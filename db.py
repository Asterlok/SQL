import sqlite3
con = sqlite3.connect('phil.db')
c = con.cursor()

"""Вывод артистов по списку"""
def show_artist():
    a = []
    c.execute('SELECT artist_id, artist_name, genre_name  FROM artist INNER JOIN genre USING(genre_id)'
              'ORDER BY 1')
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
    return a

"""Вывод импресарио по списку"""
def show_impresario():
    c.execute('SELECT impresario_id, impresario_name  FROM impresario ORDER BY 1')
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
    return a

"""Вывод сооружений по списку"""
def show_building():
    c.execute('SELECT building_id, building_name, type_name FROM building INNER JOIN type USING(type_id) ORDER BY 1')
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""Вывод мероприятий по расписанию"""
def show_activity():
    c.execute('SELECT activity_id, activity_name, activity_date FROM activity ORDER BY 3')
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""Добавить артиста"""
def add_artist(idi, name, genre):
    c.execute('INSERT INTO artist(artist_id, artist_name, genre_id) '
              'VALUES (?, ?, (SELECT genre_id FROM genre WHERE genre_name = ?))',(idi, name, genre,))
    con.commit()

"""Удалить артиста"""
def del_artist(name):
    c.execute('DELETE FROM artist WHERE artist_name = ?',(name,))
    con.commit()

"""Добавить импресарио"""
def add_impres(idi, name, genre):
    c.execute('INSERT INTO impresario(impresario_id, impresario_name, genre_id)'
              'VALUES (?, ?, ?)',(idi, name, genre))
    con.commit()

"""Удалить импресарио"""
def del_impres(name_i):
    c.execute('DELETE FROM impresario WHERE impresario_name = ?',(name_i,))
    con.commit()

"""Добавить мероприятие"""
def add_active(idi, name, date, build):
    c.execute('INSERT INTO activity(activity_id, activity_name, activity_date, building_id)'
              'VALUES (?, ?, ?, ?)',(idi, name, date, build))
    con.commit()

"""Удалить мероприятие"""
def del_active(name_a):
    c.execute('DELETE FROM activity WHERE activity_name = ?',(name_a,))
    con.commit()

"""запрос 1"""
def que_1(capa):
    c.execute('SELECT building_name FROM building INNER JOIN type USING(type_id) '
              'WHERE capacity >= ?',(capa,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 2"""
def que_2(genre):
    c.execute('SELECT artist_name FROM artist INNER JOIN genre USING(genre_id)'
              ' WHERE genre_name = ? ORDER BY artist_name',(genre,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 3"""
def que_3(name):
    c.execute('SELECT artist_name FROM artist WHERE artist_id IN'
              ' (SELECT art_imp.artist_id FROM art_imp '
              'WHERE art_imp.impresario_id ='
              ' (SELECT impresario_id FROM impresario WHERE impresario_name = ?)) '
              'ORDER BY artist_name ',(name,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 4"""
def que_4():
    c.execute('SELECT artist_name FROM artist WHERE artist_id IN'
              ' (SELECT artist_id FROM art_imp '
              'GROUP BY artist_id HAVING count(*) > 1)')
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 5"""
def que_5(name):
    c.execute('SELECT impresario_name FROM impresario WHERE impresario_id IN ('
              '	SELECT impresario_id FROM art_imp WHERE artist_id = ('
              'SELECT artist_id FROM artist WHERE artist_name = ?))', (name,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 6"""
def que_6(date_1, date_2):
    c.execute('SELECT activity_name, activity_date FROM activity '
              'WHERE activity_date BETWEEN ? AND ? ORDER BY 2', (date_1, date_2,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 7"""
def que_7(name):
    c.execute('SELECT artist_name, place, contest_name, contest_date FROM artist INNER JOIN participant USING(artist_id) INNER JOIN contest USING(contest_id)'
              'WHERE contest_name = ? AND place < 4    ORDER BY 3', (name,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 8"""
def que_8(name):
    c.execute('SELECT activity_name, building_name FROM activity INNER JOIN building USING(building_id)'
              'WHERE building_name = ?', (name,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 9"""
def que_9(name):
    c.execute('SELECT impresario_name, genre_name FROM impresario INNER JOIN genre USING(genre_id)'
              'WHERE genre_name = ?', (name,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 10"""
def que_10(date):
    c.execute('SELECT artist_name FROM artist WHERE artist_id IN'
              ' (SELECT artist_id FROM participant WHERE contest_id IN '
              '(SELECT contest_id FROM contest WHERE contest_date < ?) )', (date,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 11"""
def que_11(date):
    c.execute('SELECT building_name, count(activity_name), activity_date '
              'FROM activity INNER JOIN building USING(building_id) '
              'GROUP BY building_name HAVING activity_date > ?', (date,))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a

"""запрос 12"""
def que_12(date_1, date_2):
    c.execute('SELECT building_name, activity_date, activity_name '
              'FROM activity INNER JOIN building USING(building_id) '
              'WHERE activity_date BETWEEN ? AND ? ORDER BY 2', (date_1, date_2))
    a = []
    for data in c.fetchall():
        a.append('\n')
        a.append(data)
        a.append('\n')
    return a




