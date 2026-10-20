######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab5_problem1"
test_inputs = []

def test(monkeypatch, capsys):
    global test_file
    global test_inputs
    try:
        exists = os.path.exists(test_file + '.py')
        assert exists == True
        source = __import__(test_file)
    except:
        sys.exit()
    if len(test_inputs) > 0:
        inputs = iter(test_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 21 lines of output
    assert len(output) == 21, "Incorrect overall output"
    
    # Test: Ensure output matches expected results
    expected_output = [
        'ABCDEFG',
        'TUVWXYZ',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        'AUCWEYG',
        'TBVDXFZ',
        'BTDVFXHSCUEWGY',
        'YGWEUCSHXFVDTB'
    ]
    for i in range(1,20):
        assert output[i] == expected_output[i-1], "Incorrect output"

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################