from tkinter import *
from tkinter.messagebox import *
import requests

#showerror("오류", "오류가 발생했습니다")

api_key = 'SJG5%2FElHZi5WQY%2B28TsujYBTK5%2BGTaOiLoN0SqNtZqO0lAPopvfv8vJShCUEe05tA0Vj2Tu7%2FWZMSwFiQRqRbg%3D%3D'
region = ''
url = ''

root = Tk()
root.title('현재 날씨')

listbox = Listbox(root)
listbox.insert(END, '남중동')
listbox.insert(END, '모현동')
listbox.insert(END, '임실읍')
listbox.insert(END, '장수읍')
listbox.insert(END, '종로구')

def select_region(event):
    global region, url
    region = listbox.get(listbox.curselection()[0])
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?&numOfRows=10&pageNo=1&dataTerm=DAILY&ver=1.3&_returnType=json' + '&serviceKey=' + api_key + '&stationName=' + region
    

listbox.bind('<<ListboxSelect>>', select_region)

text = Text(root)
b1 = Button(root, text='미세먼지 정보보기')

def get_whether(event):
    if not region:
        showerror("오류", "지역을 먼저 선택해주세요.")
        return
    text.delete(1.0, END)
    result = requests.get(url).json()['list'][0]

    text.insert(1.0, region + ' 지역의 공기상태 입니다. \n')
    text.insert(3.0, 'pm10: ' + result['pm10Value'] + '\n')
    text.insert(4.0, 'pm2.5: ' + result['pm25Value'] + '\n')

b1.bind('<Button-1>', get_whether)

listbox.grid(row=0, column=0, sticky='ew')
b1.grid(row=1, column=0, sticky='ew')
text.grid(row=2, column=0)

root.mainloop()
