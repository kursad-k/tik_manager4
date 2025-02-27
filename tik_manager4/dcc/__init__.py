import os
from importlib import reload

NAME = os.getenv("TIK_DCC").lower()

if NAME == "3dsmax":
    from tik_manager4.dcc.max.main import Dcc
elif NAME == "blender":
    from tik_manager4.dcc.blender.main import Dcc
elif NAME == "houdini":
    from tik_manager4.dcc.houdini.main import Dcc
elif NAME == "katana":
    from tik_manager4.dcc.katana.main import Dcc
elif NAME == "mari":
    from tik_manager4.dcc.mari.main import Dcc
elif NAME == "maya":
    from tik_manager4.dcc.maya.main import Dcc
elif NAME == "nuke":
    from tik_manager4.dcc.nuke.main import Dcc
elif NAME == "photoshop":
    from tik_manager4.dcc.photoshop.main import Dcc
elif NAME == "standalone":
    from tik_manager4.dcc.standalone.main import Dcc
elif NAME == "trigger":
    from tik_manager4.dcc.trigger.main import Dcc
else:
    raise ValueError(f"Environment variable 'TIK_DCC' value ({NAME} is not matching any defined DCCs.")
