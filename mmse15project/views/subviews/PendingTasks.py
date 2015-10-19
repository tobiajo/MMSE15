import tkinter.ttk as ttk
from mmse15project.model.Task import TaskStatus


class PendingTasks(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        b1 = ttk.Button(self, text="Update",
                       command=lambda: self.ctrl.pending_tasks_update(self))
        b1.grid(row=0)

        self.update = self.Update(self, self.model, self.ctrl)
        self.update.grid(row=1)

    class Update(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            user = self.master.master.master.master.user
            #tasks = self.model.task_db.getByStatusAndEmail(1, user) + self.model.task_db.getByStatusAndEmail(2, user)
            #tasks = self.model.task_db.getByStatus(1)
            tasks = self.model.task_db.getByStatusAndEmail(1, user)
            print(tasks)
            ttk.Label(self, text="TaskID(Priority):").grid(row=0, sticky="E")
            ttk.Label(self, text="Status").grid(row=0, column=1, sticky="W")
            row = 1
            for t in tasks:
                ttk.Label(self, text="[id]" + "(" + str(t.priority) + "):").grid(row=row, sticky="E")
                status = TaskStatus(t.status).name
                ttk.Label(self, text=status).grid(row=row, column=1, sticky="W")
                row += 1
                print(t.operator)
