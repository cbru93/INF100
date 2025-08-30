import json
from dataclasses import dataclass
from pathlib import Path

content = Path('bankdata.json').read_text(encoding='utf-8')
data = json.loads(content)


@dataclass
class Konti:
    """Class for bank accounts."""
    kontonummer: str
    type: str
    navn: str
    saldo: float
    rente: float


@dataclass
class Laan:
    """Class for loans."""
    type: str
    beløp: float
    rente: float


@dataclass
class Personalia:
    """Class for personal information."""
    navn: str
    fødselsdato: str


@dataclass
class Bankdata:
    """Class for bank data."""
    personalia: Personalia
    konti: list[Konti]
    lån: list[Laan]


bankdata = Bankdata(
    personalia=Personalia(**data['personalia']),
    konti=[Konti(**konto) for konto in data['konti']],
    lån=[Laan(**lån) for lån in data['lån']]
)

name = bankdata.personalia.navn
total_saldo = sum(konto.saldo for konto in bankdata.konti)

print(f"{name} har {total_saldo} kroner i innskudd")
