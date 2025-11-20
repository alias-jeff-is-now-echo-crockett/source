import re

RUBY_KEYWORDS = {
    "__ENCODING__", "__LINE__", "__FILE__", "BEGIN", "END",
    "alias", "and", "begin", "break", "case", "class", "def",
    "defined?", "do", "else", "elsif", "end", "ensure", "false",
    "for", "if", "in", "module", "next", "nil", "not", "or",
    "redo", "rescue", "retry", "return", "self", "super",
    "then", "true", "undef", "unless", "until", "when",
    "while", "yield"
}

def clean_word_ruby(w):
    w = re.sub(r'[^a-z0-9]', '', w.lower())
    if not w:
        return None

    # starts with number → prefix
    if w[0].isdigit():
        w = "w_" + w

    # Ruby keywords → add underscore
    if w in (kw.lower() for kw in RUBY_KEYWORDS):
        w = w + "_"

    return w


def extract_lyrics():
    with open("rap_god/rapgodlyrics.txt", "r") as f:
        text = f.read().lower()

    raw = re.split(r'\W+', text)
    cleaned = [clean_word_ruby(w) for w in raw]
    return [w for w in cleaned if w]


def make_ruby_file(words):
    with open("source.rb", "w") as f:
        f.write(
            "def beginning(x)\n"
            "  end_fn = ->(y) { beginning }\n"
            "  end_fn\n"
            "end\n\n"
        )

        chain = " = ".join(words) + " = beginning(nil)\n"
        f.write(chain)


if __name__ == "__main__":
    make_ruby_file(extract_lyrics())
