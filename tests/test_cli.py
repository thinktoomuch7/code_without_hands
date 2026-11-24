from cwh.cli import main


def test_hello_uses_default_name(capsys):
    exit_code = main(["hello"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "hello, 世界\n"
    assert captured.out.strip() == "hello, 世界"
    assert captured.err == ""


def test_hello_accepts_custom_name(capsys):
    exit_code = main(["hello", "--name", "Ada"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "hello, Ada\n"
    assert captured.out.strip() == "hello, Ada"
    assert captured.err == ""
