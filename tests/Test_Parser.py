import Parser as Ps
import pytest

def test_parse():
    parser = Ps.Parser()

    assert parser._parse("scanresults.xml") == "?"
