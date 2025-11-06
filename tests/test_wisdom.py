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

    def test_randomQuote_runs(self, capsys):
        wisdom.randomQuote(3)
        captured = capsys.readouterr()
        assert "----------------" in captured.out
        assert "@@@@" in captured.out

    def test_randomQuote_default(self, capsys):
        wisdom.randomQuote()
        captured = capsys.readouterr()
        assert any(line.strip().startswith("-") for line in captured.out.splitlines())
        assert "@@@@" in captured.out

    def test_randomQuote_multiple_quotes_in_bubble(self, capsys):
        wisdom.randomQuote(2)
        captured = capsys.readouterr()
        lines = captured.out.splitlines()
        bubble_lines = [line for line in lines if line.strip().startswith("<") and line.strip().endswith(">")]
        assert len(bubble_lines) >= 2
        assert "@@@@" in captured.out
