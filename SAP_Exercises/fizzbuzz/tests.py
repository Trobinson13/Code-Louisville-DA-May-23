import importlib
import sys
import io

def test_output(monkeypatch):
    mocked_stdout = io.StringIO()
    expected_output = "".join("""
        12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223
        FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344
        FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz6162Fizz64
        BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283
        FizzBuzz86Fizz8889FizzBuzz9192Fizz94BuzzFizz9798FizzBuzz""".split())

    with monkeypatch.context() as m:
        m.setattr(sys, "stdout", mocked_stdout)
        sys.modules.pop("fizzbuzz", None)
        importlib.import_module(name="fizzbuzz", package="files")    
        result = mocked_stdout.getvalue()
        result = "".join(result.split()) # remove all whitespace characters
        assert result == expected_output
