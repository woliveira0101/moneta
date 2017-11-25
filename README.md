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

```
Copyright 2016-2017 Chaoyi Zha

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
