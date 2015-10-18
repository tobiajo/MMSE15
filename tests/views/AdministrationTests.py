from mmse15project.model.Account import AccountType
from mmse15project.views.Administration import Administration
from tests.views.FrameTests import FrameTests


class AdministrationTests:
    def __init__(self):
        self.root = FrameTests(Administration, AccountType(3).name, "name@test.com")

AdministrationTests().root.mainloop()
