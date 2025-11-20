import re
import keyword

def clean_word(w):
    # keep only a–z and 0–9
    w = re.sub(r'[^a-z0-9]', '', w.lower())
    if not w:
        return None

    # pure digits -> w_###
    if w.isdigit():
        return f"w_{w}"

    # starts with digit -> prefix
    if w[0].isdigit():
        w = f"w_{w}"

    # python keywords -> suffix
    if keyword.iskeyword(w):
        w = f"{w}_"

    return w


def extract_lyrics():
    with open("rap_god/rapgodlyrics.txt", "r") as f:
        text = f.read().lower()

    raw = re.split(r'\W+', text)
    cleaned = [clean_word(w) for w in raw]
    return [w for w in cleaned if w]


def make_python_file(words):
    with open("source.py", "w") as f:
        f.write(
            "def beginning(x):\n"
            "    def end(y):\n"
            "        return beginning\n"
            "    return end\n\n"
        )
        chain = " = ".join(words) + " = beginning\n"
        f.write(chain)


if __name__ == "__main__":
    make_python_file(extract_lyrics())
