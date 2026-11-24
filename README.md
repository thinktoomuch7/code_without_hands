# code_without_hands
无人编码demo

Minimal Python CLI demo built with the standard library only.

## Requirements

- Python 3.10 or newer
- pytest (development only)

## Install

```bash
python -m pip install -e ".[dev]"
```

## Run

```bash
python -m cwh.cli hello --name 世界
```

The `--name` option defaults to `世界`, so `python -m cwh.cli hello` prints
`hello, 世界`. The command always prints exactly one line: `hello, <name>`.

## 运行示例

```bash
python -m cwh.cli hello
python -m cwh.cli hello --name Ada
```

## Test

```bash
python -m pytest
```

## License

MIT — see [LICENSE](LICENSE).
