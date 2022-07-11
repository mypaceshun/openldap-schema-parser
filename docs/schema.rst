Schemaクラス
============

解析結果は ``Schema`` クラスで返されます。

``Schema`` クラスは ``name`` 、 ``objectidentifier_list`` 、 ``attribute_list`` 、 ``objectclass_list`` を持ち、それぞれスキーマファイルの解析結果が記録されます。

``name`` にはスキーマ名が記録されます。これはファイル名の ``.schema`` を除いた部分になります。
例として ``test-schema.schema`` というファイルを解析した場合は ``test-schema`` がスキーマ名になります。

``objectidentifier_list`` には ``objectIdentifier`` の解析結果が、 ``ObjectIdentifier`` クラスのリストとして記録されます。
スキーマファイル内に ``objectIdentifier`` の記述が無ければ空リストとなります。

``attribute_list`` には ``attributeType`` の解析結果が、 ``Attribute`` クラスのリストとして記録されます。
スキーマファイル内に ``attributeType`` の記述が無ければ空リストとなります。

``objectclass_list`` には ``objectClass`` の解析結果が、 ``ObjectClass`` クラスのリストとして記録されます。
スキーマファイル内に ``objectClass`` の記述が無ければ空リストとなります。
