import itertools


onsets = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
    "bl",
    "br",
    "cl",
    "cr",
    "dr",
    "fl",
    "fr",
    "gl",
    "gr",
    "pl",
    "pr",
    "sc",
    "sk",
    "sl",
    "sm",
    "sn",
    "sp",
    "st",
    "str",
    "sw",
    "tr",
    "tw",
    "thr",
    "shr",
    "spl",
    "spr",
    "squ",
    "scr",
    "chr",
    "phr",
    "kn",
    "wr",
    "gn",
    "ps",
    "pt",
    "bd",
    "dw",
]
nuclei = [
    "a",
    "e",
    "i",
    "o",
    "u",
    "aa",
    "ae",
    "ah",
    "ao",
    "aw",
    "ay",
    "ee",
    "ei",
    "ey",
    "ie",
    "iu",
    "oa",
    "oe",
    "oi",
    "oo",
    "ou",
    "ow",
    "uu",
    "ai",
    "au",
    "aw",
    "ay",
    "ea",
    "ee",
    "ei",
    "eu",
    "ey",
    "ia",
    "ie",
    "io",
    "iu",
    "oa",
    "oe",
    "oi",
    "oo",
    "ou",
    "ow",
    "oy",
    "ua",
    "ue",
    "ui",
    "air",
    "ear",
    "eer",
    "ier",
    "oor",
    "oor",
    "our",
    "ure",
]

codas = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
    "ct",
    "ft",
    "ght",
    "ld",
    "lt",
    "mp",
    "nd",
    "nk",
    "nt",
    "pt",
    "rd",
    "rf",
    "rk",
    "rl",
    "rm",
    "rn",
    "rp",
    "rs",
    "rt",
    "rv",
    "sc",
    "sk",
    "sp",
    "st",
    "th",
    "tn",
    "ts",
    "xt",
    "zz",
    "cks",
    "cts",
    "fts",
    "lks",
    "lps",
    "lts",
    "mps",
    "nds",
    "ngs",
    "nks",
    "nts",
    "rds",
    "rfs",
    "rks",
    "rms",
    "rns",
    "rps",
    "rts",
    "sts",
]

initial_middle = ["".join(x) for x in itertools.product(onsets, nuclei)]
middle_final = ["".join(x) for x in itertools.product(nuclei, codas)]
initial_middle_final = ["".join(x) for x in itertools.product(initial_middle, codas)]

syllables = initial_middle + middle_final + initial_middle_final

with open("syllables.txt", "w") as f:
    for x in syllables:
        f.write("".join(x) + "\n")
