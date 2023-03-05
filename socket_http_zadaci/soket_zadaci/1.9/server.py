'''Zadatak 1.9 Napraviti čet aplikaciju (server I klijent) koja prima više klijenata i prikazuje poruke između njih.\
Klijentska strana treba biti tako organizovana da korisnik prvo funkcijom input() upisuje svoje ime\
pa prezime a potom socketio biblioteka preuzima kreiranje konekcije, kao i slanje i primanje poruka. '''
import eventlet
import socketio
sio_server = socketio.Server() 
app = socketio.WSGIApp(sio_server)
@sio_server.event
def connect(sid, headers):
    print('Client connected: ', sid)
@sio_server.event
def my_message(sid, data):
    print('Ime "{}", Prezime "{}" poruka:{}'.format(data['name'],data['surname'], data['msg']))
eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)    