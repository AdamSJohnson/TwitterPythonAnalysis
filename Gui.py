try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class tWindow(tk.Toplevel):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Toplevel.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)

        

        self.quitb = tk.Button(self, text='Quit', command=self.close_window)
        self.quitb.pack()
    def close_window(self):
        self.destroy()

class introWindow(tk.Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Frame.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)

        self.button_1 = tk.Button(self, text='@')
        self.button_1.pack(side = tk.LEFT)

        self.button_2 = tk.Button(self, text='#')
        self.button_2.pack(side = tk.LEFT)

        self.button_3 = tk.Button(self, text='T', command=self.t_window)
        self.button_3.pack(side = tk.LEFT)

        self.button_4 = tk.Button(self, text='Quit', command=self.quit)
        self.button_4.pack(side = tk.BOTTOM)


        '''
        self.entry_1 = tk.Entry(self, width=2, **args)
        self.label_1 = tk.Label(self, text='/', **args)
        self.entry_2 = tk.Entry(self, width=2, **args)
        self.label_2 = tk.Label(self, text='/', **args)
        self.entry_3 = tk.Entry(self, width=4, **args)

        self.entry_1.pack(side=tk.LEFT)
        self.label_1.pack(side=tk.LEFT)
        self.entry_2.pack(side=tk.LEFT)
        self.label_2.pack(side=tk.LEFT)
        self.entry_3.pack(side=tk.LEFT)

        self.entries = [self.entry_1, self.entry_2, self.entry_3]

        self.entry_1.bind('<KeyRelease>', lambda e: self._check(0, 2))
        self.entry_2.bind('<KeyRelease>', lambda e: self._check(1, 2))
        self.entry_3.bind('<KeyRelease>', lambda e: self._check(2, 4))
        '''
    def t_window(self):
        #self.newWindow = tk.Toplevel(self.master)
        self.app = tWindow(self.master)
        

    def _backspace(self, entry):
        cont = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, cont[:-1])

    def _check(self, index, size):
        entry = self.entries[index]
        next_index = index + 1
        next_entry = self.entries[next_index] if next_index < len(self.entries) else None
        data = entry.get()

        if len(data) > size or not data.isdigit():
            self._backspace(entry)
        if len(data) >= size and next_entry:
            next_entry.focus()

    def get(self):
        return [e.get() for e in self.entries]


if __name__ == '__main__':        
    win = tk.Tk()
    win.title('Intro')

    dentry = introWindow(win, font=('Helvetica', 40, tk.NORMAL), border=0)
    dentry.pack()

    #win.bind('<Return>', lambda e: print(dentry.get()))
    win.mainloop()