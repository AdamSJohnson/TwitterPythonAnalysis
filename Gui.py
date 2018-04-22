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
from TwitterCommands import getUserTweets

from datetime import date
import datetime
    

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
        self.topFrame = tk.Frame(self)
        #Need a field for hashtag grabbing
        self.label1 = tk.Label(self.topFrame, text='Hashtag(#)').pack(side=tk.LEFT)
        self.hashentry = tk.Entry(self.topFrame)
        self.hashentry.pack(side=tk.RIGHT)
        self.topFrame.pack(side=tk.TOP)

        self.fromFrame = tk.Frame(self)
        #need a field for Start date grabbing
        #month selection
        self.label2 = tk.Label(self.fromFrame, text='From').pack(side=LEFT)
        self.montha = tk.Entry(self.fromFrame,width=5)
        self.montha.pack(side=tk.LEFT)
        #day selection

        self.daya = tk.Entry(self.fromFrame,width=5)
        self.daya.pack(side=tk.LEFT)
        #year selectinon
        self.yeara = tk.Entry(self.fromFrame,width=5)
        self.yeara.pack(side=tk.LEFT)
        self.fromFrame.pack()


        #need a field for end date grabbing
        self.toFrame = tk.Frame(self)
        #need a field for Start date grabbing
        #month selection
        self.label3 = tk.Label(self.toFrame, text='To').pack(side=LEFT)
        self.monthb = tk.Entry(self.toFrame,width=5)
        self.monthb.pack(side=tk.LEFT)
        #day selection

        self.dayb = tk.Entry(self.toFrame,width=5)
        self.dayb.pack(side=tk.LEFT)
        #year selectinon
        self.yearb = tk.Entry(self.toFrame,width=5)
        self.yearb.pack(side=tk.RIGHT)
        self.toFrame.pack()


        self.confirm = tk.Button(self, text='confirm',anchor=tk.W, command=self.hashsearching)
        self.confirm.pack(side=tk.TOP)

        self.quitb = tk.Button(self, text='Quit', command=self.close_window, anchor=tk.W)
        self.quitb.pack()
        
    def close_window(self):
        self.destroy()

    def hashsearching(self):
        #get the hashtag
        try:
            self.hashtag = self.hashentry.get()
        except tk._tkinter.TclError:
            print('ay no value')
            self.destroy()
            return 0

        if self.hashtag == '':
            print('no search')
            self.destroy()
            return 0
        print(self.hashtag)
        try:
            self.month_a = self.montha.get()
            self.day_a = self.daya.get()
            self.year_a = self.yeara.get()

            self.month_b = self.monthb.get()
            self.day_b = self.dayb.get()
            self.year_b = self.yearb.get()

        except tk._tkinter.TclError:
            print('no search')
            self.destroy()
            return 0
        try:
            print(self.hashtag)
            self.moa = int(self.month_a)
            self.daa = int(self.day_a)
            self.yea = int(self.year_a)

            self.mob = int(self.month_b)
            self.dab = int(self.day_b)
            self.yeb = int(self.year_b)

            self.adate = date(self.yea,self.moa,self.daa)
            self.bdate = date(self.yea,self.moa,self.daa)

            if(self.adate > self.bdate):
                #search from bdate to adate
                print('Searchin B TO A')
            else:
                #search adate to bdate
                print('Searchin A TO B')
        except ValueError:
            print('Value Error occured only searching based on hash')
            print('Searching based on hashtag')
        self.destroy()
        return 0


class introWindow(tk.Frame):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Frame.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)

        self.button_1 = tk.Button(self, text='@',width=25, command=self.user_window)
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

    def user_window(self):
        self.app = UserWindow(self.master)


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

class UserWindow(tk.Toplevel):
    def __init__(self, master, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Toplevel.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)
        self.topFrame = tk.Frame(self)
        #Need a field for hashtag grabbing
        self.label1 = tk.Label(self.topFrame, text='User').pack(side=tk.LEFT)
        self.userentry = tk.Entry(self.topFrame)
        self.userentry.pack(side=tk.RIGHT)
        self.topFrame.pack(side=tk.TOP)

        self.fromFrame = tk.Frame(self)
        #need a field for Start date grabbing
        #month selection
        self.label2 = tk.Label(self.fromFrame, text='From').pack(side=LEFT)
        self.montha = tk.Entry(self.fromFrame,width=5)
        self.montha.pack(side=tk.LEFT)
        #day selection

        self.daya = tk.Entry(self.fromFrame,width=5)
        self.daya.pack(side=tk.LEFT)
        #year selectinon
        self.yeara = tk.Entry(self.fromFrame,width=5)
        self.yeara.pack(side=tk.LEFT)
        self.fromFrame.pack()


        #need a field for end date grabbing
        self.toFrame = tk.Frame(self)
        #need a field for Start date grabbing
        #month selection
        self.label3 = tk.Label(self.toFrame, text='To').pack(side=LEFT)
        self.monthb = tk.Entry(self.toFrame,width=5)
        self.monthb.pack(side=tk.LEFT)
        #day selection

        self.dayb = tk.Entry(self.toFrame,width=5)
        self.dayb.pack(side=tk.LEFT)
        #year selectinon
        self.yearb = tk.Entry(self.toFrame,width=5)
        self.yearb.pack(side=tk.RIGHT)
        self.toFrame.pack()


        self.confirm = tk.Button(self, text='confirm',anchor=tk.W, command=self.hashsearching)
        self.confirm.pack(side=tk.TOP)

        self.quitb = tk.Button(self, text='Quit', command=self.close_window, anchor=tk.W)
        self.quitb.pack()
        
    def close_window(self):
        self.destroy()

    def hashsearching(self):
        #get the hashtag
        try:
            self.user = self.userentry.get()
        except tk._tkinter.TclError:
            print('ay no value')
            self.destroy()
            return 0

        if self.user == '':
            print('no search')
            self.destroy()
            return 0
        print(self.user)
        try:
            self.month_a = self.montha.get()
            self.day_a = self.daya.get()
            self.year_a = self.yeara.get()

            self.month_b = self.monthb.get()
            self.day_b = self.dayb.get()
            self.year_b = self.yearb.get()

        except tk._tkinter.TclError:
            print('no search')
            self.destroy()
            return 0
        try:
            print(self.user)
            self.moa = int(self.month_a)
            self.daa = int(self.day_a)
            self.yea = int(self.year_a)

            self.mob = int(self.month_b)
            self.dab = int(self.day_b)
            self.yeb = int(self.year_b)

            self.adate = date(self.yea,self.moa,self.daa)
            self.bdate = date(self.yea,self.moa,self.daa)

            if(self.adate > self.bdate):
                #search from bdate to adate
                print('Searchin B TO A')
            else:
                #search adate to bdate
                print('Searchin A TO B')
        except ValueError:
            print('Value Error occured only searching based on hash')
            print('Searching based on user')
            self.start = datetime.datetime(2016, 1, 1, 0, 0)
            self.end = datetime.datetime(2019, 12, 31, 23, 59)
            self.statuses = getUserTweets(self.user,self.start,self.end,1000)
            self.temp = []
            for tweet in self.statuses:
                char_list = [tweet[j] for j in range(len(tweet)) if ord(tweet[j]) in range(65536)]
                tweet=''
                for j in char_list:
                    tweet=tweet+j
                self.temp.append(tweet)
            self.statuses = self.temp
            self.newWindow = tk.Toplevel(self.master)
            self.app = CellWindow(self.newWindow, intensities=ac.status_list_analysis(statuslist=self.statuses))

        self.destroy()
        



if __name__ == '__main__':        
    win = tk.Tk()
    win.title('Intro')

    dentry = introWindow(win, font=('Helvetica', 40, tk.NORMAL), border=0)
    dentry.pack()

    #win.bind('<Return>', lambda e: print(dentry.get()))
    win.mainloop()