Schemaクラス
============

解析結果は :any:`Schema` クラスで返されます。

``Schema`` クラスは ``name`` 、 ``objectidentifier_list`` 、 ``attribute_list`` 、 ``objectclass_list`` を持ち、それぞれスキーマファイルの解析結果が記録されます。

``name`` にはスキーマ名が記録されます。これはファイル名の ``.schema`` を除いた部分になります。
例として ``test-schema.schema`` というファイルを解析した場合は ``test-schema`` がスキーマ名になります。

``objectidentifier_list`` には ``objectIdentifier`` の解析結果が、 :any:`ObjectIdentifier` クラスのリストとして記録されます。
スキーマファイル内に ``objectIdentifier`` の記述が無ければ空リストとなります。

``attribute_list`` には ``attributeType`` の解析結果が、 :any:`Attribute` クラスのリストとして記録されます。
スキーマファイル内に ``attributeType`` の記述が無ければ空リストとなります。

``objectclass_list`` には ``objectClass`` の解析結果が、 :any:`ObjectClass` クラスのリストとして記録されます。
スキーマファイル内に ``objectClass`` の記述が無ければ空リストとなります。

expand_oid
----------

:any:`Schema` クラスが持つ :any:`expand_oid` 関数で、ObjectIdentifierを利用して表現されているOIDの値を、全て実際のOIDの値に変換します。

例として ``testAttr 1.1.1.1`` というObjectIdentifierがあり、OIDを ``testAttr:2`` と指定している属性があるとします。

``expand_oid()`` を実行することでOIDは ``1.1.1.1.2`` と展開され上書き保存されます。

pprint
------

:any:`schema` クラスのデータを整形して出力します。
出力結果をそのままschemaファイルとして利用できます。

pprint_str
----------

:any:`schema` クラスのデータを整形した文字列を返します。
