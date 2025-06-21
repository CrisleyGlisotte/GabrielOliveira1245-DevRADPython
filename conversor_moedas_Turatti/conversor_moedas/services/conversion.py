import requests
from datetime import datetime, timedelta
import math

# Séries do BACEN (apenas moedas relacionadas ao BRL)
SERIES_IDS = {
    ("USD", "BRL"): 1,
    ("EUR", "BRL"): 21619,
}

# Função que retorna a última data útil (dia de semana) no formato exigido pela API do BACEN
def get_last_bacen_business_day():
    """Retorna a última data útil no formato dd/mm/yyyy."""
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        if date.weekday() < 5:  # Segunda (0) a sexta (4)
            return date.strftime("%d/%m/%Y")
    raise Exception("Nenhum dia útil encontrado.")

# Função principal que retorna a taxa de câmbio entre duas moedas usando a API do BACEN
def get_bacen_rate(from_currency: str, to_currency: str) -> float:
    """Retorna a taxa de câmbio entre duas moedas, usando o BACEN como fonte."""
    if from_currency == to_currency:
        return 1.0

    date_str = get_last_bacen_business_day()

    # Função interna para buscar uma taxa de câmbio na API do BACEN usando o ID da série
    def get_rate(serie_id):
        url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie_id}/dados?formato=json&dataInicial={date_str}&dataFinal={date_str}"
        print(f"URL usada: {url}")  # Debug opcional
        resp = requests.get(url)
        print(f"Status: {resp.status_code}, Conteúdo: {resp.text[:100]}...")  # Debug opcional
        if not resp.ok or not resp.json():
            raise ValueError(f"Erro na API do BACEN para série {serie_id}")
        return float(resp.json()[0]["valor"])

    # Conversão direta
    if (from_currency, to_currency) in SERIES_IDS:
        return get_rate(SERIES_IDS[(from_currency, to_currency)])

    # Conversão inversa (ex: BRL → USD)
    if (to_currency, from_currency) in SERIES_IDS:
        return 1 / get_rate(SERIES_IDS[(to_currency, from_currency)])

    # Conversão indireta via BRL (ex: USD ↔ EUR)
    if from_currency in ["USD", "EUR"] and to_currency in ["USD", "EUR"]:
        rate_from_brl = get_rate(SERIES_IDS[(from_currency, "BRL")])
        rate_to_brl = get_rate(SERIES_IDS[(to_currency, "BRL")])
        return rate_from_brl / rate_to_brl

    raise ValueError("Conversão não suportada.")

# Função que trunca um valor decimal sem arredondar, mantendo casas decimais especificadas
def truncate(value, decimals=2):
    """Trunca o valor para a quantidade de casas decimais sem arredondar."""
    factor = 10 ** decimals
    return math.trunc(value * factor) / factor
    
# Função final que converte o valor entre duas moedas, utilizando a taxa obtida via BACEN
def convert_currency(value: float, currency_from: str, currency_to: str) -> float:
    """Converte um valor entre duas moedas, truncando para 2 casas decimais."""
    try:
        rate = get_bacen_rate(currency_from, currency_to)
        resultado = value * rate
        return truncate(resultado, 2)
    except Exception as e:
        print(f"Erro ao converter: {e}")
        return "Não foi possível converter!"