from stream_delay import main
import pytest
import time


@pytest.mark.parametrize("option", ("-h", "--help"))
def test_help(capsys, option):
    try:
        main([option])
    except SystemExit:
        pass
    output = capsys.readouterr().out
    assert "Stream one or more files with a delay" in output


@pytest.mark.parametrize("delay", (None, "-d", "--delay-in-ms"))
def test_with_delay(tmpdir, capsys, delay):
    three_lines = str(tmpdir / "three_lines.txt")
    open(three_lines, "w").write("one\ntwo\nthree")
    start = time.time()
    args = [three_lines]
    if delay:
        args += [delay, "500"]
    try:
        main(args)
    except SystemExit:
        pass
    end = time.time()
    duration = (end - start) * 1000
    output = capsys.readouterr().out
    assert output == "one\ntwo\nthree"
    expected = 300
    if delay:
        expected = 1500
    assert (expected - 50) < duration < (expected + 50)
