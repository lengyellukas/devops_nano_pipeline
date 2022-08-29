from hello import toyou, add, subtract

def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10
    function.y = -10
    function.you = "Lukas"
    
def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x

def test_hello_add():
    assert add(test_hello_add.x) == 11

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
    
def test_hello_add_negative_number():
    assert add(test_hello_add_negative_number.y) == -9
    
def test_hello_subtract_negative_number():
    assert subtract(test_hello_subtract_negative_number.y) == -11 
    
def test_hello_you():
    assert toyou(test_hello_you.you) == "hi Lukas"
