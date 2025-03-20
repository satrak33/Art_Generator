import re

def trim_text(text):
    lines = text.split('\n')

    start = 0
    end = len(lines) - 1

    while start <= end and not lines[start].strip():
        start += 1

    while end >= start and not lines[end].strip():
        end -= 1

    lines = lines[start:end + 1] if start <= end else []

    if not lines:
        return ""

    left_paddings = []
    right_paddings = []
    for line in lines:
        clean_line = re.sub(r'\x1b\[[0-9;]*m', '', line)
        left = len(clean_line) - len(clean_line.lstrip())
        right = len(clean_line) - len(clean_line.rstrip())
        left_paddings.append(left)
        right_paddings.append(right)

    min_left = min((lp for lp, line in zip(left_paddings, lines) if line.strip()), default=0)
    min_right = min((rp for rp, line in zip(right_paddings, lines) if line.strip()), default=0)

    trimmed_lines = []
    for line in lines:
        trimmed = trim_left_ansi(line, min_left)
        trimmed = trim_right_ansi(trimmed, min_right)
        trimmed_lines.append(trimmed)

    return '\n'.join(trimmed_lines)


def trim_left_ansi(line, count):
    if count <= 0:
        return line
    removed = 0
    result = []
    i = 0
    n = len(line)
    while i < n and removed < count:
        if line[i] == '\x1b' and i + 1 < n and line[i + 1] == '[':
            j = i + 2
            while j < n and line[j] != 'm':
                j += 1
            if j < n and line[j] == 'm':
                result.append(line[i:j + 1])
                i = j + 1
            else:
                result.append(line[i])
                i += 1
        else:
            if line[i].isspace():
                removed += 1
                i += 1
            else:
                break
    result.append(line[i:])
    return ''.join(result)


def trim_right_ansi(line, count):
    if count <= 0:
        return line
    removed = 0
    buffer = []
    ansi_codes = []
    i = len(line) - 1
    while i >= 0 and removed < count:
        if line[i] == 'm':
            j = i - 1
            found = False
            while j >= 0:
                if line[j] == '[' and j > 0 and line[j - 1] == '\x1b':
                    ansi_codes.append(line[j - 1:i + 1])
                    i = j - 2
                    found = True
                    break
                else:
                    j -= 1
            if not found:
                if line[i].isspace():
                    removed += 1
                else:
                    buffer.append(line[i])
                i -= 1
        else:
            if line[i].isspace():
                removed += 1
            else:
                buffer.append(line[i])
            i -= 1
    while i >= 0:
        buffer.append(line[i])
        i -= 1
    buffer.reverse()
    return ''.join(ansi_codes[::-1] + buffer)