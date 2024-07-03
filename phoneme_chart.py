class Place:
    BILABIAL      = 0
    ALVEOLAR      = 1
    POST_ALVEOLAR = 2
    PALATAL       = 3
    VELAR         = 4
    UVULAR        = 5
    GLOTTAL       = 6

class Manner:
    STOP        = 0
    FRICATIVE   = 1
    AFFRICATE   = 2
    NASAL       = 3
    LATERAL     = 4
    TAP         = 5
    TRILL       = 6
    APPROXIMANT = 7

MASTER_CHART_VOICELESS = [
    [ 'p' , 't' , '*' , 'c' , 'k' , 'q' , 'ʔ'  ],
    [ 'ɸ' , 's' , 'ʃ' , 'ç' , 'x' , 'χ' , 'h'  ],
    [ 'pɸ', 'ts', 'tʃ', 'tç', 'kx', 'qχ', 'ʔh' ],
    [ 'm̥' , 'n̥' , '*' , 'ɳ̥' , 'ŋ̥' , 'ɴ̥' , '*'  ],
    [ '*' , 'l̥' , '*' , '*' , 'ʟ̥' , '*' , '*'  ],
    [ '*' , 'ɾ̥' , '*' , '*' , '*' , '*' , '*'  ],
    [ 'ʙ̥' , 'r̥' , '*' , '*' , '*' , 'ʀ̥' , '*'  ],
    [ 'w̥' , '*' , '*' , 'j̥' , 'w̥' , '*' , '*'  ]
]

MASTER_CHART_VOICED = [
    [ 'b' , 'd' , '*' , 'ɟ' , 'g' , 'ɢ' , '*'  ],
    [ 'β' , 'z' , 'ʒ' , 'ʝ' , 'ɣ' , 'ʁ' , 'ɦ'  ],
    [ 'bβ', 'dz', 'dʒ', 'dʝ', 'gɣ', 'ɢʁ', '*'  ],
    [ 'm' , 'n' , '*' , 'ɳ' , 'ŋ' , 'ɴ' , '*'  ],
    [ '*' , 'l' , '*' , '*' , 'ʟ' , '*' , '*'  ],
    [ '*' , 'ɾ' , '*' , '*' , '*' , '*' , '*'  ],
    [ 'ʙ' , 'r' , '*' , '*' , '*' , 'ʀ' , '*'  ],
    [ 'w' , '*' , '*' , 'j' , 'w' , '*' , '*'  ]
]

def get_symbol(place, manner, voiced=False):
    return [MASTER_CHART_VOICELESS, MASTER_CHART_VOICED][voiced][manner - 1][place - 1]