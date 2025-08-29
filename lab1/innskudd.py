from pathlib import Path
import json
from dataclasses import dataclass

content = Path('bankdata.json').read_text(encoding='utf-8')
data = json.loads(content)


@dataclass
class Konti:
    kontonummer: str
    type: str
    navn: str
    saldo: float
    rente: float


@dataclass
class Lån:
    type: str
    beløp: float
    rente: float


@dataclass
class Personalia:
    navn: str
    fødselsdato: str


@dataclass
class Bankdata:
    personalia: Personalia
    konti: list[Konti]
    lån: list[Lån]


bankdata = Bankdata(
    personalia=Personalia(**data['personalia']),
    konti=[Konti(**konto) for konto in data['konti']],
    lån=[Lån(**lån) for lån in data['lån']]
)

name = bankdata.personalia.navn
total_saldo = sum(konto.saldo for konto in bankdata.konti)

print(f"{name} har {total_saldo} kroner i innskudd")
