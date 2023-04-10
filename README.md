# CN-Char-Encoding

中文各编码中的汉字字符。

| 编码 | GB2312 | Big5-1984 | Big5-2003 | GBK   | GB18030-2000 | GB18030-2005 | GB18030-2022 |
|:---- |:-------|:----------|:----------|:------|:-------------|:-------------|:-------------|
| 数量 | 6763   | 13060     |           | 21003 | 27533        | 70244        |              |

## 注

### `Big5-1984`

一般认为 Big5 包含 13053 字，但减去两个重复字仅 13051 字。
但 Big5 符号区又收了 9 个单位字，计入这几个字共 13060 字。

### `GBK`

其中增补汉字和部首有 80 个 (包括 28 个部首和 52 个汉字)。
在制定 GBK 时，Unicode 中还没有这些字符，所以使用了 PUA 的码位，
这 80 个字符的 Unicode PUA 码位是 0xE815-0xE864。

### `GB18030`

在制定 GB18030 时，Unicode 已将其中 52 个汉字收录进了扩充区 A，
28 个部首中有 14 个部首被收录到部首补充区，所以还剩 14 个部首在
PUA。
