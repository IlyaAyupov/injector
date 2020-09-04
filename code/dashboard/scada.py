from tkinter import *
import math
import time
class Scada:
    root=None
    def __init__(self):
        self.root = Tk()
        canv = Canvas(self.root, width=1900, height=1080, bg="black", bd=0, highlightthickness=0, relief='ridge')
    def aMeterC(self, c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
        c = Canvas(self.root, width=widgLen, height=widgHigh, bg="black", bd=0, highlightthickness=0, relief='ridge')
        c.place(x=x, y=y)
        return (c, 'ameter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)

    def aMeter(self, c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
        if (nowValue > maxValue): nowValue = maxValue - 1
        devValue = float(180) / float(maxValue)
        mesureValue = devValue * nowValue
        x1 = widgLen / 2
        y1 = widgHigh / 2 + 10
        x2 = 10
        y2 = widgHigh / 2 + 10
        angle = math.pi * int(mesureValue) / 180
        newx = ((x2 - x1) * math.cos(angle) - (y2 - y1) * math.sin(angle)) + x1
        newy = ((x2 - x1) * math.sin(angle) + (y2 - y1) * math.cos(angle)) + y1
        c.create_oval(1, 1, widgLen - 1, widgHigh - 1, width=2, fill='black', outline=outerColor)
        c.create_text(7, y1, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor, text='0')
        c.create_text(widgLen - 30, y1, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                      text=str(maxValue))
        c.create_text(widgLen / 2 - 10, 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                      text=str(maxValue / 2))
        c.create_text(widgLen / 8, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                      text=str(maxValue / 4))
        c.create_text(widgLen / 2 + widgLen / 4, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER,
                      fill=outerColor, text=str(maxValue - maxValue / 4))
        c.create_text(widgLen / 2 - 20, widgHigh - 40, font="Verdana 14", anchor="w", justify=CENTER, fill=outerColor,
                      text=str(nowValue))
        c.create_rectangle(0, widgHigh / 2 + 18, widgLen, widgHigh, fill='black', outline='black')
        c.create_text(widgLen / 2 - 20, widgHigh - 40, font="Verdana 14", anchor="w", justify=CENTER, fill=outerColor,
                      text=str(nowValue))
        c.create_text(6, widgHigh - 20, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                      text=str(nameValue))
        c.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill=outerColor, outline=outerColor)
        c.create_line(x1, y1, newx, newy, width=5, fill=outerColor)

        def hTrendC(self, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef):
            c = Canvas(self.root, width=widgLen + 50, height=widgHigh + 40, bg="black", bd=0, highlightthickness=0,
                       relief='ridge')
            c.place(x=x, y=y)
            return (c, 'htrend', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef)

    def hTrendC(self, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef):
        c = Canvas(self.root, width=widgLen + 5, height=widgHigh + 40, bg="black", bd=0, highlightthickness=0,
                   relief='ridge')
        c.place(x=x, y=y)
        return (c, 'htrend', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef)
    def hTrend(self, arrayData, arrayValue):
        c, markErr, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef = arrayData
        c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
        c.create_line(50, widgHigh / 2, widgLen - 5, widgHigh / 2, width=0.1, fill='white', dash=(4, 2))
        c.create_line(50, widgHigh / 4, widgLen - 5, widgHigh / 4, width=0.1, fill='white', dash=(4, 2))
        c.create_line(50, widgHigh - widgHigh / 4, widgLen - 5, widgHigh - widgHigh / 4, width=0.2, fill='white',
                      dash=(4, 2))
        c.create_text(10, widgHigh - 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=0)
        c.create_text(10, 12, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=str(maxValue))
        c.create_text(10, widgHigh / 2, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text=str(int(maxValue / 2)))
        c.create_text(10, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text=str(int(maxValue - maxValue / 4)))
        c.create_text(10, widgHigh - widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text=str(int(maxValue / 4)))
        c.create_text(1, widgHigh + 25, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=nameValue)
        c.create_text(widgLen / 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='1')
        c.create_text((widgLen / 10) * 2, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='2')
        c.create_text((widgLen / 10) * 3, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='3')
        c.create_text((widgLen / 10) * 4, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='4')
        c.create_text((widgLen / 10) * 5, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='5')
        c.create_text((widgLen / 10) * 6, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='6')
        c.create_text((widgLen / 10) * 7, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='7')
        c.create_text((widgLen / 10) * 8, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='8')
        c.create_text((widgLen / 10) * 9, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='9')
        c.create_text(widgLen - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                      text='100')

        oldy = widgHigh - float(widgHigh) / float(maxValue) * arrayValue[0] * int(trendKoef)
        oldx = 5
        xval = 0

        for counter in range(0, len(arrayValue)):
            val = arrayValue[counter]
            yval = widgHigh - float(widgHigh) / float(maxValue) * val * int(trendKoef)
            xval += 10
            c.create_line(oldx, oldy, xval, yval, width=1.5, fill='green')

            oldy = yval
            oldx = xval
        mesureValue = arrayValue[len(arrayValue) - 1] * int(trendKoef)
        c.create_line(xval, widgHigh - 10, xval, 0, width=0.5, fill='white')

