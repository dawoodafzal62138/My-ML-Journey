# Regex patterns reference

---

## Characters

| Pattern | Meaning |
|---------|---------|
| `.` | Any character except newline |
| `\d` | Any digit (0–9) |
| `\D` | Any non-digit |
| `\w` | Word character (letter, digit, _) |
| `\W` | Non-word character |
| `\s` | Any whitespace (space, tab, \n) |
| `\S` | Any non-whitespace |
| `\n` | Newline |
| `\t` | Tab |
| `\b` | Word boundary |
| `\B` | Non-word boundary |

---

## Quantifiers

| Pattern | Meaning |
|---------|---------|
| `*` | Zero or more |
| `+` | One or more |
| `?` | Zero or one (optional) |
| `{n}` | Exactly n times |
| `{n,}` | n or more times |
| `{n,m}` | Between n and m times |
| `*?` | Lazy — zero or more (as few as possible) |
| `+?` | Lazy — one or more (as few as possible) |

---

## Anchors

| Pattern | Meaning |
|---------|---------|
| `^` | Start of string |
| `$` | End of string |
| `\A` | Absolute start of string |
| `\Z` | Absolute end of string |
| `\b` | Word boundary |

---

## Groups

| Pattern | Meaning |
|---------|---------|
| `(abc)` | Capture group |
| `(?:abc)` | Non-capturing group |
| `(?P<name>)` | Named capture group |
| `\1` | Backreference to group 1 |
| `a\|b` | Alternation (a or b) |
| `(?=abc)` | Lookahead |
| `(?!abc)` | Negative lookahead |
| `(?<=abc)` | Lookbehind |
| `(?<!abc)` | Negative lookbehind |

---

## Sets

| Pattern | Meaning |
|---------|---------|
| `[abc]` | Any one of a, b, c |
| `[^abc]` | Any character NOT in set |
| `[a-z]` | Any lowercase letter |
| `[A-Z]` | Any uppercase letter |
| `[0-9]` | Any digit |
| `[a-zA-Z]` | Any letter |
| `[a-zA-Z0-9_]` | Same as `\w` |
| `[\s\S]` | Any character including newline |

---

## Flags (Python)

| Flag | Meaning |
|------|---------|
| `re.I` | Case-insensitive |
| `re.M` | Multiline (^ and $ match per line) |
| `re.S` | Dot matches newline |
| `re.X` | Verbose (allow comments in pattern) |
| `re.A` | ASCII only |
| `re.U` | Unicode (default in Python 3) |

---

## Common ready-to-use patterns

| Pattern | Matches |
|---------|---------|
| `[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}` | Email address |
| `https?:\/\/[\w./?=#&%-]+` | URL (http or https) |
| `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` | IPv4 address |
| `<[^>]+>` | HTML tag |
| `#[0-9a-fA-F]{3,6}` | Hex color code |
| `\b\d{4}-\d{2}-\d{2}\b` | Date (YYYY-MM-DD) |
| `^(?=.*[A-Z])(?=.*\d).{8,}$` | Strong password |
| `^[a-z0-9-]+$` | URL slug |
| `\s{2,}` | Two or more spaces |
| `\b[A-Z][a-z]+ [A-Z][a-z]+\b` | Full name (basic) |