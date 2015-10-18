from mmse15project.model.Account import AccountType
from mmse15project.views.TopManagement import TopManagement
from tests.views.FrameTests import FrameTests


class TopManagementTests:
    def __init__(self):
        self.root = FrameTests(TopManagement, AccountType(3).name, "name@test.com")

TopManagementTests().root.mainloop()
