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
        self.destroy()
       

class HashtagWindow(tk.Toplevel):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Toplevel.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)

        #Need a field for hashtag grabbing
        self.label1 = tk.Label(self, text='Hashtag(#)').pack()
        self.hashentry = tk.Entry(self)
        self.hashentry.pack(side=tk.TOP)

        #need a field for Start date grabbing
        #month selection

        #day selection

        #year selectinon


        #need a field for end date grabbing
        
        self.confirm = tk.Button(self, text='confirm')
        self.confirm.pack(side=tk.TOP)

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

        self.button_1 = tk.Button(self, text='@',width=25)
        self.button_1.pack(side = tk.TOP)

        self.button_2 = tk.Button(self, text='#',command=self.hash_window, width=25)
        self.button_2.pack(side = tk.TOP)

        self.button_3 = tk.Button(self, text='T', command=self.t_window,width=25)
        self.button_3.pack(side = tk.TOP)

        self.button_4 = tk.Button(self, text='Quit', command=self.quit,width=25)
        self.button_4.pack(side = tk.BOTTOM)


        
    def t_window(self):
        
        self.app = tWindow(self.master)
        
    def hash_window(self):
        
        self.app = HashtagWindow(self.master)


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


if __name__ == '__main__':        
    win = tk.Tk()
    win.title('Intro')

    dentry = introWindow(win, font=('Helvetica', 40, tk.NORMAL), border=0)
    dentry.pack()

    #win.bind('<Return>', lambda e: print(dentry.get()))
    win.mainloop()