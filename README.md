<img height="170em" src="http://i.imgur.com/eVj2DWl.png">

_money management, simplified._

> moneta helps you organise your accounts, budgets, and credit cards, all under one umbrella.

> moneta analyses your spending behavior to predict future spending patterns and offers suggestions to help you save for what matters most.

### Running moneta
- Install dependencies:
  - Python 2
  - MySQL
  - `pip install -r requirements.txt`
- Configure APIs
  - Set Plaid API keys in `settings.py`
- Migrate database
  - `python manage.py migrate`
- Run moneta
  - `python manage.py runserver`

Copyright 2016-2017 Chaoyi Zha
