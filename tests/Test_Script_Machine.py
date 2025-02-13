import Script_Machine as Scm
import pytest

def test_launch_script():
    script_machine = Scm.Script_Machine()

    script_machine.launch_script("scan.bat")

    assert True