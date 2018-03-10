Утилита для сравнения *epf*-, *erf*-, *ert*- и *md*-файлов
===

Что делает
---

Файлы разбираются с помощью пакета [parse-1c-build][1] в каталоги, которые затем сравниваются указанной в аргументах 
командной строки утилитой сравнения. Поддерживаются AraxisMerge, ExamDiff, KDiff3, WinMerge.

При установке пакета в каталоге скриптов интерпретатора Python создаётся исполняемый файл *diff1c.exe*.

Требования
---

- Windows
- Python 3.5 и выше. Каталоги интерпретатора и скриптов Python должны быть прописаны в переменной окружения Path
- Пакет [parse-1c-build][1] с необходимыми настройками

[1]: https://github.com/Cujoko/parse-1c-build
