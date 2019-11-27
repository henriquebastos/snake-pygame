# Stallonecobra

Stallonecobra é um projeto de código aberto do jogo Snake com multiplayer.
O projeto utiliza python e pygame.

## Como jogar?

1. Clone o repositório.
2. Crie um virtualenv com Python >= 3.7
3. Ative o vitualenv.
4. Instale as dependências.
5. Execute os testes.
6. Execute o jogo

```console
git clone https://github.com/henriquebastos/stallonecobra.git
cd stallonecobra
python -m venv .snakenv
source .snakenv/bin/activate (Unix) || .snakenv\Scripts\activate.bat (Windows)
pip install -r requirements-dev.txt
pytest
python -m snake
```

**A versão miníma do python para rodar o jogo é 3.7**
