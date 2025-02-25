### Hexlet tests and linter status:
[![Actions Status](https://github.com/azamuzapbar0808/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/azamuzapbar0808/python-project-50/actions)

# Gendiff

## Описание  
Утилита `gendiff` сравнивает два файла (JSON/YAML) и показывает разницу в удобном формате.

## Установка  
```sh
pip install gendiff
```

# gendiff

## Установка


## Использование


## Пример работы
```bash
$ gendiff file1.json file2.json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}



Теперь `gendiff` работает и как CLI, и как библиотека 🚀


![CI](https://github.com/your-username/your-repo-name/actions/workflows/ci.yml/badge.svg)
[![Code Climate](https://api.codeclimate.com/v1/badges/your-badge-id/test_coverage.svg)](https://codeclimate.com/github/your-username/your-repo-name/test_coverage)
[![Code Climate](https://api.codeclimate.com/v1/badges/your-badge-id/maintainability.svg)](https://codeclimate.com/github/your-username/your-repo-name/maintainability)

# Генератор различий для YAML файлов

Этот проект реализует генератор различий между двумя YAML файлами. Он позволяет сравнивать два файла и отображать различия в виде списка изменений в формате:

```yaml
{
  - key: value1
  + key: value2
  ...
}

