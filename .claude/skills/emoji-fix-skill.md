# Emoji Encoding Fix Skill

This skill explains how to fix Unicode/emoji encoding issues in Python on Windows.

## The Problem

When running Python scripts on Windows, you may see errors like:
```
UnicodeEncodeError: 'charmap' codec can't encode character
```

This happens because Windows console defaults to cp1252 encoding, which doesn't support emojis.

## The Solution

Add this at the top of your Python script:

```python
import sys
import io

# Force UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

## Why This Works

1. `sys.platform == 'win32'` - Checks if running on Windows
2. `sys.stdout.buffer` - The raw binary output stream
3. `io.TextIOWrapper(..., encoding='utf-8')` - Wraps it with UTF-8 encoding

This forces Python to output UTF-8 regardless of console settings.

## Alternative Solutions

**Option 2: Set environment variable before running**
```bash
set PYTHONIOENCODING=utf-8
python script.py
```

**Option 3: Use win32console (requires install)**
```python
import win32console
win32console.SetConsoleOutputCP(65001)  # UTF-8 codepage
```

## Example

```python
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Hello 🐶 🐱 🐭 🌍 ⭐")
```

This will print emojis correctly on Windows!
