from mmse15project.model.Model import Model
from mmse15project.views.MainView import MainView
from mmse15project.ctrls.MainController import MainController
from mmse15project.views.Login import Login
from mmse15project.database.DBInterface import  DBInterface

__author__ = ('tobias','alessior@kth.se')


def main():
    m = Model()
    v = MainView()
    db = DBInterface("sepdb.db")
    c = MainController(m, v, db)

    c.set_frame(Login)
    v.mainloop()
