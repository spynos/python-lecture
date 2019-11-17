from tkinter import *
from tkinter.messagebox import *
from herb_model import *

root = Tk()
root.title('본초사전')

# use components
listbox = Listbox(root, exportselection=False)
label = Label(root, text='본초명')
entry = Entry(root)
text = Text(root)
b1 = Button(root, text='생성')
b2 = Button(root, text='수정')
b3 = Button(root, text='삭제')

# placements
listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=1, column=0)
entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew')
b2.grid(row=3, column=1, sticky='ew')
b3.grid(row=3, column=2, sticky='ew')

ROW_IDS = []


def load_herb_list():
    listbox.delete(0, END)
    herb_list = get_herb_list()
    for i, herb in enumerate(herb_list):
        ROW_IDS.append(herb["id"])
        listbox.insert(i, '[%s/%s/%s] %s' % (
            herb["date"][:4], herb["date"][4:6], herb["date"][6:], herb["subject"]))


def get_herb(event):
    _id = ROW_IDS[listbox.curselection()[0]]
    herb = read_herb(_id)
    entry.delete(0, END)
    entry.insert(0, herb["subject"])
    text.delete(1.0, END)
    text.insert(1.0, herb["content"])


listbox.bind('<<ListboxSelect>>', get_herb)


def refresh():
    ROW_IDS.clear()
    entry.delete(0, END)   # clear subject
    text.delete(1.0, END)  # clear content
    load_herb_list()


def btn_add(event):
    subject = entry.get().strip()
    content = text.get(1.0, END).strip()
    if not subject or not content:
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return
    add_herb(subject, content)
    refresh()


b1.bind('<Button-1>', btn_add)


def btn_modify(event):
    sel = listbox.curselection()
    if not sel:
        showerror("오류", "리스트를 먼저 선택해 주세요")
    else:
        _id = ROW_IDS[sel[0]]
    subject = entry.get().strip()
    content = text.get(1.0, END).strip()
    if not subject or not content:
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return

    modify_herb(_id, subject, content)
    refresh()


b2.bind('<Button-1>', btn_modify)


def btn_remove(event):
    sel = listbox.curselection()
    if not sel:
        showerror("오류", "리스트를 먼저 선택해 주세요")
        return
    _id = ROW_IDS[sel[0]]
    if askyesno("확인", "정말로 삭제하시겠습니까?"):
        remove_herb(_id)
        refresh()


b3.bind('<Button-1>', btn_remove)


load_herb_list()
root.mainloop()
