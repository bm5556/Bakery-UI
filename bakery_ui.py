import tkinter
from tkinter import *

class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view: BakeryView):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        self.sand = StringVar()
        Label(window, text="샌드위치 (5000원)").grid(column=1, row=1, sticky=W)
        sand_entry = Entry(window, width=7, textvariable=self.sand)
        sand_entry.grid(column=2, row=1, sticky=(W, E))

        self.cake = StringVar()
        Label(window, text="케이크 (20000원)").grid(column=1, row=2, sticky=W)
        sand_entry = Entry(window, width=7, textvariable=self.cake)
        sand_entry.grid(column=2, row=2, sticky=(W, E))

        Button(window, text="주문하기", command=self.send_order).grid(column=1, row=3, sticky=W)

    def send_order(self):

        sand = str(self.sand.get())
        cake = str(self.cake.get())

        is_sand = True
        is_cake = True
        for s in sand:
            if (s < '0') or (s > '9'):
                is_sand = False
                break
        for c in cake:
            if (c < '0') or (c > '9'):
                is_cake = False
                break

        if is_sand and is_cake:
            order_text = str(f"{self.name}: 샌드위치 (5000원) {sand}개, 케이크 (20000원) {cake}개")
        elif is_sand:
            order_text = str(f"{self.name}: 샌드위치 (5000원) {sand}개")
        elif is_cake:
            order_text = str(f"{self.name}: 케이크 (20000원) {cake}개")

        if is_sand or is_cake:
            self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
