Quickstart
==========

インストール手順
----------------

以下のコマンドでPyPI経由でインストールが可能です。::

  pip install openldap-schema-parser

Githubより最新版をインストールする場合は以下のコマンドを実施してください。::

  pip install git+http://github.com/mypaceshun/openldap-schema-parser.git

コマンド利用手順
----------------

インストール後 ``schema-parser`` というコマンドが追加されます。
``schema-parser`` コマンドを利用することでschemaファイルを構文解析し、
解析結果を標準出力へ出力します。 ::

  $ schema-parser test.schema
  [15:08:39] Schema(name=test, objectidentifier_list=[ObjectIdentifier(key='testRoot', oid='1.1.1.1'),                            command.py:25
             ObjectIdentifier(key='testAttribute', oid='testRoot:1'), ObjectIdentifier(key='testObjectClass', oid='testRoot:2')],              
             attribute_list=[Attribute(oid='testAttribute:1', name='testAttrStr', description='test directoryString attribute',                
             obsolete=False, equality='caseExactMatch', substr='caseExactSubstringsMatch',                                                     
             syntax='1.3.6.1.4.1.1466.115.121.1.15{1024}', single_value=False, collective=False, no_user_modification=False)],                 
             objectclass_list=[ObjectClass(oid='testObjectClass:1',name='testUser',alias=None,description='test                                
             objectClass',obsolete=False,sup='top',structural_type=<STRUCTURAL_TYPE.AUXILIARY: 'AUXILIARY'>,must=[],may=[])])

コマンドは解析結果のSchemaクラスを `Rich Console API <https://rich.readthedocs.io/en/stable/console.html>`_ を利用して出力します。

``--expand-oid`` オプションをつけることでObjectIdentifierを利用して表現されているOIDを実際のOIDへ変換することが出来ます。 ::

  $ schema-parser --expand-oid test.schema
  [15:12:33] Schema(name=test, objectidentifier_list=[ObjectIdentifier(key='testRoot', oid='1.1.1.1'),                            command.py:25
             ObjectIdentifier(key='testAttribute', oid='1.1.1.1.1'), ObjectIdentifier(key='testObjectClass', oid='1.1.1.1.2')],
             attribute_list=[Attribute(oid='1.1.1.1.1.1', name='testAttrStr', description='test directoryString attribute',
             obsolete=False, equality='caseExactMatch', substr='caseExactSubstringsMatch',
             syntax='1.3.6.1.4.1.1466.115.121.1.15{1024}', single_value=False, collective=False, no_user_modification=False)],
             objectclass_list=[ObjectClass(oid='1.1.1.1.2.1',name='testUser',alias=None,description='test
             objectClass',obsolete=False,sup='top',structural_type=<STRUCTURAL_TYPE.AUXILIARY: 'AUXILIARY'>,must=[],may=[])])

ライブラリ利用手順
------------------

ライブラリとして利用するサンプルは以下になります。 ::

  from rich import print
  from openldap_schema_parser.parser import parse

  result = parse("test.schema")
  print(result)

解析結果は :any:`Schemaクラス <Schema>` で返ります。

ObjectIdentifierを利用して表現されているOIDの変換は :any:`Schemaクラス <Schema>` に定義されている、
:any:`expand_oid` という関数を利用してください。::

  from openldap_schema_parser.parser import parse
  result = parse("test.schema")
  result.expand_oid()

解析に失敗した場合は :any:`SchemaParseError` が発生します。

