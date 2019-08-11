import os
from datetime import date
import pytest
from whichcraft import which
import sys

@pytest.mark.skipif(sys.platform == "win32", reason= "Does not run on windows")
def test_existing_linux():
    cmd = which("date")
    assert cmd
    assert os.path.exists(cmd)
    assert os.access(cmd, os.F_OK | os.X_OK)
    assert not os.path.isdir(cmd)


def test_non_existing_command():
    assert which("stringthatisntashellcommand") is None

@pytest.mark.skipif(sys.platform != "win32", reason= "Does not run on windows")
def test_existing_windows():
    cmd = which("cmd")
    assert cmd
    assert os.path.exists(cmd)
    assert os.access(cmd, os.F_OK | os.X_OK)
    assert not os.path.isdir(cmd)


if __name__ == "__main__":
    pytest.main()
