class Place:
    BILABIAL      = 1
    ALVEOLAR      = 2
    POST_ALVEOLAR = 3
    PALATAL       = 4
    VELAR         = 5
    UVULAR        = 6
    GLOTTAL       = 7

class Manner:
    STOP        = 1
    FRICATIVE   = 2
    AFFRICATE   = 3
    NASAL       = 4
    LATERAL     = 5
    TAP         = 6
    TRILL       = 7
    APPROXIMANT = 8

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