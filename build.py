from TBM_RezManager import utils
import os
import shutil

EXE_CMD = """
echo ############################# & ^
echo #                           # & ^
echo #   Launching TBM_factory   # & ^
echo #                           # & ^
echo ############################# & ^
start "" pythonw -c "from gaa_to_delete.UI import show;show()"
"""

class Build(utils.Build):

    def post_build(self):



        # launchers
        dest_bin = os.path.join(self.base_path, "bin")
        utils.make_dir(dest_bin)

        for ext in ["exe", "bat"]:
            self.create_launcher(data=EXE_CMD, 
                                 path=dest_bin, 
                                 name=self.project, 
                                 ext=ext,
                                 icon=os.path.join(self.build_path, "resources", 'TBM.ico'))

        #Package info file
        self.create_package_info(
            os.path.join(self.build_path, "python", "gaa_to_delete", '__version__.py'))

if __name__ == "__main__":
    Build(exclude_patterns=["*.pyc", "__pycache__"], 
          keep_roots=["LICENCE", 
                      "resources", 
                      "README.md", 
                      "bin",
                      "shelves",
                      "scripts",
                      "icons",
                      "docs", 
                      "python"],
          compile=True
    )
