import tkinter.ttk as ttk
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails
from mmse15project.views.subviews.NewTask import NewTask
from mmse15project.views.subviews.PendingTasks import PendingTasks


# AccountTeam view for Production
class Production(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        container = ttk.Frame(self)
        container.pack()
        user_info = "Production, %s — %s" % (self.acc_type, self.user)
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        if self.acc_type == "Manager":
            f1 = SearchRequest(n, self.model, self.ctrl)
            f2 = SearchRequestDetails(n, self.model, self.ctrl)
            f3 = NewTask(n, self.model, self.ctrl)
            n.add(f1, text="Search request", sticky="NS")
            n.add(f2, text="Search request details", sticky="NS")
            n.add(f3, text="New task", sticky="NS")
        if self.acc_type == "Employee" or self.acc_type == "Senior":
            f4 = PendingTasks(n, self.model, self.ctrl)
            n.add(f4, text="My task", sticky="NS")