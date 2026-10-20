######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest
import random
import string

test_file = "lab5_problem2"
test_inputs = [''.join(random.choices(
    string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, 
    k=random.randrange(14, 50)))]

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

    assert test_inputs[0] == source.decrypt_message(
        source.encrypt_message(test_inputs[0], source.key),
        source.key), "Encryption/decrypt process failed"

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 4 lines of output
    assert len(output) == 4, "Incorrect overall output"

    # Test: Original message
    assert output[1] == 'Original message: ' + test_inputs[0], "Incorrect output"
    
    # Test: Encrypted message
    assert output[2] == 'Encrypted message: ' + source.encrypt_message(test_inputs[0], source.key), "Incorrect output"
    
    # Test: Decrypted message
    assert output[3] == 'Decrypted message: ' + test_inputs[0], "Incorrect output"

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################