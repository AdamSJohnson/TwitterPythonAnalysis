try:
    import Tkinter as tk
    import ScrolledText as tkst
except ImportError:
    import tkinter as tk
    import tkinter.scrolledtext as tkst

from tkinter import END, LEFT, RIGHT, TOP, BOTTOM, BOTH, Y, NE, NS, NSEW, W, E, YES
from tkinter import ttk
from tkinter.font import Font
from tkinter import VERTICAL, HORIZONTAL
import AnalysisCommands as ac


class CellWindow:
    SortDir = True
    def __init__(self, master, intensities=''):
        self.master = master
        self.frame = tk.Frame( self.master, height=0, width=900 )
        self.tree_frame = tk.Frame(self.frame, height=0, width=900)
        self.tree_frame.pack_propagate(0)
        self.tree_frame.pack()
        self.dataCols = ('Tweet', 'Negative', 'Neutral', 'Positive', 'Compound')
        self.tree = ttk.Treeview( self.frame, height = 14, columns= self.dataCols, selectmode="extended", show='headings')

        for x in self.dataCols:
            self.data = self.intensity_fixer( intensities=intensities)

        self.tree.pack(fill=BOTH)
        self._load_data()
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack(side=LEFT)

        self.exportButton = tk.Button(self.frame, text='Export', width=25, command=self.export_data)


        self.exportButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def export_data(self):
        file_obj = open('export.txt', 'w')
        for item in self.data:
            for x in item:
                file_obj.write(x + " ")
            file_obj.write('\r\n')


    def intensity_fixer(self, intensities=''):
        #[songname, comp, neg, neu, pos, art, sample]
        result =[]
        for i in intensities:
            temp = []
            temp.append(i[0])
            temp.append('{:05.2f}'.format(100 * i[1]))
            temp.append('{:05.2f}'.format(100 * i[2]))
            temp.append('{:05.2f}'.format(100 * i[3]))
            temp.append('{:05.2f}'.format(100 * i[4]))
            result.append(temp)

        return result

    def _load_data(self):
        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(),
                              command=lambda c=c: self._column_sort(c, CellWindow.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', values=item)


    def _column_sort(self, col, descending=False):

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier
            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth =  Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                    self.tree.column(self.dataCols[idx], width=iwidth)

        # reverse sort direction for next sort operation
        CellWindow.SortDir = not descending
    

class tWindow(tk.Toplevel):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Toplevel.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)

        self.textbox = tkst.ScrolledText(self, width  = 20, height = 18)
        self.textbox.pack(side=tk.TOP)

        self.confirm = tk.Button(self, text='confirm', command=self.testingsystem)
        self.confirm.pack(side=tk.TOP)

        self.quitb = tk.Button(self, text='Quit', command=self.close_window)
        self.quitb.pack()

    def close_window(self):
        self.destroy()

    def testingsystem(self):
        self.test = self.textbox.get('1.0', tk.END)
        self.statuses = []
        self.statuses.append(self.test)
        #print(self.statuses)
        self.newWindow = tk.Toplevel(self.master)
        self.app = CellWindow(self.newWindow, intensities=ac.status_list_analysis(statuslist=self.statuses))
       

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