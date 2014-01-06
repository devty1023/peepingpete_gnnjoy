# coding=utf-8

import sqlite3
from tpmp import getCourse
from tptwt import TpTwt

print '-------------------------------'
print 'worker is running... '

DATABASE = 'twtp.db'
def connect_db():
    return sqlite3.connect(DATABASE)

tptwt = TpTwt()
db = connect_db()

# fetch all courses
cur = db.execute('select course, seats from entries')
entries = cur.fetchall()

for item in entries:
    course = item[0]
    last_seat = item[1]

    print '\t[database] course: %s seat: %i' % (course, last_seat)
    # BAD BAD PYTHON Code but whatever..
    for key, val in  getCourse(course)['Lecture'].iteritems():
        cur_seat = int(val['seat'])

    print '\t[peepingete] seat: %d' % cur_seat

    if cur_seat > last_seat:
        # tweet message
        print 'twt!'

        user = { 'twtid': 'gnnjoy', 'course': course, 'seat': cur_seat }
        tptwt.updateTwt(user)
        
    # update databse
    print '\tupdating db...\n'
    db.execute('UPDATE entries SET seats=? where course=?', [cur_seat, course])
    db.commit()


print 'exiting worker...'
