from machine import Pin,Timer

led25 = Pin ("LED",Pin.OUT)

i = 0
def second1(t):
    global i
    print("過一秒")
    led25.toggle()
    i = i + 1
    if (i>=3):
        t.deinit()
    
    
tim1 = Timer()
tim1 = Timer(period=1000, callback=second1)

