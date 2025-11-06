import pytest
from bloomsayspackage import wisdom

class Tests:

    def test_avg_simple(self, capsys):
        wisdom.avg(97, 76, 67)
        captured = capsys.readouterr()
        assert "Your average grade is 80.00" in captured.out
        assert "----------------" in captured.out
        assert "@@@@" in captured.out

    def test_avg_identical_numbers(self, capsys):
        wisdom.avg(67, 67, 67)
        captured = capsys.readouterr()
        assert "Your average grade is 67.00" in captured.out
        assert "----------------" in captured.out
        assert "@@@@" in captured.out

    def test_avg_random_floats(self, capsys):
        wisdom.avg(5.5, 7.3, 8.2)
        captured = capsys.readouterr()
        assert "Your average grade is 7.00" in captured.out
        assert "----------------" in captured.out
        assert "@@@@" in captured.out

    def test_random_quote_runs(self, capsys):
        wisdom.random_quote(3)
        captured = capsys.readouterr()
        assert "----------------" in captured.out
        assert "@@@@" in captured.out

    def test_random_quote_default(self, capsys):
        wisdom.random_quote()
        captured = capsys.readouterr()
        assert any(line.strip().startswith("-") for line in captured.out.splitlines())
        assert "@@@@" in captured.out

    def test_random_quote_multiple_quotes_in_bubble(self, capsys):
        wisdom.random_quote(2)
        captured = capsys.readouterr()
        lines = captured.out.splitlines()
        bubble_lines = [line for line in lines if line.strip().startswith("<") and line.strip().endswith(">")]
        assert len(bubble_lines) >= 2
        assert "@@@@" in captured.out

    def test_coding_wisdom_default(self, capsys):
        message = wisdom.coding_wisdom()
        captured = capsys.readouterr()
        assert isinstance(message, str)
        assert "Python wisdom:" in captured.out
        assert "@@@" in captured.out
    
    def test_coding_wisdom_javascript(self, capsys):
        message = wisdom.coding_wisdom("JavaScript")
        captured = capsys.readouterr()
        assert isinstance(message, str)
        assert "JavaScript wisdom:" in captured.out
        assert "@@@" in captured.out
    
    def test_coding_wisdom_java(self, capsys):
        message = wisdom.coding_wisdom("Java")
        captured = capsys.readouterr()
        assert isinstance(message, str)
        assert "Java wisdom:" in captured.out
        assert "@@@" in captured.out
    
    def test_coding_wisdom_cpp(self, capsys):
        message = wisdom.coding_wisdom("C++")
        captured = capsys.readouterr()
        assert isinstance(message, str)
        assert "C++ wisdom:" in captured.out
        assert "@@@" in captured.out
    
    def test_coding_wisdom_unknown_language(self, capsys):
        message = wisdom.coding_wisdom("COBOL")
        captured = capsys.readouterr()
        assert isinstance(message, str)
        assert "COBOL wisdom:" in captured.out
        assert "@@@" in captured.out
    
    def test_coding_wisdom_returns_string(self):
        message = wisdom.coding_wisdom("Python")
        assert isinstance(message, str)
        assert len(message) > 0

