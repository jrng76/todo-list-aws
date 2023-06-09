# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-05-16
### Added
- Versión inicial de código.

## [1.0.1] - 2023-05-26
### Added
- Se añade al fichero requirement.txt una linea con el texto "urllib3<2" para solucionar un problema con esta biblioteca de python.
- Se modifica el fichero samconfig.toml para añadir los s3_bucket 

## [1.1.0] - 2023-06-09
- Nueva acción de la API llamada translate para traducir el texto de un registro dado al idioma indicado como paramétro.
- Nuevo test unitario para probar transtale
- Nueva prueba de integración para probar translate

## [1.1.1] - 2023-06-09
- Para evitar el error del translate y poder pasar las tost se modifica el método 'gettranslate_todo_text' para que devuelva siempre la misma cadena 'traducida' cuando existe el registro en base de datos.

