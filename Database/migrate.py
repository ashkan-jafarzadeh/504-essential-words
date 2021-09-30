import os
import pathlib

from Helpers.StrHelper import StrHelper
from Helpers.UserInput import UserInput

migrations = []
for file in os.listdir(str(pathlib.Path().absolute()) + "/Database/Migrations"):
    if str.endswith(file, ".py"):
        name = os.path.splitext(file)[0]
        migration = StrHelper.get_class("Database.Migrations." + name + "." + name)()
        migrations.append(migration)

method = UserInput.choice("Run the migrations or revert them?", ["up", "down"])
for migration in migrations:
    getattr(migration, method)()
    if method == "up":
        UserInput.print(migration.__class__.__name__ + " migrated.")
    else:
        UserInput.print(migration.__class__.__name__ + " reversed.")
