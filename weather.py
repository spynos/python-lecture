from tkinter import *
from tkinter.messagebox import *
import requests

#showerror("오류", "오류가 발생했습니다")

api_key = 'a6500f0fd8e6fd71b8da2cc402bc9f5e'
region = ''
url = ''

root = Tk()
root.title('현재 날씨')

listbox = Listbox(root)
listbox.insert(END, 'Seoul')
listbox.insert(END, 'Iksan')
listbox.insert(END, 'Ulsan')
listbox.insert(END, 'Jeju')
listbox.insert(END, 'Busan')

def select_region(event):
    global region, url
    region = listbox.get(listbox.curselection()[0])
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + region + '&appid=' + api_key
    #print(url)
listbox.bind('<<ListboxSelect>>', select_region)

label = Label(root, text='제목')
entry = Entry(root)
text = Text(root)
b1 = Button(root, text='날씨보기')

def get_whether(event):
    if not region:
        showerror("오류", "지역을 먼저 선택해주세요.")
        return
    text.delete(1.0, END)
    result = requests.get(url).json()
    weather = result['weather'][0]['description']
    temp = result['main']['temp'] - 273.15
    temp = round(temp, 2)
    hum = result['main']['humidity']

    text.insert(1.0, region + ' 지역의 현재 날씨 입니다.\n\n')
    text.insert(3.0, '- 기상: ' + str(weather) + '\n')
    text.insert(4.0, '- 기온: ' + str(temp) + '도\n')
    text.insert(5.0, '- 습도: ' + str(hum) + '%')

b1.bind('<Button-1>', get_whether)

listbox.grid(row=0, column=0, sticky='ew')
b1.grid(row=1, column=0, sticky='ew')
text.grid(row=2, column=0)

root.mainloop()
