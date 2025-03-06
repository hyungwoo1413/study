import socketio

sio = socketio.Client()
number = 0

@sio.event
def connect():
    print("연결 완료")

@sio.event
def disconnect():
    print("연결 해제")

@sio.on('take')
def on_take(data):
    global number
    number = data

if __name__ == "__main__":
    sio.connect('http://localhost:5000', wait_timeout= 10)

    while True:
        num = int(input('정수를 입력하세요(종료-X) : '))
        sio.call('double', num)
        print(number)
        
        if 'x' == num:
            sio.disconnect()
            break