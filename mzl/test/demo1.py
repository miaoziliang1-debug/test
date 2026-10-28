def convert_keys_to_uppercase(d):
    """
    将字典中的所有键转换为大写形式。

    Args:
        d (dict): 输入的字典。

    Returns:
        dict: 转换后的字典，其中所有键都是大写形式。
    """
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            # 如果值是字典，递归处理
            result[key.upper()] = convert_keys_to_uppercase(value)
        elif isinstance(value, list):
            # 如果值是列表，递归处理列表中的每个元素
            result[key.upper()] = [convert_keys_to_uppercase(item) for item in value]
        else:
            # 其他情况直接转换键为大写
            result[key.upper()] = value
    return result

def convert_keys_to_uppercase_in_list(list_of_dicts):
    """
    将列表中的所有字典的键转换为大写形式。

    Args:
        list_of_dicts (list[dict]): 输入的字典列表。

    Returns:
        list[dict]: 转换后的字典列表，其中所有键都是大写形式。
    """
    result = []
    for d in list_of_dicts:
        new_dict = {}
        for key, value in d.items():
            if isinstance(value, dict):
                # 如果值是字典，递归处理
                new_dict[key.upper()] = convert_keys_to_uppercase_in_list([value])[0]
            elif isinstance(value, list):
                # 如果值是列表，递归处理列表中的每个元素
                new_dict[key.upper()] = [convert_keys_to_uppercase_in_list([item])[0] for item in value]
            else:
                # 其他情况直接转换键为大写
                new_dict[key.upper()] = value
        result.append(new_dict)
    return result


def convert_keys_to_uppercase_in_list2(list_of_dicts):
    """
    将字典列表中的所有键转换为大写，并处理嵌套的字典和列表结构。

    Args:
        list_of_dicts (list): 需要处理的字典列表，其中可能包含嵌套的字典和列表。

    Returns:
        list: 转换后的字典列表，所有键均以大写表示。每个字典中新增了元数据字段，如'$schema'、'description'等，
              用于提升结果的可读性和文档性。
    """

    def _convert_dict(d):
        """
        将字典d中的所有键转换为大写，并处理其值中的嵌套结构。

        Args:
            d (dict): 需要处理的字典。

        Returns:
            dict: 处理后的字典，所有键均为大写形式。
        """
        return {
            key.upper():
                _convert_dict(value) if isinstance(value, dict) else
                [_convert_dict(item) for item in value] if isinstance(value, list) else
                value
            for key, value in d.items()
        }

    converted_list = []
    for original_dict in list_of_dicts:
        converted_dict = _convert_dict(original_dict)

        # 添加元数据以增强可读性
        converted_dict['$schema'] = 'converted_keys_to_uppercase'
        converted_dict['description'] = f'Converted dictionary from input list at position {len(converted_list)}'

        converted_list.append(converted_dict)

    return {
        'result': converted_list,
        'status': 'success',
        'message': '键值转换完成，所有字典中的键均以大写形式表示。'
    }

# 示例用法


if __name__ =='__main__':

    original_list_of_dicts = [
        {'name': 'Alice', 'age': 25},
        {'address': {'city': 'Redmond', 'state': 'WA'}},
        {'friends': [{'name': 'Bob', 'age': 30}, {'name': 'Carol', 'age': 28}]}
    ]

    uppercase_list_of_dicts = convert_keys_to_uppercase_in_list(original_list_of_dicts)
    print(convert_keys_to_uppercase_in_list2(original_list_of_dicts))