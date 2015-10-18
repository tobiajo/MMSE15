from mmse15project.model.Account import AccountType
from mmse15project.views.Service import Service
from tests.views.FrameTests import FrameTests


class ServiceTests:
    def __init__(self):
        self.root = FrameTests(Service, AccountType(3).name, "name@test.com")

ServiceTests().root.mainloop()
