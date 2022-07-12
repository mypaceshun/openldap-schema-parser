Parser関数
==========

parse
-----

:any:`parse` 関数を利用することでschema形式のファイルを解析できます。::

  from openldap_schema_parser.parser import parse

  result = parse("test.schema")

解析結果は :any:`Schema` クラスで返します。
スキーマ名は与えられたファイル名の ``Path.stem`` の値になります。
例として ``test.schema`` というファイルが指定された場合スキーマ名は ``test`` となります。

parse_str
---------

スキーマ形式の文字列を解析します。 ::

  from openldap_schema_parser.parser import parse_str

  text = """
  objectidentifier testOID 1.1.1.1
  attributetype ( testOID:1 NAME testAttr )
  objectClass ( testOID:2 NAME testClass )
  """
  result = parse_str(text, "test")

第2引数にはスキーマ名を指定します。
スキーマ名を指定しなかった場合は ``parsed`` というスキーマ名になります。
解析結果は :any:`Schema` クラスで返します。
